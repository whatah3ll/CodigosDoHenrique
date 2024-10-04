import FormRepositorie from "../repositories/FormRepositorie.js";
import XLSX from "xlsx";

const dbPath = "./src/db/database.db";
const repositorie = new FormRepositorie(dbPath);
class FormControler {
  async add(req, res) {
    console.log(req.body);
    const { produto, precobase, tipo, multimposto, precoreais } = req.body;
    console.log(produto, precobase, tipo, multimposto, precoreais);
    try {
      const lastID = await repositorie.insertProd(
        produto,
        precobase,
        tipo,
        multimposto,
        precoreais
      );
      console.log("Produto inserido com ID:", lastID);
      res.status(200).send(lastID);
    } catch (err) {
      console.error("Erro ao inserir o produto:", err);
    }
  }

  async auto(req, res) {
    if (!req.file) {
      console.log("Não foi possivel acessar o arquivo!");
      // return res.status(400).send("Nenhum arquivo enviado.");
    }
    console.log(JSON.parse(JSON.stringify(req.file)));
    const wb = XLSX.read(req.file.buffer, { type: "buffer" });
    const ws = wb.Sheets[wb.SheetNames[0]];
    const data = XLSX.utils.sheet_to_json(ws);
    res.status(200).send(data);
  }
}

export default new FormControler();
