new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["Python", "SQL", "AWS"],
    datasets: [{
      label: "Trending Skills",
      data: [10, 7, 5]
    }]
  }
});