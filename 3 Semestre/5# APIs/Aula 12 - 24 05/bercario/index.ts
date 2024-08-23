import express  from "express";
const app = express()
const port = 3000
import maesRoutes from './routes/maes'
import medicoRoutes from './routes/medicos';

app.use(express.json())
app.use("/maes", maesRoutes)
app.use("/medicos", medicoRoutes)

app.get('/', (req, res) => {
    res.send('APIs: Berçario')
})

app.listen(port, () =>{
    console.log(`Servidor rodando na porta : ${port}`);
    
})
    