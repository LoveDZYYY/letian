-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: letian
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add temporary_order',8,'add_temporary_order'),(30,'Can change temporary_order',8,'change_temporary_order'),(31,'Can delete temporary_order',8,'delete_temporary_order'),(32,'Can view temporary_order',8,'view_temporary_order'),(33,'Can add open_shengxiao',9,'add_open_shengxiao'),(34,'Can change open_shengxiao',9,'change_open_shengxiao'),(35,'Can delete open_shengxiao',9,'delete_open_shengxiao'),(36,'Can view open_shengxiao',9,'view_open_shengxiao'),(37,'Can add user_bet',10,'add_user_bet'),(38,'Can change user_bet',10,'change_user_bet'),(39,'Can delete user_bet',10,'delete_user_bet'),(40,'Can view user_bet',10,'view_user_bet');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(9,'web','open_shengxiao'),(8,'web','temporary_order'),(7,'web','user'),(10,'web','user_bet');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-02-24 19:56:05.193517'),(2,'auth','0001_initial','2024-02-24 19:56:05.883644'),(3,'admin','0001_initial','2024-02-24 19:56:06.033745'),(4,'admin','0002_logentry_remove_auto_add','2024-02-24 19:56:06.033745'),(5,'admin','0003_logentry_add_action_flag_choices','2024-02-24 19:56:06.043938'),(6,'contenttypes','0002_remove_content_type_name','2024-02-24 19:56:06.123676'),(7,'auth','0002_alter_permission_name_max_length','2024-02-24 19:56:06.193276'),(8,'auth','0003_alter_user_email_max_length','2024-02-24 19:56:06.209598'),(9,'auth','0004_alter_user_username_opts','2024-02-24 19:56:06.218025'),(10,'auth','0005_alter_user_last_login_null','2024-02-24 19:56:06.293487'),(11,'auth','0006_require_contenttypes_0002','2024-02-24 19:56:06.293487'),(12,'auth','0007_alter_validators_add_error_messages','2024-02-24 19:56:06.303307'),(13,'auth','0008_alter_user_username_max_length','2024-02-24 19:56:06.383765'),(14,'auth','0009_alter_user_last_name_max_length','2024-02-24 19:56:06.453699'),(15,'auth','0010_alter_group_name_max_length','2024-02-24 19:56:06.463278'),(16,'auth','0011_update_proxy_permissions','2024-02-24 19:56:06.474913'),(17,'auth','0012_alter_user_first_name_max_length','2024-02-24 19:56:06.553743'),(18,'sessions','0001_initial','2024-02-24 19:56:06.604811'),(19,'web','0001_initial','2024-02-24 19:56:06.643568'),(20,'web','0002_alter_user_mobile_alter_user_money','2024-02-24 20:52:14.807718'),(21,'web','0003_temporary_order','2024-02-25 10:07:31.269822'),(22,'web','0004_temporary_order_is_pay','2024-02-25 15:41:33.432894'),(23,'web','0005_alter_user_money','2024-02-25 20:47:05.118378'),(24,'web','0006_alter_user_money','2024-02-25 20:51:01.354782'),(25,'web','0007_temporary_order_userprizereceipt','2024-02-25 21:05:31.705508'),(26,'web','0008_open_shengxiao','2024-02-25 21:36:49.702029'),(27,'web','0009_open_shengxiao_current_phase','2024-02-25 21:39:39.571546'),(28,'web','0010_alter_open_shengxiao_current_phase_user_bet','2024-02-26 12:25:39.254769'),(29,'web','0011_alter_temporary_order_order_create_time','2024-02-26 20:51:50.681687'),(30,'web','0012_temporary_order_current_phase','2024-02-27 05:30:30.396217'),(31,'web','0013_user_bet_open_time','2024-02-27 06:37:14.543869'),(32,'web','0014_user_bet_is_pay','2024-02-28 01:59:32.292290'),(33,'web','0015_user_bet_pay_how_much','2024-02-28 01:59:32.328715'),(34,'web','0016_alter_user_bet_pay_how_much','2024-02-28 01:59:32.331995');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bhmy7b95i7uamtbthpqt9k2yp07dl8bt','.eJwli0EKgCAUBe_y1i7M_KWeRQgrA6EUqr8K757RbphhHqS8FbgHfMVzSiucEj_ncEQ4eNZRdp5pW0fP1tgBAmFZCue7Za2JRpKk-r75o8xp_67OWtWSlkah1hdhEB2i:1reZpH:aMkxPiVLdEHU2aI_UwYffqHT8B-ES4w9w_ilMf5EzZM','2024-03-11 12:11:19.112148'),('cn4onqeqqvtxkood4tfn8pvt3s1yfa7c','.eJwli0EKgCAUBe_y1i7M_KWeRQgrA6EUqr8K757RbphhHqS8FbgHfMVzSiucEj_ncEQ4eNZRdp5pW0fP1tgBAmFZCue7Za2JRpKk-r75o8xp_67OWtWSlkah1hdhEB2i:1reBix:46TBFJ2yMW9crLGRntO0kPxFxpxAWxBUjAUG4JpIfNc','2024-03-10 10:27:11.315137'),('ex0pt7mtplldrmivi9w6e3wonjrfhqeo','.eJwli0EKgCAUBe_y1i7M_KWeRQgrA6EUqr8K757RbphhHqS8FbgHfMVzSiucEj_ncEQ4eNZRdp5pW0fP1tgBAmFZCue7Za2JRpKk-r75o8xp_67OWtWSlkah1hdhEB2i:1reLTD:rJMFzp9o5xt7z_OLYlZepQ9csNc95z2OneFv3hgkCXk','2024-03-10 20:51:35.317848'),('owq6v3xcyx0qiog69oqmfa1ws4n1vvme','.eJwtjMsKgzAQRf_lrqVMwjh5fEugqI0QMAnYzqKI_15Lu7ucw7kHSls74gF95v1eHohu-O021YyIpEHYJ3XOrEllFsGAaVm6ttel2XqxPJJhd_Ha57J9KxOCZR6ZvMX5P6y95TeiIbrR-QHDvCNa:1rf4bz:Yo0MgqLesZLGPd5gMb0rTwq881e4ehpWNoaeiib1tEA','2024-03-13 05:03:39.849874'),('styseolwyzxuzavf921p3zqc1l370al8','.eJwtjEEKhDAQBP_SZ5FJzKjJWwKLqxECJoFd5yDi3zey3oouuk7EvBa4E_INn1dc4HTz5zylAAcvJpDywusyeLGj7dFgmuciea_aGOaBiXXX1T2Vd9zul7JWV2Vo1LieYCo5HHCKWrp-rcojUQ:1remXK:dbseDIlG1N0P9sl7tjrIPOtpIIxNGF9eLFnoRYjs1mE','2024-03-12 09:45:38.773084'),('vtfze6d1bw54jdysqito9na0vtz3jwwh','.eJwli00KgCAUBu_yrdv4ymd6FiG0HxBSoXIl3j2j3TDDVIR0ZJiKcu_XEjaYcfg5ubjDwBZWPNsinfbeY4Bb11zS05MiLZgk8cTdx-zD-R1iJGJSSmiB1l7oyByS:1re0XE:BhRuhIjcyao9uOC0WSFeW1APARKTd4dUYlgtY0kC2b0','2024-03-09 22:30:20.702473');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_open_shengxiao`
--

DROP TABLE IF EXISTS `web_open_shengxiao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `web_open_shengxiao` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `open_time` datetime(6) NOT NULL,
  `open_shengxiao` varchar(200) NOT NULL,
  `is_edit` tinyint(1) NOT NULL,
  `current_phase` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `web_open_shengxiao_current_phase_4b0d67b8_uniq` (`current_phase`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_open_shengxiao`
--

LOCK TABLES `web_open_shengxiao` WRITE;
/*!40000 ALTER TABLE `web_open_shengxiao` DISABLE KEYS */;
INSERT INTO `web_open_shengxiao` VALUES (15,'2024-02-28 22:10:47.095391','[\'龙\', \'牛\', \'鸡\', \'羊\', \'蛇\']',0,1);
/*!40000 ALTER TABLE `web_open_shengxiao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_temporary_order`
--

DROP TABLE IF EXISTS `web_temporary_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `web_temporary_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_buy_goods` varchar(200) NOT NULL,
  `stay_pay_money` int NOT NULL,
  `order_create_time` datetime(6) NOT NULL,
  `user_id_id` bigint NOT NULL,
  `is_pay` tinyint(1) NOT NULL,
  `userPrizeReceipt` tinyint(1) NOT NULL,
  `current_phase` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_temporary_order_user_id_id_36b04ac7_fk_web_user_id` (`user_id_id`),
  CONSTRAINT `web_temporary_order_user_id_id_36b04ac7_fk_web_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `web_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_temporary_order`
--

LOCK TABLES `web_temporary_order` WRITE;
/*!40000 ALTER TABLE `web_temporary_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `web_temporary_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_user`
--

DROP TABLE IF EXISTS `web_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `web_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `account` varchar(16) NOT NULL,
  `password` varchar(32) NOT NULL,
  `mobile` varchar(32) NOT NULL,
  `money` decimal(30,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account` (`account`),
  UNIQUE KEY `web_user_mobile_d1dc3846_uniq` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_user`
--

LOCK TABLES `web_user` WRITE;
/*!40000 ALTER TABLE `web_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `web_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web_user_bet`
--

DROP TABLE IF EXISTS `web_user_bet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `web_user_bet` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_bet_shengxiao` varchar(200) NOT NULL,
  `user_bet_money` decimal(30,2) NOT NULL,
  `user_bet_time` datetime(6) NOT NULL,
  `open_shengxiao` varchar(200) NOT NULL,
  `current_phase_id` int NOT NULL,
  `user_id` bigint NOT NULL,
  `open_time` datetime(6) NOT NULL,
  `is_pay` tinyint(1) NOT NULL,
  `pay_how_much` decimal(30,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `web_user_bet_current_phase_id_c98d6cc2_fk_web_open_` (`current_phase_id`),
  KEY `web_user_bet_user_id_c331cde5_fk_web_user_id` (`user_id`),
  CONSTRAINT `web_user_bet_current_phase_id_c98d6cc2_fk_web_open_` FOREIGN KEY (`current_phase_id`) REFERENCES `web_open_shengxiao` (`current_phase`),
  CONSTRAINT `web_user_bet_user_id_c331cde5_fk_web_user_id` FOREIGN KEY (`user_id`) REFERENCES `web_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web_user_bet`
--

LOCK TABLES `web_user_bet` WRITE;
/*!40000 ALTER TABLE `web_user_bet` DISABLE KEYS */;
/*!40000 ALTER TABLE `web_user_bet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-28  5:07:58
