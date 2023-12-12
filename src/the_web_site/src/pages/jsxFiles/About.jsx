import React, { useState } from "react";
import "../css/About.css";

function About() {
  return (
    <div className="mainContainer">
      <h2>About</h2>
      <div className="aboutUsContiner">
        <div className="titleBox1">
          <h3>Who are we</h3>
        </div>
        <div className="txtContainer1">
          <p>Some text goes here.</p>
        </div>
      </div>
      <div>
        <div>
          <div className="titleBox2">
            <h3>Links</h3>
          </div>
          <div className="txtContainer1">
          <p>Link to our: 
            <a href="https://gitlab.lnu.se/ll224hf/homeautomation">Repository</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
