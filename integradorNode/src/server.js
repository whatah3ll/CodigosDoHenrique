import App from "./app.js";

const PORT = process.env.PORT | 5000;

App.listen(PORT, () => {
  console.log(`Servidor rodando no endereço http://localhost:${PORT}`);
});
