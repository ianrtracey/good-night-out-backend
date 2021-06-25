from supabase_py import create_client

URL = "https://azaltxjpnmbhqwhthlyg.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYyNDU5MTM0MywiZXhwIjoxOTQwMTY3MzQzfQ.AMhTndWrBXc5l795-grTokNeZ-g4RQLVgc79XBsj68k"
client = create_client(URL, KEY)


def add_signup(message: str, phone_number: str):
    try:
        data = (
            client.table("signups")
            .insert({"message": message, "phone_number": phone_number})
            .execute()
        )
    except Error as e:
        print(e)
        return False

    print(data)
    return True


add_signup(None, None)
