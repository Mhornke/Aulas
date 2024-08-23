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
    if (params.model == 'Medico') {
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
    const medicos = await prisma.medico.findMany({
      
    })
    res.status(200).json(medicos)
  } catch (error) {
    res.status(400).json(error)
  }
})

router.post("/", verificaToken, async (req: any, res) => {
  // dados que são fornecidos no corpo da requisição
  const { nome, crm, celular, especialidade } = req.body

  // dado que é acrescentado pelo Token (verificaToken) no req
  const { userLogadoId } = req

  if (!nome || !crm || !celular || !especialidade) {
    res.status(400).json({ erro: "Informe nome, crm, celular e especialidade " })
    return
  }

  try {
    const medico = await prisma.medico.create({
      data: { nome, crm, celular, especialidade, usuarioId: userLogadoId }
    })
    res.status(201).json(medico)
  } catch (error) {
    res.status(400).json(error)
  }
})

router.delete("/:id", async (req, res) => {
    const { id } = req.params
  
    try {
      const medico = await prisma.medico.delete({
        where: { id: Number(id) }
      })
      res.status(200).json(medico)
    } catch (error) {
      res.status(400).json(error)
    }
  })
  
  router.put("/:id", async (req, res) => {
    const { id } = req.params
    const { nome, crm, celular, especialidade } = req.body
  
    if (!nome || !crm || !celular || !especialidade) {
      res.status(400).json({ "erro": "Informe nome, crm, celular e especialidade" })
      return
    }
  
    try {
      const medico = await prisma.medico.update({
        where: { id: Number(id) },
        data: { nome, crm, celular, especialidade }
      })
      res.status(200).json(medico)
    } catch (error) {
      res.status(400).json(error)
    }
  })

export default router