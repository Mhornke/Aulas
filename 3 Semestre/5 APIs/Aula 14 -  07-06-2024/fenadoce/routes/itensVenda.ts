import { PrismaClient } from "@prisma/client"
import { Router } from "express"

const prisma = new PrismaClient()
const router = Router()

router.get("/", async (req, res) => {
  try {
    const itensVenda = await prisma.itensVenda.findMany({
      include: {
        venda: true,
        medicamento: true
      }
    })
    res.status(200).json(itensVenda)
  } catch (error) {
    res.status(400).json(error)
  }
})

router.post("/", async (req, res) => {
  const { vendaId, medicamentoId, quant, preco } = req.body

  if (!vendaId || !medicamentoId || !quant || !preco) {
    res.status(400).json({ "erro": "Informe vendaId, medicamentoId, preco e quant" })
    return
  }

  try { //transação --
    const [itensVenda, venda, medicamento] = await prisma.$transaction([
      prisma.itensVenda.create({
         data: { medicamentoId, vendaId, quant, preco}
         }),
      prisma.venda.update({ 
        where: { id: vendaId }, data: { total: { increment: quant * preco } }
       }),
       prisma.medicamento.update({
        where:{ id: medicamentoId},
        data: { quant: {decrement: quant}}
       })
    ])
    res.status(201).json({ itensVenda, venda, medicamento })
  } catch (error) {
    res.status(400).json(error)
  }
})

router.delete("/:id", async (req, res) => {
  const { vendaId, medicamentoId, quant, preco} = req.body

  if (!vendaId || !medicamentoId || !quant ) {
    res.status(400).json({ "erro": "Informe vendaId, medicamentoId, preco e quant" })
    return
  }

  try { //transação --
    const [itensVenda, venda, medicamento] = await prisma.$transaction([
      prisma.itensVenda.create({
         data: { medicamentoId, vendaId, quant, preco}
         }),
      prisma.venda.update({ 
        where: { id: vendaId }, data: { total: { decrement: quant * preco } }
       }),
       prisma.medicamento.update({
        where:{ id: medicamentoId},
        data: { quant: {increment: quant}}
       })
    ])
    res.status(201).json({ itensVenda, venda, medicamento })
  } catch (error) {
    res.status(400).json(error)
  }
})
export default router