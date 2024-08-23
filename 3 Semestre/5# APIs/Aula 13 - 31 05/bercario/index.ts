import express  from "express";
const app = express()
const port = 3000
import candidatasRoutes from './routes/candidatas'
import clientesRoutes from './routes/clientes';

app.use(express.json())
app.use("/candidatas", candidatasRoutes)
app.use("/clientes", clientesRoutes)

app.get('/', (req, res) => {
    res.send('APIs: Berçario')
})

app.listen(port, () =>{
    console.log(`Servidor rodando na porta : ${port}`);
    
})
    