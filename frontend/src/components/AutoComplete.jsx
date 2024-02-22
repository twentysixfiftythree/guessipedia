import React from "react";
import AsyncSelect from "react-select/async";

//returns a JSON object of all the wiki names fetched from the backend
//I think this can be done in a much simpler way
function LoadWikis() {
  const [wikis, setWikis] = React.useState([]);
  React.useEffect(() => {
    fetch("/get_wiki_name", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }).then((response) =>
      response.json().then((data) => {
        //console.log(data);
        setWikis(data.wikis);
      })
    );
  }, []);
  return wikis;
}

//creates an autocomplete bar for the wiki names
export const AutoCompleteBar = (props) => {
  //let options = LoadWikis();
  const options = LoadWikis();

  const handleChange = (selectedOption) => {
    console.log("handleChange", selectedOption);
    fetch("/check_wiki", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ wiki: selectedOption.label }),
    }).then((response) => {
      response.json().then((data) => {
        console.log("data_sent = ", data);
      });
    });
    return <div>data</div>;
  };
  const loadOptions = (searchValue, callback) => {
    setTimeout(() => {
      const filteredOptions = options.filter((option) =>
        option.label.toLowerCase().startsWith(searchValue.toLowerCase())
      );
      console.log("loadOptions", searchValue, filteredOptions);
      console.log("options", options);
      callback(filteredOptions);
    }, 0);
  };
  const customStyles = {
    control: (provided) => ({
      ...provided,
      backgroundColor: "#212529",
    }),
    menu: (provided) => ({
      ...provided,
      backgroundColor: "#212529",
    }),
    option: (provided, state) => ({
      ...provided,
      color: "white",
      backgroundColor: "#212529",
    }),
    singleValue: (provided) => ({
      ...provided,
      color: "white",
    }),
    input: (provided) => ({
      ...provided,
      color: "white",
    }),
  };
  return (
    <AsyncSelect
      loadOptions={loadOptions}
      onChange={handleChange}
      styles={customStyles}
    />
  );
};
