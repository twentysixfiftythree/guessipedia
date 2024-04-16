import logo from "./logo.svg";
import "./App.css";
import NavBar from "./components/NavBar";

import PullWiki from "./components/django_api";
import { AutoCompleteBar } from "./components/AutoComplete";
import React, { useEffect, useState, useRef, useCallback } from "react";
import axios from "axios";

function App() {
  const [pageToGuess, setPageToGuess] = useState("");
  const [surroundingLinks, setSurroundingLinks] = useState("");
  const [surroundingTitles, setSurroundingTitles] = useState("");
  const [categories, setCategories] = useState("");
  const [allTitles, setAllTitles] = useState("");
  const [result, setResult] = useState("");
  const fetched = useRef(false);

  const handleSelect = useCallback(
    (selectedOption) => {
      console.log(selectedOption);
      if (selectedOption === pageToGuess) {
        setResult("Correct");
      } else {
        setResult("Incorrect");
      }
    },
    [pageToGuess]
  );

  const handlSearchValueChange = useCallback((value) => {
    console.log(value);
  }, []);

  useEffect(() => {
    if (!fetched.current) {
      axios
        .get("http://localhost:8000/wikis/get-page-data/")
        .then((response) => {
          setPageToGuess(response.data.title);

          setSurroundingTitles(JSON.parse(response.data.surrounding_titles));

          setCategories(JSON.parse(response.data.categories));

          setAllTitles(JSON.parse(response.data.all_titles));

          console.log(response.data.categories);
          fetched.current = true;
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }, []);
  console.log(allTitles);
  return (
    <>
      <NavBar />
      <PullWiki
        message={pageToGuess}
        surroundingLinks={surroundingLinks}
        surroundingTitles={surroundingTitles}
        categories={categories}
      />
      <AutoCompleteBar
        options={allTitles}
        onSelect={handleSelect}
        onSearchValueChange={handlSearchValueChange}
      />
      <p>You have Guessed {result}</p>
    </>
  );
}

export default App;
