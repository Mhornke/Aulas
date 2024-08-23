import { PrismaClient } from "@prisma/client"
import { Router } from "express"

import { verificaToken } from "../middewares/verificaToken"

const prisma = new PrismaClient()

async function main() {
  /***********************************/
  /* SOFT DELETE MIDDLEWARE */
  /***********************************/
  prisma.$use(async (params, next) => {
    // Check incoming query type
    if (params.model == 'Mae') {
      if (params.action == 'delete') {
        // Delete queries
        // Change action to an update
        params.action = 'update'
        params.args['data'] = { deleted: true }
      }
    }
    return next(params)
  })
}
main()

const router = Router()

router.get("/", async (req, res) => {
  try {
    const maes = await prisma.mae.findMany({
      where: { deleted: false }
    })
    res.status(200).json(maes)
  } catch (error) {
    res.status(400).json(error)
  }
})

router.post("/", verificaToken, async (req: any, res) => {
  // dados que são fornecidos no corpo da requisição
  const { nome, endereco, telefone, datanasc } = req.body

  // dado que é acrescentado pelo Token (verificaToken) no req
  const { userLogadoId } = req

  if (!nome || !endereco || !telefone || !datanasc) {
    res.status(400).json({ erro: "Informe nome, endereco, telefone, datanasc " })
    return
  }

  try {
    const mae = await prisma.mae.create({
      data: { nome, endereco, telefone, datanasc, usuarioId: userLogadoId }
    })
    res.status(201).json(mae)
  } catch (error) {
    res.status(400).json(error)
  }
})

router.delete("/:id", verificaToken, async (req, res) => {
  const { id } = req.params

  try {
    const mae = await prisma.mae.delete({
      where: { id: Number(id) }
    })
    res.status(200).json(mae)
  } catch (error) {
    res.status(400).json(error)
  }
})

router.put("/:id", verificaToken, async (req, res) => {
  const { id } = req.params
  const { nome, endereco, telefone, datanasc } = req.body

  if (!nome || !endereco || !telefone || !datanasc) {
    res.status(400).json({ erro: "Informe nome, endereco, telefone e datanasc" })
    return
  }

  try {
    const mae = await prisma.mae.update({
      where: { id: Number(id) },
      data: { nome, endereco, telefone, datanasc }
    })
    res.status(200).json(mae)
  } catch (error) {
    res.status(400).json(error)
  }
})

export default router