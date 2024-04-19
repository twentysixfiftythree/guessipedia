import React from "react";
import CanvasJSReact from "@canvasjs/react-charts";

var CanvasJSChart = CanvasJSReact.CanvasJSChart;

const BarChart = ({ dataPoints }) => {
  const options = {
    backgroundColor: "#1e293b",
    axisX: {
      labelFontColor: "white",
      tickColor: "white",
    },
    axisY: {
      labelFontColor: "white",
      tickColor: "white",
    },

    data: [
      {
        type: "column",
        dataPoints: dataPoints,
      },
    ],
  };

  return (
    <div>
      <CanvasJSChart options={options} />
    </div>
  );
};

export default BarChart;
