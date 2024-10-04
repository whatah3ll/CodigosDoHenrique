import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./Pages/Home/Home";
import Form from "./Pages/Form/Form";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/formulario" element={<Form />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;
