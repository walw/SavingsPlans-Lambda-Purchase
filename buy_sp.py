import json,boto3
# Author: Prem Nambi & Wayne Wang
# Parameters. Please change prior to upload/execution

# Change these options based on the type of SP's to purchase
# savingsPlanID = "OneYearCommittment"

# NOTE: Partial upfront payment type and EC2Instance type has additional parameters undefined in script
# NOTE2: Do not use partial upfront or EC2Instance type yet

#Payment options "All Upfront" | "Partial Upfront" | "No Upfront"
savingsPlanPaymentOptions = "No Upfront"
# Plan Type "Compute" | "EC2Instance"
PlanType = "Compute"
# Commitment $ amount
commitment = "0.001"
# Term in seconds. 31536000 == 12 months
purchaseTerm = 31536000


print('Savings Plan Purchase')

#instantiate SavingsPlan client
client = boto3.client('savingsplans')

def lambda_handler(event, context):
    print("Execute Savings Plan purchase")
    sp_purchase(commitment, purchaseTerm)

def sp_purchase(commitment,purchaseTerm):
    #Function for the actual purchase
    
    #Getting Offer ID for the term:   
    sp_client = boto3.client('savingsplans')
    sp_offer_response = sp_client.describe_savings_plans_offerings(
        paymentOptions=[savingsPlanPaymentOptions],
        planTypes= [PlanType],
        currencies= ['USD'],
        durations = [purchaseTerm]
        )
    # print("Here is the offering ID: " + sp_offer_response['searchResults'][0]['offeringId'])
    sp_offer_id = sp_offer_response['searchResults'][0]['offeringId']
    
    # Purchasing SP using the Offer received above
    
    sp_purchase_response = sp_client.create_savings_plan(
        savingsPlanOfferingId = sp_offer_id,
        commitment = str(commitment)
        )
    print("Savings Plan : " + sp_offer_id + ", purchased successfully, please verify your Savings Plan page for the purchase")