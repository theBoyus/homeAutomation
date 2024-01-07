import "../css/About.css";

function About() {
  return (
    <div className="aboutContainer">
      <h2 className="header">About</h2>
      <section className="aboutSection">
        <div className="titleBox">
          <h3>Who are we</h3>
        </div>
        <div className="txtContainer">
          <p>
            We are a group consisting of three engineers attending Linnaeus
            University. We created this website for our group project in the
            course 'Introduction to Projects,' focusing on home automation using
            lights to improve energy efficiency. This project will take place
            from the end of November to early January.
          </p>
        </div>
      </section>
      <section className="linksSection">
        <div className="titleBox">
          <h3>Links</h3>
        </div>
        <div className="txtContainer">
          <p>
            Link to our:
            <a href="https://gitlab.lnu.se/ll224hf/homeautomation">
              {" "}
              Repository
            </a>
          </p>
        </div>
      </section>
    </div>
  );
}

export default About;
