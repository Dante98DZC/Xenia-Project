var chartScript = document.currentScript;
window.addEventListener("DOMContentLoaded", (event) => {
    data = JSON.parse(chartScript.getAttribute("data").split("'").join('"'));
    agree_values = [];
    not_agree_values = [];
    labels = [];
    for (let i = 0; i < data["dates"].length; i += 1) {
        let current_date = new Date(data["dates"][i]);
        agree_values.push({
            x: current_date,
            y: data["agree_series"][i],
        });
        not_agree_values.push({
            x: current_date,
            y: data["not_agree_serise"][i],
        });
        labels.push(
            ("0" + current_date.getDate()).slice(-2) +
                "/" +
                ("0" + (current_date.getMonth() + 1)).slice(-2) +
                "/" +
                current_date.getFullYear()
        );
    }
    var ctx = document.getElementById("Sat-line-chart").getContext("2d");
    var chartData = {
        labels: labels,
        datasets: [
            {
                label: "Inconformes",
                data: not_agree_values,
                backgroundColor: "rgba(255, 0, 0, 0.2)",
                borderColor: "rgba(255, 0, 0, 1)",
                borderWidth: 1,
                fill: true,
                tension: 0.15
            },
            {
                label: "Conformes",
                data: agree_values,
                backgroundColor: "rgba(0, 255, 0, 0.2)",
                borderColor: "rgba(0, 255, 0, 1)",
                borderWidth: 1,
                fill: true,
                tension: 0.15
            },
        ],
    };

    var myChart = new Chart(ctx, {
        type: "line",
        data: chartData,
        options: {
            responsive: true,
            scales: {
                xAxes: [
                    {
                        type: "time",
                    }
                ],
                y:{
                    ticks: {
                        stepSize: 1
                    }
                }
                
            },
        },
    });
    $(".countdowns").each(function(){
        let duration = $(this).data("duration");
        let current = $(this).data("current");
        $(this).timer({
            duration: duration,
            current:current,
        });
    });
});
