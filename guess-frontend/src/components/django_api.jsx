import React, { useState, useEffect } from "react";
import axios from "axios";

function PullWiki({
  message,
  surroundingLinks,
  surroundingTitles,
  categories,
}) {
  const [indices, setIndices] = useState([]);
  const [catIndex, setCatIndex] = useState(0);

  useEffect(() => {
    if (
      Object.keys(surroundingTitles).length > 0 &&
      Object.keys(categories).length > 0
    ) {
      const json_length = Object.keys(surroundingTitles).length;
      const tempIndices = [];
      for (let i = 0; i < 5; i++) {
        let index = Math.floor(Math.random() * json_length);
        while (tempIndices.includes(index)) {
          index = Math.floor(Math.random() * json_length);
        }
        tempIndices.push(index);
      }
      setIndices(tempIndices);

      const cat_index = Math.floor(
        Math.random() * Object.keys(categories).length
      );
      setCatIndex(cat_index);
    }
  }, [surroundingTitles, categories]);

  return (
    <div>
      <h1 className="text-red-500 font-bold">Surrounding pages</h1>
      <ul>
        {indices.map((index) => (
          <li key={index}>{decodeURIComponent(surroundingTitles[index])}</li>
        ))}
      </ul>
      <h1 className="text-red-500 font-bold">Wiki Category</h1>
      <ul>
        <li>{decodeURIComponent(categories[catIndex])}</li>
      </ul>
    </div>
  );
}

export default PullWiki;
