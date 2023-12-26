import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import app from './firebaseConfig';

const auth = getAuth(app);

const signIn = (email, password) => {

  return signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      const user = userCredential.user;
      return user;
    })
    .catch((error) => {
      const errorMessage = error.message;
      throw new Error(errorMessage);
    });
};

export default signIn;
