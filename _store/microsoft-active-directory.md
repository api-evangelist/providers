---
aid: microsoft-active-directory
url: https://raw.githubusercontent.com/api-evangelist/microsoft-active-directory/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph API (Azure AD)
  description: REST API for accessing Azure Active Directory resources including users, groups, applications, and directory data.
  image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
  humanURL: https://docs.microsoft.com/en-us/graph/overview
  baseURL: https://graph.microsoft.com
  tags:
  - Azure
  - Groups
  - Identity
  - Rest
  - Users
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/overview
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
  contact:
  - FN: Microsoft Support
    url: https://support.microsoft.com
- name: LDAP Protocol Interface
  description: Lightweight Directory Access Protocol interface for querying and modifying Active Directory.
  humanURL: https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api
  baseURL: ldap://[domain-controller]:389
  tags:
  - Directory
  - Ldap
  - Protocol
  - Queries
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/windows/win32/ad/active-directory-ldap
  - type: Protocol Specification
    url: https://datatracker.ietf.org/doc/html/rfc4511
  - type: Examples
    url: https://docs.microsoft.com/en-us/windows/win32/ad/example-code-for-searching-active-directory
- name: PowerShell Active Directory Module
  description: PowerShell cmdlets for managing Active Directory Domain Services.
  humanURL: https://docs.microsoft.com/en-us/powershell/module/activedirectory/
  tags:
  - Administration
  - Automation
  - Powershell
  - Scripting
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/powershell/module/activedirectory/
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-aduser
  - type: Examples
    url: https://docs.microsoft.com/en-us/powershell/scripting/samples/sample-scripts-for-administration
- name: Azure AD Graph API (Deprecated)
  description: Legacy REST API for Azure Active Directory (being replaced by Microsoft Graph).
  humanURL: https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/
  baseURL: https://graph.windows.net
  tags:
  - Azure
  - Deprecated
  - Legacy
  - Rest
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/api/api-catalog
  - type: Migration Guide
    url: https://docs.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview
  - type: Deprecation Notice
    url: https://docs.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview
name: Microsoft Active Directory
tags:
- Authentication
- Authorization
- Directory Services
- Enterprise
- Identity
- Ldap
- Windows
type: Contract
image: https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/media/active-directory-domain-services.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Active Directory (AD) is a directory service developed by Microsoft for Windows domain networks. It provides authentication and authorization services, centralized domain management, and directory services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

