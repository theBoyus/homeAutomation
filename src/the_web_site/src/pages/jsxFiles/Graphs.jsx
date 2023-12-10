import { useState } from "react";
import "../css/Graph.css";
function Graphs() {
  function importAllImages(r) {
    return r.keys().map(r);
  }
  const images = importAllImages(
    require.context("../../img", false, /\.(png|jpe?g|svg|gif)$/)
  );
  const [currentImage, setCurrentImage] = useState(images[0]);
  console.log(images);

  return (
    <div>
      <>selfies with the boys</>
      <div>
        {images.map((image, index) => (
          <button key={index} onClick={() => setCurrentImage(image)}>
            Image {index + 1}
          </button>
        ))}
      </div>
      <div className="graphImage">
        <img src={currentImage} alt="Graph" />
      </div>
    </div>
  );
}

export default Graphs;
