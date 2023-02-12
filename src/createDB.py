from database.db import get_connection

def page_not_found(error):
    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                DROP TABLE IF EXIST user;
                CREATE UNLOGGED SELECT id, title, duration, released FROM movie ORDER BY title ASC;
            """)
            resultset = cursor.fetchall()

            for row in resultset:
                movie = Movie(row[0], row[1], row[2], row[3])
                movies.append(movie.to_JSON())

        connection.close()
        return movies
    except Exception as ex:
        raise Exception(ex)

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(Movie.main, url_prefix = '/api/movies')

    # Error Handlers
    app.register_error_handler(404, page_not_found)
    
    app.run()