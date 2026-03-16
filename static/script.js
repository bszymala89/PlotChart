const plot_data_element = document.getElementById("plot_data")
const plot_data = JSON.parse(plot_data_element.dataset.plots)

const table = document.getElementById("plot_table")

//create header
// const thead = document.createElement("thead")
// const header_row = document.createElement("tr")
// const headers = ["Equation", "Min X", "Max X", "Color"]

headers.forEach(text => {
    const th = document.createElement("th")
    th.textContent = text
    header_row.appendChild(th)
});

thead.appendChild(header_row)
table.appendChild(thead)

const tbody = document.createElement("tbody")

plot_data.forEach(element => {
    const row = document.createElement("tr")

    const equation = document.createElement("td")
    equation.textContent = element.equation
    row.appendChild(equation)

    const min_x = document.createElement("td")
    min_x.textContent = element.min_x
    row.appendChild(min_x)

    const max_x = document.createElement("td")
    max_x.textContent = element.max_x
    row.appendChild(max_x)

    const color = document.createElement("td")
    const color_box = document.createElement("div")

    color_box.style.width = "20px"
    color_box.style.height = "20px"

    color_box.style.backgroundColor = element.color

    color.appendChild(color_box)

    row.appendChild(color)

    tbody.appendChild(row)
});

table.appendChild(tbody)

plot_data_element.appendChild(table)