"""

Function to run the TradeGate program.

The function prompts the user for various inputs and performs calculations based on the inputs.
It then provides recommendations on whether the user can place a trade based on the risk and reward factors.
The function uses multiple if-else conditions to determine the appropriate actions and prints the result.

:return:
"""


def main():
    while True:  # Start of the wrapping loop
        import os
        os.system('cls')
        print("Welcome to the TradeGate Program.\n".upper())

        tick_value = float(input("What's the dollar amount per tick?\n>>> $"))

        tick_risk = int(input("What's the ATR?\n>>> "))

        tick_reward = int(input("How many ticks is the reward?\n>>> "))

        contract_number = int(input("How many contracts?\n>>> "))

        portfolio_balance = float(input("What's your portfolio balance OR max allowable loss?\n>>> $"))

        # maths

        # calculating risk
        currency_risk = "{:.2f}".format(tick_value * contract_number * tick_risk)
        currency_risk = float(currency_risk)  # converts to float
        currency_risk = float(
            "{:.2f}".format(currency_risk))  # formats float to have 2 decimal places (not working currently)
        risk_one_more_contract = float(
            (contract_number + 1) * tick_value * tick_risk)  # calculates risking one more contract
        risk_one_less_contract = float("{:.2}".format((contract_number - 1) * tick_value * tick_risk))
        risk_portfolio_balance_percent = float(
            (currency_risk / portfolio_balance))  # calculates risk as a percent to the portfolio balance
        suggested_risk_percent = (portfolio_balance / 100)
        risk_one_more_contract_percent = (risk_one_more_contract - currency_risk) / portfolio_balance

        # calculating reward
        currency_reward = "{:.2f}".format(tick_value * contract_number * tick_reward)
        currency_reward = float(currency_reward)
        reward_portfolio_balance_percent = float((currency_reward / portfolio_balance) / 100)

        reward_one_more_contract = float("{:.2}".format(
            (contract_number + 1) * tick_value * tick_reward))  # calculates reward with one more contract
        reward_one_less_contract = float("{:.2}".format((contract_number - 1) * tick_value * tick_reward))

        suggested_reward_percent = (portfolio_balance * .03)

        # creating risk: reward ratio
        risk_ratio = (tick_reward / tick_risk)

        # 1st box responses. -1 risk and reward not working. Showing $ amount of 0
        print("\nBasic Stats")  # title for box 1
        print("----------------------------------------------")

        risk_response = ("{:.2f}".format(float(currency_risk)))  # formats risk to have 2 decimal points (not working)
        risk_response = print(f"\nYour risk is: ${(currency_risk)}")  # prints risk response
        reward_response = print(f"Your reward is: ${currency_reward}\n")  # prints reward response

        risk_ratio_response = print(f"Your risk-to-reward ratio is: {risk_ratio}\n")  # prints risk to reward response

        risk_portfolio_balance_percent_response = print(
            f"Portfolio risk: {round(risk_portfolio_balance_percent * 100, 2)}%")
        reward_portfolio_balance_percent_response = print(
            f"Portfolio reward: {round(risk_portfolio_balance_percent * 100, 2) * risk_ratio}%\n")

        suggested_risk_percent_response = print(
            f"Suggested portfolio risk percent: 10% (${portfolio_balance * .1}) - 13% (${portfolio_balance * .13})")
        suggested_reward_percent_response = print(
            f"Suggested portfolio reward percent: 30% (${portfolio_balance * .3}) - 39% (${portfolio_balance * .39})\n")

        print("\n")

        print("Can you place a trade?")
        print("----------------------------------------------")

        # could i have used 'or' to determine trend or chop?
        # ex:
        # if adx_value >= 25 or chop_value is >= 38:

        if risk_portfolio_balance_percent <= (13 / 100):
            print(f"Your risk meets the threshold: {round(risk_portfolio_balance_percent * 100, 2)}% / 13%")
            if risk_ratio >= 2:
                print(f"Your risk-to-reward meets the minimum requirement: {risk_ratio} / 2\n")
                adx_price_action = input("What's the ADX value\n>>> ").lower()
                adx_price_action = int(adx_price_action)
                if adx_price_action >= 25:
                    pa_trending_yes = input("Are you buying with the trend?\n>>> ").lower()
                    if pa_trending_yes == "yes" or pa_trending_yes == "y":
                        pa_trending_buy_delta = input("Is delta confirming a long bias?\n>>> ").lower()
                        if pa_trending_buy_delta == "yes" or pa_trending_buy_delta == "y":
                            print("Delta confirms your long bias. Place the trade on a pullback.")
                        else:
                            print("Delta does not confirm your bias. You cannot place a trade.")
                    else:
                        shorting_with_trend = input("Are you shorting with the trend?\n>>> ").lower()
                        if shorting_with_trend == 'yes' or shorting_with_trend == "y":
                            short_delta_confirmation = input("Does delta confirm this short bias?\n>>> ").lower()
                            if short_delta_confirmation == 'yes' or short_delta_confirmation == "y":
                                print("You can short on a pullback.")
                            else:
                                print("Delta does not confirm this short bias. You cannot place a trade.")
                        else:
                            print("This is counter-trend. You cannot place a trade.")

                # below is chopping if else
                else:
                    chop_value = input("What's the Choppiness Index value?\n>>>")
                    chop_value = int(chop_value)
                    if chop_value >= 38:
                        pa_chopping = input("Are you buying the bottom?\n>>> ")
                    else:
                        print("Error. Please retry.")
                    if pa_chopping == "yes" or pa_chopping == "y":
                        pa_chopping_failed_breakout = input("Is there a failed breakout?\n>>> ")
                        if pa_chopping_failed_breakout == "yes" or pa_chopping_failed_breakout == "y":
                            pa_chopping_delta_confirmed = input("Does delta confirm a long bias?\n>>> ")
                            if pa_chopping_delta_confirmed == 'yes' or pa_chopping_delta_confirmed == "y":
                                print("You can place a trade at the body of the candlestick")
                            else:
                                print("Delta does not confirm this long bias. You cannot place a trade.")
                        else:
                            pa_chopping_failed_breakout = input("Does delta confirm a long bias?\n>>> ")
                            if pa_chopping_failed_breakout == "yes" or pa_chopping_failed_breakout == "y":
                                print("Place trade below longest wick.")
                            else:
                                print("Delta does not confirm a long bias. You cannot place a trade.")
                    else:
                        pa_chopping_failed_breakout = input("Are you shorting the top?\n>>> ")
                        if pa_chopping_failed_breakout == "yes" or pa_chopping_failed_breakout == "y":
                            pa_chopping_failed_breakout = input("Is there a failed breakout?\n>>> ")
                            if pa_chopping_failed_breakout == "yes" or pa_chopping_failed_breakout == "y":
                                pa_chopping_delta_confirmed = input("Does delta confirm a short bias?\n>>> ")
                                if pa_chopping_delta_confirmed == "yes" or pa_chopping_delta_confirmed == "y":
                                    print("Place trade at the body of the candlestick")
                                else:
                                    print("Delta does not confirm this short bias. You cannot place a trade.")
                            else:
                                pa_chopping_failed_breakout = input("Does delta confirm a short bias?\n>>> ")
                                if pa_chopping_failed_breakout == "yes" or pa_chopping_failed_breakout == "y":
                                    print("Place trade just passed longest wick.")
                                else:
                                    print("Delta does not confirm a short bias. You cannot place a trade.")

                        else:
                            print("You're neither going long nor short. There's no trade to take.")
            else:
                print(
                    f"Your risk-to-reward does not meet the minimum requirement: {round(risk_ratio, 2)} / 2. You cannot place a trade\n")
        else:
            print(
                f"Your risk exceeds threshold: {round(risk_portfolio_balance_percent * 100, 2)}%/ 13%. You cannot place a trade")

        print("\n")

        # Ask user if they want to restart
        user_choice = input(
            "If you want to restart the program , enter 'y'. Enter any other key to quit.\n>>> ")
        if user_choice.lower() != 'y':  # i.e., if the user did NOT enter 'y'
            break  # This will break the while loop, effectively ending the program


# Run the main function when the script is run
if __name__ == "__main__":
    main()
