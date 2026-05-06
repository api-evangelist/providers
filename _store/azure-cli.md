---
aid: azure-cli
name: Azure CLI
description: Azure CLI is the official cross-platform command-line tool for managing Microsoft Azure resources and services from the terminal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Provider CLI
  - Command Line Interface
url: https://raw.githubusercontent.com/api-evangelist/azure-cli/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-cli:azure-cli
    name: Azure CLI
    description: Azure CLI is the official cross-platform command-line tool for managing Microsoft Azure resources and services from the terminal.
    humanURL: https://learn.microsoft.com/en-us/cli/azure/
    tags:
      - Cloud Provider CLI
      - Command Line Interface
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli
      - type: GitHubRepository
        url: https://github.com/Azure/azure-cli
common:
  - type: Website
    url: https://learn.microsoft.com/en-us/cli/azure/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli
  - type: GitHubRepository
    url: https://github.com/Azure/azure-cli
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/cli/azure/release-notes-azure-cli
  - type: Features
    data:
      - name: Cross-Platform Support
        description: Runs on Windows, macOS, and Linux with identical command syntax.
      - name: Interactive Mode
        description: Interactive shell with auto-complete and inline help for command discovery.
      - name: Multiple Output Formats
        description: Output as JSON, YAML, table, or TSV for pipeline integration.
      - name: JMESPath Querying
        description: Filter and transform output with JMESPath query language using --query.
      - name: Azure Cloud Shell
        description: Run Azure CLI in the browser via Azure Cloud Shell without local installation.
      - name: Bash Scripting Integration
        description: Embed Azure CLI commands in Bash and PowerShell automation scripts.
      - name: Extension Support
        description: Extend CLI functionality with official and community extensions.
      - name: Service Principal Auth
        description: Authenticate with service principals for automated/non-interactive scenarios.
  - type: UseCases
    data:
      - name: Resource Provisioning
        description: Provision Azure resources like VMs, storage accounts, and databases from the command line.
      - name: DevOps Automation
        description: Automate Azure infrastructure tasks in CI/CD pipelines and deployment scripts.
      - name: Monitoring and Diagnostics
        description: Query resource metrics, logs, and health status from the terminal.
      - name: Batch Operations
        description: Perform bulk operations across multiple Azure resources in a single script.
      - name: Infrastructure as Code
        description: Complement Terraform and Bicep with scripted Azure CLI commands.
  - type: Integrations
    data:
      - name: Azure DevOps
        description: Use Azure CLI in Azure DevOps pipelines with the AzureCLI task.
      - name: GitHub Actions
        description: Authenticate and run Azure CLI commands in GitHub Actions workflows.
      - name: Terraform
        description: Complement Terraform with Azure CLI for tasks outside the Terraform provider.
      - name: Azure Cloud Shell
        description: Access a pre-configured Azure CLI environment via browser.
      - name: VS Code
        description: Integrated terminal support and Azure CLI extension for Visual Studio Code.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
