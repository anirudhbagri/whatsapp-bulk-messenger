document.addEventListener('DOMContentLoaded', function() {
    // Tab Switching
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');
  
    tabButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Remove active class from all buttons and panes
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabPanes.forEach(pane => pane.classList.remove('active'));
        
        // Add active class to clicked button and corresponding pane
        button.classList.add('active');
        const tabId = button.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
      });
    });
  
    // Add Number Button
    document.getElementById('addNumberBtn').addEventListener('click', () => {
      const phoneNumber = prompt('Telefon numarasını giriniz (ülke koduyla):');
      if (phoneNumber && /^\d+$/.test(phoneNumber)) {
        addNumberToList(phoneNumber);
        saveNumbers();
      } else if (phoneNumber) {
        alert('Geçerli bir telefon numarası giriniz (sadece rakamlar).');
      }
    });
  
    // Remove Number Button
    document.getElementById('removeNumberBtn').addEventListener('click', () => {
      const selectedItem = document.querySelector('#numbersList .selected');
      if (selectedItem) {
        selectedItem.remove();
        saveNumbers();
      } else {
        alert('Lütfen silinecek bir numara seçin.');
      }
    });
  
    // Import Numbers Button
    document.getElementById('importNumbersBtn').addEventListener('click', () => {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.txt,.csv';
      
      input.onchange = e => {
        const file = e.target.files[0];
        const reader = new FileReader();
        
        reader.onload = function(event) {
          const content = event.target.result;
          const numbers = content.split(/[\r\n,;]+/).filter(num => num.trim() !== '');
          
          numbers.forEach(num => {
            if (/^\d+$/.test(num.trim())) {
              addNumberToList(num.trim());
            }
          });
          
          saveNumbers();
        };
        
        reader.readAsText(file);
      };
      
      input.click();
    });
  
    // Add Media Button
    document.getElementById('addMediaBtn').addEventListener('click', () => {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*,video/*';
      
      input.onchange = e => {
        const files = e.target.files;
        for (let i = 0; i < files.length; i++) {
          addMediaToList(files[i].name);
        }
      };
      
      input.click();
    });
  
    // Remove Media Button
    document.getElementById('removeMediaBtn').addEventListener('click', () => {
      const selectedItem = document.querySelector('#mediaList .selected');
      if (selectedItem) {
        selectedItem.remove();
      } else {
        alert('Lütfen silinecek bir medya dosyası seçin.');
      }
    });
  
    // Clear Media Button
    document.getElementById('clearMediaBtn').addEventListener('click', () => {
      document.getElementById('mediaList').innerHTML = '';
    });
  
    // Save Media Message Button
    document.getElementById('saveMediaMessageBtn').addEventListener('click', () => {
      const selectedItem = document.querySelector('#mediaList .selected');
      if (selectedItem) {
        const message = document.getElementById('mediaMessageText').value;
        selectedItem.setAttribute('data-message', message);
        
        const statusElement = document.getElementById('mediaMessageStatus');
        statusElement.textContent = 'Mesaj kaydedildi!';
        setTimeout(() => {
          statusElement.textContent = '';
        }, 3000);
      } else {
        alert('Lütfen bir medya dosyası seçin.');
      }
    });
  
    // Select item in list
    document.getElementById('numbersList').addEventListener('click', event => {
      if (event.target.tagName === 'LI') {
        const items = document.querySelectorAll('#numbersList li');
        items.forEach(item => {
          item.classList.remove('selected');
          item.classList.remove('highlight'); // Remove highlight from all
        });
        event.target.classList.add('selected');
        event.target.classList.add('highlight'); // Add highlight class to the selected item
      }
    });

    // Clear All Numbers Button
    document.getElementById('clearAllNumbersBtn').addEventListener('click', () => {
      document.getElementById('numbersList').innerHTML = '';
    });
  
    document.getElementById('mediaList').addEventListener('click', event => {
      if (event.target.tagName === 'LI') {
        const items = document.querySelectorAll('#mediaList li');
        items.forEach(item => item.classList.remove('selected'));
        event.target.classList.add('selected');
        
        // Load associated message if any
        const message = event.target.getAttribute('data-message') || '';
        document.getElementById('mediaMessageText').value = message;
      }
    });
  
    // Start Button
    document.getElementById('startBtn').addEventListener('click', () => {
      const numbers = getNumbersList();
      const message = document.getElementById('messageText').value;
      const delay = document.getElementById('delayTime').value;
      
      if (numbers.length === 0) {
        alert('Lütfen en az bir telefon numarası ekleyin.');
        return;
      }
      
      if (!message.trim()) {
        alert('Lütfen bir mesaj yazın.');
        return;
      }
      
      // Check if WhatsApp Web is open
      chrome.tabs.query({url: 'https://web.whatsapp.com/*'}, function(tabs) {
        if (tabs.length === 0) {
          // WhatsApp Web isn't open, open it
          chrome.tabs.create({url: 'https://web.whatsapp.com/'}, function(tab) {
            alert('WhatsApp Web açıldı. Lütfen QR kodu okuttuktan sonra tekrar deneyin.');
          });
        } else {
          // WhatsApp Web is open, start sending
          startSending(numbers, message, delay);
        }
      });
    });
  
    // Stop Button
    document.getElementById('stopBtn').addEventListener('click', () => {
      stopSending();
    });
  
    // Helper Functions
    function addNumberToList(number) {
      const li = document.createElement('li');
      li.textContent = number;
      document.getElementById('numbersList').appendChild(li);
    }
  
    function addMediaToList(filename) {
      const li = document.createElement('li');
      li.textContent = filename;
      li.setAttribute('data-message', '');
      document.getElementById('mediaList').appendChild(li);
    }
  
    function getNumbersList() {
      const items = document.querySelectorAll('#numbersList li');
      return Array.from(items).map(item => item.textContent);
    }
  
    function saveNumbers() {
      const numbers = getNumbersList();
      chrome.storage.local.set({whatsappNumbers: numbers});
    }
  
    function startSending(numbers, message, delay) {
      document.getElementById('startBtn').disabled = true;
      document.getElementById('stopBtn').disabled = false;
      
      // Update status
      addStatusMessage('Gönderim başlatılıyor...');
      
      // Send messages to content script to handle sending
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {
          action: 'startSending',
          numbers: numbers,
          message: message,
          delay: delay
        });
      });
      
      // For demonstration, update progress
      updateProgress(0, numbers.length);
      simulateProgress(numbers.length);
    }
  
    function stopSending() {
      document.getElementById('startBtn').disabled = false;
      document.getElementById('stopBtn').disabled = true;
      
      // Send stop message to content script
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {action: 'stopSending'});
      });
      
      addStatusMessage('Gönderim durduruldu.');
    }
  
    function addStatusMessage(message) {
      const statusText = document.getElementById('statusText');
      const now = new Date().toLocaleTimeString();
      statusText.innerHTML += `[${now}] ${message}<br>`;
      statusText.scrollTop = statusText.scrollHeight;
    }
  
    function updateProgress(current, total) {
      const percentage = total === 0 ? 0 : Math.round((current / total) * 100);
      document.querySelector('.progress-fill').style.width = `${percentage}%`;
      document.getElementById('progressText').textContent = `${percentage}%`;
    }
  
    // Just for demonstration
    function simulateProgress(total) {
      let current = 0;
      const interval = setInterval(() => {
        current++;
        updateProgress(current, total);
        addStatusMessage(`Mesaj gönderiliyor: ${current}/${total}`);
        
        if (current >= total) {
          clearInterval(interval);
          document.getElementById('startBtn').disabled = false;
          document.getElementById('stopBtn').disabled = true;
          addStatusMessage('Tüm mesajlar gönderildi!');
        }
      }, 2000);
      
      // Store interval ID to be able to clear it when stopping
      window.sendingInterval = interval;
    }
  
    // Load saved numbers
    chrome.storage.local.get('whatsappNumbers', function(result) {
      if (result.whatsappNumbers) {
        result.whatsappNumbers.forEach(number => {
          addNumberToList(number);
        });
      }
    });

    // Memory Feature Implementation
    const messageText = document.getElementById('messageText');
    const savedMessage = localStorage.getItem('lastMessage');
    if (savedMessage) {
        messageText.value = savedMessage;
    }

    messageText.addEventListener('input', () => {
        localStorage.setItem('lastMessage', messageText.value);
    });
});
