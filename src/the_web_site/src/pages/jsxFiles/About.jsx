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
          <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eleifend sed nisl non dapibus. Praesent finibus eros at libero commodo, eu malesuada erat malesuada. Nulla pulvinar ligula eget neque posuere, in tempor dui pharetra. Nam ut tincidunt felis. Aliquam et ipsum mollis, vulputate libero non, pellentesque nisl. Etiam iaculis scelerisque lectus, et feugiat enim dictum vel. Vestibulum posuere consequat viverra. Phasellus ut sem tempor, feugiat nunc imperdiet, bibendum leo. Curabitur fringilla magna non mi convallis euismod. In hac habitasse platea dictumst. Integer quis tempor purus, a vulputate lacus.
</p>
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
