CREATE DATABASE IF NOT EXISTS `Друзья человека`;
USE `Друзья человека`;

CREATE TABLE IF NOT EXISTS `animals` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100),
    `birthdate` DATE
);

CREATE TABLE IF NOT EXISTS `horses` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100),
    `birthdate` DATE,
    `horse_specific_field` VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS `donkeys` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100),
    `birthdate` DATE,
    `donkey_specific_field` VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS `camels` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100),
    `birthdate` DATE,
    `camel_specific_field` VARCHAR(100)
);

INSERT INTO `horses` (`name`, `birthdate`, `horse_specific_field`)
VALUES ('Лошадь1', '2020-01-01', 'Конкретные данные лошади1'),
       ('Лошадь2', '2019-03-15', 'Конкретные данные лошади2');

INSERT INTO `donkeys` (`name`, `birthdate`, `donkey_specific_field`)
VALUES ('Осел1', '2022-05-10', 'Конкретные данные осла1'),
       ('Осел2', '2021-02-28', 'Конкретные данные осла2');

INSERT INTO `camels` (`name`, `birthdate`, `camel_specific_field`)
VALUES ('Верблюд1', '2021-11-20', 'Конкретные данные верблюда1'),
       ('Верблюд2', '2020-07-05', 'Конкретные данные верблюда2');

      CREATE TABLE IF NOT EXISTS `young_animals` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100),
    `birthdate` DATE,
    `age_months` INT -- Возраст в месяцах
);

INSERT INTO `young_animals` (`name`, `birthdate`, `age_months`)
SELECT `name`, `birthdate`, TIMESTAMPDIFF(MONTH, `birthdate`, NOW()) AS `age_months`
FROM `animals`
WHERE `birthdate` > DATE_SUB(NOW(), INTERVAL 3 YEAR)
AND `birthdate` <= DATE_SUB(NOW(), INTERVAL 1 YEAR);

CREATE TABLE IF NOT EXISTS `all_animals` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100),
    `birthdate` DATE,
    `animal_type` VARCHAR(20),
    `specific_field` VARCHAR(100), 
    `previous_table` VARCHAR(20)
);

INSERT INTO `all_animals` (`name`, `birthdate`, `animal_type`, `specific_field`, `previous_table`)
SELECT `name`, `birthdate`, 'horse' AS `animal_type`, `horse_specific_field` AS `specific_field`, 'horses' AS `previous_table`
FROM `horses_and_donkeys`
WHERE `animal_type` = 'horse'

UNION ALL

SELECT `name`, `birthdate`, 'donkey' AS `animal_type`, `specific_field`, 'donkeys' AS `previous_table`
FROM `horses_and_donkeys`
WHERE `animal_type` = 'donkey'

UNION ALL

SELECT `name`, `birthdate`, 'camel' AS `animal_type`, `camel_specific_field` AS `specific_field`, 'camels' AS `previous_table`
FROM `camels`;

-- Удаление временной таблицы
DROP TABLE `horses_and_donkeys`;
