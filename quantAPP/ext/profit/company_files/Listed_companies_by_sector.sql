BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Listed_companies_by_sector" (
	"index"	BIGINT,
	"Empresas"	TEXT,
	"Ativos"	TEXT,
	"Unnamed: 2"	TEXT,
	"Unnamed: 3"	TEXT,
	"Unnamed: 4"	TEXT,
	"Unnamed: 5"	TEXT,
	"Unnamed: 6"	TEXT,
	"Setor"	TEXT
);
INSERT INTO "Listed_companies_by_sector" ("index","Empresas","Ativos","Unnamed: 2","Unnamed: 3","Unnamed: 4","Unnamed: 5","Unnamed: 6","Setor") VALUES (0,'CELPE','CEPE6F','CEPE5F','CEPE3F','CEPE6','CEPE5','CEPE3','Utilidade Pública'),
 (1,'CEEE-D','CEED3F','CEED4F','CEED4','CEED3',NULL,NULL,'Utilidade Pública'),
 (2,'CEEE-GT','EEEL4F','EEEL3F','EEEL4','EEEL3',NULL,NULL,'Utilidade Pública'),
 (3,'CASAN','CASN4F','CASN3F','CASN4','CASN3',NULL,NULL,'Utilidade Pública'),
 (4,'CEG','CEGR3F','CEGR3',NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (5,'CEB','CEBR3F','CEBR6F','CEBR5F','CEBR6','CEBR5','CEBR3','Utilidade Pública'),
 (6,'RENOVA','RNEW11F','RNEW11F','RNEW4F','RNEW4','RNEW3',NULL,'Utilidade Pública'),
 (7,'COELCE','COCE6F','COCE5F','COCE3F','COCE6','COCE5','COCE3','Utilidade Pública'),
 (8,'CELESC','CLSC4F','CLSC3F','CLSC4','CLSC3',NULL,NULL,'Utilidade Pública'),
 (9,'ALUPAR INVESTIMENTO','ALUP4F','ALUP3F','ALUP11F','ALUP4','ALUP3','ALUP11','Utilidade Pública'),
 (10,'SANEPAR','SAPR11F','SAPR4F','SAPR3F','SAPR4','SAPR3','SAPR11','Utilidade Pública'),
 (11,'CPFL RENOVAV','CPRE3F','CPRE3',NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (12,'COPEL','CPLE5F','CPLE6F','CPLE6','CPLE5','CPLE3F','CPLE3','Utilidade Pública'),
 (13,'CPFL ENERGIA','CPFE3F','CPFE3',NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (14,'COMGÁS','CGAS3F','CGAS5F','CGAS5','CGAS3',NULL,NULL,'Utilidade Pública'),
 (15,'AES BRASIL','AESB3F','AESB3',NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (16,'NEOENERGIA','NEOE3',NULL,NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (17,'ISA CTEEP','TRPL4F','TRPL4','TRPL3F','TRPL3',NULL,NULL,'Utilidade Pública'),
 (18,'ENGIE BRASIL','EGIE3',NULL,NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (19,'TAESA','TAEE4','TAEE3','TAEE11',NULL,NULL,NULL,'Utilidade Pública'),
 (20,'SABESP','SBSP3F','SBSP3',NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (21,'RENAOVA','RNEW11',NULL,NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (22,'GER PARANAPANEMA','GEPA4','GEPA3',NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (23,'CESP','CESP6','CESP5','CESP3F','CESP3',NULL,NULL,'Utilidade Pública'),
 (24,'CEMIG','CMIG4','CMIG3F','CMIG3',NULL,NULL,NULL,'Utilidade Pública'),
 (25,'AFLUENTE T','AFLT3',NULL,NULL,NULL,NULL,NULL,'Utilidade Pública'),
 (26,'VERIZON','VERZ34F','VERZ34',NULL,NULL,NULL,NULL,'Telecomunicações'),
 (27,'OI','OIBR4F','OIBR4','OIBR',NULL,NULL,NULL,'Telecomunicações'),
 (28,'TIM PARTICIPAÇÕES','TIMS3F','TIMS3',NULL,NULL,NULL,NULL,'Telecomunicações'),
 (29,'TELEFÔNICA BRASIL S.A','VIVT4F','VIVT4','VIVT3F','VIVT3',NULL,NULL,'Telecomunicações'),
 (30,'TELEBRAS','TELB4F','TELB4','TELB3F','TELB3',NULL,NULL,'Telecomunicações'),
 (31,'ATT INC','ATTB34',NULL,NULL,NULL,NULL,NULL,'Telecomunicações'),
 (32,'ADOBE SYSTEMS INCORPORATED','ADBE',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (33,'COMCAST CORPORATION','CMCSA',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (34,'CISCO SYSTEMS INC','CSCO',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (35,'INTEL CORPORATION','INTC',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (36,'FACEBOOK INC','FB',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (37,'AMAZON.COM INC','AMZN',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (38,'APPLE INC','AAPL',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (39,'MICROSOFT CORPORATION','MSFT',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (40,'ALPHABET','GOGL35',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (41,'LOCAWEB','LWSA3',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (42,'TOTVS','TOTS3F','TOTS3',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (43,'XEROX','XRXB34F','XRXB34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (44,'QUALCOMM','QCOM34F','QCOM34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (45,'ORACLE','ORCL34F','ORCL34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (46,'MICROSOFT','MSFT34F','MSFT34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (47,'IBM','IBMB34F','IBMB34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (48,'INTEL','ITLC34F','ITLC34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (49,'HP COMPANY','HPQB34F','HPQB34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (50,'EBAY','EBAY34F',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (51,'CISCO','CSCO34F','CSCO34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (52,'ATT INC','ATTB34F',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (53,'APPLE','AAPL34F','AAPL34',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (54,'LINX','LINX3F','LINX3',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (55,'POSITIVO INF','POSI3F','POSI3',NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (56,'EBAY','EBAY34',NULL,NULL,NULL,NULL,NULL,'Tecnologia da Informação'),
 (57,'INSTITUTO HERMES PARDINI SA','PARD3',NULL,NULL,NULL,NULL,NULL,'Saúde'),
 (58,'BIOMM','BIOM3F','BIOM3',NULL,NULL,NULL,NULL,'Saúde'),
 (59,'BAUMER','BALM3F','BALM4F','BALM4','BALM3',NULL,NULL,'Saúde'),
 (60,'PFIZER','PFIZ34F','PFIZ34',NULL,NULL,NULL,NULL,'Saúde'),
 (61,'MERCK','MRCK34F','MRCK34',NULL,NULL,NULL,NULL,'Saúde'),
 (62,'BIOTOSCANA','GBIO33F','GBIO33',NULL,NULL,NULL,NULL,'Saúde'),
 (63,'DIMED','PNVL4F','PNVL3F','PNVL4','PNVL3',NULL,NULL,'Saúde'),
 (64,'ALLIAR','AALR3F','AALR3',NULL,NULL,NULL,NULL,'Saúde'),
 (65,'ODONTOPREV','ODPV3F','ODPV3',NULL,NULL,NULL,NULL,'Saúde'),
 (66,'RD','RADL3F','RADL3',NULL,NULL,NULL,NULL,'Saúde'),
 (67,'QUALICORP','QUAL3F','QUAL3',NULL,NULL,NULL,NULL,'Saúde'),
 (68,'OUROFINO S/A','OFSA3',NULL,NULL,NULL,NULL,NULL,'Saúde'),
 (69,'JOHNSON','JNJB34',NULL,NULL,NULL,NULL,NULL,'Saúde'),
 (70,'HYPERA PHARMA','HYPE3',NULL,NULL,NULL,NULL,NULL,'Saúde'),
 (71,'FLEURY','FLRY3',NULL,NULL,NULL,NULL,NULL,'Saúde'),
 (72,'BRISTOLMYERS','BMYB34',NULL,NULL,NULL,NULL,NULL,'Saúde'),
 (73,'ABBOTT LABORATORIES','ABTT34',NULL,NULL,NULL,NULL,NULL,'Saúde'),
 (74,'PETRORECÔNCAVO GERAL SA','RECV3',NULL,NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (75,'SCHLUMBERGER','SLBG34F','SLBG34',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (76,'HALLIBURTON','HALI34F','HALI34',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (77,'COPHILLIPS','COPH34','COPH34',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (78,'CHEVRON','CHVX34F','CHVX34',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (79,'PETRORIO','PRIO3F','PRIO3',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (80,'OSX BRASIL','OSXB3F','OSXB3',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (81,'DOMMO','DMMO11','DMMO3F','DMMO3',NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (82,'PET MANGUINHOS','RPMG3F','RPMG3',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (83,'ULTRAPAR','UGPA3','UGPA3F',NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (84,'PETROBRAS','PETR4F','PETR4','PETR3F','PETR3',NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (85,'PETROBRAS DISTRIBUIDORA','BRDT3',NULL,NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (86,'EXXON MOBIL','EXXO34',NULL,NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (87,'ENAUTA PART','ENAT3',NULL,NULL,NULL,NULL,NULL,'Petróleo, Gás e Biocombustíveis'),
 (88,'DEXXOS PART','DEXP4','DEXP3',NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (89,'CELUL IRANI','RANI3F','RANI4F',NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (90,'FREEPORT','FCXO34F','FCXO34',NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (91,'PARANAPANEMA','PMAM3F','PMAM3',NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (92,'FERBASA','FESA4F','FESA3F','FESA4','FESA3',NULL,NULL,'Materiais Básicos'),
 (93,'EUCATEX','EUCA4F','EUCA3F','EUCA4','EUCA3',NULL,NULL,'Materiais Básicos'),
 (94,'SUZANO PAPEL','SUZB3F','SUZB3',NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (95,'KLABIN S/A','KLBN4F','KLBN3F','KLBN11F','KLBN4','KLBN3','KLBN11','Materiais Básicos'),
 (96,'VALE','VALE5',NULL,NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (97,'UNIPAR','UNIP6F','UNIP6','UNIP5F','UNIP5','UNIP3',NULL,'Materiais Básicos'),
 (98,'SUZANO HOLDING','NEMO6','NEMO5','NEMO3',NULL,NULL,NULL,'Materiais Básicos'),
 (99,'MMX MINERAÇÃO','MMXM3','MMXM11',NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (100,'GERDAU','GOAU4',NULL,NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (101,'CSN','CSNA3F','CSNA3',NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (102,'CELULOSE IRANI','RANI4',NULL,NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (103,'BRASKEM','BRKM6','BRKM5F','BRKM5','BRKM3',NULL,NULL,'Materiais Básicos'),
 (104,'BRADESPAR','BRAP4F','BRAP4','BRAP3F','BRAP3',NULL,NULL,'Materiais Básicos'),
 (105,'ARCELOR','ARMT34',NULL,NULL,NULL,NULL,NULL,'Materiais Básicos'),
 (106,'BOA SAFRA','SOJA3',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (107,'ZYNGA INC','Z2NG34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (108,'TRADE DESK','T2TD34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (109,'TELADOCHEALT','T2DH34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (110,'SUN COMMUN','S2UI34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (111,'SQUARE INC','S2QU34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (112,'SNOWFLAKE','S2NW34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (113,'SHOPIFY INC','S2HO34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (114,'CAESARS ENTT','C2ZR34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (115,'UNITY SOFTWR','U2ST34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (116,'SEA LTD','S2EA34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (117,'PENN NATIONL','P2EN34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (118,'MEDICAL P TR','M2PW34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (119,'KINGSOFT CHL','K2CG34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (120,'DRAFTKINGS','D2KN34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (121,'CYRUSONE INC','C2ON34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (122,'CHURCHILL DW','C2HD34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (123,'BEYOND MEAT','B2YN34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (124,'ENERGISA MT','ENMT4','ENMT3',NULL,NULL,NULL,NULL,'Outros'),
 (125,'AIRBNB','AIRB34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (126,'PAGSEGURO','PAGS34',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (127,'HBR REALTY','HBRE3','HBRE3F',NULL,NULL,NULL,NULL,'Outros'),
 (128,'TREND CHINA','XINA11',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (129,'AUTOMATIC DATA PROCESSING INC.','ADP',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (130,'ONE LIBERTY PROPERTIES INC.','OLP',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (131,'AKEBIA THERAPEUTICS INC.','AKBA',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (132,'DULUTH HOLDINGS INC. CLASS B','DLTH',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (133,'ENDURANCE INTERNATIONAL GROUP HOLDINGS INC.','EIGI',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (134,'KBL MERGER CORP. IV','KBLM',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (135,'EVERSPIN TECHNOLOGIES INC.','MRAM',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (136,'DESPEGAR.COM CORP.','DESP',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (137,'BELLICUM PHARMACEUTICALS INC','BLCM',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (138,'CULP INC.','CULP',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (139,'LEVI STRAUSS & CO. CLASS A','LEVI',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (140,'HUNTINGTON INGALLS INDUSTRIES INC.','HII',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (141,'ASSEMBLY BIOSCIENCES INC.','ASMB',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (142,'CABALETTA BIO INC.','CABA',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (143,'TRIMBLE INC.','TRMB',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (144,'RIBBON COMMUNICATIONS INC.','RBBN',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (145,'FIDELITY D & D BANCORP INC.','FDBC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (146,'PARTNERS BANCORP','PTRS',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (147,'HUDSON LTD. CLASS A','HUD',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (148,'OSHKOSH CORP','OSK',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (149,'OP BANCORP','OPBK',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (150,'EQUILLIUM INC.','EQ',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (151,'SEACHANGE INTERNATIONAL INC.','SEAC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (152,'RAND CAPITAL CORPORATION','RAND',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (153,'EASTMAN CHEMICAL COMPANY','EMN',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (154,'REPRO MED SYSTEMS INC.','KRMD',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (155,'GX ACQUISITION CORP. CLASS A','GXGX',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (156,'MOHAWK INDUSTRIES INC.','MHK',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (157,'APOGEE ENTERPRISES INC.','APOG',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (158,'HUDSON EXECUTIVE INVESTMENT CORP CLASS A','HEC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (159,'XENON PHARMACEUTICALS INC.','XENE',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (160,'ALPHABET INC. CLASS A','GOOGL',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (161,'LIVE NATION ENTERTAINMENT INC.','LYV',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (162,'ADVANCED DRAINAGE SYSTEMS INC.','WMS',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (163,'BLACK DIAMOND THERAPEUTICS INC.','BDTX',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (164,'VIRTUSA CORPORATION','VRTU',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (165,'KBR INC.','KBR',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (166,'WESTWOOD HOLDINGS GROUP INC.','WHG',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (167,'HARTFORD FINANCIAL SERVICES GROUP INC.','HIG',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (168,'NEURONETICS INC.','STIM',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (169,'MAGNACHIP SEMICONDUCTOR CORPORATION','MX',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (170,'STATE AUTO FINANCIAL CORPORATION','STFC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (171,'VAPOTHERM INC.','VAPO',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (172,'MESA ROYALTY TRUST','MTR',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (173,'CITIGROUP INC.','C',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (174,'L.S. STARRETT COMPANY CLASS A','SCX',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (175,'EKSO BIONICS HOLDINGS INC.','EKSO',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (176,'AMERISERV FINANCIAL INC.','ASRV',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (177,'GLADSTONE CAPITAL CORPORATION','GLAD',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (178,'HOUGHTON MIFFLIN HARCOURT COMPANY','HMHC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (179,'HEALTHEQUITY INC','HQY',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (180,'LEMONADE INC','LMND',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (181,'CHECK POINT SOFTWARE TECHNOLOGIES LTD.','CHKP',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (182,'VICTORY CAPITAL HOLDINGS INC. CLASS A','VCTR',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (183,'VEEVA SYSTEMS INC CLASS A','VEEV',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (184,'CONSTELLATION BRANDS INC. CLASS B','STZ.B',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (185,'CONSUMER PORTFOLIO SERVICES INC.','CPSS',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (186,'NATURAL HEALTH TRENDS CORP.','NHTC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (187,'CHARLES RIVER LABORATORIES INTERNATIONAL INC.','CRL',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (188,'SEI INVESTMENTS COMPANY','SEIC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (189,'DMY TECHNOLOGY GROUP INC CLASS A','DMYT',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (190,'ALTABANCORP','ALTA',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (191,'BOEING COMPANY','BA',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (192,'BARRETT BUSINESS SERVICES INC.','BBSI',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (193,'BOOT BARN HOLDINGS INC.','BOOT',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (194,'MARKEL CORPORATION','MKL',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (195,'ARCH RESOURCES INC. CLASS A','ARCH',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (196,'EVER-GLORY INTERNATIONAL GROUP INC.','EVK',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (197,'ITERUM THERAPEUTICS PLC','ITRM',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (198,'GCP APPLIED TECHNOLOGIES INC.','GCP',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (199,'KEARNY FINANCIAL CORP.','KRNY',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (200,'FLUX POWER HOLDINGS INC.','FLUX',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (201,'OHIO VALLEY BANC CORP.','OVBC',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (202,'INTERPACE BIOSCIENCES INC.','IDXG',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (203,'SAIA INC.','SAIA',NULL,NULL,NULL,NULL,NULL,'Outros'),
 (204,'THE BANK OF NEW YORK MELLON CORPORATION','BK',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (205,'BANK OF AMERICA CORPORATION','BAC',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (206,'BRB BANCO','BSLI4F','BSLI3F','BSLI4','BSLI3',NULL,NULL,'Financeiro'),
 (207,'BATTISTELLA','BTTL3F','BTTL3',NULL,NULL,NULL,NULL,'Financeiro'),
 (208,'BANPARA','BPAR3F','BPAR3',NULL,NULL,NULL,NULL,'Financeiro'),
 (209,'WELLS FARGO','WFCO34F','WFCO34',NULL,NULL,NULL,NULL,'Financeiro'),
 (210,'VISA','VISA34F','VISA34',NULL,NULL,NULL,NULL,'Financeiro'),
 (211,'MORGAN STANLEY','MSBR34F','MSBR34',NULL,NULL,NULL,NULL,'Financeiro'),
 (212,'MASTERCARD','MSCD34F','MSCD34',NULL,NULL,NULL,NULL,'Financeiro'),
 (213,'JPMORGAN','JPMC34F','JPMC34',NULL,NULL,NULL,NULL,'Financeiro'),
 (214,'HONEYWELL','HONB34F','HONB34',NULL,NULL,NULL,NULL,'Financeiro'),
 (215,'GE','GEOO34F','GEOO34',NULL,NULL,NULL,NULL,'Financeiro'),
 (216,'GOLDMAN SACHS','GSGI34F','GSGI34',NULL,NULL,NULL,NULL,'Financeiro'),
 (217,'CITIGROUP','CTGP34F','CTGP34',NULL,NULL,NULL,NULL,'Financeiro'),
 (218,'BANK AMERICA','BOAC34F','BOAC34',NULL,NULL,NULL,NULL,'Financeiro'),
 (219,'3M','MMMC34F','MMMC34',NULL,NULL,NULL,NULL,'Financeiro'),
 (220,'SAO CARLOS','SCAR3F','SCAR3',NULL,NULL,NULL,NULL,'Financeiro'),
 (221,'LPS BRASIL','LPSB3F','LPSB3',NULL,NULL,NULL,NULL,'Financeiro'),
 (222,'BMG','BMGB11','BMGB4',NULL,NULL,NULL,NULL,'Financeiro'),
 (223,'GRADIENTE','IGBR3F','IGBR3',NULL,NULL,NULL,NULL,'Financeiro'),
 (224,'GENERAL SHOPPING','GSHP3F','GSHP3',NULL,NULL,NULL,NULL,'Financeiro'),
 (225,'PORTO SEGURO','PSSA3F','PSSA3',NULL,NULL,NULL,NULL,'Financeiro'),
 (226,'CSU CARDSYST','CARD3F','CARD3',NULL,NULL,NULL,NULL,'Financeiro'),
 (227,'BRASIL BROKERS','BBRK3F','BBRK3',NULL,NULL,NULL,NULL,'Financeiro'),
 (228,'BR PROPERTIES','BRPR3F','BRPR3',NULL,NULL,NULL,NULL,'Financeiro'),
 (229,'BANRISUL','BRSR6F','BRSR5F','BRSR3F','BRSR6','BRSR5','BRSR3','Financeiro'),
 (230,'BANCO INTER','BIDI3','BIDI11','BIDI4',NULL,NULL,NULL,'Financeiro'),
 (231,'SANTANDER BR','SANB4F','SANB3F','SANB11F','SANB4','SANB3','SANB11','Financeiro'),
 (232,'MULTIPLAN','MULT3F','MULT3',NULL,NULL,NULL,NULL,'Financeiro'),
 (233,'ITAÚ UNIBANCO','ITUB3F','ITUB4','ITUB3','ITUB4F',NULL,NULL,'Financeiro'),
 (234,'ALIANSCE SONAE','ALSO3',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (235,'BANCO MERCANTIL DE INVESTIMENTOS','BMIN3',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (236,'MERCANTIL DO BRASIL FINANCEIRA','MERC4',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (237,'LOG','LOGG3',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (238,'ITAÚSA','ITSA4F','ITSA4','ITSA3F',NULL,NULL,NULL,'Financeiro'),
 (239,'IRB BRASIL RE','IRBR3',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (240,'IGUATEMI','IGTA3',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (241,'BRADESCO','BBDC4F','BBDC4','BBDC3',NULL,NULL,NULL,'Financeiro'),
 (242,'BRMALLS','BRML3',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (243,'ALPER','APER3F','APER3',NULL,NULL,NULL,NULL,'Financeiro'),
 (244,'BB SEGURIDADE','BBSE3',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (245,'BANCO PAN','BPAN4',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (246,'BANCO DO BRASIL','BBAS3F','BBAS3','BBAS12','BBAS11',NULL,NULL,'Financeiro'),
 (247,'AMERICAN EXPRESS','AXPB34',NULL,NULL,NULL,NULL,NULL,'Financeiro'),
 (248,'WALMART','WALM34F','WALM34',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (249,'STARBUCKS','SBUB34F',NULL,NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (250,'PROCTER GAMBLE','PGCO34F',NULL,NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (251,'PEPSICO INC','PEPB34F','PEPB34',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (252,'COLGATE','COLG34F','COLG34',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (253,'COCA-COLA','COCA34F','COCA34',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (254,'AVON','AVON34F','AVON34',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (255,'SÃO MARTINHO','SMTO3F','SMTO3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (256,'MDIASBRANCO','MDIA3F','MDIA3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (257,'CAMIL','CAML3F','CAML3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (258,'BRASILAGRO','AGRO3F','AGRO3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (259,'BIOSEV','BSEV3F','BSEV3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (260,'MINERVA','BEEF3F','BEEF3','BEEF11',NULL,NULL,NULL,'Consumo não Cíclico'),
 (261,'VIVARA','VIVA3',NULL,NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (262,'CARREFOUR','CRFB3F','CRFB3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (263,'PÃO DE AÇÚCAR','PCAR3F','PCAR4F','PCAR3',NULL,NULL,NULL,'Consumo não Cíclico'),
 (264,'NATURA','NTCO3F','NTCO3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (265,'MARFRIG','MRFG3F','MRFG3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (266,'JBS','JBSS3F','JBSS3',NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (267,'PROCTOR GAMBLE','PGCO34',NULL,NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (268,'BRF','BRFS3',NULL,NULL,NULL,NULL,NULL,'Consumo não Cíclico'),
 (269,'CEDRO','CEDO4F','CEDO3F',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (270,'NETFLIX','NFLX34F','NFLX34',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (271,'NIKE','NIKE34F','NIKE34',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (272,'MC DONALD''S','MCDC34F','MCDC34',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (273,'HOME DEPOT','HOME34F','HOME34',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (274,'FORD MOTORS','FDMO34F','FDMO34',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (275,'COMCAST','CMCS34F',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (276,'AMAZON','AMZO34F',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (277,'RODOBENS','RDNI3F','RDNI3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (278,'SARAIVA LIVR','SLED4F','SLED3F','SLED3',NULL,NULL,NULL,'Consumo Cíclico'),
 (279,'ROSSI RESID','RSID3F','RSID3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (280,'MUNDIAL','MNDL3F','MNDL3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (281,'METAL LEVE','LEVE3F','LEVE3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (282,'KARSTEN','CTKA4F','CTKA3F','CTKA4','CTKA3',NULL,NULL,'Consumo Cíclico'),
 (283,'IOCHPE-MAXION','MYPK3F','MYPK3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (284,'GRENDENE','GRND3F','GRND3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (285,'LOCAMERICA','LCAM3F','LCAM3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (286,'C&A','CEAB3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (287,'LE LIS BLANC','LLIS3F','LLIS3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (288,'GRAZZIOTIN','CGRA3F','CGRA4F','CGRA4','CGRA3',NULL,NULL,'Consumo Cíclico'),
 (289,'ESTRELA','ESTR4F','ESTR3F','ESTR4','ESTR3',NULL,NULL,'Consumo Cíclico'),
 (290,'DIRECIONAL','DIRR3F','DIRR3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (291,'COTEMINAS','CTNM3F','CTNM4F','CTNM4','CTNM3',NULL,NULL,'Consumo Cíclico'),
 (292,'ANIMA','ANIM3F',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (293,'EVEN','EVEN3F','EVEN3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (294,'MARISA','AMAR3F','AMAR3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (295,'MOVIDA','MOVI3F','MOVI3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (296,'JHSF','JHSF3F','JHSF3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (297,'HELBOR','HBOR3F','HBOR3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (298,'PDG REALTY','PDGR3F','PDGR3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (299,'AREZZO','ARZZ3F',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (300,'EZ TEC','EZTC3F','EZTC3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (301,'CIA HERING','HGTX3F',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (302,'ALPARGATAS','ALPA3F','ALPA4F',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (303,'SMILES','SMLS3F','SMLS3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (304,'LOCALIZA','RENT3F','RENT3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (305,'MRV ENGENHARIA','MRVE3F','MRVE3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (306,'MAGAZINE LUIZA','MGLU3F','MGLU3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (307,'LOJAS RENNER','LREN3F','LREN3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (308,'COGNA','COGN3F','COGN3',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (309,'WHIRLPOOL','WHRL4',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (310,'WHIRPOOL','WHRL3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (311,'VIA VAREJO','VVAR3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (312,'TECNISA','TCSA3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (313,'STARBUCKS','SBUB34',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (314,'SER EDUCACIONAL','SEER3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (315,'SARAIVA LIVR','SLED4',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (316,'LOJAS AMERICANAS','LAME4F','LAME4','LAME3F','LAME3',NULL,NULL,'Consumo Cíclico'),
 (317,'HOTEIS OTHON','HOOT4',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (318,'GAFISA','GFSA3','GFSA3F',NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (319,'YDUQS','YDUQ3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (320,'CYRELA REALTY','CYRE3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (321,'CVC','CVCB3',NULL,NULL,NULL,NULL,NULL,'Consumo Cíclico'),
 (322,'BR PARTNERS','BRBI11',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (323,'GETNINJAS','NINJ3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (324,'DOTZ','DOTZ3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (325,'ATHENA SAÚDE','ATEA3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (326,'BANCO MODAL','MODL4','MODL11',NULL,NULL,NULL,NULL,'Bens Industriais'),
 (327,'BANCO MODAL','MODL3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (328,'VITT3','Vittia Fertilizantes',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (329,'KORA SAÚDE','KRSA3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (330,'INFRACOMMERCE','IFCM3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (331,'BOA SAFRA',NULL,NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (332,'CAIXA SEGURIDADE','CXSE3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (333,'RIO ALTO ENERGIAS RENOVÁVEIS','RIOS3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (334,'HOSPITAL CARE CALEDONIA','HCAR3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (335,'GRUPOS GPS','GGPS3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (336,'MATER DEI','MATD3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (337,'CM HOSPITALAR','VVEO3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (338,'ALLIED TECNOLOGIA','ALLD3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (339,'BLAU FARMACÊUTICA','BLAU3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (340,'ATMA PARTICIPAÇÕES','ATMP3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (341,'ASSAÍ','ASAI3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (342,'GRUPO JSL','JSLG3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (343,'CSN MINERAÇÃO','CMIN3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (344,'ELETROMÍDIA','ELMD3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (345,'ORIZON','ORVR3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (346,'OCEANPACT','OPCT3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (347,'WESTWING','WEST3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (348,'CRUZEIRO DO SUL EDUCACIONAL','CSED3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (349,'BEMOBI','BMOB3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (350,'JALLES MACHADO','JALL3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (351,'FOCUS ENERGIA','POWE3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (352,'MOSAICO','MOSI3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (353,'MOBLY','MBLY3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (354,'ESPAÇOLASER','ESPA3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (355,'VAMOS','VAMO3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (356,'INTELBRAS SA','INTB3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (357,'HEDGE INVESTIMENTS','CJCT11',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (358,'BM BRASCAM LAJES CORPORATIVAS','BMLC11',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (359,'REAL ESTATE CAPITAL','RECR11',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (360,'URCA PRIME','URPR11',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (361,'DEVANT RECEBÍVEIS IMOBILIÁRIOS','DEVA11',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (362,'MÉRITO INVESTIMENTOS','MFAI11',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (363,'NEOGRID','NGRD3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (364,'BERKSHIRE HATHAWAY INC.','BRK.B',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (365,'BAXTER INTERNATIONAL INC.','BAX',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (366,'BAKER HUGHES COMPANY','BKR',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (367,'AT&T INC.','T',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (368,'ALTRIA GROUP, INC.','MO',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (369,'AMERICAN INTERNATIONAL GROUP, INC.','AIG',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (370,'ACCENTURE PLC','ACN',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (371,'ABBOTT LABORATORIES','ABT','ABTT34F',NULL,NULL,NULL,NULL,'Bens Industriais'),
 (372,'3M COMPANY','MMM',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (373,'PEPSICO INC','PEP',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (374,'ALPHAVILLE S.A.','AVLL3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (375,'3R PETROLEUM','RRRP3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (376,'AERIS','AERI3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (377,'ENJOEI','ENJU3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (378,'MÉLIUZ','CASH3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (379,'TRACK & FIELD','TFCO4',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (380,'TRIPLE PLAY','CONX3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (381,'GRUPO MATEUS','GMAT3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (382,'SEQUOIA','SEQL3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (383,'COMPASS','PASS3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (384,'BOA VISTA SCPC','BOAS3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (385,'MELNICK','MELK3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (386,'HIDROVIAS DO BRASIL','HBSA3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (387,'SIMPAR','SIMH3F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (388,'CURY','CURY3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (389,'PLANO & PLANO','PLPL3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (390,'PETZ','PETZ3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (391,'PAGUE MENOS','PGMN3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (392,'LAVVI INCORPORADORA','LAVV3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (393,'QUERO-QUERO','LJQQ3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (394,'D1000','DMVF3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (395,'GRUPO SOMA','SOMA3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (396,'RIVA 9','RIVA3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (397,'AMBIPAR','AMBP3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (398,'ALLPARK','ALPK3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (399,'MITRE REALTY','MTRE3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (400,'MOURA DUBEUX','MDNE3',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (401,'BARDELLA','BDLL4F','BDLL3F',NULL,NULL,NULL,NULL,'Bens Industriais'),
 (402,'UPS','UPSS34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (403,'LOCKHEED','LMTB34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (404,'JOHNSON','JNJB34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (405,'FEDEX CORP','FDXB34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (406,'EXXON MOBILE','EXXO34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (407,'CATERPILLAR','CATP34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (408,'BRISTOLMYERS','BMYB34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (409,'BOEING','BOEI34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (410,'ARCELOR','ARMT34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (411,'AMERICAN EXPRESS','AXPB34F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (412,'SANTOS - BRASIL','STBP3F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (413,'RANDON PART','RAPT3F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (414,'ENGIE','EGIE3F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (415,'MMX MINERAÇÃO','MMXM11F','MMXM3F',NULL,NULL,NULL,NULL,'Bens Industriais'),
 (416,'LUPATECH','LUPA3F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais'),
 (417,'INEPAR','INEP4F',NULL,NULL,NULL,NULL,NULL,'Bens Industriais');
CREATE INDEX IF NOT EXISTS "ix_Listed_companies_by_sector_index" ON "Listed_companies_by_sector" (
	"index"
);
COMMIT;