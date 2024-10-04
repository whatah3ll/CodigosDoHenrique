const express = require("express");
const multer = require("multer");
const XLSX = require("xlsx");
const mysql = require("mysql");

const app = express();
const PORT = process.env.PORT || 5000;

// Configuração do Multer para armazenar temporariamente o arquivo enviado
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

// Conectar ao MySQL (substitua com suas credenciais)
const connection = mysql.createConnection({
  host: "localhost",
  user: "seu_usuario_mysql",
  password: "sua_senha_mysql",
  database: "seu_banco_de_dados_mysql",
});

connection.connect((err) => {
  if (err) {
    console.error("Erro ao conectar ao MySQL:", err);
    throw err;
  }
  console.log("Conectado ao MySQL");
});

// Rota para upload do arquivo Excel
app.post("/upload", upload.single("file"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).send("Nenhum arquivo enviado.");
    }

    // Ler o arquivo Excel a partir dos dados no buffer
    const workbook = XLSX.read(req.file.buffer, { type: "buffer" });

    // Supondo que o primeiro sheet seja usado
    const sheet = workbook.Sheets[workbook.SheetNames[0]];

    // Mapear colunas no Excel para campos do formulário
    const formData = {
      campo1: "Título da Coluna 1",
      campo2: "Título da Coluna 2",
      // Adicione mais campos conforme necessário
    };

    // Array para armazenar todos os dados do Excel
    const dataFromExcel = [];

    // Iterar sobre todas as linhas do arquivo Excel
    const range = XLSX.utils.decode_range(sheet["!ref"]);
    for (let i = range.s.r + 1; i <= range.e.r; i++) {
      const rowData = {};
      Object.keys(formData).forEach((campo) => {
        const tituloColuna = formData[campo];
        const celula =
          sheet[
            XLSX.utils.encode_cell({
              r: i,
              c: sheet["!ref"].split(":")[1].replace(/\d/g, ""),
            })
          ];
        const valor = sheet[`${celula.c}${celula.r}`]?.v;
        rowData[campo] = valor;
      });
      dataFromExcel.push(rowData);
    }

    // Salvar os dados no banco de dados MySQL
    const insertQuery = "INSERT INTO formulario (campo1, campo2) VALUES ?";
    const values = dataFromExcel.map((obj) => [
      obj.campo1,
      obj.campo2 /* Adicione mais campos conforme necessário */,
    ]);

    connection.query(insertQuery, [values], (error, results) => {
      if (error) {
        console.error("Erro ao inserir dados no MySQL:", error);
        return res
          .status(500)
          .send("Erro ao enviar dados para o banco de dados.");
      }
      console.log("Dados inseridos no MySQL com sucesso:", results);
      res.json({
        message: "Dados enviados para o banco de dados com sucesso.",
      });
    });
  } catch (error) {
    console.error("Erro ao processar o arquivo:", error);
    res.status(500).send("Erro ao processar o arquivo.");
  }
});

// Iniciar o servidor
app.listen(PORT, () => {
  console.log(`Servidor iniciado na porta ${PORT}`);
});
