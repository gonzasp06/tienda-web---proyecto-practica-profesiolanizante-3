-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: catalogo
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `is_admin` tinyint NOT NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'ADMIN','ADMIN','admin123@gmail.com','$2b$12$LiVyR9tF8p5sM8iYsz6TKelxVNjFg198EN4zaywhIMl/cBV8kmiSm',1),(34,'Juan','Pérez','juan.perez@gmail.com','$2b$12$B4s2cffEeR2on1ewCVf7UubKx9T99e.bUuslp0f7supw.EPTXRt0u',0),(35,'María','García','marigarcia@gmail.com','$2b$12$McQrL0rhaIqsglJDrvAG8e2urSMrOfsmDIclZlM2WxfiJ7n77pe7C',0),(36,'Carlos','Martinez','martinezcarl0@gmai.com','$2b$12$6bX2i6dFt2n2FFnnlJgrTOxTVqsXubAmXsoWfwEeQUAP3WouvFfLG',0),(37,'Ana','Rodriguez','annrodrig5@gmail.com','$2b$12$oenvJFXdbEnVqyAg3yLFH.TQh0gOrfZNHQY9y9jKOreMFbHRsiXSm',0),(38,'Luis','Lopez','luis.lopez@gmail.com','$2b$12$Gmm.NTfvIj5MGbp.YeTNY.ucuaYR4CY4r/0vPMIqAbZp8Xy2z0ebS',0),(39,'Laura','Sanchez','lauusanchez20@gmail.com','$2b$12$AHAngRSQQVGWrNVuGV12aOvWbdjyHCPFtYIntm9Pr0A5M8K5.5Sua',0),(41,'Alejandro','Diaz','diazale100@gmail.com','$2b$12$26tTVoY7ZAz63noPwZ/SfOJwFjHEaDnpmDTN.0DmCzAm2VP5qpKg.',0),(42,'Silvia','Lujan','sillujan543@gmail.com','$2b$12$zCr07wCRAfil2Y6WeNU7GeYglcvCbXk7o25x/iN6QLcLP0zj9ToEG',0),(43,'Ezequiel','Mendoza','ezemendo34@gmail.com','$2b$12$qHav7b6vD68wqae/HpoCS.e0u487cUhDCsC.BtirJg3XVkkMeylpO',0),(44,'Valentina','Herrera','valentinaa34herrera@gmail.com','$2b$12$TNafuNuH.wL5RhpNHgl3g.guPi8kZlL7o.vdEkmJCS8BIGdNty9TG',0),(45,'Matias','Gomez','go6matias@gmail.com','$2b$12$8Q23tAxa1RgpNAwmavZHm.2TjwY6DXaJJ5VqkX9lM0fghul5Aq5B.',0),(46,'Renata','Velazquez','rennavela67@gmail.com','$2b$12$RsrByhDe0ulwt6moHwGsEu.j1j/7l.NqXY.xj7fR12FrrNCupO9iq',0),(47,'Gael','Rios','riosg66gael@gmail.com','$2b$12$fxTmQa/qohd7TlprClWRBOyWy6nGC4axMpImBf/rtY/YsEaLnwuTq',0),(48,'Brisa','Molina','brisamolii10@gmail.com','$2b$12$Ni1glCtiyIcv803Go9kkkuxi1OxRu24Dpg3V6.oAfy85Rg8phMmlK',0),(49,'Luciano','Peralta','lucpera5o6yhi@gmail.com','$2b$12$WNzcyua7iDI2Rrr1DZh5yufdrt7HdQvRKNVnqOcWfwCWCpGZ4cvXq',0),(85,'victoria','vara','ghoulr1704@gmail.com','$2b$12$ikhDpi8.bKCxxTDRkhzCQejvEuFE3tmnI2OH1sK3biekrykOnRp5K',0),(95,'David','Veisaga','davidveisaga@gmail.com','$2b$12$y59Nrsgy5jWbHz23OudlcOGV8O8rZjRGGqxuQdrdVjOGqEeXjt/6G',0),(96,'Rosario','Chaves','rosariochaves111@gmail.com','$2b$12$O9ZtPowJuJm19Jki6jKBbuAx1RxJIVD.kYJH9Y.eFcFbRHmKvOyd6',0),(100,'Martina','Funes','martinafunez21@gmail.com','$2b$12$hW89k7cDlcZ6DwHZF9W.MuLTGHSinAtGJNTOJfGhMTY72hDDxvvOy',0);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-02  8:01:14
