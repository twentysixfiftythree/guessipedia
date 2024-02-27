import React, { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import { AutoCompleteBar } from "./components/AutoComplete";
function App() {
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
