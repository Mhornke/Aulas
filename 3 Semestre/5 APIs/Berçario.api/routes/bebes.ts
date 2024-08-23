import { PrismaClient } from "@prisma/client"
import { Router } from "express"

import { verificaToken } from "../middewares/verificaToken"
import { connect } from "http2"

const prisma = new PrismaClient()

async function main() {
  /***********************************/
  /* SOFT DELETE MIDDLEWARE */
  /***********************************/
  prisma.$use(async (params, next) => {
    // Check incoming query type
    if (params.model == 'Bebe') {
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

const validaEtapaBebe = (req: any, res: any, next: any) => {

  const {etapa} = req.body.mae;
  const {nome, datanasc, peso, altura, sexo} = req.body

  if(etapa == 'RecemNascido'){
    if(!nome || !datanasc || !peso || !altura || !sexo)
        return res.status(400).json({error: 'Campos obrigarotios para Recém Nascido não preenchido '})

  }
  next()
}

router.post("/", verificaToken, validaEtapaBebe, async (req: any, res) => {
  // dados que são fornecidos no corpo da requisição
  const { nome, datanasc, peso, altura, sexo, etapa, maeId, medicoId } = req.body

  // dado que é acrescentado pelo Token (verificaToken) no req
  const { userLogadoId } = req
  

  try {
    const bebe = await prisma.bebe.create({
      data: { 
        nome,
        datanasc,
        peso,
        altura,
        sexo,
        etapa,
        mae: {connect:{id: maeId}},
        medico: {connect: { id: medicoId}},
        usuario: { connect: { id: userLogadoId}}
      }
    })
    res.status(201).json(bebe)
  } catch (error: unknown) {
    //teste feito pelo chatGbt
    console.error("Error creating Bebe:", error)
    if (error instanceof Error) {
        res.status(400).json({ error: error.message })
      } else {
        res.status(400).json({ error: "Unknown error occurred" })
      }
  }
})

router.delete("/:id", verificaToken, async (req, res) => {
  const { id } = req.params

  try {
    const bebe = await prisma.bebe.delete({
      where: { id: Number(id) }
    })
    res.status(200).json(bebe)
  } catch (error) {
    res.status(400).json(error)
  }
})

router.put("/:id", verificaToken, async (req, res) => {
  const { id } = req.params
  const { nome, datanasc, peso, altura, sexo, etapa } = req.body

  if (!nome || !datanasc || !peso || !altura || !sexo || !etapa) {
    res.status(400).json({ erro: "Informe nome, datanasc, peso, altura e etapa" })
    return
  }

  try {
    const bebe = await prisma.bebe.update({
      where: { id: Number(id) },
      data:  {nome, datanasc, peso, altura, sexo, etapa }
    })
    res.status(200).json(bebe)
  } catch (error) {
    res.status(400).json(error)
  }
})

export default router