import json
from pathlib import Path

MENU_PATH = Path(__file__).parent / "jsons" / "menu.json"


def load_menu(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Menu file not found at {path}")
        exit(1)


def take_order(menu):
    user_order = {}
    while True:
        print(f"Menu: {menu}")
        item = input("Please enter the item you want to order: ").strip().lower()

        if item not in menu:
            print("Item not found in menu.")
            continue

        while True:
            try:
                quantity = int(input(f"How many {item}s would you like to order? "))
                if quantity < 0:
                    raise ValueError("Please enter a positive number.")
                break
            except ValueError as e:
                print(e if str(e) else "Please enter a valid whole number.")

        if quantity > 0:
            user_order[item] = user_order.get(item, 0) + quantity
            print(f"Added {quantity} {item}(s) to your order.")

        while True:
            add_more = input("Do you want to add more items? (yes/no): ").strip().lower()
            if add_more not in ("yes", "no", "y", "n"):
                print("Please answer with 'yes' or 'no'.")
                continue
            break

        if add_more == "no":
            return user_order


def build_receipt_lines(menu, user_order):
    lines = []
    total = 0
    for item, quantity in user_order.items():
        line_total = menu[item] * quantity
        total += line_total
        lines.append(f"{item} x{quantity}: ${line_total:.2f}")
    lines.append(f"Total = ${total:.2f}")
    return lines


def main():
    menu = load_menu(MENU_PATH)
    user_order = take_order(menu)

    receipt_lines = build_receipt_lines(menu, user_order)

    print("\n--- Receipt ---")
    print("\n".join(receipt_lines))

    with open("receipt.txt", "w") as f:
        f.write("--- Receipt ---\n")
        f.write("\n".join(receipt_lines) + "\n")


if __name__ == "__main__":
    main()