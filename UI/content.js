// WhatsApp Web sitesinde çalışacak content script
let isRunning = false;
let currentNumberIndex = 0;
let numbers = [];
let message = '';
let delay = 3;

// Listen for messages from popup
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'startSending') {
    numbers = request.numbers;
    message = request.message;
    delay = request.delay;
    currentNumberIndex = 0;
    isRunning = true;
    
    // Start sending messages
    sendNextMessage();
  } else if (request.action === 'stopSending') {
    isRunning = false;
  }
});

// Function to send messages
function sendNextMessage() {
  if (!isRunning || currentNumberIndex >= numbers.length) {
    isRunning = false;
    return;
  }
  
  const number = numbers[currentNumberIndex];
  
  // Open chat with the number
  openChat(number)
    .then(() => {
      // Send message
      return sendMessage(message);
    })
    .then(() => {
      // Update index and send next after delay
      currentNumberIndex++;
      
      // Report progress back to popup
      chrome.runtime.sendMessage({
        action: 'updateProgress',
        current: currentNumberIndex,
        total: numbers.length
      });
      
      setTimeout(sendNextMessage, delay * 1000);
    })
    .catch(error => {
      console.error('Error sending message:', error);
      
      // Skip this number and continue
      currentNumberIndex++;
      setTimeout(sendNextMessage, delay * 1000);
    });
}

// Open chat with a specific number
function openChat(number) {
  return new Promise((resolve, reject) => {
    // Create the WhatsApp chat URL
    const url = `https://web.whatsapp.com/send?phone=${number}`;
    
    // Change window location
    window.location.href = url;
    
    // Wait for chat to load
    const chatLoadInterval = setInterval(() => {
      // Check if chat input is available
      const chatInput = document.querySelector('div[contenteditable="true"]');
      
      if (chatInput) {
        clearInterval(chatLoadInterval);
        resolve();
      }
    }, 1000);
    
    // Timeout after 30 seconds
    setTimeout(() => {
      clearInterval(chatLoadInterval);
      reject(new Error('Chat loading timeout'));
    }, 30000);
  });
}

// Send message in the current chat
function sendMessage(text) {
  return new Promise((resolve, reject) => {
    // Find the input field
    const chatInput = document.querySelector('div[contenteditable="true"]');
    
    if (!chatInput) {
      reject(new Error('Chat input not found'));
      return;
    }
    
    // Set the message text
    chatInput.textContent = text;
    
    // Trigger input event
    chatInput.dispatchEvent(new Event('input', { bubbles: true }));
    
    // Find and click send button
    setTimeout(() => {
      const sendButton = document.querySelector('span[data-icon="send"]');
      
      if (sendButton) {
        sendButton.click();
        resolve();
      } else {
        reject(new Error('Send button not found'));
      }
    }, 500);
  });
}