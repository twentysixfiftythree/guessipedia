import React, { useState, useRef } from "react";
import {
  AiFillGithub,
  AiFillSetting,
  AiFillQuestionCircle,
} from "react-icons/ai";
import SettingsMenu from "./pages/SettingsMenu";
import { link } from "react-router-dom";
import { CSSTransition } from "react-transition-group";

const NavBar = () => {
  const [showSettings, setShowSettings] = useState(false);
  const nodeRef = useRef(null);
  console.log(showSettings);
  return (
    <>
      <div
        className=" relative top-0 left-0 w-full h-14 m-0 
                    flex flex-row justify-between items-center bg-gray-700 text-white shadow-md"
      >
        <h1 className="ml-4 text-yellow-500">Guessipedia</h1>
        <NavBarIcons setShowSettings={setShowSettings} />
        <h2>
          <CSSTransition
            in={showSettings}
            timeout={300}
            classNames="settings"
            nodeRef={nodeRef}
            unmountOnExit
          >
            <div ref={nodeRef}>
              <SettingsMenu setShowSettings={setShowSettings} />
            </div>
          </CSSTransition>
        </h2>
      </div>
    </>
  );
};

const NavBarIcons = ({ setShowSettings }) => {
  return (
    <div
      className="top-0 left-0 w-full h-10 m-0 
      flex flex-row justify-end items-center bg-gray-700 text-white "
    >
      <Icon
        icon={
          <AiFillSetting size="24" onClick={() => setShowSettings((v) => !v)} />
        }
      />
      <Icon icon={<AiFillQuestionCircle size="24" />} />
      <Icon icon={<AiFillGithub size="24" />} href="https://github.com" />
    </div>
  );
};

const Icon = ({ icon, href }) => {
  return (
    <a href={href} target="_blank" className="sidebar-icon mx-2">
      {icon}
    </a>
  );
};

export default NavBar;
