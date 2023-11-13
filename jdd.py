user = {
    "id": "estelle",
    "password": "estelle",
    "expected": True
}
admin = {
    "id": "bob",
    "password": "bob",
    "expected": True
}
gestionnaire = {
    "id": "reda",
    "password": "reda",
    "expected": True
}

KO_password = {
    "id": "estelle",
    "password": "ko",
    "expected": False
}

KO_id = {
    "id": "ko",
    "password": "estelle",
    "expected": False
}

fail_id = {
    "id": "erreur",
    "password": "password",
    "expected": True

}


# ----------------- Test case Dataset -------------- 

### Dataset : adp-01 ###
adp_01 = {
    "user": user,
    "admin": admin,
    "gestionnaire": gestionnaire,
    "KO_password": KO_password,
    "KO_id": KO_id,
    "fail": fail_id
}


#### Dataset : adp-02 ###

all_credentials = {
    "user": user,
    "admin": admin,
    "gestionnaire": gestionnaire
}
