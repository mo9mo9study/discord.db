/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

##########################################
# ポイント
# - 検索条件に使用する項目にはIndexをつける
# - Database nameはDDLをMySQLに流し込む際に指定するのでここでは記載しなくてok
# - (好みによるけど)物事を複雑にしがちな外部キー制約の濫用は避ける
##########################################


# ------------------------------------------------------------

# DROP TABLE IF EXISTS `entry_exit_logs`;

CREATE TABLE IF NOT EXISTS `entry_exit_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `guild_id` int,
  `user_id` int NOT NULL,
  `voicechannel_id` int,
  `timestamp_entry` datetime,
  `timestamp_exit` datetime,
  `study_target_id` int COMMENT '勉強対象をセットできる',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp COMMENT 'INSERT時に自動でセットされる作成日時',
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE current_timestamp COMMENT 'INSERT/UPDATE時に自動でセットされる作成日時',
  PRIMARY KEY (`id`),
  KEY `index_of_user_id` (`user_id`),
  KEY `index_of_studytarget_id` (`studytarget_id`),
  KEY `index_of_created_at` (`created_at`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='勉強時間記録テーブル';

# ------------------------------------------------------------

# DROP TABLE IF EXISTS `current_study_target`;

CREATE TABLE IF NOT EXISTS `current_study_target` (
  `id` int NOT NULL AUTO_INCREMENT,
  `guild_id` int,
  `user_id` int NOT NULL,
  `study_target_id` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp COMMENT 'INSERT時に自動でセットされる作成日時',
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE current_timestamp COMMENT 'INSERT/UPDATE時に自動でセットされる作成日時',
  PRIMARY KEY (`id`),
  KEY `index_of_user_id` (`user_id`),
  UNIQUE KEY `uq_user_id` (`user_id`) COMMENT '同時に設定できる勉強対象はユーザごとに１つ',
  KEY `index_of_created_at` (`created_at`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='現在勉強している対象情報テーブル';


# ------------------------------------------------------------

# DROP TABLE IF EXISTS `study_target`;

CREATE TABLE IF NOT EXISTS `study_target` (
  `id` int NOT NULL AUTO_INCREMENT,
  `guild_id` int,
  `user_id` int NOT NULL,
  `study_target_name` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp COMMENT 'INSERT時に自動でセットされる作成日時',
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE current_timestamp COMMENT 'INSERT/UPDATE時に自動でセットされる作成日時',
  PRIMARY KEY (`id`),
  KEY `index_of_user_id` (`user_id`),
  UNIQUE KEY `uq_user_id_target_name` (`user_id`,`target_name`) COMMENT '勉強対象はユーザ単位でユニーク',
  KEY `index_of_created_at` (`created_at`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='日毎の？勉強時間集計テーブル';



# ------------------------------------------------------------

# DROP TABLE IF EXISTS `studytimes_logs`;

CREATE TABLE IF NOT EXISTS `studytimes_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `guild_id` int,
  `user_id` int NOT NULL,
  `voicechannel_id` int,
  `studydate` datetime NOT NULL COMMENT '集計対象日付',
  `studytime_min` int NOT NULL,
  `study_target_id` int COMMENT '勉強対象をセットできる',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp COMMENT 'INSERT時に自動でセットされる作成日時',
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE current_timestamp COMMENT 'INSERT/UPDATE時に自動でセットされる作成日時',
  PRIMARY KEY (`id`),
  KEY `index_of_user_id` (`user_id`),
  KEY `index_of_studydate` (`studydate`),
  KEY `index_of_studytarget_id` (`studytarget_id`),
  KEY `index_of_created_at` (`created_at`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='日毎の？勉強時間集計テーブル';
