# Host: localhost  (Version: 5.5.53)
# Date: 2018-09-14 22:23:39
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "fl3g"
#

DROP TABLE IF EXISTS `fl3g`;
CREATE TABLE `fl3g` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `fl4g` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Data for table "fl3g"
#

/*!40000 ALTER TABLE `fl3g` DISABLE KEYS */;
INSERT INTO `fl3g` VALUES (1,'NTUCTF{594f803b380a41396ed63dca39503542}');
/*!40000 ALTER TABLE `fl3g` ENABLE KEYS */;

#
# Structure for table "info"
#

DROP TABLE IF EXISTS `info`;
CREATE TABLE `info` (
  `Id` char(1) NOT NULL DEFAULT '',
  `class` varchar(255) DEFAULT NULL,
  `boy` varchar(255) DEFAULT NULL,
  `girl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Data for table "info"
#

/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES ('1','one','23','23'),('2','two','18','34'),('3','three','44','3');
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
