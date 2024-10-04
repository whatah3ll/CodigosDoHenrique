import { useNavigate } from "react-router-dom";
import { useState } from "react";
import prodFetch from "../../axios/config";

import Container from "../Container/Container";
import Button from "../Button/Button";

import "./FileAdd.css";

function FileAdd() {
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState();
  const navigate = useNavigate();
  // const navigate = useNavigate();
  const handleChangeInput = (e) => {
    setFile(e.target.files[0]);
  };
  const onClickFunc = async () => {
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await prodFetch.post("/autoForm", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      // Salvar os dados no localStorage
      window.localStorage.setItem("produtos", JSON.stringify(res.data));
      // Navegar para a página desejada
      navigate("/formulario");
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    <Container>
      return <div>Loading...</div>;
    </Container>;
  }

  return (
    <div className="form">
      <h1>Importe um arquivo </h1>
      <label htmlFor="file" className="custom-file-upload">
        Escolha um arquivo
      </label>
      <input
        type="file"
        name="file"
        id="file"
        accept=".xlsx"
        onChange={handleChangeInput}
      />
      <div className="containerBtn">
        <Button className="buttonAdd" onClickFunc={onClickFunc}>
          Adicionar
        </Button>
      </div>
    </div>
  );
}

export default FileAdd;
