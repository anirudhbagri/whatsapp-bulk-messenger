// Background script
chrome.runtime.onInstalled.addListener(function() {
    console.log('WhatsApp Toplu Mesaj eklentisi yüklendi.');
  });
  
  // Handle messages from content script
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'updateProgress') {
      // Forward progress updates to popup if it's open
      chrome.runtime.sendMessage(request);
    }
  });