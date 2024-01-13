(() => {
    document.addEventListener("DOMContentLoaded", () => {
        document.getElementById("search-btn").focus();
        var sbtn = document.getElementById("search-btn");

        var homepage = document.getElementById("homepage");
        function redirect(uri) {
            chrome.tabs.create({ url: uri });
        }
        sbtn.addEventListener("click", () => {
            




            
        })
        homepage.addEventListener("click", () => {
            redirect(homepage.href);
        })
    })
})();