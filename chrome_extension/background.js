function sendCurrentURL() {
    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        let tabURL = tabs[0].url;
        console.log(tabURL);

        let sendObject = {
            'CurrentURL': tabURL
        };
        let json = JSON.stringify(sendObject);

        let xhr = new XMLHttpRequest();

        xhr.open('POST', 'http://127.0.0.1:5000/request');
        xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

        xhr.onerror = function() {
            alert('Request Error');
        };
        xhr.send(json);
    });
}


setInterval(sendCurrentURL, 1500)




