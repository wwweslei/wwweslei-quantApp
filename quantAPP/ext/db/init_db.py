
from quantAPP.config import Config
from sqlalchemy import create_engine

config = Config()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       echo=config.SQLALCHEMY_ECHO)


wallet_sql = """
            BEGIN TRANSACTION;
INSERT INTO "wallets" ("id","ticket","kind","date","amount","price","commission","users_id") VALUES (1,'petr4','v','2021-07-13 20:42:00.000000',100,28.5,1.0,1),
 (2,'vale3','c','2021-07-06 20:43:00.000000',100,115.0,2.0,1),
 (3,'ciel3','c','2021-07-06 20:43:00.000000',100,4.5,1.0,1),
 (4,'rect11','c','2021-05-04 20:44:00.000000',100,2.0,NULL,2);
COMMIT;
"""

users_sql = """
        BEGIN TRANSACTION;
INSERT INTO "users" ("id","email","username","first_name","last_name","password_hash","is_admin") VALUES (1,'www.weslei@gmail.com','weslei','Weslei','Bomfim','pbkdf2:sha256:260000$RIPzigihLGcwb9tD$8b9a6cb964d66b9dbbecd75659a030c24dd6793bf2396a7e218a945c10d8842e',1),
 (2,'www.weslei@hotmail.com','wwweslei','wwwwwwwwwwwww','wwwwwwwwww','pbkdf2:sha256:260000$w3Fl6yqpOmYKrzHj$a9f5c9e80a547ad694c451a5fe46be3a88183edab9882f7fc7c04f7cb1e31599',0),
 (3,'1701961@aluno.univesp.br','univesp','Weslei','dddd','pbkdf2:sha256:260000$zQHukF4q6GAvTl9I$92159108c429eedd74c44bd90452e9b12b84fcf13edb02ab1837830822e89a9a',0);
COMMIT;
"""


engine.execute(wallet_sql)
engine.execute(users_sql)