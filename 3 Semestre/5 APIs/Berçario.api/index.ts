import express from 'express'
const app = express()
const port = 3000
import cors from 'cors'

import usuariosRoutes from './routes/usuarios'
import loginRoutes from './routes/login'
import maesRoutes from './routes/maes'
import medicosRoutes from './routes/medicos'
import bebesRoutes from './routes/bebes'
//import recuperaRoutes from './routes/recupera'

app.use(express.json())
app.use(cors())
app.use("/maes", maesRoutes)
app.use("/medicos", medicosRoutes)
app.use("/bebes", bebesRoutes)
app.use("/usuarios", usuariosRoutes)
app.use("/login", loginRoutes)
//app.use("/recupera", recuperaRoutes)

app.get('/', (req, res) => {
  res.send('API do Zoológico: Controle de Animais')
})

app.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`)
})