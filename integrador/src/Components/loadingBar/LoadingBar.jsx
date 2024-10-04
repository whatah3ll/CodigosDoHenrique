// src/LoadingBar.js
import React from "react";
import "./LoadingBar.css";

const LoadingBar = ({ percentage }) => {
  return (
    <div className="loading-bar">
      <div
        className="loading-bar-progress"
        style={{ width: `${percentage}%` }}
      ></div>
    </div>
  );
};

export default LoadingBar;
