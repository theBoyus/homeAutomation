import { useNavigate } from "react-router-dom";
import "../css/Toolbar.css"

function Toolbar() {
    let navigate = useNavigate();
    const navigateTo = (path) => {
    navigate(path);
  };
    return (
        <div className="toolbar">
            <button className="button-16" onClick={() => navigateTo('/')}>Home</button>
            <button className="button-16" onClick={() => navigateTo('/Graphs')}>Graphs</button>
            <button className="button-16" onClick={() => navigateTo('/About')}>About</button>
        </div>
    );
};

export default Toolbar