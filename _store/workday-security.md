---
aid: workday-security
specificationVersion: '0.19'
name: Workday Security
description: Collection of Workday Security APIs for managing authentication, authorization, and security configurations including identity management, security groups, audit logging, privacy, and user activity monitoring.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-security/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-03-16'
apis:
  - name: Workday Authentication API
    description: Manage authentication methods, SSO configuration, and session management. Supports WS-Security authentication with Integration System Users and OAuth 2.0 token-based authentication for REST API access.
    image: https://www.workday.com/content/dam/web/images/icons/wd-icon.png
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Authentication.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Authentication
      - OAuth
      - SAML
      - Security
      - SSO
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Authentication.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Authentication_OpenAPI.json
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Authentication.wsdl
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-authentication.html
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://community.workday.com
  - name: Workday Identity Management API
    description: Manage user identities, roles, and access permissions within Workday. Provides operations for tracking Workday account signons and identifying unauthorized authentication attempts, including Get_Workday_Account_Signons and Get_Unidentified_Signons operations.
    image: https://www.workday.com/content/dam/web/images/icons/wd-icon.png
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Identity_Management/v45.2/Identity_Management.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Access Management
      - Identity
      - Security
      - Signons
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Identity_Management.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Identity_Management_OpenAPI.json
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Identity_Management.wsdl
      - type: Reference
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Identity_Management/v45.2/Identity_Management.html
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://community.workday.com
  - name: Workday Security Groups API
    description: Manage security groups, domain security policies, and security group memberships. Controls access to securable items within Workday domains and business processes through Integration System Security Groups and role-based permission assignments.
    image: https://www.workday.com/content/dam/web/images/icons/wd-icon.png
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Security_Groups.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Domain Security
      - Groups
      - Permissions
      - Security
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Security_Groups.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Security_Groups_OpenAPI.json
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Security_Groups.wsdl
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://community.workday.com
  - name: Workday Audit and Compliance API
    description: Access audit logs, security reports, and compliance data. Provides programmatic access to audit trail information for security monitoring, regulatory compliance, and governance reporting within Workday.
    image: https://www.workday.com/content/dam/web/images/icons/wd-icon.png
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Audit.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Audit
      - Compliance
      - Logging
      - Security
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Audit.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Audit_OpenAPI.json
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Audit.wsdl
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://community.workday.com
  - name: Workday Privacy API
    description: Manage data privacy settings, consent, and data subject requests. Supports GDPR and other data protection regulation compliance through programmatic access to privacy controls and data governance workflows.
    image: https://www.workday.com/content/dam/web/images/icons/wd-icon.png
    humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Privacy.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service/
    tags:
      - Data Protection
      - GDPR
      - Privacy
      - Security
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Privacy.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Privacy_OpenAPI.json
      - type: WSDL
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Security/v44.0/Privacy.wsdl
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://community.workday.com
  - name: Workday User Activity Logging API
    description: REST API for retrieving user activity logs and signon data from a Workday tenant. Returns detailed JSON records of user actions including task information, timestamps, IP addresses, activity actions, system accounts, and session identifiers. Used by SIEM platforms for security monitoring.
    image: https://www.workday.com/content/dam/web/images/icons/wd-icon.png
    humanURL: https://doc.workday.com/admin-guide/en-us/integrations/workday-rest-api/rest-api-guides/user-activity-logging-rest-api/mhr1626995534900.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/api/privacy/v1/
    tags:
      - Activity Logging
      - Audit
      - Security
      - SIEM
      - Signons
    properties:
      - type: Documentation
        url: https://doc.workday.com/admin-guide/en-us/integrations/workday-rest-api/rest-api-guides/user-activity-logging-rest-api/mhr1626995534900.html
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-authentication.html
    contact:
      - FN: Workday Support
        email: support@workday.com
        url: https://community.workday.com
common:
  - type: Portal
    url: https://community.workday.com
  - type: Getting Started
    url: https://community.workday.com/articles/1317963
  - type: Authentication Guide
    url: https://community.workday.com/articles/1311418
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-authentication.html
  - type: Best Practices
    url: https://community.workday.com/articles/security-best-practices
  - type: Documentation
    url: https://community.workday.com/api
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: Rate Limits
    url: https://community.workday.com/articles/api-rate-limits
  - type: Status
    url: https://status.workday.com
  - type: Support
    url: https://www.workday.com/en-us/customer-experience/support.html
  - type: Website
    url: https://www.workday.com
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: Security
    url: https://www.workday.com/en-us/why-workday/trust/security.html
  - type: Compliance
    url: https://www.workday.com/en-us/why-workday/trust/compliance.html
  - type: Blog
    url: https://blog.workday.com/en-us/application-development.html
  - type: GitHub Organization
    url: https://github.com/workday
  - type: Sign Up
    url: https://resourcecenter.workday.com/
  - type: Login
    url: https://www.myworkday.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Access Control
  - Audit
  - Authentication
  - Compliance
  - Enterprise
  - Identity Management
  - Privacy
  - SAML
  - Security
  - SSO
---
