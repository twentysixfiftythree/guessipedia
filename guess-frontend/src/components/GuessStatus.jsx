import React from "react";

export const GuessStatus = (props) => {
  let guessed = "";
  props.guess === 1 ? (guessed = "correctly") : (guessed = "incorrectly");

  return (
    <div className="card bg-dark text-white">
      <div className="card-body">
        <p className="card-text">You have guessed {guessed}</p>
      </div>
    </div>
  );
};
