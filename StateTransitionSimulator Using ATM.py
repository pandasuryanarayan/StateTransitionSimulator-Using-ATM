class ATM:
    def __init__(self):
        self.state = 'IDLE'
        self.balance = ""
        self.transition_history = []

    def transition(self, action):
        transitions = {
            'IDLE': {
                'insert_card': 'CARD_INSERTED',
                'withdraw_money': 'IDLE',
                'check_balance': 'IDLE',
                'remove_card': 'IDLE'
            },
            'BALANCE_CHECKED': {
                'insert_card': 'CARD_INSERTED',
                'withdraw_money': 'MONEY_WITHDRAWN',
                'check_balance': 'BALANCE_CHECKED',
                'remove_card': 'IDLE'
            },
            'CARD_INSERTED': {
                'insert_card': 'CARD_INSERTED',
                'withdraw_money': 'MONEY_WITHDRAWN',
                'check_balance': 'BALANCE_CHECKED',
                'remove_card': 'IDLE'
            },
            'MONEY_WITHDRAWN': {
                'insert_card': 'CARD_INSERTED',
                'withdraw_money': 'MONEY_WITHDRAWN',
                'check_balance': 'BALANCE_CHECKED',
                'remove_card': 'IDLE'
            },
            'AMOUNT': {
                'insert_card': 'CARD_INSERTED',
                'withdraw_money': 'MONEY_WITHDRAWN',
                'check_balance': 'BALANCE_CHECKED',
                'remove_card': 'IDLE'
            }
        }

        while True:
            user_action = input(f"Current state: {self.state}\nEnter action (insert_card, remove_card): ")

            if user_action == 'insert_card':
                self.state = transitions[self.state][user_action]
                
                if self.state == 'CARD_INSERTED':
                    self.transition_history.append((self.state, user_action))
                    print(f"Current state: {self.state}")
                    self.handle_card_inserted_actions()
                print(f"Transition successful. New state: {self.state}")
                self.transition_history.append((self.state, user_action))
            elif user_action == 'remove_card':
                self.state = 'CARD_INSERTED'
                print(f"Current state: {self.state}")
                self.transition_history.append((self.state, 'insert_card'))
                print("Card Removed.\nTransaction Successful.\nExited")
                self.state = 'IDLE'
                print(f"Current state: {self.state}")
                self.transition_history.append((self.state, 'exit'))
                print("\nFINAL TRANSISTION TABLE:")
                self.generate_transition_table()
                break
            else:
                print("Invalid action. Please try again.")

    def handle_card_inserted_actions(self):
        while True:
            action = input("Enter 'exit' to Exit.\nWhat action will you do (Withdraw, Check_balance, Enter_amount, exit): ")
            if action.lower() == 'exit':
                print("Transaction Successful.\nExited")
                self.state = 'IDLE'
                print(f"Current state: {self.state}")
                self.transition_history.append((self.state, action))
                self.generate_transition_table()
                print()
                break

            if action == 'Enter_amount':
                if not self.balance:
                    self.state = 'AMOUNT'
                    self.transition_history.append((self.state, action))
                    print(f"Current state: {self.state}")
                    c = int(input("Enter Amount to deposit: "))
                    self.balance = str(c)
                    print(f"Amount Deposited: {c}")
                    print("Now proceed with Withdraw and Check Balance")
                    self.state = 'CARD_INSERTED'
                    print(f"Current state: {self.state}")
                    self.transition_history.append((self.state, 'Back'))
            elif action == 'Withdraw':
                if self.balance:
                    self.state = 'MONEY_WITHDRAWN'
                    self.transition_history.append((self.state, action))
                    print(f"Current state: {self.state}")
                    d = int(input("Enter Amount to Withdraw: "))
                    self.balance = str(int(self.balance) - d)
                    print(f"Updated Balance: {self.balance}")
                    self.state = 'CARD_INSERTED'
                    print(f"Current state: {self.state}")
                    self.transition_history.append((self.state, 'Back'))
                else:
                    print("Deposit the amount first.")
                    self.state = 'CARD_INSERTED'
                    self.transition_history.append((self.state, action))
                    print(f"Current state: {self.state}")
            elif action == 'Check_balance':
                if self.balance:
                    self.state = 'BALANCE_CHECKED'
                    self.transition_history.append((self.state, action))
                    print(f"Current state: {self.state}")
                    print(f"Current Balance: {self.balance}")
                    self.state = 'CARD_INSERTED'
                    print(f"Current state: {self.state}")
                    self.transition_history.append((self.state, 'Back'))
                else:
                    print("Deposit the amount first. ")
                    self.state = 'CARD_INSERTED'
                    self.transition_history.append((self.state, action))
                    print(f"Current state: {self.state}")
            else:
                print("Invalid action. Choose from options given.")
                self.transition_history.append((self.state, action))

    def generate_transition_table(self):
        print("\nTransition History:")
        print("{:<20}{}".format("State", "Action"))
        max_state_length = max(len(state) for state, _ in self.transition_history)
        max_action_length = max(len(action) for _, action in self.transition_history)

        for state, action in self.transition_history:
            state_format = "{:<{}}".format(state, max_state_length + 5)
            action_format = "{:<{}}".format(action, max_action_length + 5)
            print(f"{state_format}{action_format}")


# Example usage
atm_machine = ATM()
atm_machine.transition('')
