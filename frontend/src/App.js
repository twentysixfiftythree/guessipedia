import logo from "./logo.svg";
import React, { useEffect, useState } from "react";
//import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Select from "react-select";
import AsyncSelect from "react-select/async";
import { Wikis } from "./components/Wikis";
import { AutoCompleteBar, LoadWikis } from "./components/AutoComplete";
import Message from "./components/Message";
import ListGroup from "./components/ListGroup";

function App() {
  const [wikis, setWikis] = React.useState([]);

  useEffect(() => {
    fetch("/get_wikis").then((response) =>
      response.json().then((data) => {
        setWikis(data.wikis);
      })
    );
  }, []);

  return (
    <>
      <div className="text-bg-dark p-3">Guessipedia</div>
      <div
        className="App bg-secondary text-white d-flex align-items-center justify-content-center"
        style={{ height: "100vh" }}
      >
        <div className="col-md-4">
          <AutoCompleteBar className="bg-success" />
        </div>
      </div>
    </>
  );
}

export default App;
