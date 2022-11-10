INSERT INTO `labmysql`.`Cars` (`idCars`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('0', '3K096I98581DHSNUP	', 'Volkswagen', 'Tiguan', '2019', 'Blue');
INSERT INTO `labmysql`.`Cars` (`idCars`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('1', 'ZM8G7BEUQZ97IH46V	', 'Peugeot', 'Rifter', '2019', 'Red');
INSERT INTO `labmysql`.`Cars` (`idCars`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('2', 'RKXVNNIHLVVZOUB4M', 'Ford', 'Fiesta', '2018', 'White');
INSERT INTO `labmysql`.`Cars` (`idCars`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('3', 'HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', '2018', 'Silver');
INSERT INTO `labmysql`.`Cars` (`idCars`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('4', 'DAM41UDN3CHU2WVF6', 'Renault', 'V60', '2019', 'Black');
INSERT INTO `labmysql`.`Cars` (`idCars`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('5', 'DAM41UDN3CHU2WVF6', 'BMW', 'X6', '2019', 'Yellow');

INSERT INTO `labmysql`.`Customers` (`idCustomers`, `CustomerID`, `Name`, `PhoneNumber`, `Address`, `City`, `state/province`, `Country`, `PostalCode`) VALUES ('0', '10001', 'Pablo Picasso', '+34 636 17 63 82', 'Paseo de la Chopera, 14', 'Madrid', 'Madrid', 'Spain', '28045');
INSERT INTO `labmysql`.`Customers` (`idCustomers`, `CustomerID`, `Name`, `PhoneNumber`, `Address`, `City`, `state/province`, `Country`, `PostalCode`) VALUES ('1', '20001', 'Miguel de Unamuno', '+34 666 987 000', 'Fuencarral, 76', 'Madrid', 'Madrid', 'Spain', '28004');
INSERT INTO `labmysql`.`Customers` (`idCustomers`, `CustomerID`, `Name`, `PhoneNumber`, `Address`, `City`, `state/province`, `Country`, `PostalCode`) VALUES ('2', '30001', 'Manuela Malasaña', '+34 678 901 234', 'Manuela Malasaña, 12', 'Madrid', 'Madrid', 'Spain', '28004');


INSERT INTO `lab_mysql`.`Salespersons` (`idSalespersons`, `Staff ID`, `Name`, `Store`) VALUES ('2', '00003', 'Marie Curie', 'Berlin');
INSERT INTO `lab_mysql`.`Salespersons` (`idSalespersons`, `Staff ID`, `Name`, `Store`) VALUES ('3', '00004', 'Rosa Parks', 'Paris');
INSERT INTO `lab_mysql`.`Salespersons` (`idSalespersons`, `Staff ID`, `Name`, `Store`) VALUES ('4', '00005', 'Emmeline Pankhurst', 'Londres');
INSERT INTO `lab_mysql`.`Salespersons` (`idSalespersons`, `Staff ID`, `Name`, `Store`) VALUES ('5', '00006', 'Ada Lovelace', 'Roma');
INSERT INTO `lab_mysql`.`Salespersons` (`idSalespersons`, `Staff ID`, `Name`, `Store`) VALUES ('6', '00007', 'Rosalind Franklin', 'Dubrovnik');
INSERT INTO `lab_mysql`.`Salespersons` (`idSalespersons`, `Staff ID`, `Name`, `Store`) VALUES ('7', '00008', 'Margaret Thatcher', 'San Sebastián');

INSERT INTO `lab_mysql`.`Invoice` (`idInvoice`, `InvoiceNumber`, `Date`, `idCars`, `idCustomers`, `idSalespersons`) VALUES ('0', '852399038', '22-08-2018', '0', '1', '3');
INSERT INTO `lab_mysql`.`Invoice` (`idInvoice`, `InvoiceNumber`, `Date`, `idCars`, `idCustomers`, `idSalespersons`) VALUES ('2', '731166526', '31-12-2018', '3', '0', '5');
INSERT INTO `lab_mysql`.`Invoice` (`idInvoice`, `InvoiceNumber`, `Date`, `idCars`, `idCustomers`, `idSalespersons`) VALUES ('3', '271135104', '22-01-2019', '2', '2', '7');