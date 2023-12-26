import { useNavigate } from "react-router-dom";
import "../css/Toolbar.css"
import signOut from '../../firebase/auth_signout';
import { useData } from "../DataContext";

function Toolbar() {
    const { clearData } = useData();
    let navigate = useNavigate();
    const navigateTo = (path) => {
    navigate(path);
    };
    const handleSignOut = () => {
    signOut().then(() => {
    clearData();
  });
};
    return (
        <div className="toolbar">
            <button className="button-16" onClick={() => navigateTo('/')}>Home</button>
            <button className="button-16" onClick={() => navigateTo('/Graphs')}>Graphs</button>
            <button className="button-16" onClick={() => navigateTo('/About')}>About</button>
            <button className="button-16" onClick={() => navigateTo('/AdafruitIO')}>AdafruitIO</button>
            <button onClick={handleSignOut} className="sign-out-button">Sign Out</button>
        </div>
    );
};

export default Toolbar