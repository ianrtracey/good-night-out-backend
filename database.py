import os
from supabase_py import create_client

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
if not supabase_key or not supabase_url:
    print("Cannot find supabase creds")
    exit(1)
client = create_client(supabase_url, supabase_key)


def add_signup(message: str, phone_number: str):
    try:
        data = (
            client.table("signups")
            .insert({"message": message, "phone_number": phone_number})
            .execute()
        )
    except Exception as e:
        print(e)
        return False

    print(data)
    return True


add_signup(None, None)
