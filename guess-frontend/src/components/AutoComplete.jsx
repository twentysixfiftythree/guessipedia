import React, { useState, useEffect } from "react";

export const AutoCompleteBar = ({ options, onSelect }) => {
  const [searchValue, setSearchValue] = useState("");
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
  }, [searchValue, options]);

  const handleOptionClick = (option) => {
    setSearchValue(option);
    setFilteredOptions([]);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      onSelect(searchValue);
    } else if (event.key === "Tab") {
      event.preventDefault(); // Prevent the default action
      if (filteredOptions.length > 0) {
        setSearchValue(filteredOptions[0]);
      }
    }
  };

  useEffect(() => {
    if (searchValue === filteredOptions[0]) {
      setFilteredOptions([]);
    }
  }, [searchValue, filteredOptions]);

  return (
    <div className="w-72">
      <input
        type="text"
        value={searchValue}
        onChange={(e) => setSearchValue(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Search..."
        className="w-full p-2 text-sm border border-gray-300 rounded-md" // Tailwind CSS classes
      />
      <div className="mt-2 border border-gray-300 rounded-md overflow-auto max-h-48">
        {" "}
        {/* Tailwind CSS classes */}
        {filteredOptions.map((option, index) => (
          <div
            key={index}
            onClick={() => handleOptionClick(option)}
            className="p-2 cursor-pointer hover:bg-gray-200" // Tailwind CSS classes
          >
            {option}
          </div>
        ))}
      </div>
    </div>
  );
};

export default AutoCompleteBar;
