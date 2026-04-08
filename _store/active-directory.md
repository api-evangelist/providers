---
aid: active-directory
url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/apis.yml
apis:
- name: Active Directory Domain Services (AD DS)
  description: Core directory service for Windows domain environments providing authentication and authorization services.
  image: https://docs.microsoft.com/azure/media/index/active-directory.svg
  humanURL: https://docs.microsoft.com/windows-server/identity/ad-ds/
  baseURL: ldap://domain-controller.example.com:389
  tags:
  - Authentication
  - Domain Services
  - Ldap
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
  - type: LDAP Protocol
    url: ldap://domain-controller.example.com:389
  - type: LDAPS Protocol
    url: ldaps://domain-controller.example.com:636
  - type: Global Catalog
    url: ldap://domain-controller.example.com:3268
  contact:
  - type: Support
    url: https://support.microsoft.com
- name: Active Directory Lightweight Directory Services (AD LDS)
  description: Lightweight LDAP directory service for directory-enabled applications.
  humanURL: https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831593(v=ws.11)
  baseURL: ldap://adlds-server.example.com:389
  tags:
  - Application Directory
  - Directory Services
  - Ldap
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831593(v=ws.11)
  - type: LDAP Endpoint
    url: ldap://adlds-server.example.com:389
- name: Active Directory PowerShell Module
  description: PowerShell cmdlets for managing Active Directory objects and services.
  humanURL: https://docs.microsoft.com/powershell/module/activedirectory/
  baseURL: https://powershell.example.com/ad
  tags:
  - Automation
  - Management
  - Powershell
  - Scripting
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/powershell/module/activedirectory/
  - type: API Reference
    url: https://docs.microsoft.com/powershell/module/activedirectory/?view=windowsserver2022-ps
  - type: Examples
    url: https://docs.microsoft.com/powershell/scripting/samples/sample-scripts-for-administration
  operations:
  - name: Get-ADUser
    description: Gets one or more Active Directory users
  - name: New-ADUser
    description: Creates a new Active Directory user
  - name: Set-ADUser
    description: Modifies an Active Directory user
  - name: Remove-ADUser
    description: Removes an Active Directory user
  - name: Get-ADGroup
    description: Gets one or more Active Directory groups
  - name: New-ADGroup
    description: Creates a new Active Directory group
  - name: Add-ADGroupMember
    description: Adds members to an Active Directory group
- name: Microsoft Graph API - Directory Objects
  description: REST API for accessing and managing Azure Active Directory objects.
  humanURL: https://docs.microsoft.com/graph/api/resources/azure-ad-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Azure Ad
  - Cloud
  - Graph Api
  - Rest Api
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/graph/api/resources/azure-ad-overview
  - type: OpenAPI
    url: https://github.com/microsoftgraph/microsoft-graph-openapi
  - type: Authentication
    url: https://docs.microsoft.com/graph/auth/
  - type: SDK
    url: https://docs.microsoft.com/graph/sdks/sdks-overview
  operations:
  - name: List Users
    description: Retrieve a list of user objects
    method: GET
    endpoint: /users
  - name: Create User
    description: Create a new user
    method: POST
    endpoint: /users
  - name: Get User
    description: Retrieve the properties of a user object
    method: GET
    endpoint: /users/{id}
  - name: Update User
    description: Update user properties
    method: PATCH
    endpoint: /users/{id}
  - name: Delete User
    description: Delete a user
    method: DELETE
    endpoint: /users/{id}
  - name: List Groups
    description: Retrieve a list of group objects
    method: GET
    endpoint: /groups
- name: LDAP API
  description: Lightweight Directory Access Protocol for querying and modifying directory services.
  humanURL: https://ldap.com/
  baseURL: ldap://domain-controller.example.com:389
  tags:
  - Directory Access
  - Ldap
  - Protocol
  properties:
  - type: Protocol Specification
    url: https://datatracker.ietf.org/doc/html/rfc4511
  - type: Documentation
    url: https://ldap.com/ldap-specifications/
  - type: Best Practices
    url: https://docs.microsoft.com/troubleshoot/windows-server/identity/best-practices-for-ldap-client-settings
  operations:
  - name: Bind
    description: Authenticate to the directory
  - name: Search
    description: Search for directory entries
  - name: Add
    description: Add a new entry to the directory
  - name: Modify
    description: Modify an existing entry
  - name: Delete
    description: Delete an entry from the directory
  - name: Compare
    description: Compare attribute values
- name: Kerberos Authentication Protocol
  description: Network authentication protocol for secure authentication in AD environments.
  humanURL: https://docs.microsoft.com/windows-server/security/kerberos/kerberos-authentication-overview
  baseURL: kerberos://domain-controller.example.com:88
  tags:
  - Authentication
  - Kerberos
  - Protocol
  - Security
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/windows-server/security/kerberos/kerberos-authentication-overview
  - type: RFC Specification
    url: https://datatracker.ietf.org/doc/html/rfc4120
  - type: Troubleshooting
    url: https://docs.microsoft.com/troubleshoot/windows-server/windows-security/kerberos-authentication-troubleshooting-guidance
name: Microsoft Active Directory
tags:
- Active Directory
- Authentication
- Domain Services
- Identity Management
- Ldap
- Windows Server
type: Contract
image: https://docs.microsoft.com/azure/media/index/active-directory.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and services for managing Active Directory domain services, user authentication, group management, and directory operations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

