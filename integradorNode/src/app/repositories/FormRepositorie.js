import sqlite3 from "sqlite3";
sqlite3.verbose();
class FormRepositorie {
  constructor(dbFile) {
    this.db = new sqlite3.Database(dbFile, (err) => {
      if (err) {
        console.error("Erro ao abrir o banco de dados:", err.message);
      } else {
        console.log("Conectado ao banco de dados SQLite.");
        this.createTable(); // Cria a tabela ao inicializar
      }
    });
  }

  createTable() {
    const query = `
      CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        precobase TEXT NOT NULL,
        tipo TEXT NOT NULL,
        multimposto TEXT NOT NULL,
        precoreais TEXT NOT NULL
      )
    `;
    this.db.run(query, (err) => {
      if (err) {
        console.error("Erro ao criar tabela:", err.message);
        return { err: err };
      } else {
        console.log("Tabela criada com sucesso.");
        return { sucess: "sucesso" };
      }
    });
  }

  insertProd(produto, precobase, tipo, multimposto, precoreais) {
    const query =
      "INSERT INTO produtos (produto, precobase, tipo, multimposto, precoreais) VALUES (?, ?, ?, ?, ?)";

    return new Promise((resolve, reject) => {
      this.db.run(
        query,
        [produto, precobase, tipo, multimposto, precoreais],
        function (err) {
          if (err) {
            console.error("Erro ao inserir dados:", err.message);
            reject(err); // Rejeita a Promise em caso de erro
          } else {
            console.log(`Produto inserido com ID ${this.lastID}`);
            resolve(this.lastID); // Resolve a Promise com o ID da última inserção
          }
        }.bind(this)
      ); // Usa bind para manter o contexto de `this`
    });
  }

  getUsers(callback) {
    const query = "SELECT id, name, email FROM user";
    this.db.all(query, [], (err, rows) => {
      if (err) {
        console.error("Erro ao consultar dados:", err.message);
        callback(err);
      } else {
        callback(null, rows);
      }
    });
  }

  close() {
    this.db.close((err) => {
      if (err) {
        console.error("Erro ao fechar o banco de dados:", err.message);
      } else {
        console.log("Banco de dados fechado.");
      }
    });
  }
}

export default FormRepositorie;
