-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mag 12, 2019 alle 19:49
-- Versione del server: 10.1.38-MariaDB
-- Versione PHP: 7.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `homework`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `contenuto`
--

CREATE TABLE `contenuto` (
  `Titolo` varchar(50) NOT NULL,
  `Immagine` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `contenuto`
--

INSERT INTO `contenuto` (`Titolo`, `Immagine`) VALUES
('Hulk (2016) #10', 'http://i.annihil.us/u/prod/marvel/i/mg/6/b0/59b04ca43779d/portrait_uncanny.jpg'),
('Hulk (2016) #8', 'http://i.annihil.us/u/prod/marvel/i/mg/4/04/595ea9ed9afe3/portrait_uncanny.jpg');

-- --------------------------------------------------------

--
-- Struttura della tabella `raccolta`
--

CREATE TABLE `raccolta` (
  `IDRaccolta` int(11) NOT NULL,
  `imurl` varchar(400) NOT NULL,
  `Nome` varchar(30) NOT NULL,
  `IdU` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `raccolta`
--

INSERT INTO `raccolta` (`IDRaccolta`, `imurl`, `Nome`, `IdU`) VALUES
(78, 'http://i.annihil.us/u/prod/marvel/i/mg/4/04/595ea9ed9afe3/portrait_uncanny.jpg', 'Iron-Man', 'puglio');

-- --------------------------------------------------------

--
-- Struttura della tabella `rc`
--

CREATE TABLE `rc` (
  `IdRac` varchar(50) NOT NULL,
  `IdCont` varchar(50) NOT NULL,
  `IdR` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `rc`
--

INSERT INTO `rc` (`IdRac`, `IdCont`, `IdR`) VALUES
('Iron-Man', 'Hulk (2016) #10', 78),
('Iron-Man', 'Hulk (2016) #8', 78);

-- --------------------------------------------------------

--
-- Struttura della tabella `utente`
--

CREATE TABLE `utente` (
  `Nome` varchar(20) NOT NULL,
  `Cognome` varchar(20) NOT NULL,
  `Nickname` varchar(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Pswd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `utente`
--

INSERT INTO `utente` (`Nome`, `Cognome`, `Nickname`, `Email`, `Pswd`) VALUES
('Andrea', 'Puglisi', 'puglio', 'atos.andre96@gmail.com', 'anove678'),
('Spinello', 'Sebastiano', 'spina', 'spina@inter97.com', 'asd');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `contenuto`
--
ALTER TABLE `contenuto`
  ADD PRIMARY KEY (`Titolo`);

--
-- Indici per le tabelle `raccolta`
--
ALTER TABLE `raccolta`
  ADD PRIMARY KEY (`IDRaccolta`),
  ADD KEY `IdU` (`IdU`),
  ADD KEY `Nome` (`Nome`);

--
-- Indici per le tabelle `rc`
--
ALTER TABLE `rc`
  ADD PRIMARY KEY (`IdCont`,`IdR`),
  ADD KEY `boh` (`IdR`);

--
-- Indici per le tabelle `utente`
--
ALTER TABLE `utente`
  ADD PRIMARY KEY (`Nickname`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `raccolta`
--
ALTER TABLE `raccolta`
  MODIFY `IDRaccolta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `raccolta`
--
ALTER TABLE `raccolta`
  ADD CONSTRAINT `raccolta_ibfk_1` FOREIGN KEY (`IdU`) REFERENCES `utente` (`Nickname`);

--
-- Limiti per la tabella `rc`
--
ALTER TABLE `rc`
  ADD CONSTRAINT `rc_ibfk_1` FOREIGN KEY (`IdCont`) REFERENCES `contenuto` (`Titolo`),
  ADD CONSTRAINT `rc_ibfk_2` FOREIGN KEY (`IdR`) REFERENCES `raccolta` (`IDRaccolta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
