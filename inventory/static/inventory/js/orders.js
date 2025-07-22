// Orders JS
fetch("/api/orders/")
  .then((res) => res.json())
  .then((data) => {
    const list = document.getElementById("orders-list");
    list.innerHTML = data
      .map((o) => `<div>Order #${o.id} - ${o.status}</div>`)
      .join("");
  });
