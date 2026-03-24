function addPlot() {
  const eq = document.getElementById("equation").value.trim();
  if (!eq) {
    alert("Please enter an equation.");
    return;
  }

  const color = document.getElementById("color").value;
  const minX = document.getElementById("minX").value.trim() || "-10";
  const maxX = document.getElementById("maxX").value.trim() || "10";

  const tbody = document.querySelector("#plotTable tbody");
  const row = tbody.insertRow();
  row.innerHTML = `
    <td contenteditable="true">${eq}</td>
    <td><input type="color" value="${color}" style="width:50px;height:26px;border:none;cursor:pointer"></td>
    <td contenteditable="true">${minX}</td>
    <td contenteditable="true">${maxX}</td>
    <td><button class="del-btn" onclick="this.closest('tr').remove()">&times;</button></td>
  `;

  document.getElementById("equation").value = "";
  refreshChart();
}

function refreshChart() {
  const rows = document.querySelectorAll("#plotTable tbody tr");
  if (rows.length === 0) {
    return;
  }

  const plots = [];
  rows.forEach((row) => {
    const cells = row.cells;
    plots.push({
      equation: cells[0].innerText.trim(),
      color: cells[1].querySelector("input").value,
      min_x: cells[2].innerText.trim() || "-10",
      max_x: cells[3].innerText.trim() || "10"
    });
  });

  fetch("/plot", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(plots)
  })
    .then((r) => r.json())
    .then((data) => {
      const img = document.getElementById("chartImg");
      img.src = "data:image/png;base64," + data.image;
      img.style.display = "block";
      document.getElementById("placeholder").style.display = "none";
    });
}