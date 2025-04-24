use sustentabilidade;
CREATE TABLE sistema (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    usuario varchar(45),
    data DATE,
    l_agua decimal (10,2),
    energia decimal (10,2),
    kg_residuos decimal (10,2),
    por_residuos decimal (5,2),
    transporte_publico enum ('Sim','Nao'),
    bicicleta enum ('Sim','Nao'),
    caminhada enum ('Sim','Nao'),
    carro_fossil enum ('Sim','Nao'),
    carro_eletrico enum ('Sim','Nao'),
    carona_fossil enum ('Sim','Nao')
);

alter table sistema