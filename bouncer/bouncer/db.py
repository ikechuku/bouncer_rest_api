import os


class DB:
    @classmethod
    def config(cls, debug):
        return cls.development() if debug else cls.production()

    @classmethod
    def production(cls):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join('local', 'bouncerdb')
            }
        }

    @classmethod
    def development(cls):
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'bouncerdb',
                'HOST': 'db',
                'USER': 'postgres',
                'PASSWORD': 'postgres'
            }
        }
