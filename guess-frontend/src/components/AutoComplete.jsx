import React, { useState, useEffect } from "react";

export const AutoCompleteBar = ({
  options,
  onSelect,
  searchValue,
  setSearchValue,
  score,
}) => {
  const [filteredOptions, setFilteredOptions] = useState([]);

  useEffect(() => {
    if (searchValue) {
      const filtered = options.filter((option) =>
        option.toLowerCase().includes(searchValue.toLowerCase())
      );
      setFilteredOptions(filtered);
    } else {
      setFilteredOptions([]);
    }
    //clear search options when the option typed is a valid option
    if (searchValue === filteredOptions[0]) {
      setFilteredOptions([]);
    }
  }, [searchValue, options]);

  //set the search value to the option clicked
  const handleOptionClick = (option) => {
    if (filteredOptions.length > 0) {
      setSearchValue(filteredOptions[0]);
    }
  };

  //Handles enter key press and tab autofilling
  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      onSelect(searchValue, score);
      setSearchValue("");
    } else if (event.key === "Tab") {
      event.preventDefault(); // Prevent the default action
      if (filteredOptions.length > 0) {
        setSearchValue(filteredOptions[0]);
      }
    }
  };

  return (
    <>
      <div className="flex items-center justify-center">
        <div className="w-72 my-4 ">
          <input
            type="text"
            value={searchValue}
            onChange={(e) => setSearchValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Guess a wiki..."
            className="w-full p-2 text-sm bg-gray-700 text-white placeholder-yellow-600 border border-black rounded-md" // Tailwind CSS classes
          />
          <div className=" bg-gray-800 border-gray-600 rounded-md overflow-auto max-h-48 fixed w-72 border-t-0">
            {filteredOptions.map((option, index) => (
              <div
                key={index}
                onClick={() => handleOptionClick(option)}
                className="p-2 cursor-pointer text-white hover:bg-gray-700" // Tailwind CSS classes
              >
                {option}
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default AutoCompleteBar;
