from sqlalchemy.orm import Session
from src.dal.config import SessionLocal
from src.services.user_service import UserService
from src.services.role_service import RoleService
from src.services.country_service import CountryService
from src.services.vacation_service import VacationService
from src.services.like_service import LikeService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def main():
    db: Session = next(get_db())

    user_service = UserService(db)
    role_service = RoleService(db)
    country_service = CountryService(db)
    vacation_service = VacationService(db)
    like_service = LikeService(db)

    while True:
        print("\nChoose an option:")
        print("1 - Create a new user")
        print("2 - Get all users")
        print("3 - Create a new role")
        print("4 - Get all roles")
        print("5 - Create a new country")
        print("6 - Get all countries")
        print("7 - Create a new vacation")
        print("8 - Get all vacations")
        print("9 - Like a vacation")
        print("10 - Get likes by user")
        print("11 - Exit")

        choice = input("Enter option: ")

        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            password = input("Password: ")
            role_id = int(input("Role ID: "))
            user = user_service.create_user(first_name, last_name, email, password, role_id)
            print("User created:", user.as_dict() if user else "Error")

        elif choice == "2":
            users = user_service.get_all_users()
            print("Users:", [user.as_dict() for user in users])

        elif choice == "3":
            role_name = input("Role name: ")
            role = role_service.create_role(role_name)
            print("Role created:", role.as_dict() if role else "Error")

        elif choice == "4":
            roles = role_service.get_all_roles()
            print("Roles:", [role.as_dict() for role in roles])

        elif choice == "5":
            country_name = input("Country name: ")
            country = country_service.create_country(country_name)
            print("Country created:", country.as_dict() if country else "Error")

        elif choice == "6":
            countries = country_service.get_all_countries()
            print("Countries:", [country.as_dict() for country in countries])

        elif choice == "7":
            country_id = int(input("Country ID: "))
            description = input("Description: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            price = float(input("Price: "))
            image_url = input("Image URL: ")
            vacation = vacation_service.create_vacation(country_id, description, start_date, end_date, price, image_url)
            print("Vacation created:", vacation.as_dict() if vacation else "Error")

        elif choice == "8":
            vacations = vacation_service.get_all_vacations()
            print("Vacations:", [vac.as_dict() for vac in vacations])

        elif choice == "9":
            user_id = int(input("User ID: "))
            vacation_id = int(input("Vacation ID: "))
            like = like_service.add_like(user_id, vacation_id)
            print("Vacation liked:", like.as_dict() if like else "Error")

        elif choice == "10":
            user_id = int(input("User ID: "))
            likes = like_service.get_likes_by_user(user_id)
            print("User's likes:", [like.as_dict() for like in likes])

        elif choice == "11":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
