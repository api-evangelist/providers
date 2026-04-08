---
aid: microsoft-azure-repo
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-repo/refs/heads/main/apis.yml
apis:
- name: Azure DevOps Services REST API - Git
  description: REST API for Git repositories in Azure Repos, including repositories, commits, pull requests, branches, and more.
  image: https://docs.microsoft.com/en-us/azure/devops/repos/media/index/repos.svg
  humanURL: https://docs.microsoft.com/en-us/rest/api/azure/devops/git/
  baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  tags:
  - Branches
  - Commits
  - Git
  - Pull Requests
  - Repositories
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/rest/api/azure/devops/git/
  - type: OpenAPI
    url: https://github.com/MicrosoftDocs/vsts-rest-api-specs/blob/master/specification/git/7.1/git.json
  - type: Authentication
    url: https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
  - type: Rate Limits
    url: https://docs.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits
  - type: Reference
    url: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/?view=azure-devops-rest-7.1
  - type: Quickstart
    url: https://learn.microsoft.com/en-us/azure/devops/repos/git/gitquickstart?view=azure-devops
  - type: Client Libraries
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries?view=azure-devops
  contact:
  - FN: Azure DevOps Support
    email:
    - email protected
    url: https://azure.microsoft.com/en-us/support/devops/
- name: Azure DevOps Services REST API - TFVC
  description: REST API for Team Foundation Version Control (TFVC) repositories in Azure Repos.
  image: https://docs.microsoft.com/en-us/azure/devops/repos/media/index/repos.svg
  humanURL: https://docs.microsoft.com/en-us/rest/api/azure/devops/tfvc/
  baseURL: https://dev.azure.com/{organization}/{project}/_apis/tfvc
  tags:
  - Changesets
  - Shelvesets
  - TFVC
  - Version Control
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/rest/api/azure/devops/tfvc/
  - type: OpenAPI
    url: https://github.com/MicrosoftDocs/vsts-rest-api-specs/blob/master/specification/tfvc/7.1/tfvc.json
  - type: Authentication
    url: https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
  - type: Reference
    url: https://learn.microsoft.com/en-us/rest/api/azure/devops/tfvc/?view=azure-devops-rest-7.1
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits
  - type: Client Libraries
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries?view=azure-devops
  contact:
  - FN: Azure DevOps Support
    email:
    - email protected
    url: https://azure.microsoft.com/en-us/support/devops/
- name: Azure DevOps Services REST API - Policy
  description: REST API for managing repository policies including branch policies, required reviewers, and build validation.
  image: https://docs.microsoft.com/en-us/azure/devops/repos/media/index/repos.svg
  humanURL: https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/
  baseURL: https://dev.azure.com/{organization}/{project}/_apis/policy
  tags:
  - Branch Policy
  - Build Validation
  - Code Review
  - Policy
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/
  - type: OpenAPI
    url: https://github.com/MicrosoftDocs/vsts-rest-api-specs/blob/master/specification/policy/7.1/policy.json
  - type: Reference
    url: https://learn.microsoft.com/en-us/rest/api/azure/devops/policy/?view=azure-devops-rest-7.1
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits
  contact:
  - FN: Azure DevOps Support
    email:
    - email protected
    url: https://azure.microsoft.com/en-us/support/devops/
name: Azure Repos
tags:
- DevOps
- Git
- Repositories
- Source Control
- TFVC
- Version Control
type: Contract
image: https://docs.microsoft.com/en-us/azure/devops/repos/media/index/repos.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Repos is a set of version control tools that you can use to manage your code. Whether your software project is large or small, using version control as soon as possible is a good idea.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

