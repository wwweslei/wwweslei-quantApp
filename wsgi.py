from quantAPP import init_app
from quantAPP import config

app = init_app()

if __name__ == "__main__":
    if app.config["ENV"] == "production":
        app.config.from_object(config.ProdConfig)
    else:
        app.config.from_object(config.DevConfig)
    app.run(host='0.0.0.0')
