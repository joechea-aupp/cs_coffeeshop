-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.17-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for cs_coffee
CREATE DATABASE IF NOT EXISTS `cs_coffee` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `cs_coffee`;

-- Dumping structure for table cs_coffee.coffee
CREATE TABLE IF NOT EXISTS `coffee` (
  `coffee_id` int(3) unsigned NOT NULL AUTO_INCREMENT,
  `coffee_name` varchar(255) DEFAULT NULL,
  `coffee_price` float DEFAULT NULL,
  `mat_id` int(3) unsigned NOT NULL,
  PRIMARY KEY (`coffee_id`),
  KEY `FORIEGN KEY` (`mat_id`),
  CONSTRAINT `mat_id` FOREIGN KEY (`mat_id`) REFERENCES `material` (`mat_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table cs_coffee.coffee: ~2 rows (approximately)
/*!40000 ALTER TABLE `coffee` DISABLE KEYS */;
REPLACE INTO `coffee` (`coffee_id`, `coffee_name`, `coffee_price`, `mat_id`) VALUES
	(1, 'latte', 2.5, 1),
	(2, 'americano', 2, 3),
	(3, 'black_coffee', 1.8, 2);
/*!40000 ALTER TABLE `coffee` ENABLE KEYS */;

-- Dumping structure for table cs_coffee.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `cus_id` int(3) unsigned NOT NULL AUTO_INCREMENT,
  `cus_firstname` varchar(255) NOT NULL DEFAULT '',
  `cus_lastname` varchar(255) NOT NULL DEFAULT '',
  `cus_ph` varchar(255) NOT NULL DEFAULT '',
  `created_on` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`cus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table cs_coffee.customer: ~9 rows (approximately)
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
REPLACE INTO `customer` (`cus_id`, `cus_firstname`, `cus_lastname`, `cus_ph`, `created_on`) VALUES
	(1, 'guest', 'user', '88888888', NULL),
	(4, 'joe', 'chea', '011702696', '2021-03-21 20:00:26'),
	(7, 'hope', 'chea', '0112345678', '2021-03-22 01:20:00'),
	(8, 'jone', 'netial', '012345678', '2021-03-22 11:57:55'),
	(9, 'jacky', 'chan', '099778899', '2021-03-22 12:20:45'),
	(10, 'jacky', 'chea', '088778899', '2021-03-22 12:23:18'),
	(11, 'shelock', 'homes', '066778899', '2021-03-22 12:26:25'),
	(12, 'selina', 'jone', '044556677', '2021-03-22 12:47:33'),
	(13, 'joe', 'gardner', '099887766', '2021-03-30 11:02:28'),
	(14, 'koko', 'jan', '088552211', '2021-04-09 13:16:16');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

-- Dumping structure for table cs_coffee.material
CREATE TABLE IF NOT EXISTS `material` (
  `mat_id` int(3) unsigned NOT NULL AUTO_INCREMENT,
  `mat_cofbean` int(10) unsigned NOT NULL DEFAULT 0,
  `mat_water` int(10) unsigned NOT NULL DEFAULT 0,
  `mat_sugar` int(10) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`mat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table cs_coffee.material: ~2 rows (approximately)
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
REPLACE INTO `material` (`mat_id`, `mat_cofbean`, `mat_water`, `mat_sugar`) VALUES
	(1, 50, 10, 5),
	(2, 60, 4, 0),
	(3, 80, 10, 0);
/*!40000 ALTER TABLE `material` ENABLE KEYS */;

-- Dumping structure for table cs_coffee.resource
CREATE TABLE IF NOT EXISTS `resource` (
  `res_id` int(3) unsigned NOT NULL AUTO_INCREMENT,
  `cof_bean` int(4) unsigned NOT NULL DEFAULT 0,
  `water` int(4) unsigned NOT NULL DEFAULT 0,
  `sugar` int(4) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`res_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table cs_coffee.resource: ~0 rows (approximately)
/*!40000 ALTER TABLE `resource` DISABLE KEYS */;
REPLACE INTO `resource` (`res_id`, `cof_bean`, `water`, `sugar`) VALUES
	(1, 6360, 1036, 325);
/*!40000 ALTER TABLE `resource` ENABLE KEYS */;

-- Dumping structure for table cs_coffee.sell
CREATE TABLE IF NOT EXISTS `sell` (
  `sell_id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `coffee_id` int(3) unsigned NOT NULL,
  `cus_id` int(3) unsigned NOT NULL,
  `sell_total` float unsigned NOT NULL DEFAULT 0,
  `sell_date` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`sell_id`),
  KEY `cus_id` (`cus_id`),
  KEY `FK` (`coffee_id`) USING BTREE,
  CONSTRAINT `coffee_id` FOREIGN KEY (`coffee_id`) REFERENCES `coffee` (`coffee_id`),
  CONSTRAINT `cus_id` FOREIGN KEY (`cus_id`) REFERENCES `customer` (`cus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table cs_coffee.sell: ~23 rows (approximately)
/*!40000 ALTER TABLE `sell` DISABLE KEYS */;
REPLACE INTO `sell` (`sell_id`, `coffee_id`, `cus_id`, `sell_total`, `sell_date`) VALUES
	(5, 2, 4, 1.8, '2021-03-21 20:58:13'),
	(6, 2, 4, 1.8, '2021-03-21 20:59:12'),
	(7, 2, 1, 2, '2021-03-21 21:01:44'),
	(8, 2, 4, 1.8, '2021-03-21 22:10:07'),
	(9, 3, 4, 1.62, '2021-03-21 22:13:16'),
	(10, 2, 4, 1.8, '2021-03-21 23:11:27'),
	(11, 3, 4, 1.62, '2021-03-22 00:43:23'),
	(12, 2, 4, 1.8, '2021-03-22 00:55:07'),
	(13, 2, 4, 1.8, '2021-03-22 01:13:12'),
	(14, 3, 1, 1.8, '2021-03-22 01:15:01'),
	(15, 2, 7, 1.8, '2021-03-22 01:21:24'),
	(16, 1, 1, 2.5, '2021-03-22 11:52:33'),
	(17, 3, 7, 1.62, '2021-03-22 11:52:33'),
	(18, 2, 1, 2, '2021-03-22 11:57:55'),
	(19, 1, 4, 2.25, '2021-03-22 11:57:55'),
	(20, 2, 1, 2, '2021-03-22 12:04:42'),
	(21, 2, 1, 2, '2021-03-22 12:20:45'),
	(22, 1, 1, 2.5, '2021-03-22 12:46:24'),
	(23, 1, 1, 2.5, '2021-03-22 12:47:33'),
	(24, 1, 11, 2.25, '2021-03-22 12:47:33'),
	(25, 3, 12, 1.62, '2021-03-22 12:47:33'),
	(26, 2, 13, 1.8, '2021-03-30 13:22:01'),
	(27, 2, 1, 2, '2021-04-09 13:16:16'),
	(28, 3, 4, 1.62, '2021-04-09 13:16:16');
/*!40000 ALTER TABLE `sell` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
