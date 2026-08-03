let apiUrl = "/items";

window.onload = function () {
    loadItems();
};


// ======================================
// Load All Items
// ======================================
function loadItems() {

    fetch(apiUrl)
        .then(response => response.json())
        .then(result => {

            let table = "";

            if (result.status === "success") {

                result.data.forEach(item => {

                    table += `
                        <tr>
                            <td>${item.id}</td>
                            <td>${item.name}</td>
                            <td>${item.price}</td>
                            <td>
                                <button onclick="editItem(${item.id}, '${item.name}', ${item.price})">
                                    Edit
                                </button>

                                <button onclick="deleteItem(${item.id})">
                                    Delete
                                </button>
                            </td>
                        </tr>
                    `;
                });
            }

            document.getElementById("itemTable").innerHTML = table;

        })
        .catch(error => {

            alert("Error : " + error);

        });

}


// ======================================
// Save Item
// ======================================
function saveItem() {

    let id = document.getElementById("itemId").value;

    let item = {

        name: document.getElementById("name").value,
        price: document.getElementById("price").value

    };


    if (id == "") {

        addItem(item);

    }
    else {

        updateItem(id, item);

    }

}


// ======================================
// Add Item
// ======================================
function addItem(item) {

    fetch(apiUrl, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(item)

    })

        .then(async response => {

            let result = await response.json();

            if (!response.ok) {

                throw new Error(result.message);

            }

            alert(result.message);

            clearForm();

            loadItems();

        })

        .catch(error => {

            alert(error.message);

        });

}


// ======================================
// Update Item
// ======================================
function updateItem(id, item) {

    fetch(apiUrl + "/" + id, {

        method: "PUT",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(item)

    })

        .then(async response => {

            let result = await response.json();

            if (!response.ok) {

                throw new Error(result.message);

            }

            alert(result.message);

            clearForm();

            loadItems();

        })

        .catch(error => {

            alert(error.message);

        });

}


// ======================================
// Delete Item
// ======================================
function deleteItem(id) {

    if (!confirm("Are you sure?"))
        return;

    fetch(apiUrl + "/" + id, {

        method: "DELETE"

    })

        .then(async response => {

            let result = await response.json();

            if (!response.ok) {

                throw new Error(result.message);

            }

            alert(result.message);

            loadItems();

        })

        .catch(error => {

            alert(error.message);

        });

}


// ======================================
// Edit Item
// ======================================
function editItem(id, name, price) {

    document.getElementById("itemId").value = id;

    document.getElementById("name").value = name;

    document.getElementById("price").value = price;

}


// ======================================
// Clear Form
// ======================================
function clearForm() {

    document.getElementById("itemId").value = "";

    document.getElementById("name").value = "";

    document.getElementById("price").value = "";

}