#!/bin/bash

# list attached customer managed policies
LocalPolicies=$(aws iam list-policies --scope Local --only-attached) 
echo "Local attached policies: "
echo "$LocalPolicies" 

# Get Arn and version id from filtered result 
Arn=$(aws iam list-policies --scope Local --only-attached --query 'Policies[0].Arn')
VersionId=$(aws iam list-policies --scope Local --only-attached --query 'Policies[0].DefaultVersionId')

# Remove quotes from Arnd and VersionId
NewArn=$(echo "$Arn" | tr -d \")
NewId=$(echo "$VersionId" | tr -d \")

# Use results to download policy document for lab_policy  
PolicyDoc=$(aws iam get-policy-version --policy-arn $NewArn --version-id $NewId)

# Save document to lab_policy.json
echo "$PolicyDoc" > lab_policy.json 

echo "Lab Policy Document: "
echo "$(cat lab_policy.json)" 


# sed -e 's/"//g'

