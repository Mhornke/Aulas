import express from 'express'
import  Prisma  from '@prisma/client'
//import candidatasRoutes from './routes/candidatas'
import clientesRoutes from './routes/clientes'
import itensVendasRoutes from './routes/itensVenda'
const app = express()
// const port = 3000
const port = process.env.PORT ?? 3000

app.use(express.json())
//app.use("/candidatas", candidatasRoutes)
app.use("/clientes", clientesRoutes)
app.use("/votos", itensVendasRoutes)

app.get('/', (req, res) => {
  res.send('API: Sistema de Controle de Votos Rainha da Fenadoce')
})

app.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`)
})