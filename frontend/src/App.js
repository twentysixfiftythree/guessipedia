import logo from './logo.svg';
import React, { useEffect, useState } from 'react';
import './App.css';
import { Wikis } from './components/Wikis';
import { AutoCompleteBar } from './components/AutoComplete';
import Select from 'react-select';
import AsyncSelect from 'react-select/async';



function App() {
 
  const [wikis, setWikis] = React.useState([]);

 
  useEffect(() => {
    fetch('/get_wikis').then(response => 
      response.json().then(data => {
      //console.log(data);
      setWikis(data.wikis);
    })
  );
  }, []);

  console.log(wikis);

  return (
    <div className="App">
      <Wikis wikis={wikis}/>
      <AutoCompleteBar/>
    </div>

  );
}

export default App;
