import { useNavigate } from "react-router-dom";
import prodFetch from "../../axios/config.js";
import { useEffect, useState } from "react";
import LoadingBar from "../loadingBar/LoadingBar.jsx";
import Button from "../Button/Button";

import "./AutoForm.css";

function AutoForm() {
  const produtos = JSON.parse(window.localStorage.getItem("produtos"));
  const navigate = useNavigate();
  const [percentage, setPercentage] = useState(0);
  const [isSubmitting, setIsSubmitting] = useState(false);

  useEffect(() => {
    const handlePopState = (event) => {
      if (isSubmitting) {
        window.history.pushState(null, null, window.location.href);
      }
    };

    window.history.pushState(null, null, window.location.href);
    window.addEventListener("popstate", handlePopState);

    return () => {
      window.removeEventListener("popstate", handlePopState);
    };
  }, [isSubmitting]);

  const onClickFuncSair = () => {
    if (!isSubmitting) {
      navigate("/");
    }
  };

  const preencherEEnviar = async () => {
    const total = produtos.length;
    setIsSubmitting(true);
    for (let i = 0; i < total; i++) {
      const dado = produtos[i];
      document.getElementById("produto").value = dado["Produtos"];
      document.getElementById("tipo").value = dado["Tipo"];
      document.getElementById("precoOri").value = dado["Preço Base Original"];
      document.getElementById("imposto").value = dado["Multiplicador Imposto"];
      document.getElementById("precoReal").value = dado["Preço Base Reais"];
      await addProd();
      const newPercentage = ((i + 1) / total) * 100;
      setPercentage(newPercentage);
    }
    setIsSubmitting(false);
  };

  const addProd = async () => {
    const produto = document.getElementById("produto").value;
    const precobase = document.getElementById("tipo").value;
    const tipo = document.getElementById("precoOri").value;
    const multimposto = document.getElementById("imposto").value;
    const precoreal = document.getElementById("precoReal").value;
    try {
      await prodFetch.post("/formulario", {
        produto: produto,
        precobase: precobase,
        tipo: tipo,
        multimposto: multimposto,
        precoreais: precoreal,
      });
    } catch (error) {
      if (error.response) {
        console.log("Error response:", error.response);
      } else if (error.request) {
        console.log("Error request:", error.request);
      } else {
        console.log("Error message:", error.message);
      }
    }
  };

  useEffect(() => {
    preencherEEnviar();
  }, []);

  return (
    <div className="autoForm">
      <h1>Formulario de produtos</h1>
      <div className="containerProd">
        <div style={{ display: "flex", flexDirection: "column" }}>
          <label htmlFor="produto">Produto</label>
          <input
            type="text"
            name="produto"
            id="produto"
            placeholder="Digite o nome do produto:"
          />
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <label htmlFor="tipo">Tipo</label>
          <input type="text" name="tipo" id="tipo" placeholder="Serviço..." />
        </div>
      </div>
      <div className="containerPreco">
        <div style={{ display: "flex", flexDirection: "column" }}>
          <label htmlFor="precoOri">Preço</label>
          <input
            type="number"
            name="precoOri"
            id="precoOri"
            placeholder="Preço original:"
          />
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <label htmlFor="imposto">Imposto</label>
          <input
            type="number"
            name="imposto"
            id="imposto"
            placeholder="Multiplicador:"
          />
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <label htmlFor="precoReal">Preço real</label>
          <input
            type="number"
            name="precoReal"
            id="precoReal"
            placeholder="Preço em real:"
          />
        </div>
      </div>
      <div className="containerLoading">
        <LoadingBar percentage={percentage} />
      </div>
      <div className="containerBtns">
        <div className="containerBtnSalvar">
          <Button className="btnSalvar" onClickFunc={addProd}>
            Salvar
          </Button>
        </div>
        <div className="containerBtnSair">
          <Button className="btnSair" onClickFunc={onClickFuncSair}>
            Sair
          </Button>
        </div>
      </div>
    </div>
  );
}

export default AutoForm;
