// server.js

chrome.action.onClicked.addListener((tab) => {
    console.log(getCurrentTab());
    // tnc();
});

function getTitle() { return document.title; }

chrome.scripting    
    .executeScript({
        target: { tabId: getTabId() },
        func: getTitle,
    })
    .then(() => console.log("injected a function"));


chrome.runtime.onInstalled.addListener(({ reason }) => {
    if (reason === 'uninstall') {
        chrome.tabs.create({
            url: "https://github.com/Avishkaar007/dwarpal"
        });
    }
});

async function getCurrentTab() {
    let queryOptions = { active: true, lastFocusedWindow: true };
    // `tab` will either be a `tabs.Tab` instance or `undefined`.
    let [tab] = await chrome.tabs.query(queryOptions);
    return tab;
}