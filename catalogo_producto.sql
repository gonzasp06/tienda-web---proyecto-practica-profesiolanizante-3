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
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` text,
  `categoria` varchar(100) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (13,'Lavarropas Automático Carga Frontal 7 Kg Inverter Silver','Disfrutá de una mayor eficiencia energética, menos ruido y un rendimiento duradero. La tecnología Digital Inverter utiliza imanes potentes para un rendimiento más silencioso y potente, pero consume menos energía que un motor universal. Brinda una durabilidad excepcional*, respaldada por 20 años de garantía','electrodomesticos',89249.00,5,'static/uploads\\Lavarropas_Automatico_Carga_Frontal_7_Kg_Inverter_Silver.webp'),(14,'Split Frio/Calor 5850W Inverter con ahorro energético AR24BSH','Ahorrá dinero cada día con la tecnología Digital Inverter. Mantiene la temperatura deseada sin apagar y encender con frecuencia, por lo que hay menos fluctuaciones. Además, utiliza potentes imanes y un silenciador, por lo que es más silencioso, dura mucho más y reduce el consumo de energía.','climatizacion',1667999.00,8,'static/uploads\\Split_Frio_-_Calor_5850W_Inverter_con_ahorro_energetico_AR24BSH.png'),(15,'Microondas de Integración 22L 850W/Grill 1100W Inox','El botón Grill+30sec logra la textura y el color ideal para tus alimentos, para que se vean y sepan deliciosos. Aumentá el tiempo de cocción en 30 segundos para dorar y grillar los alimentos exquisitamente con el calentador de la parrilla.','electrodomesticos',744999.00,9,'static/uploads\\Microondas_de_Integracion_22L_850W.png'),(16,'Aspiradora sin bolsa 2000 W Negra','Acabar con la suciedad, el pelo de las mascotas y también con las bolsas. Las aspiradoras con bolsas no atrapan el polvo como las aspiradoras sin. Incluso las bolsas pueden tener que ser reemplazadas antes de que siquiera esté medio llena. Eso no es eficiente ni económico. Con una aspiradora sin bolsa, podés dejar de buscar y gastar dinero en aspiradoras comunes. Después de todo, tu aspiradora debe ser la limpieza de tus pisos, no la limpieza de tu cartera.','electrodomesticos',212499.00,2,'static/uploads\\Aspiradora_sin_bolsa_2000_W_Negra.png'),(17,'Licuadora Philips Jarra 2lts 550W','Excelente rendimiento de licuado y picado de hielo en una jarra de 2 l* Domine cualquier receta gracias a la licuadora de uso diario Philips. La exclusiva tecnología ProBlend 4 permite crear el entorno perfecto para licuar de forma rápida y suave','electrodomesticos',69999.00,10,'static/uploads\\Licuadora_Philips_Jarra_2lts_550W.png'),(18,'Android TV Philips LED 4K 50\" HDR+','Ya sea que veas una película hoy, programas y partidos mañana, o deportes el fin de semana, este Smart TV 4K de Philips siempre te ofrecerá imágenes brillantes. Obtendrás una imagen y un sonido cinematográficos con Dolby Vision y Dolby Atmos, así como un Smart TV Android sin problemas.','tv & video',524699.00,9,'static/uploads\\55PUD7406-77.webp'),(19,'Parlante deportivo Bluetooth','Surfear. Correr. Bailar. Entrenar. No importa lo que hagas, este altavoz resistente al agua con un moderno diseño en dos tonos será tu compañero perfecto. A pesar de su tamaño compacto, disfrutarás de un sonido potente y la correa facilita el transporte del altavoz. ¡Vamos!','tecnologia',128959.00,18,'static/uploads\\Parlante_deportivo_Bluetooth.webp'),(20,'Monitor Curvo Philips LED de 27\" Full HD','La pantalla curva E-Line de 27” ofrece una experiencia verdaderamente envolvente con un diseño elegante. Disfrutá de imágenes Full HD nítidas y una acción suave gracias a la tecnología AMD FreeSync.','tecnologia',35490.00,6,'static/uploads\\157283-800-auto.webp'),(21,'Cafetera Philips Daily Collection Jarra 1.2 Lts','Con Espiral Aroma para disfrutar del mejor sabor Disfrute el sabor y el aroma del café recién preparado con esta confiable cafetera Philips. Gracias al espiral Aroma, experimentará un sabor óptimo en cada taza de café.','electrodomesticos',99999.00,9,'static/uploads\\HD7462-20.png'),(22,'Multiprocesadora Liliana Simplix AM700 700W negra 220V - 240V','La Multiprocesadora Liliana Simplix AM700 es la solución perfecta para simplificar tus tareas en la cocina. Con su potente motor de 700W y su capacidad de 1.2 litros, podrás preparar una gran variedad de recetas de manera rápida y eficiente. Sus dos velocidades y función pulsar te permiten controlar la textura de tus preparaciones, desde amasar hasta picar, rallar y rebanar. Además, cuenta con una traba de seguridad para garantizar un uso seguro en todo momento.','electrodomesticos',84999.00,4,'static/uploads\\Multiprocesadora_Liliana_Simplix_AM700_700W_negra_220V_-_240V.webp'),(23,'Heladera no frost SAMSUNG digital inverter inoxidable','Solo Twin Cooling Plus™ crea un entorno favorable para preservar los alimentos frescos en la heladera con un 70% de humedad, comparada con el 30% de un las heladeras convencionales. De esta manera, mantiene los ingredientes frescos durante más tiempo sin secarlos. Congeladores','electrodomesticos',1129999.00,2,'static/uploads\\HELADERA_NO_FROST_SAMSUNG_RT32K5930SL_DIGITAL_INVERTER_INOXIDABLE.jpeg'),(24,'Freezer Congelador Horizontal Philco 290 Lts Phch301bm - PHILCO','El freezer Philco PHCH301BM tiene un diseño tradicional horizontal en color blanco. Para organizar mejor los productos almacenados, cuenta con canasto contenedor para accesibilidad inmediata. Además, las patas son ajustables.','electrodomesticos',559999.00,3,'static/uploads\\Freezer_Congelador_Horizontal_Philco_290_Lts_Phch301bm_-_PHILCO.jpg');
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-06 13:51:24
