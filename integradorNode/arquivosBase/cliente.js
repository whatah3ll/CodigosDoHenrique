import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [formDataList, setFormDataList] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await axios.post(
        "http://localhost:5000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setFormDataList(response.data);
      setCurrentIndex(0); // Começar com o primeiro conjunto de dados do Excel
      setError(null);
    } catch (error) {
      console.error("Erro ao fazer upload do arquivo:", error);
      setError("Erro ao processar o arquivo.");
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Enviar os dados atuais para o servidor (formDataList[currentIndex])
      const response = await axios.post(
        "http://localhost:5000/enviar-dados",
        formDataList[currentIndex]
      );

      console.log("Dados enviados para o banco de dados:", response.data);

      // Limpar o formulário atual
      setFormDataList([]);
      setCurrentIndex(0);
      setError(null);
    } catch (error) {
      console.error("Erro ao enviar dados para o banco de dados:", error);
      setError("Erro ao enviar dados para o banco de dados.");
    }
  };

  const handleNext = () => {
    setCurrentIndex(currentIndex + 1);
  };

  return (
    <div className="App">
      <h1>Upload de Arquivo Excel e Preenchimento Automático</h1>

      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Enviar</button>

      {error && <p>{error}</p>}

      {formDataList.length > 0 && (
        <div>
          <h2>Formulário Automático</h2>
          <form onSubmit={handleSubmit}>
            <label htmlFor="campo1">Campo 1:</label>
            <input
              type="text"
              id="campo1"
              name="campo1"
              value={formDataList[currentIndex].campo1 || ""}
              readOnly
            />
            <br />
            <br />

            <label htmlFor="campo2">Campo 2:</label>
            <input
              type="text"
              id="campo2"
              name="campo2"
              value={formDataList[currentIndex].campo2 || ""}
              readOnly
            />
            <br />
            <br />

            {/* Adicione mais campos conforme necessário */}

            <button type="submit">Enviar para o Banco de Dados</button>
            <button
              type="button"
              onClick={handleNext}
              disabled={currentIndex === formDataList.length - 1}
            >
              Próximo
            </button>
          </form>
        </div>
      )}
    </div>
  );
}

export default App;
