-- CreateTable
CREATE TABLE "maes" (
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(60) NOT NULL,
    "endereco" VARCHAR(40) NOT NULL,
    "telefone" VARCHAR(20) NOT NULL,
    "datanasc" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "maes_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "medicos" (
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(60) NOT NULL,
    "crm" VARCHAR(40) NOT NULL,
    "celular" VARCHAR(40) NOT NULL,
    "especialidade" VARCHAR(20) NOT NULL,

    CONSTRAINT "medicos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "criancas" (
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(30) NOT NULL,
    "datanasc" TIMESTAMP(3) NOT NULL,
    "peso" DECIMAL(5,3) NOT NULL,
    "altura" DECIMAL(4,2) NOT NULL,
    "maeId" INTEGER NOT NULL,
    "medicoId" INTEGER NOT NULL,

    CONSTRAINT "criancas_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "criancas" ADD CONSTRAINT "criancas_maeId_fkey" FOREIGN KEY ("maeId") REFERENCES "maes"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "criancas" ADD CONSTRAINT "criancas_medicoId_fkey" FOREIGN KEY ("medicoId") REFERENCES "medicos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
