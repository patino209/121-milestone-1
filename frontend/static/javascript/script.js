function getQuery() {
    let query = document.getElementById("query").value;

    console.log(query);
}

document.getElementById("search-button").addEventListener("click", getQuery);