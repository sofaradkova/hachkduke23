<script>
  import { onMount } from "svelte";
  import Chart from "chart.js/auto";

  let chart; // Variable to store the chart instance

  const chartData = {
    labels: ["Travel", "Food", "Transport", "Other", "Rent"],
    datasets: [
      {
        data: [12, 19, 3, 5, 2],
        backgroundColor: [
          "#0D0630",
          "#8BBEB2",
          "#18314F",
          "#384E77",
          "#E6F9AF",
        ],
      },
    ],
  };

  const chartConfig = {
    type: "doughnut",
    data: chartData,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "left",
        },
      },
    },
  };

  // Create the chart when the component mounts
  onMount(() => {
    const ctx = document.getElementById("doughnut-chart").getContext("2d");
    chart = new Chart(ctx, chartConfig);
  });
</script>

<canvas id="doughnut-chart" width="400" height="400" />
