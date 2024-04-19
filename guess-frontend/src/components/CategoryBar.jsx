import React, { useState, useEffect } from "react";

export const CategoryBar = ({ categories }) => {
  const [catIndex, setCatIndex] = useState(0);

  useEffect(() => {
    if (Object.keys(categories).length > 0) {
      const cat_index = Math.floor(
        Math.random() * Object.keys(categories).length
      );
      setCatIndex(cat_index);
    }
  }, [categories]);

  return (
    <div className="grid, col-span-3">
      <div className="categoryBox">
        {decodeURIComponent(categories[catIndex])}
      </div>
    </div>
  );
};

export default CategoryBar;
