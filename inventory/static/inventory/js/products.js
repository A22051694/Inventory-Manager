// Products JS
fetch("/api/products/")
  .then((res) => res.json())
  .then((data) => {
    const list = document.getElementById("products-list");
    list.innerHTML = data
      .map((p) => `<div>${p.name} - ${p.price}</div>`)
      .join("");
  });
