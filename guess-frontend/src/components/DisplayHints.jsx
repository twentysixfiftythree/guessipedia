import React, { useState, useEffect } from "react";

export const DisplayHints = ({ wikiData, hiddenBoxes }) => {
  const [indices, setIndices] = useState([]);

  useEffect(() => {
    if (
      Object.keys(wikiData.surroundingTitles).length > 0 &&
      Object.keys(wikiData.categories).length > 0
    ) {
      const json_length = Object.keys(wikiData.surroundingTitles).length;
      const tempIndices = [];
      for (let i = 0; i < 15; i++) {
        let index = Math.floor(Math.random() * json_length);
        while (tempIndices.includes(index)) {
          index = Math.floor(Math.random() * json_length);
        }
        tempIndices.push(index);
      }
      setIndices(tempIndices);

      const cat_index = Math.floor(
        Math.random() * Object.keys(wikiData.categories).length
      );
    }
  }, [wikiData.surroundingTitles, wikiData.categories]);

  console.log("boxes: ", hiddenBoxes);

  return (
    <>
      <div className="justify-center flex">
        <div className="grid grid-cols-3 gap-y-2 gap-x-2">
          {indices.map((index, i) => (
            <div key={i} className="hintBoxes break-words ">
              {!hiddenBoxes.includes(i) &&
                decodeURIComponent(wikiData.surroundingTitles[index])}
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default DisplayHints;
