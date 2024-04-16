import React from "react";

const SettingsMenu = ({ setShowSettings }) => {
  return (
    <div
      className="absolute top-full right-0 flex justify-center m-0 h-40 
      w-1/4 rounded-2xl bg-gray-700 text-white shadow-md cursor-pointer "
    >
      <button onClick={() => setShowSettings((v) => !v)}> close</button>
    </div>
  );
};
export default SettingsMenu;
