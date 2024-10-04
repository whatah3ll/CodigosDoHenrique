import express, { json } from "express";
import routes from "./routes.js";
import cors from "cors";

const App = express();

App.use(express.json());

App.use(cors());

App.use(routes);

export default App;
