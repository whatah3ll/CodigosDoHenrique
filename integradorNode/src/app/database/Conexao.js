import sqlite3 from "sqlite3";
import { open } from "sqlite";

// you would have to import / invoke this in another file
async function openDb() {
  return open({
    filename: "/tmp/database.db",
    driver: sqlite3.Database,
  });
}

export default openDb;
