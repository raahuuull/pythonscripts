import boto3
import os
import string
import uuid

client = boto3.client('ssm')

def handler(event,context):
    TargetAccounts=os.environ['TargetAccounts']
    b = str(TargetAccounts)
    TargetAccountsArray = b.split(",")
    TargetRegionIds=os.environ['TargetRegionIds']
    b = str(TargetRegionIds)
    TargetRegionIdsArray = b.split(",")
    RunPatchBaselineOperation=os.environ['RunPatchBaselineOperation']
    RunPatchBaselineRebootOption=os.environ['RunPatchBaselineRebootOption']
    RunPatchBaselineInstallOverrideList=os.environ['RunPatchBaselineInstallOverrideList']
    ResourceGroupName=os.environ['ResourceGroupName']
    MaximumConcurrency=os.environ['MaximumConcurrency']
    MaximumErrors=os.environ['MaximumErrors']
    TargetLocationMaxConcurrency=os.environ['TargetLocationMaxConcurrency']
    TargetLocationMaxErrors=os.environ['TargetLocationMaxErrors']
    ExecutionRoleName=os.environ['ExecutionRoleName']
    MasterAccountID=os.environ['MasterAccountID']
    AutomationDocumentMamrRunPatchBaseline=os.environ['AutomationDocumentMamrRunPatchBaseline']
    
    if len(RunPatchBaselineInstallOverrideList) > 0:
        response = client.start_automation_execution(
        DocumentName=f'{AutomationDocumentMamrRunPatchBaseline}',
        
        Parameters={
            'AutomationAssumeRole':[f'arn:aws:iam::{MasterAccountID}:role/AWS-SystemsManager-AutomationAdministrationRole'] ,
            'Operation' : [f'{RunPatchBaselineOperation}'] ,
            'RebootOption' : [f'{RunPatchBaselineRebootOption}'] ,
            'InstallOverrideList' : [f'{RunPatchBaselineInstallOverrideList}'] ,
            'SnapshotId' : [str(uuid.uuid4())]
        },
        TargetLocations=[
            {
                'Accounts': TargetAccountsArray,
                'Regions': TargetRegionIdsArray,
                'TargetLocationMaxConcurrency': f'{TargetLocationMaxConcurrency}',
                'TargetLocationMaxErrors': f'{TargetLocationMaxErrors}',
                'ExecutionRoleName': f'{ExecutionRoleName}'
            }
        ]
    )
    else:
        response = client.start_automation_execution(
        DocumentName=f'{AutomationDocumentMamrRunPatchBaseline}',
        
        Parameters={
            'AutomationAssumeRole':[f'arn:aws:iam::{MasterAccountID}:role/AWS-SystemsManager-AutomationAdministrationRole'] ,
            'Operation' : [f'{RunPatchBaselineOperation}'] ,
            'RebootOption' : [f'{RunPatchBaselineRebootOption}'] ,
            'SnapshotId' : [str(uuid.uuid4())]
        },
        TargetLocations=[
            {
                'Accounts': TargetAccountsArray,
                'Regions': TargetRegionIdsArray,
                'TargetLocationMaxConcurrency': f'{TargetLocationMaxConcurrency}',
                'TargetLocationMaxErrors': f'{TargetLocationMaxErrors}',
                'ExecutionRoleName': f'{ExecutionRoleName}'
            }
        ]
    )
    print(response)
