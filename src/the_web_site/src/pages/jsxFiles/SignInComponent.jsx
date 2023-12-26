import React, { useEffect, useState } from 'react';
import signIn from '../../firebase/auth_signin_password';
import signOut from '../../firebase/auth_signout';
import { getMQTTCredentials } from '../../firebase/mqttUtils';
import { useAuth } from '../../firebase/useAuth';
import { useData } from '../DataContext';
import { useNavigate } from 'react-router-dom';
import "../css/SignInComponent.css"

const SignInComponent = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [mqttCredentials, setMqttCredentials] = useState(null);
  const { currentUser } = useAuth();
  const { data, updateData } = useData();
  const navigate = useNavigate();
  
  const handleSubmit = (e) => {
    e.preventDefault();
    signIn(email, password)
      .then(user => {
        console.log('Signed in user:', user);
        navigate('/');
      })
      .catch(error => {
        console.error('Error signing in:', error);
        setError(error.message);
      });
  };

  useEffect(() => {
  if (currentUser) {
    getMQTTCredentials(currentUser.uid)
      .then(credentials => {
        if (credentials && credentials.mqtt_password && credentials.mqtt_username) {
          setMqttCredentials(credentials);
          updateData('mqtt_password', credentials.mqtt_password);
          updateData('mqtt_username', credentials.mqtt_username);
        } else {
          console.log('MQTT credentials are not available.');
        }
      });
  }
}, [currentUser]);

  return (
    <div className="sign-in-container">
        <form onSubmit={handleSubmit} className="sign-in-form">
          <p className={`error-message ${error ? 'show' : ''}`}>
            {error ? "Wrong username or password" : ""}
          </p>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            required
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
            required
          />
          <button type="submit">Sign In</button>
        </form>
    </div>
  );
};

export default SignInComponent;
