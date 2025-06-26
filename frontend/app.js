fetch("http://127.0.0.1:5001/api/health-data")
  .then((response) => response.json())
  .then((data) => {
    const bmiData = data.bmi_by_region;
    const chargesData = data.charges_by_smoker;

    Plotly.newPlot("bmiChart", [
      {
        x: bmiData.map((d) => d.region),
        y: bmiData.map((d) => d.avg_bmi),
        type: "bar",
      },
    ]);

    Plotly.newPlot("chargesChart", [
      {
        x: chargesData.map((d) => d.smoker),
        y: chargesData.map((d) => d.avg_charges),
        type: "bar",
      },
    ]);
  });
