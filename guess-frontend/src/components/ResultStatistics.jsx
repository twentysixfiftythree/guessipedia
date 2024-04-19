import React from "react";
import useOnclickOutside from "react-cool-onclickoutside";
import BarChart from "./BarChart";
import axios from "axios";
import { useEffect, useState } from "react";

const add_To_db = (score) => {
  axios
    .post("http://localhost:8000/wikis/add-score/", {
      score: score,
    })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
};

export const ResultStatistics = ({
  gameStats,
  showResults,
  setShowResults,
  resetGame,
}) => {
  const ref = useOnclickOutside(() => {
    setShowResults(false);
    resetGame();
  });

  const [scoreStats, setScoreStats] = useState("");

  const getScoreStats = () => {
    axios
      .get("http://localhost:8000/wikis/send-stats/")
      .then((response) => {
        console.log("semen", response.data.scores);
        setScoreStats(response.data.scores);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(() => {
    if (showResults) {
      getScoreStats();
      console.log("butthole", scoreStats);
      add_To_db(gameStats.score); // Replace 696969 with the actual score
    }
  }, [showResults]);

  return (
    <>
      <div className="resultStats bg-opacity-75">
        {gameStats.guessResult}

        <div
          ref={ref}
          className="w-3/5 h-5/6 flex justify-left p-10 rounded-lg bg-gray-800 z-10 absolute"
        >
          <div className="flex flex-col w-full">
            <div>
              <h1>You guessed Correct! </h1>
              <p>Score: {gameStats.score}</p>
            </div>
            {console.log("buttholefajgfks", scoreStats)}
            <BarChart
              dataPoints={[
                { label: "0-20", y: scoreStats.first },
                { label: "20-40", y: scoreStats.second },
                { label: "40-60", y: scoreStats.third },
                { label: "60-80", y: scoreStats.fourth },
                { label: "80-100", y: scoreStats.fifth },
              ]}
            />
          </div>
        </div>
      </div>
    </>
  );
};
export default ResultStatistics;
