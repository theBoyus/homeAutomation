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
          <p>
            "We are a group consisting of three engineers attending Linneus
            University. We created this website for our group project in the
            course 'Introduction to Projects,' where we are focusing on home
            automation using lights to improve energy efficiency. This project
            will take place from the end of November to early January."
          </p>
        </div>
      </div>
      <div>
        <div className="secondContainer">
          <div className="titleBox2">
            <h3>Links</h3>
          </div>
          <div className="txtContainer1">
            <p>
              Link to our:
              <a href="https://gitlab.lnu.se/ll224hf/homeautomation">
                Repository
              </a>
            </p>
          </div>
        </div>
        <div>
          <div>
            <h3></h3>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
