---
aid: cisco-directory-connector
url: https://raw.githubusercontent.com/api-evangelist/cisco-directory-connector/refs/heads/main/apis.yml
name: Cisco Directory Connector
tags:
  - Active Directory
  - Directory
  - Enterprise
  - Identity Management
  - LDAP
  - Provisioning
  - SCIM
  - Synchronization
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: The Cisco Directory Connector is an on-premises Windows service that synchronizes users and groups from a corporate directory (typically Microsoft Active Directory or LDAP) into Cisco Webex Control Hub. It supports full and incremental sync, attribute mapping, dry-run preview, and scheduled jobs. Programmatic management is via the related Webex People, Groups, and Organizations APIs in Control Hub; modern deployments increasingly use SCIM 2.0 provisioning from identity providers (Azure AD, Okta) as an alternative to the on-premises connector.
apis:
  - aid: cisco-directory-connector:cisco-directory-connector-sync-api
    name: Cisco Directory Connector Sync API
    tags:
      - Directory Sync
      - Group Management
      - User Provisioning
    humanURL: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/directoryconnector/wbx_b_directory-connector-guide.html
    properties:
      - url: https://developer.webex.com/docs/api/guides/directory-connector
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
      - url: https://developer.webex.com/docs/integrations
        type: Authentication
      - url: https://developer.webex.com/docs/sdks
        type: SDKs
      - url: https://developer.webex.com/docs/api/basics#rate-limiting
        type: Rate Limits
    description: Manage and observe directory synchronization between on-premises directory services and Cisco Webex Control Hub, including sync scheduling, status, and error reporting.
  - aid: cisco-directory-connector:webex-control-hub-api
    name: Webex Control Hub API
    tags:
      - Administration
      - Licenses
      - Organizations
      - Users
    humanURL: https://admin.webex.com
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/organizations
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
      - url: https://admin.webex.com
        type: Console
    description: Administrative API for managing Webex organizations, including users, groups, licenses, and directory-sync settings.
  - aid: cisco-directory-connector:webex-scim
    name: Webex SCIM 2.0 Provisioning
    tags:
      - Identity
      - Provisioning
      - SCIM
      - Standards
    humanURL: https://developer.webex.com/docs/api/v1/scim2-people
    baseURL: https://webexapis.com/identity/scim
    properties:
      - url: https://developer.webex.com/docs/api/v1/scim2-people
        type: Documentation
      - url: https://datatracker.ietf.org/doc/html/rfc7644
        type: Specification
    description: SCIM 2.0 endpoints used by identity providers such as Microsoft Entra (Azure AD) and Okta to provision users and groups into Webex as an alternative to the on-premises Directory Connector.
common:
  - type: Portal
    url: https://developer.webex.com
  - type: Admin Console
    url: https://admin.webex.com
  - type: Getting Started
    url: https://developer.webex.com/docs/getting-started
  - type: Authentication
    url: https://developer.webex.com/docs/integrations
  - type: Status
    url: https://status.webex.com
  - type: Blog
    url: https://developer.webex.com/blog
  - type: Support
    url: https://help.webex.com
  - type: Downloads
    url: https://help.webex.com/en-us/article/nivpu1g/Deployment-Guide-for-Cisco-Directory-Connector
  - type: Terms of Service
    url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: JSON-LD
    url: json-ld/cisco-directory-connector-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
