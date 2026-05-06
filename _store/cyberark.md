---
aid: cyberark
name: CyberArk
x-type: company
description: CyberArk is the global leader in identity security, providing a unified Identity Security Platform that protects human, machine, and application identities across hybrid and multi-cloud environments. Core product lines include Privileged Access Manager (PAM Self-Hosted) and Privilege Cloud for credential vaulting and session management; Conjur Secrets Manager (Open Source, Enterprise, and Cloud) for machine-identity and DevOps secrets; CyberArk Identity for workforce SSO, MFA, and lifecycle; Endpoint Privilege Manager for least-privilege enforcement on Windows / macOS / Linux endpoints; Secure Cloud Access for just-in-time cloud entitlements; and Customer Identity for B2B / B2C identity. CyberArk publishes a canonical OpenAPI 3.1 specification for Conjur Secrets Manager at github.com/cyberark/conjur-openapi-spec, and REST APIs for PAM Self-Hosted, Privilege Cloud, and CyberArk Identity are documented on docs.cyberark.com and developer.cyberark.com.
url: https://raw.githubusercontent.com/api-evangelist/cyberark/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Authentication
  - Cloud Security
  - Conjur
  - Credential Vault
  - DevOps Secrets
  - Endpoint Privilege Management
  - Identity Security
  - Machine Identity
  - MFA
  - OpenAPI
  - PAM
  - Privileged Access
  - Privileged Access Management
  - Secrets Management
  - Session Management
  - SSO
  - Vault
  - Zero Trust
apis:
  - aid: cyberark:conjur
    name: CyberArk Conjur Secrets Manager API
    description: Conjur is CyberArk's secrets management platform for machine identities and DevOps workloads, delivered as Conjur Open Source, Conjur Enterprise (Self-Hosted), and Conjur Cloud (SaaS). The REST API supports authenticating hosts and users, loading and replacing policy YAML, storing and retrieving versioned secrets, managing resources and roles, and retrieving public keys. The canonical OpenAPI 3.1 spec is open-sourced at github.com/cyberark/conjur-openapi-spec.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cyberark.com/conjur-cloud/latest/en/content/developer/conjur-api-openapi.html
    baseURL: https://conjur.example.com
    tags:
      - Authentication
      - Conjur
      - DevOps Secrets
      - Machine Identity
      - Policies
      - Resources
      - Roles
      - Secrets
      - Vault
    properties:
      - type: Documentation
        url: https://docs.cyberark.com/conjur-cloud/latest/en/content/developer/conjur-api-openapi.html
      - type: OpenAPI
        url: openapi/cyberark-conjur-openapi.yml
      - type: CanonicalOpenAPI
        url: https://github.com/cyberark/conjur-openapi-spec
      - type: Capabilities
        url: capabilities/cyberark-conjur-capabilities.yml
      - type: Rules
        url: rules/cyberark-conjur-rules.yml
      - type: GitHubRepository
        url: https://github.com/cyberark/conjur
      - type: Blog
        url: https://developer.cyberark.com/blog/introducing-the-conjur-openapi-description/
  - aid: cyberark:pam-self-hosted
    name: CyberArk PAM Self-Hosted REST API
    description: The Privileged Access Manager Self-Hosted REST API exposes the Vault for managing accounts, safes, platforms, users, sessions, and applications. Authentication uses the Logon endpoint at /PasswordVault/API/Auth/{provider}/Logon to obtain a session token used in the Authorization header for subsequent calls.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cyberark.com/pam-self-hosted/latest/en/content/webservices/implementing%20privileged%20account%20security%20web%20services%20.htm
    tags:
      - Accounts
      - PAM
      - Privileged Access
      - REST
      - Safes
      - Sessions
      - Vault
    properties:
      - type: Documentation
        url: https://docs.cyberark.com/pam-self-hosted/latest/en/content/webservices/implementing%20privileged%20account%20security%20web%20services%20.htm
      - type: SampleScripts
        url: https://github.com/cyberark/epv-api-scripts
      - type: PowerShellModule
        url: https://github.com/pspete/psPAS
  - aid: cyberark:privilege-cloud
    name: CyberArk Privilege Cloud REST API
    description: The Privilege Cloud Shared Services REST API mirrors the PAM Self-Hosted surface for accounts, safes, platforms, and users while running as a SaaS on the CyberArk Identity Security Platform. Identities and groups reference the tenant's CyberArk Identity directory.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cyberark.com/privilege-cloud-shared-services/latest/en/content/sdk/sdk-overview.htm
    tags:
      - Accounts
      - PAM
      - Privilege Cloud
      - Safes
      - SaaS
      - Vault
    properties:
      - type: Documentation
        url: https://docs.cyberark.com/privilege-cloud-shared-services/latest/en/content/sdk/sdk-overview.htm
      - type: WhatsNew
        url: https://docs.cyberark.com/privilege-cloud-shared-services/latest/en/content/privilege%20cloud/privcloud-whatsnew-v12.2.htm
  - aid: cyberark:identity
    name: CyberArk Identity REST API
    description: The CyberArk Identity REST API enables programmatic management of users, roles, applications, MFA policies, SSO, and SCIM-based provisioning across the workforce identity tenant. Tenants are addressed at {tenant}.id.cyberark.cloud and authentication uses OAuth2.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cyberark.com/identity/Latest/en/Content/Developer/Developer.htm
    tags:
      - Identity
      - MFA
      - OAuth2
      - SCIM
      - SSO
      - Workforce Identity
    properties:
      - type: Documentation
        url: https://docs.cyberark.com/identity/Latest/en/Content/Developer/Developer.htm
      - type: SCIM
        url: https://docs.cyberark.com/identity/latest/en/content/developer/scim-management/scim-overview.htm
      - type: DeveloperPortal
        url: https://developer.cyberark.com/
common:
  - type: Website
    url: https://www.cyberark.com
  - type: Products
    url: https://www.cyberark.com/products/
  - type: Documentation
    url: https://docs.cyberark.com
  - type: DeveloperPortal
    url: https://developer.cyberark.com/
  - type: GitHubOrganization
    url: https://github.com/cyberark
  - type: ConjurOpenAPISpec
    url: https://github.com/cyberark/conjur-openapi-spec
  - type: Marketplace
    url: https://marketplace.cyberark.com/
  - type: Trust
    url: https://www.cyberark.com/trust/
  - type: TermsOfService
    url: https://www.cyberark.com/legal-terms-of-use/
  - type: PrivacyPolicy
    url: https://www.cyberark.com/privacy-policy/
  - type: JSON-LD
    url: json-ld/cyberark-context.jsonld
  - type: JSONSchema
    url: json-schema/cyberark-conjur-resource-schema.json
  - type: JSONSchema
    url: json-schema/cyberark-privileged-account-schema.json
  - type: Vocabulary
    url: vocabulary/cyberark-vocabulary.yml
  - type: Capabilities
    url: capabilities/cyberark-conjur-capabilities.yml
  - type: Rules
    url: rules/cyberark-conjur-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
