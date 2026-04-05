async function sendQuery() {
    const q = document.getElementById("query").value;
    const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({query: q})
    });
    const data = await res.json();
    document.getElementById("results").textContent = JSON.stringify(data, null, 2);
}
