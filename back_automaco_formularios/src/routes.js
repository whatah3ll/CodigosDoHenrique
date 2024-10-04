import { Router } from "express";
import FormControler from "./app/controlers/FormControler.js";
import { storage } from "./multerConfig.js";
import multer from "multer";

const router = new Router();

const upload = multer({ storage: storage });
//rota para adicionar o produto
router.post("/formulario", FormControler.add);

router.post("/autoForm", upload.single("file"), FormControler.auto);

export default router;
