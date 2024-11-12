from src import app, current_env

if __name__ == "__main__":
    app.run(host=current_env.HOST, port=current_env.PORT, debug=current_env.DEBUG)
