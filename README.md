# SavingsPlans-Lambda-Purchase
Lambda script to invoke AWS Savings Plans purchases. Schedule this to replace manual buys

# Summary:

Savings Plans currently do not have a method to be purchased automatically through a queue or schedule. Customers are left with a manual process, and may experience gaps with coverage if they intend to replace their Reserved Instances (RI) with Savings Plans (SP). The function to schedule purchases is currently on the roadmap for 2020.
Temporary workaround:

This python script can be ran in Lambda to execute a SP purchase, while scheduled with CloudWatch events to specify the exact date and time to trigger.

Permissions required for lambda function : Basic Lambda execution role and Savings Plan full access.

# WARNING: Please ensure to not run this script multiple times, as the purchases are non-refundable.

# Setup Instructions:

1. Go to Lambda and create Lambda Function with an identifiable name

    a. Role permissions

        i. Basic Lambda Execution (default) - AWSLambdaBasicExecutionRole

        ii. Savings Plan full access - AWSSavingsPlansFullAccess

2. Copy and paste or load script into your Lambda fucntion

    a. Script - https://github.com/walw/SavingsPlans-Lambda-Purchase

3. Modify & Verify script parameters at the top of the script

4. Go to CloudWatch and create an Event Rule

    a. Set Event source to Schedule

    b. Change Schedule to Cron expression

    c. Enter cron expression for scheduled GMT time of execution

        i. NOTE: The cron expression uses GMT time

        ii. I suggest using something like https://savvytime.com/converter/est-to-gmt

    d. Click Add Target on the right

    e. Select Lambda Function from the drop down

    f. Select the function from step 1

    g. Click on Next

    h. Add a name and description to the rule and click on create rule

    i. Verify your purchase on the Savings Plans page, and be sure to disable your Cloudwatch event just in case
