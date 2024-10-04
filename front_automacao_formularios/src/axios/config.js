import axios from "axios";

const prodFetch = axios.create({
  baseURL: "http://localhost:5000",
  headers: {
    "Content-Type": "application/json",
  },
});

export default prodFetch;
