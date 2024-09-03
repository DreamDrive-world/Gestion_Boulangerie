
CREATE DATABASE Gesboulanger;
USE Gesboulanger;


CREATE TABLE Client (
    id_cli INTEGER PRIMARY KEY AUTO_INCREMENT,
    nom_cli VARCHAR(100) NOT NULL,
    adr_cli VARCHAR(200) NOT NULL,
    ville_cli VARCHAR(100) NOT NULL
);

CREATE TABLE Melange (
    id_melange INTEGER PRIMARY KEY AUTO_INCREMENT,
    description TEXT NOT NULL
);

CREATE TABLE Pain (
    id_pain INTEGER PRIMARY KEY AUTO_INCREMENT,
    description TEXT NOT NULL,
    prix_pain_ht DECIMAL(8,2) NOT NULL,
    melange_id INTEGER NOT NULL,
    FOREIGN KEY (melange_id) REFERENCES Melange(id_melange) ON DELETE CASCADE
);

CREATE TABLE Approvisionnement (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    melange_id INTEGER NOT NULL,
    semaine_appro INTEGER NOT NULL,
    quantite_melange INTEGER NOT NULL,
    FOREIGN KEY (melange_id) REFERENCES Melange(id_melange) ON DELETE CASCADE
);

CREATE TABLE Livraison (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    client_id INTEGER NOT NULL,
    pain_id INTEGER NOT NULL,
    date_livraison INTEGER NOT NULL,
    nombre_pains INTEGER NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(id_cli) ON DELETE CASCADE,
    FOREIGN KEY (pain_id) REFERENCES Pain(id_pain) ON DELETE CASCADE
);