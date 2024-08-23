import ArqTeste from 'react';


interface ComponentTeste {

    message: string;
}

const Componente: React.FC<ComponentTeste> = () => {
    return(
        <div>
            <input type="button" value="Login" />
        </div>
    );
};

export default Componente