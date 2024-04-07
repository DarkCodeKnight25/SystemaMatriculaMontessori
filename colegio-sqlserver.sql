-- CREACIÓN DE BASE DE DATOS
CREATE DATABASE colegio_python
ON (
	NAME = colegio_data, FILENAME ='D:\colegio\colegio_data.MDF', 
	Size = 10MB, MaxSize = 20MB, Filegrowth = 5MB
	)
LOG ON
    (
    NAME = colegio_log, FILENAME ='D:\colegio\colegio_log.LDF',
	Size = 5MB, MaxSize = 10MB, Filegrowth = 5MB
	)

-- CREACIÓN DE GRUPOS "SECRETARIA" Y "CAJA"
ALTER DATABASE colegio_python ADD FILEGROUP [FG_SECRETARIA]
ALTER DATABASE colegio_python ADD FILEGROUP [FG_CAJA]

ALTER DATABASE colegio_python
ADD FILE
	(
		NAME = colegio_data_G1, FILENAME = 'D:\colegio\fg_data_secretaria.NDF'
	)	TO FILEGROUP [FG_SECRETARIA]

ALTER DATABASE colegio_python
ADD FILE
	(
		NAME = colegio_data_G2, FILENAME = 'D:\colegio\fg_data_caja.NDF'
	)	TO FILEGROUP [FG_CAJA]

EXEC sp_helpdb colegio_python
USE colegio_python; 
SET DATEFORMAT DMY

-- CREACIÓN DE TABLAS
CREATE TABLE tipo_documento
(	tipo_documento_id 	INT			NOT NULL,
	descripcion			VARCHAR(50) NOT NULL,	
	CONSTRAINT PK_TIPO_DOC PRIMARY KEY (tipo_documento_id)	)	
ON [FG_SECRETARIA]	

CREATE TABLE turno
(	turno_id 			INT			NOT NULL,
	tipo_turno			CHAR(1)		NOT NULL DEFAULT 'M',	
	descripcion			VARCHAR(50) NOT NULL,	
	CONSTRAINT PK_TURNO PRIMARY KEY (turno_id)	)
ON [FG_SECRETARIA]

CREATE TABLE aula
(	aula_cod			CHAR(4)		NOT NULL,					
	capacidad			INT			NOT NULL DEFAULT 28,
	vacante				INT			NOT NULL DEFAULT 28,
	CONSTRAINT PK_AULA PRIMARY KEY (aula_cod)	)
ON [FG_SECRETARIA]

CREATE TABLE nivel 
(	nivel_id			INT			NOT NULL,
	descripcion			VARCHAR(10)	NOT NULL,
	CONSTRAINT PK_NIVEL PRIMARY KEY (nivel_id)	)
ON [FG_SECRETARIA]

CREATE TABLE grado 
(	grado_id			INT			NOT NULL,
	grado_cod			CHAR(2)		NOT NULL,						
	descripcion			VARCHAR(10)	NOT NULL,
	nivel_id			INT			NOT NULL,
	CONSTRAINT PK_GRADO PRIMARY KEY (grado_id),	
	CONSTRAINT FK_NIVEL FOREIGN KEY (nivel_id) REFERENCES nivel	)
ON [FG_SECRETARIA]	

CREATE TABLE curso
(	curso_id			INT			NOT NULL,
	curso_cod			VARCHAR(10) NOT NULL,		
	descripcion			VARCHAR(70) NOT NULL,	 
	CONSTRAINT PK_CURSO PRIMARY KEY (curso_id)	)
ON [FG_SECRETARIA]
 
CREATE TABLE docente	
(	docente_id			INT			NOT NULL,
	numero_documento	VARCHAR(12)	NOT NULL,
	tipo_documento_id	INT			NOT NULL, 				
	apellido_paterno 	VARCHAR(20) NOT NULL,
	apellido_materno	VARCHAR(20) NOT NULL,
	nombre				VARCHAR(30) NOT NULL,
	sexo				CHAR(1)		NOT NULL,	
	correo				VARCHAR(50) NULL DEFAULT 'correo@montessori.pe',
	CONSTRAINT PK_DOCENTE PRIMARY KEY (docente_id),
	CONSTRAINT FK_TIPO_DOC_DOC FOREIGN KEY (tipo_documento_id) REFERENCES tipo_documento,
	CONSTRAINT U_DOCUMENTO_DOC UNIQUE(numero_documento),
	CONSTRAINT CHK_SEXO_DOC CHECK (sexo IN ('M','F'))	)
ON [FG_SECRETARIA]

CREATE TABLE apoderado
(	apoderado_id		INT			NOT NULL, 
	numero_documento	VARCHAR(12)	NOT NULL,
	tipo_documento_id	INT			NOT NULL, 
	apellido_paterno 	VARCHAR(20) NOT NULL,
	apellido_materno	VARCHAR(20) NOT NULL,	
	nombre				VARCHAR(30) NOT NULL,
	celular				VARCHAR(50) NOT NULL,		
	correo				VARCHAR(50) NULL DEFAULT 'correo@gmail.com',
	CONSTRAINT PK_APODERADO PRIMARY KEY (apoderado_id),
	CONSTRAINT FK_TIPO_DOC_APOD FOREIGN KEY (tipo_documento_id) REFERENCES tipo_documento,
	CONSTRAINT U_DOCUMENTO_APOD UNIQUE(numero_documento)	)
ON [FG_SECRETARIA]

CREATE TABLE estudiante
(	estudiante_id		INT			NOT NULL,
	numero_documento	VARCHAR(12)	NOT NULL,
	tipo_documento_id	INT			NOT NULL,
	apellido_paterno  	VARCHAR(20) NOT NULL,
	apellido_materno	VARCHAR(20) NOT NULL,
	nombre				VARCHAR(30) NOT NULL,
	sexo				CHAR(1)		NOT NULL,
	fecha_nacimiento	DATETIME	NOT NULL,
	direccion			VARCHAR(100)	NULL,
  	apoderado_id		INT			NOT NULL,
	CONSTRAINT PK_ESTUDIANTE PRIMARY KEY (estudiante_id),	
	CONSTRAINT FK_TIPO_DOC_ESTUD FOREIGN KEY (tipo_documento_id) REFERENCES tipo_documento,
	CONSTRAINT FK_APODERADO FOREIGN KEY (apoderado_id) REFERENCES apoderado,
	CONSTRAINT U_DOCUMENTO_ESTUD UNIQUE(numero_documento),
	CONSTRAINT CHK_SEXO_ESTUD CHECK (sexo IN ('M','F'))	)
ON [FG_SECRETARIA]
   	
CREATE TABLE matricula  
(	matricula_id		INT	IDENTITY NOT NULL,
	fecha				DATETIME	 NOT NULL DEFAULT GETDATE(),
	pension				INT			 NOT NULL,
	grado_id			INT			 NOT NULL,
    aula_cod			CHAR(4)		 NOT NULL,
	anio				INT			 NOT NULL,
	estudiante_id 		INT			 NOT NULL,
	CONSTRAINT PK_MATRICULA PRIMARY KEY (matricula_id),
	CONSTRAINT FK_GRADO FOREIGN KEY (grado_id) REFERENCES grado,
	CONSTRAINT FK_AULA FOREIGN KEY (aula_cod) REFERENCES aula,
	CONSTRAINT FK_ESTUDIANTE FOREIGN KEY (estudiante_id) REFERENCES estudiante	)
ON [FG_SECRETARIA]

CREATE TABLE comprobante
(	tipo_comprobante	INT	IDENTITY NOT NULL,	
	nro_comprobante		INT			 NOT NULL,	
	fecha				DATETIME	 NOT NULL DEFAULT GETDATE(),
	descripcion			VARCHAR(50)  NOT NULL,
	matricula_id		INT			 NOT NULL,
	CONSTRAINT PK_COMPROBANTE PRIMARY KEY (tipo_comprobante, nro_comprobante),
	CONSTRAINT FK_MATRICULA FOREIGN KEY (matricula_id) REFERENCES matricula,
	CONSTRAINT CHK_TIPO_COMP CHECK (tipo_comprobante IN ('BOLETA','FACTURA'))	)
ON [FG_CAJA]	
    	
CREATE TABLE horario 
(	horario_id			INT IDENTITY NOT NULL,
	dia					VARCHAR(9)	 NOT NULL,
	hora_inicio			VARCHAR(5)	 NOT NULL,
	hora_fin			VARCHAR(5)	 NOT NULL,
	curso_id			INT			 NOT NULL,
	aula_cod			CHAR(4)		 NOT NULL,
    docente_id			INT			 NOT NULL,
	turno_id			INT			 NOT NULL,
	CONSTRAINT PK_HORARIO PRIMARY KEY (horario_id),
	CONSTRAINT FK_CURSO FOREIGN KEY (curso_id) REFERENCES curso,
	CONSTRAINT FK_AULA_HORARIO FOREIGN KEY (aula_cod) REFERENCES aula,
	CONSTRAINT FK_TURNO FOREIGN KEY (turno_id) REFERENCES turno,
	CONSTRAINT FK_DOCENTE FOREIGN KEY (docente_id) REFERENCES docente	)
ON [FG_SECRETARIA]

EXEC sp_help tipo_documento;
EXEC sp_help turno;
EXEC sp_help aula;
EXEC sp_help nivel;
EXEC sp_help grado;
EXEC sp_help curso;
EXEC sp_help docente;
EXEC sp_help apoderado;
EXEC sp_help estudiante;
EXEC sp_help matricula;
EXEC sp_help comprobante;
EXEC sp_help horario;
    	
-- INSERTACIÓN REGISTROS
-- TABLE tipo_documento
INSERT INTO tipo_documento VALUES (1,'DNI'); 
INSERT INTO tipo_documento VALUES (2,'PASAPORTE');
INSERT INTO tipo_documento VALUES (3,'CARNÉ DE EXTRANJERÍA');
INSERT INTO tipo_documento VALUES (4,'PTP');

-- TABLE turno
INSERT INTO turno VALUES (1,'M', 'MAÑANA'); 
INSERT INTO turno VALUES (2,'T', 'TARDE'); 
INSERT INTO turno VALUES (3,'N', 'NOCHE'); 

-- TABLE  aula 
INSERT INTO aula VALUES('A101',28,28); 
INSERT INTO aula VALUES('A201',28,28);
INSERT INTO aula VALUES('A202',28,28);
INSERT INTO aula VALUES('A203',28,28);
INSERT INTO aula VALUES('A301',28,28);
INSERT INTO aula VALUES('A302',28,28);
INSERT INTO aula VALUES('A303',28,28);
INSERT INTO aula VALUES('B101',28,28);
INSERT INTO aula VALUES('B102',28,28);
INSERT INTO aula VALUES('B103',28,28);
INSERT INTO aula VALUES('B201',28,28);
INSERT INTO aula VALUES('B202',28,28);
INSERT INTO aula VALUES('B203',28,28);
INSERT INTO aula VALUES('B301',28,28);
INSERT INTO aula VALUES('B302',28,10);
SELECT * FROM aula
-- TABLE  nivel 
INSERT INTO nivel VALUES(1,'INICIAL');
INSERT INTO nivel VALUES(2,'PRIMARIA');
INSERT INTO nivel VALUES(3,'SECUNDARIA');

-- TABLE  grado 
INSERT INTO grado VALUES(1,'3A','3 AÑOS',1); 
INSERT INTO grado VALUES(2,'4A','4 AÑOS',1);
INSERT INTO grado VALUES(3,'5A','5 AÑOS',1);
INSERT INTO grado VALUES(4,'1P','PRIMERO',2);
INSERT INTO grado VALUES(5,'2P','SEGUNDO',2);
INSERT INTO grado VALUES(6,'3P','TERCERO',2);
INSERT INTO grado VALUES(7,'4P','CUARTO',2);
INSERT INTO grado VALUES(8,'5P','QUINTO',2);
INSERT INTO grado VALUES(9,'6P','SEXTO',2);
INSERT INTO grado VALUES(10,'1S','PRIMERO',3);
INSERT INTO grado VALUES(11,'2S','SEGUNDO',3);
INSERT INTO grado VALUES(12,'3S','TERCERO',3);
INSERT INTO grado VALUES(13,'4S','CUARTO',3);
INSERT INTO grado VALUES(14,'5S','QUINTO',3);

-- TABLE curso 
INSERT INTO curso VALUES (1,'PSICO','PSICOMOTRIZ');
INSERT INTO curso VALUES (2,'ART Y CULT','ARTE Y CULTURA');
INSERT INTO curso VALUES (3,'CAST SEGNL','CASTELLANO COMO SEGUNDA LENGUA');
INSERT INTO curso VALUES (4,'CIENC Y TEC', 'CIENCIA Y TECNOLOGÍA');
INSERT INTO curso VALUES (5,'CCSS','CIENCIAS SOCIALES');
INSERT INTO curso VALUES (6,'PPSS','PERSONAL SOCIAL');
INSERT INTO curso VALUES (7,'COMU','COMUNICACIÓN');
INSERT INTO curso VALUES (8,'DESARR PCC','DESARROLLO PERSONAL, CIUDADANÍA Y CÍVICA');
INSERT INTO curso VALUES (9,'EFIS','EDUCACIÓN FÍSICA');
INSERT INTO curso VALUES (10,'ETRA','EDUCACIÓN PARA EL TRABAJO');
INSERT INTO curso VALUES (11,'EREL','EDUCACIÓN RELIGIOSA');
INSERT INTO curso VALUES (12,'INGLES','INGLÉS COMO LENGUA EXTRANJERA');
INSERT INTO curso VALUES (13,'MATE','MATEMÁTICA');
INSERT INTO curso VALUES (14,'GEST AUTO','GESTIONA SU APRENDIZAJE DE MANERA AUTÓNOMA');
INSERT INTO curso VALUES (15,'DESEN TIC','SE DESENVUELVE EN ENTORNOS VIRTUALES GENERADOS POR LAS TIC');

--TABLE  docente 
INSERT INTO docente VALUES(1,41954449,1,'FLORES', 'VILA', 'DIANA FLOR', 'F','correo@montessori.pe');
INSERT INTO docente VALUES(2,45628586,1,'ZAPATA', 'ARIAS', 'RAFAEL DAVID', 'M','correo@montessori.pe');
INSERT INTO docente VALUES(3,43910769,1,'CUENCA', 'ESPINOZA', 'ISMAEL ENDERSON', 'M','correo@montessori.pe');
INSERT INTO docente VALUES(4,43818888,1,'ROBLES', 'CHANCAHUAÑA', 'LISSETH SONIA', 'F','correo@montessori.pe');
INSERT INTO docente VALUES(5,41062291,1,'ARIZAPANA', 'CRUZ', 'GERALDINE NAHOMY', 'F','correo@montessori.pe');
INSERT INTO docente VALUES(6,71224184,1,'CORZO', 'MAYTA', 'EDINZN RAINIERO', 'M','correo@montessori.pe');
INSERT INTO docente VALUES(7,70339328,1,'ARANGO', 'ROJAS', 'SANDRA VERONICA', 'F','correo@montessori.pe');
INSERT INTO docente VALUES(8,41629413,1,'BUSTOS', 'AYBAR', 'ROSA ELIZABETH', 'F','correo@montessori.pe');
INSERT INTO docente VALUES(9,80040712,1,'SAENZ', 'HUAMANI', 'CARLOS ALBERTO', 'M','correo@montessori.pe');
INSERT INTO docente VALUES(10,42947479,1,'MENDOZA', 'SANTISTEBAN', 'ERICK JUAN JOSE', 'M','correo@montessori.pe');
INSERT INTO docente VALUES(11,45277233,1,'COTRINA', 'ESPINOZA', 'JESUS GONZALO', 'M','correo@montessori.pe');
INSERT INTO docente VALUES(12,44405211,1,'AGÜERO', 'MENDOZA', 'YADIRA CECILIA', 'F','correo@montessori.pe');
INSERT INTO docente VALUES(13,43856697,1,'CASTELLON', 'RAMOS', 'JHON ERICK', 'M','correo@montessori.pe');
INSERT INTO docente VALUES(14,40720459,1,'ROMERO', 'SILVA', 'YESABEL YARELY', 'F','correo@montessori.pe');
INSERT INTO docente VALUES(15,41639286,1,'MARTINEZ', 'CONDEMARIN', 'ANGELLO MARTIN', 'M','correo@montessori.pe');

--TABLE apoderado
INSERT INTO apoderado VALUES(1,20071681,1,'CORAL','PACCO', 'JOSE MANUEL',997567217,'correo@gmail.com');
INSERT INTO apoderado VALUES(2,44387937,1,'PANDURO','OCHOA', 'NICOLAS ENRIQUE',932567280,'correo@gmail.com');
INSERT INTO apoderado VALUES(3,71729196,1,'NEGREROS','MOLINA', 'ALEXIS GIOVANNY',997567225,'correo@gmail.com' );
INSERT INTO apoderado VALUES(4,157941098871,3,'LEON','VERA', 'DAYANNA MIRELLA',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(5,09940316,1,'MENDOZA','ANCHAYHUA', 'LUIS DAVID',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(6,70365497,1,'YALLI','RAMON', 'EMILY AYME',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(7,259343266883,3,'INOCENTE','ABANTO', 'LINDA DANNA',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(8,40659017,1,'NEYRA','VELASQUEZ', 'RAUL CRISTOBAL',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(9,987242720182,3,'AROSTEGUI','PORRAS', 'MIGUEL ANGEL',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(10,40837713,1,'LOPEZ','ESPINOZA', 'JEREMY IMANOL',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(11,365845879698,3,'MENDOZA','HUAYANCA', 'YAJHAIRA XIMENA',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(12,40875917,1,'MAYTA','MACHUCA', 'KARINA MARLEN',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(13,539846118319,3,'SERPA','TORRES', 'FABIOLA SUGEY',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(14,43427607,1,'VALDIVIA','VILLEGAS', 'EDILSON JARECK',997567217,'correo@gmail.com' );
INSERT INTO apoderado VALUES(15,44345310,1,'HUACAC','LINARES', 'DAVID BRYAM',997567217,'correo@gmail.com' );

--TABLE estudiante 
INSERT INTO estudiante VALUES(1,60085301,1,'ACEVEDO', 'MANTARI', 'RONALD WILLIAMS', 'M',2010/03/01,'Jr. Jiron Garcia Y Garcia #870',1);
INSERT INTO estudiante VALUES(2,72306548,1,'ARCOS', 'MONTALBAN', 'JOSE ANTONIO', 'M',2011/03/01,'Av. Avenida Guillermo Dansey #1799',2);
INSERT INTO estudiante VALUES(3,78113024,1,'CARDENAS', 'ESPINOZA', 'JULIANA ANGELA', 'F',2012/03/01,'Av. Avenida Tomas Marsano #507',3);
INSERT INTO estudiante VALUES(4,75332354,1,'ACHO','CHAVEZ','JONATHAN SMITH', 'M',2012/03/01,'Av. Avenida Aviacion #2501',4);
INSERT INTO estudiante VALUES(5,71914480,1,'ALCA','OSORIO','FREDDY ANTONIO', 'M',2012/03/01,'Av. Avenida Petit Thouars #3595',5);
INSERT INTO estudiante VALUES(6,76127533,1,'ARROYO','CENTENO','BRAYAN WALTER', 'M',2013/03/01,'Av. Avenida Emancipacion #282',6);
INSERT INTO estudiante VALUES(7,76448010,1,'AVELINO','BONILLA','JAZMIN ADRIANA', 'F',2010/03/01,'Av. Avenida Coronel Andres Reyes #420',7);
INSERT INTO estudiante VALUES(8,77535412,1,'CABANILLAS','TINOCO','JOAQUIN OMAR', 'M',2014/03/01,'Av. Avenida La Molina #2830',8);
INSERT INTO estudiante VALUES(9,71658467,1,'CALOPINO','LLACCHUARIMAY','CESAR DAVID', 'M',2013/03/01,'Jr. Jiron Boccioni #386',9);
INSERT INTO estudiante VALUES(10,77496208,1,'CAMPOS','MANRIQUE','JHOSTIN JESUS', 'M',2011/03/01,'Av. Avenida Victor Andres Belaunde #147',10);
INSERT INTO estudiante VALUES(11,74806709,1,'CANCHASTO','ACHO','CARLOS ALFONSO', 'M',2010/03/01,'Av. Avenida Emancipacion #282',11);
INSERT INTO estudiante VALUES(12,76809322,1,'CORREA','ROSADO','MIRELLA KAREN', 'F',2012/03/01,'Av. Avenida Aviacion #2501',12);
INSERT INTO estudiante VALUES(13,71768803,1,'DELGADO','MACHUCA','GRECIA CAROLINA', 'F',2009/03/01,'Av. Avenida Guillermo Dansey #1799',13);
INSERT INTO estudiante VALUES(14,73463765,1,'ZACARIAS', 'CALDERON', 'JOSE SEBASTIAN', 'M',2008/03/01,'Jr. Jiron Garcia Y Garcia #870',14);
INSERT INTO estudiante VALUES(15,74737726,1,'ZARATE', 'CASAS', 'GREYSI MILAGROS', 'F',2008/03/01,'Av. Avenida La Molina #2830',15);

--TABLE horario 
INSERT INTO horario VALUES('LUNES','8:00','10:00',5,'A101',2,1)
INSERT INTO horario VALUES('LUNES','1:00','2:00',1,'A101',2,1)
INSERT INTO horario VALUES('MARTES','10:00','12:00',2,'A101',10,1)
INSERT INTO horario VALUES('MIERCOLES','10:00','12:00',4,'A101',9,1)
INSERT INTO horario VALUES('JUEVES','10:00','12:00',6,'A101',5,1)
INSERT INTO horario VALUES('VIERNES','8:00','9:00',7,'A101',4,1)
INSERT INTO horario VALUES('LUNES','8:00','10:00',8,'A101',4,1)
INSERT INTO horario VALUES('MARTES','10:00','12:00',9,'A101',5,1)
INSERT INTO horario VALUES('MIERCOLES','10:00','12:00',15,'A101',2,1)
INSERT INTO horario VALUES('JUEVES','10:00','12:00',5,'A201',3,1)
INSERT INTO horario VALUES('VIERNES','8:00','9:00',4,'A201',12,1)
INSERT INTO horario VALUES('LUNES','8:00','10:00',3,'A201',11,1)
INSERT INTO horario VALUES('MARTES','10:00','12:00',12,'A201',9,1)
INSERT INTO horario VALUES('MIERCOLES','8:00','9:00',11,'A201',14,1)
INSERT INTO horario VALUES('JUEVES','10:00','12:00',10,'A201',13,1)

--TABLE matricula 
INSERT INTO matricula VALUES(GETDATE(),300,'1','A101',2022,'1') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='A101'

INSERT INTO matricula VALUES(GETDATE(),300,'1','A101',2022,'10') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='A101'

INSERT INTO matricula VALUES(GETDATE(),300,'1','A101',2022,'12') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='A101'

INSERT INTO matricula VALUES(GETDATE(),310,'3','B101',2022,'3') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='B101'

INSERT INTO matricula VALUES(GETDATE(),310,'3','B101',2022,'5') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='B101'

INSERT INTO matricula VALUES(GETDATE(),310,'3','B101',2022,'7') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='B101'

INSERT INTO matricula VALUES(GETDATE(),320,'6','A302',2022,'9') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='A302'

INSERT INTO matricula VALUES(GETDATE(),320,'6','A302',2022,'11') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='A302'

INSERT INTO matricula VALUES(GETDATE(),320,'4', 'A203',2022,'13') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='A203'

INSERT INTO matricula VALUES(GETDATE(),320,'4','A203',2022,'15') 
UPDATE aula SET vacante = vacante-1 WHERE aula_cod ='A203'

SELECT * FROM aula
SELECT * FROM matricula

-- CONSULTAS
-- CURSOS DOCENTES 
SELECT  d.numero_documento  AS "Codigo Docente",
        d.apellido_paterno +' '+ d.apellido_materno AS "Apellidos Docente",
        d.nombre	AS "Nombres Docente",
        c.descripcion AS "Curso Docente"
FROM	horario cd
        INNER JOIN	docente d ON (cd.docente_id=d.docente_id) 
        INNER JOIN	curso c ON (cd.curso_id=c.curso_id)
GROUP BY d.numero_documento, d.apellido_paterno, d.apellido_materno, d.nombre, c.descripcion
ORDER BY d.apellido_paterno;

-- HORARIOS DOCENTES
SELECT  d.numero_documento AS "Codigo Docente",
        d.apellido_paterno +' '+ d.apellido_materno AS "Apellidos Docente",
        d.nombre	AS "Nombres Docente",
        c.descripcion AS "Curso Docente",
        cd.dia AS "Día",
        cd.hora_inicio AS "Horario Inicio",
        cd.hora_fin AS "Horario Fin",
        a.aula_cod AS "Aula"
FROM	horario cd
        INNER JOIN	docente d ON (cd.docente_id=d.docente_id) 
        INNER JOIN	curso c ON (cd.curso_id=c.curso_id)
        INNER JOIN	aula a ON (cd.aula_cod=a.aula_cod)  
GROUP BY d.numero_documento, d.apellido_paterno, d.apellido_materno, d.nombre, c.descripcion,cd.dia, cd.hora_inicio, cd.hora_fin,a.aula_cod
ORDER BY d.apellido_paterno;

-- CONSTANCIA DE MATRÍCULA
SELECT m.anio AS "Año lectivo",
       e.numero_documento AS "DNI Estudiante",
       e.apellido_paterno + e.apellido_materno AS "Apellidos Estudiante",
       e.nombre	AS "Nombres Estudiante",
       g.descripcion AS Grado,
       n.descripcion AS Nivel,
       a.numero_documento "Código Apoderado",
       a.apellido_paterno +' '+ a.apellido_materno AS "Apellidos Apoderado",
       a.nombre	AS "Nombres Apoderado"
FROM matricula m 
    INNER JOIN estudiante e ON (m.estudiante_id=e.estudiante_id)
    INNER JOIN apoderado a ON (e.apoderado_id=a.apoderado_id)
    INNER JOIN grado g ON (m.grado_id=g.grado_id)
    INNER JOIN nivel n ON (g.nivel_id=n.nivel_id)
GO

-- VISTA CONSTANCIA DE MATRÍCULA
CREATE VIEW constancia_matricula
AS
SELECT m.anio AS "Año lectivo",
       e.numero_documento AS "DNI Estudiante",
       e.apellido_paterno + e.apellido_materno AS "Apellidos Estudiante",
       e.nombre	AS "Nombres Estudiante",
       g.descripcion AS Grado,
       n.descripcion AS Nivel,
       a.numero_documento "Código Apoderado",
       a.apellido_paterno +' '+ a.apellido_materno AS "Apellidos Apoderado",
       a.nombre	AS "Nombres Apoderado"
FROM matricula m 
    INNER JOIN estudiante e ON (m.estudiante_id=e.estudiante_id)
    INNER JOIN apoderado a ON (e.apoderado_id=a.apoderado_id)
    INNER JOIN grado g ON (m.grado_id=g.grado_id)
    INNER JOIN nivel n ON (g.nivel_id=n.nivel_id)
GO

SELECT * FROM constancia_matricula;
GO

-- PROCEDURE MATRÍCULA
CREATE OR ALTER PROCEDURE sp_registrar_matricula (
    @p_pension          INT,
    @p_grado            INT,
    @p_aula_cod         CHAR(4),
	@p_anio_id			INT, 
    @p_estudiante_id    INT	)
AS 
BEGIN
    INSERT INTO matricula (fecha, pension, grado_id, aula_cod, anio, estudiante_id) 
	VALUES (GETDATE(), @p_pension, @p_grado, @p_aula_cod , @p_anio_id, @p_estudiante_id);
	UPDATE aula SET vacante = vacante-1 WHERE aula_cod = @p_aula_cod;
	PRINT('MATRÍCULA REGISTRADA');
END;

SELECT * FROM aula

EXECUTE sp_registrar_matricula 350,'1','B302',2022,'1'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'2'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'3'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'4'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'5'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'6'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'7'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'8'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'9'
EXECUTE sp_registrar_matricula 350,'1','B302',2022,'10'

EXECUTE sp_registrar_matricula 350,'1','B302',2022,'11'


SELECT * FROM matricula
SELECT * FROM aula
GO

-- TRIGGER vacante
CREATE OR ALTER TRIGGER tg_vacante
ON aula
FOR UPDATE 
AS
IF (SELECT vacante FROM INSERTED) < 0 
BEGIN
    RAISERROR ('NO QUEDAN VACANTES DISPONIBLES EN EL AULA',10,1)
    ROLLBACK TRANSACTION
END;