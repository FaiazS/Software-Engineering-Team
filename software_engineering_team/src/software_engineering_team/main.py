from software_engineering_team.crew import SoftwareEngineeringTeam


software_requirements = """ 

                            A simple account management system for a trading simulation platform. 

                            The system should allow users to create an account, deposit and withdraw funds.

                            The system should allow users to record that they have bought or sold shares, providing a quantity.

                            The system should calculate the total value of the user's portfolio, and the profit or loss from the initial deposit.

                            The system should be able to report the holdings of the user at any point of time.

                            The system should be able to list the transactions the user has made over time.

                            The system should prevent the user from withdrawing what would leave a negative balance in their account or from buying more shares than they could afford, and even selling shares that they do not have.

                            The system has access to a function 'get_share_price(company_symbol)' which returns the current price of a share and includes a test implementation that returns fixed prices for 'AAPL','TSLA' and for 'GOOGL'.

                            
"""

module_name = "equity_account"

class_name = "EquityAccount"

def run():
    """
    Run the crew.
    """
    inputs = {

        'software_requirements' : software_requirements,

        'module_name' : module_name,

        'class_name' : class_name

    }
    
    try:

        SoftwareEngineeringTeam().crew().kickoff(inputs=inputs)

    except Exception as e:

        raise Exception(f"An error occurred while running the crew: {e}")
    


if __name__ == '__main__':

    run()



