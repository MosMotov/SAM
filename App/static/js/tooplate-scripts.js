const width_threshold = 480;

function drawLineChart() {
  if ($("#lineChart").length) {
    ctxLine = document.getElementById("lineChart").getContext("2d");
    optionsLine = {
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Data"
            }
          }
        ]
      }
    };

    configLine = {
      type: "line",
      data: {
        labels: [
          "Data"
        ],
        datasets: [
          {
            label: "Height",
            data: [f1, f1, f1, f1, f1],
            fill: false,
            borderColor: "rgb(255, 0, 0)",
            lineTension: 0.1
          },
          {
            label: "Weight",
            data: [f2, f2, f2, f2, f2],
            fill: false,
            borderColor: "rgb(0, 255, 0)",
            lineTension: 0.1
          },
          {
            label: "Systolic Pressure",
            data: [f3, f3, f3, f3, f3],
            fill: false,
            borderColor: "rgb(0, 0, 255)",
            lineTension: 0.1
          },
          {
            label: "Diastolic Pressure",
            data: [f4, f4, f4, f4, f4],
            fill: false,
            borderColor: "rgb(255, 0, 255)",
            lineTension: 0.1
          },
          {
            label: "Heart Rate",
            data: [f5, f5, f5, f5, f5],
            fill: false,
            borderColor: "rgb(0, 255, 255)",
            lineTension: 0.1
          }
        ]
      },
      options: optionsLine
    };

    lineChart = new Chart(ctxLine, configLine);
  }
}

function drawBarChart() {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: "Data"
            }
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: ["Height","Weight","Systolic Pressure","Diastolic Pressure","Heart Rate"],
        datasets: [
          {
            label: "Data",
            data: [f1,f2,f3,f4,f5],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(255, 0, 0, 0.2)",
              "rgba(0, 255, 0, 0.2)",
              "rgba(0, 0, 255, 0.2)",
              "rgba(255, 0, 255, 0.2)",
            ],
            borderColor: [
              "rgba(255,99,132,1)",
              "rgba(255,0,0,1)",
              "rgba(0,255,0,1)",
              "rgba(0,0,255,1)",
              "rgba(255,0,255,1)",
            ],
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}

function drawPieChart() {
  if ($("#pieChart").length) {
    ctxPie = document.getElementById("pieChart").getContext("2d");
    optionsPie = {
      responsive: true,
      maintainAspectRatio: false
    };

    configPie = {
      type: "pie",
      data: {
        datasets: [
          {
            data: [risk, safe],
            backgroundColor: [
              window.chartColors.red,
              window.chartColors.green,
            ],
            label: "Storage"
          }
        ],
        labels: ["Risk", "Safe"]
      },
      options: optionsPie
    };
    

    pieChart = new Chart(ctxPie, configPie);
    
  }
}
function drawPieChart() {
  if ($("#pieChart2").length) {
  ctxPie2 = document.getElementById("pieChart2").getContext("2d");
      optionsPie = {
        responsive: true,
        maintainAspectRatio: false
      };

      configPie2 = {
        type: "pie",
        data: {
          datasets: [
            {
              data: [!ran, ran, 0],
              backgroundColor: [
                window.chartColors.red,
                window.chartColors.green,
                window.chartColors.gray,
              ],
              label: "Storage"
            }
          ],
          labels: ["Risk", "Safe", "Not Available"]
        },
        options: optionsPie
      };
      pieChart2 = new Chart(ctxPie2, configPie2);
    }
  }

function updateChartOptions() {
  if ($(window).width() < width_threshold) {
    if (optionsLine) {
      optionsLine.maintainAspectRatio = false;
    }
    if (optionsBar) {
      optionsBar.maintainAspectRatio = false;
    }
  } else {
    if (optionsLine) {
      optionsLine.maintainAspectRatio = true;
    }
    if (optionsBar) {
      optionsBar.maintainAspectRatio = true;
    }
  }
}

function updateLineChart() {
  if (lineChart) {
    lineChart.options = optionsLine;
    lineChart.update();
  }
}

function updateBarChart() {
  if (barChart) {
    barChart.options = optionsBar;
    barChart.update();
  }
}

function reloadPage() {
  setTimeout(function() {
    window.location.reload();
  }); // Reload the page so that charts will display correctly
}

function drawCalendar() {
  if ($("#calendar").length) {
    $("#calendar").fullCalendar({
      height: 400,
      events: [
        {
          title: "Meeting",
          start: "2018-09-1",
          end: "2018-09-2"
        },
        {
          title: "Marketing trip",
          start: "2018-09-6",
          end: "2018-09-8"
        },
        {
          title: "Follow up",
          start: "2018-10-12"
        },
        {
          title: "Team",
          start: "2018-10-17"
        },
        {
          title: "Company Trip",
          start: "2018-10-25",
		  end: "2018-10-27"
        },
        {
          title: "Review",
          start: "2018-11-12"
        },
        {
          title: "Plan",
          start: "2018-11-18"
        }
      ],
      eventColor: "rgba(54, 162, 235, 0.4)"
    });
  }
}
