import logo from "./logo.svg";
import "./App.css";
import NavBar from "./components/NavBar";

import DisplayHints from "./components/DisplayHints";
import { AutoCompleteBar } from "./components/AutoComplete";
import { CategoryBar } from "./components/CategoryBar";
import { ResultStatistics } from "./components/ResultStatistics";
import React, { useEffect, useState, useCallback } from "react";
import axios from "axios";

function App() {
  const [searchValue, setSearchValue] = useState("");
  const [hiddenHints, setHiddenHints] = useState([
    1, 2, 4, 5, 7, 8, 10, 11, 13, 14,
  ]);
  const [showResults, setShowResults] = useState(false);

  const [wikiData, setwikiData] = useState({
    pageToGuess: "",
    surroundingTitles: "",
    categories: "",
    allTitles: "",
  });

  const [gameStats, setGameStats] = useState({
    score: 100,
    hintsUsed: 0,
    wrongGuesses: 0,
    guessResult: "",
  });

  const resetGame = () => {
    fetchAPI();
    setHiddenHints([1, 2, 4, 5, 7, 8, 10, 11, 13, 14]);
    setGameStats({
      score: 100,
      hintsUsed: 0,
      wrongGuesses: 0,
      guessResult: "",
    });
  };

  const handleSelect = useCallback(
    (selectedOption, score) => {
      console.log(selectedOption);
      if (selectedOption.toLowerCase() === wikiData.pageToGuess.toLowerCase()) {
        setGameStats((prevStats) => ({
          ...prevStats,
          guessResult: "Correct",
        }));

        setShowResults(true);
      } else {
        console.log(score);
        setGameStats((prevStats) => ({
          ...prevStats,
          score: prevStats.score - 10,
          wrongGuesses: prevStats.wrongGuesses + 1,
          guessResult: "Incorrect",
        }));
      }
    },
    [wikiData.pageToGuess]
  );

  const updateHints = () => {
    if (hiddenHints.length !== 0) {
      setGameStats((prevStats) => ({
        ...prevStats,
        score: prevStats.score - 20,
        hintsUsed: prevStats.hintsUsed + 1,
      }));
      if (hiddenHints.length % 2 === 0) {
        setHiddenHints([2, 5, 8, 11, 14]);
      } else if (hiddenHints.length % 2 === 1) {
        setHiddenHints([]);
      }
    }
  };

  const fetchAPI = () => {
    axios
      .get("http://localhost:8000/wikis/get-page-data/")
      .then((response) => {
        setwikiData({
          pageToGuess: response.data.title,
          surroundingTitles: JSON.parse(response.data.surrounding_titles),
          categories: JSON.parse(response.data.categories),
          allTitles: JSON.parse(response.data.all_titles),
        });
        setSearchValue("");
      })
      .catch((error) => {
        console.log(error);
      });
  };
  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <div className="fixed bg-gray-600 h-screen w-screen overscroll-none">
        <NavBar />
        {showResults && (
          <div className="absolute top-0 left-0 w-full h-full z-20">
            <ResultStatistics
              gameStats={gameStats}
              setShowResults={setShowResults}
              resetGame={resetGame}
              showResults={showResults}
            />
          </div>
        )}
        <div className="flex justify-between items-center">
          <div className="flex-1"></div>
          <div className="flex justify-center z-10">
            <CategoryBar categories={wikiData.categories} />
          </div>
          <div className="flex justify-end flex-1">
            <button className="newGameButton w-24 z-10" onClick={resetGame}>
              New Game
            </button>
          </div>
        </div>

        <DisplayHints wikiData={wikiData} hiddenBoxes={hiddenHints} />
        <div className="justify-center flex relative">
          <button className="button" onClick={updateHints}>
            Hint
          </button>
          <AutoCompleteBar
            options={wikiData.allTitles}
            onSelect={handleSelect}
            searchValue={searchValue}
            setSearchValue={setSearchValue}
            score={gameStats.score}
          />

          <button
            className="button"
            onClick={() => {
              handleSelect(searchValue, gameStats.score);
              setSearchValue("");
            }}
          >
            Go
          </button>
        </div>
        <div className="justify-center flex text-yellow-500">
          <p>Guess {gameStats.guessResult}</p>
        </div>
      </div>
    </>
  );
}

export default App;
