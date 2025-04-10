VALID_USER_DATA = [
    {
        "id": 5,
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "Sorokina",
        "email": "sorokina@lala.ru",
        "password": "SorokinaCool",
        "phone": "79995553322",
        "userStatus": 1
    },
    {
        "id": 57122357,
        "username": "301`84-+3498",
        "firstName": ">QPD)A!~",
        "lastName": "23o0" * 100,
        "email": "lalaame@mafc.ru",
        "password": "kii321jr04ncp29!ph2948fJFN",
        "phone": "79993332211",
        "userStatus": 13
    }
]

INCORRECT_ID_DATA = [
    {
        "id": 10**20,
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "Sorokina",
        "email": "sorokina@lala.ru",
        "password": "SorokinaCool",
        "phone": "79995553322",
        "userStatus": 1
    },
    {
        "id": "gsal",
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "Sorokina",
        "email": "sorokina@lala.ru",
        "password": "SorokinaCool",
        "phone": "79995553322",
        "userStatus": 1
    },
]

INVALID_EMAIL_DATA = [
    {
        "id": 523,
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "Sorokina",
        "email": "sorokina",
        "password": "SorokinaCool",
        "phone": "79995553322",
        "userStatus": 1
    },
    {
        "id": 3252,
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "Sorokina",
        "email": "3.ru",
        "password": "SorokinaCool",
        "phone": "79995553322",
        "userStatus": 1
    }
]

INCORRECT_FIELDS_DATA = [
    {
        "id": 3252,
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "Sorokina",
        "email": "f@f3.ru",
        "password": "SorokinaCool",
        "phone": "79995553322",
        "userStatus": "48912nv"
    },
    {
        "id": 3252,
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "591985",
        "email": "f@f3.ru",
        "password": "SorokinaCool",
        "phone": 79993332211798709,
        "userStatus": 1
    }
]

EMPTY_FIELDS_DATA = [
    {
        "username": "Kate",
        "firstName": "Katerina",
        "lastName": "591985",
        "email": "f@f3.ru",
        "password": "SorokinaCool",
        "phone": "79993332211",
        "userStatus": 1
    },
    {
        "id": 24,
        "username": "",
        "firstName": "Katerina",
        "lastName": "591985",
        "email": "f@f3.ru",
        "password": "SorokinaCool",
        "phone": 79993332211,
        "userStatus": 1
    },
    {
        "id": 3252,
        "firstName": "Katerina",
        "lastName": "591985",
        "email": "f@f3.ru",
        "password": "SorokinaCool",
        "phone": 79993332211,
        "userStatus": 1
    },
    {
        "id": 0,
        "username": "",
        "firstName": "",
        "lastName": "",
        "email": "",
        "password": "",
        "phone": 0,
        "userStatus": 0
    },
    {
        "id": 5213,
        "username": "r",
        "firstName": "f",
        "lastName": "a",
        "email": "a@a.ru",
        "password": "aaaa",
        "phone": 79995553322
    },
    {
        "id": 5,
        "firstName": "Katerina",
        "lastName": "Sorokina",
        "email": "sorokina@lala.ru",
        "phone": "79995553322",
        "userStatus": 1
    }
]