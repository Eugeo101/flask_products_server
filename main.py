from app import create_app

app = create_app(config_type='prd')


# if __name__ == '__main__':
#     print(app.url_map)
#     app.run(port=5000)