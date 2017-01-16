-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema businesses
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema businesses
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `businesses` DEFAULT CHARACTER SET utf8 ;
USE `businesses` ;

-- -----------------------------------------------------
-- Table `businesses`.`states`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `businesses`.`states` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `state` VARCHAR(2) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `businesses`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `businesses`.`cities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city` VARCHAR(45) NULL,
  `updated_at` DATETIME NULL,
  `states_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cities_states1_idx` (`states_id` ASC),
  CONSTRAINT `fk_cities_states1`
    FOREIGN KEY (`states_id`)
    REFERENCES `businesses`.`states` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `businesses`.`businesses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `businesses`.`businesses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `business` CHAR(2) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `businesses`.`cities_have_business`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `businesses`.`cities_have_business` (
  `city_id` INT NOT NULL,
  `business_id` INT NOT NULL,
  INDEX `fk_cities_have_business_cities1_idx` (`city_id` ASC),
  INDEX `fk_cities_have_business_businesses1_idx` (`business_id` ASC),
  CONSTRAINT `fk_cities_have_business_cities1`
    FOREIGN KEY (`city_id`)
    REFERENCES `businesses`.`cities` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cities_have_business_businesses1`
    FOREIGN KEY (`business_id`)
    REFERENCES `businesses`.`businesses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
