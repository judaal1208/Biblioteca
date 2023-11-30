-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-11-2023 a las 02:49:13
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devoluciones`
--

CREATE TABLE `devoluciones` (
  `ID_devolucion` int(11) NOT NULL,
  `fecha_devolucion` datetime NOT NULL,
  `ID_usuario` int(11) NOT NULL,
  `ID_libro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `devoluciones`
--

INSERT INTO `devoluciones` (`ID_devolucion`, `fecha_devolucion`, `ID_usuario`, `ID_libro`) VALUES
(3, '2023-11-29 19:35:51', 1, 1);

--
-- Disparadores `devoluciones`
--
DELIMITER $$
CREATE TRIGGER `after_insert_devolucion` AFTER INSERT ON `devoluciones` FOR EACH ROW BEGIN
    UPDATE libros
    SET Stock = Stock + 1
    WHERE ID_libro = NEW.ID_libro;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `ID_libro` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`ID_libro`, `Nombre`, `Stock`) VALUES
(0, 'James Mosquera\'s Adventure', 5),
(1, 'La divina comedia.', 5),
(2, '100 años de soledad.', 14),
(3, 'Viaje al centro de la tierra', 6),
(4, 'Don Quijote de la Mancha', 19),
(5, 'Harry Potter', 34);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `ID_prestamo` int(11) NOT NULL,
  `fecha_prestamo` datetime NOT NULL,
  `ID_usuario` int(11) NOT NULL,
  `ID_libro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`ID_prestamo`, `fecha_prestamo`, `ID_usuario`, `ID_libro`) VALUES
(11, '2023-11-29 19:34:12', 1, 1);

--
-- Disparadores `prestamos`
--
DELIMITER $$
CREATE TRIGGER `after_insert_prestamo` AFTER INSERT ON `prestamos` FOR EACH ROW BEGIN
    UPDATE libros
    SET Stock = Stock - 1
    WHERE ID_libro = NEW.ID_libro;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `ID_usuario` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Direccion` varchar(255) NOT NULL,
  `DNI` varchar(20) NOT NULL,
  `libros_prestados` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`ID_usuario`, `Nombre`, `Direccion`, `DNI`, `libros_prestados`) VALUES
(0, 'Jhon', '13', '105', 0),
(1, 'Juan Pérez', 'Calle A #123', '12345678', 0),
(2, 'María Gómez', 'Avenida B #456', '87654321', 0),
(3, 'Pedro López', 'Calle C #789', '56789012', 0),
(4, 'Ana Martínez', 'Avenida D #1011', '23456789', 0),
(5, 'Carlos Rodríguez', 'Calle E #1213', '34567890', 0),
(8, 'Fer', '10', '1001', 0),
(9, 'tiny', '50', '52', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD PRIMARY KEY (`ID_devolucion`),
  ADD KEY `fk_devolucion_usuario` (`ID_usuario`),
  ADD KEY `fk_devolucion_libro` (`ID_libro`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`ID_libro`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`ID_prestamo`),
  ADD KEY `fk_prestamos_usuario` (`ID_usuario`),
  ADD KEY `fk_prestamos_libro` (`ID_libro`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  MODIFY `ID_devolucion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `ID_prestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD CONSTRAINT `fk_devolucion_libro` FOREIGN KEY (`ID_libro`) REFERENCES `libros` (`ID_libro`),
  ADD CONSTRAINT `fk_devolucion_usuario` FOREIGN KEY (`ID_usuario`) REFERENCES `usuario` (`ID_usuario`);

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `fk_prestamos_libro` FOREIGN KEY (`ID_libro`) REFERENCES `libros` (`ID_libro`),
  ADD CONSTRAINT `fk_prestamos_usuario` FOREIGN KEY (`ID_usuario`) REFERENCES `usuario` (`ID_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
