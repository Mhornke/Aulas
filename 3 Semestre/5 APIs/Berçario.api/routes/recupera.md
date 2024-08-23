// Importações necessárias
import { PrismaClient } from '@prisma/client';
import { Router } from 'express';

const prisma = new PrismaClient();
const router = Router();

// Função para validar a senha de recuperação
 async function validaSenhaRecupera(email: string, recupera: string) {
  const erros: string[] = [];

  try{
    const usuario = await prisma.usuario.findUnique({
        where:{
            email,
        },
    })
    if (!usuario){
        erros.push('Usuario Não encontrado')
      }else{
        if(recupera !==usuario.senhaRecupera) {
            erros.push('Senha de recuperação invalida')
        }
      }
  }catch(erro){
    erro.push("erro ao buscar usuario")
  }

  // Lógica de validação da senha de recuperação
  // Você pode implementar a lógica específica aqui conforme suas necessidades

  return erros;
}
router.post('/', async (req, res) => {
    const { email, senhaRecupera } = req.body;
  
    if (!email || !senhaRecupera) {
      return res.status(400).json({ erro: 'Informe email e senha de recuperação' });
    }
  
    try {
      // Validação da senha de recuperação
      const erros = await validaSenhaRecupera(email, senhaRecupera);
      if (erros.length > 0) {
        return res.status(400).json({ erro: erros.join('; ') });
      }
  
      // Cria a solicitação de recuperação de senha no banco de dados
      const recuperasenha = await prisma.recuperasenha.create({
        data: {
          email,
          senhaRecupera,
        },
      });
  
      res.status(201).json(recuperasenha);
    } catch (error) {
      res.status(400).json({ erro: 'Erro ao processar a solicitação de recuperação de senha' });
    }
  });
  
  export default router;

