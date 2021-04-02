function sendCurrentURL() {
    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        var tabURL = tabs[0].url;
        console.log(tabURL);

        var sendObject = {
            'CurrentURL': tabURL
        };
        var json = JSON.stringify(sendObject);

        var xhr = new XMLHttpRequest();

        xhr.open('POST', 'http://127.0.0.1:5000/request');
        xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

        // occurs only when request cannot be executed
        xhr.onerror = function() {
            alert('Request Error');
        };
        xhr.send(json);
    });
}


setInterval(sendCurrentURL, 1500)




