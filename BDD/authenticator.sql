-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Feb 16, 2022 at 11:14 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `authenticator`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Log_ID` int(11) NOT NULL,
  `User_ID` varchar(55) NOT NULL,
  `Password` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Log_ID`, `User_ID`, `Password`) VALUES
(1, 'Adra', 'test'),
(52, 'Interrupt Handler', 'The Algorithm'),
(55, 'Yaldabaoth', 'The Algorithm'),
(56, 'Overlock', 'The Algorithm'),
(58, 'Yanou22260', 'Yanou22260'),
(59, 'Pythagoras', 'The Algorithm'),
(60, 'Binary Space', 'The Algorithm'),
(62, 'Critical Error', 'The Algorithm'),
(63, 'Polymorphic Code', 'The Algorithm'),
(64, 'Hyppotraktor', 'Meridian');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`Log_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `Log_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
