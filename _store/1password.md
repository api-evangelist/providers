---
aid: 1password
url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/apis.yml
name: 1Password
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Password Manager
  - Passwords
  - Security
  - Secrets
description: 1Password is a password manager that helps individuals and businesses securely store and manage passwords, credentials, and sensitive information. The platform provides a Connect Server API for programmatic secrets management, an Events API for security monitoring and audit logging, and a Partnership API for managing partner billing accounts.
created: '2025-02-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: 1password:1password-connect-api
    name: 1Password Connect Server API
    tags:
      - Items
      - Passwords
      - Secrets
      - Vaults
    humanURL: https://developer.1password.com/docs/connect/api-reference/
    baseURL: http://localhost:8080
    properties:
      - url: https://developer.1password.com/docs/connect/api-reference/
        type: Documentation
      - url: openapi/1password-connect-openapi.yml
        type: OpenAPI
      - url: json-schema/1password-connect-vault-schema.json
        type: JSONSchema
      - url: json-schema/1password-connect-item-schema.json
        type: JSONSchema
      - url: json-schema/1password-connect-full-item-schema.json
        type: JSONSchema
      - url: json-ld/1password-connect-context.jsonld
        type: JSON-LD
    description: The 1Password Connect Server API provides secure access to 1Password items and vaults in your company's apps and cloud infrastructure through a private REST API. Connect Servers bridge the gap between 1Password and your infrastructure by enabling programmatic access to secrets stored in shared vaults. You can create, read, update, and delete items, manage vaults, and retrieve files attached to items.
  - aid: 1password:1password-events-api
    name: 1Password Events API
    tags:
      - Audit
      - Events
      - Monitoring
      - Security
    humanURL: https://developer.1password.com/docs/events-api/reference/
    baseURL: https://events.1password.com
    properties:
      - url: https://developer.1password.com/docs/events-api/reference/
        type: Documentation
      - url: openapi/1password-events-openapi.yml
        type: OpenAPI
      - url: json-schema/1password-events-sign-in-attempt-schema.json
        type: JSONSchema
      - url: json-schema/1password-events-item-usage-schema.json
        type: JSONSchema
      - url: json-ld/1password-events-context.jsonld
        type: JSON-LD
    description: The 1Password Events API provides programmatic access to event data generated within a 1Password account. It enables security teams and administrators to retrieve sign-in attempts, item usage records, and audit events for monitoring, compliance, and security analysis. The API uses cursor-based pagination with POST requests to efficiently stream large volumes of event data.
  - aid: 1password:1password-partnership-api
    name: 1Password Partnership API
    tags:
      - Billing
      - Partners
      - Passwords
    humanURL: https://developer.1password.com/docs/partnership-api/reference/
    baseURL: https://billing.b5test.eu/api/v1
    properties:
      - url: https://developer.1password.com/docs/partnership-api/reference/
        type: Documentation
      - url: openapi/1password-partnership-openapi.yml
        type: OpenAPI
      - url: json-ld/1password-partnership-context.jsonld
        type: JSON-LD
    description: You can use the 1Password Partnership API to manage the provisioning and deprovisioning of third-party partner billing accounts for your customers. The API supports partner billing accounts for 1Password individual and family accounts. The Partnership API does not support 1Password team or business accounts.
common:
  - type: Website
    url: https://1password.com/
  - type: Portal
    url: https://developer.1password.com/
  - type: Documentation
    url: https://developer.1password.com/docs/
  - type: GettingStarted
    url: https://developer.1password.com/docs/get-started/
  - type: Authentication
    url: https://developer.1password.com/docs/connect/connect-api-reference/#authentication
  - type: SDK
    url: https://developer.1password.com/docs/sdks/
    title: Official SDKs
  - type: SDK
    url: https://pypi.org/project/onepassword-sdk/
    title: Python SDK
  - type: SDK
    url: https://www.npmjs.com/package/@1password/sdk
    title: JavaScript SDK
  - type: SDK
    url: https://pkg.go.dev/github.com/1Password/onepassword-sdk-go
    title: Go SDK
  - type: SDK
    url: https://pypi.org/project/onepassword-connect-sdk/
    title: Connect Python SDK
  - type: SDK
    url: https://www.npmjs.com/package/@1password/connect
    title: Connect Node.js SDK
  - type: SDK
    url: https://pkg.go.dev/github.com/1Password/connect-sdk-go
    title: Connect Go SDK
  - type: CLI
    url: https://developer.1password.com/docs/cli/
    title: 1Password CLI
  - type: Blog
    url: https://blog.1password.com/
  - type: Support
    url: https://support.1password.com/
  - type: PrivacyPolicy
    url: https://1password.com/legal/privacy/
  - type: TermsOfService
    url: https://1password.com/legal/terms-of-service/
  - type: SignUp
    url: https://start.1password.com/sign-up/
  - type: ChangeLog
    url: https://developer.1password.com/docs/events-api/changelog/
  - type: GitHubOrganization
    url: https://github.com/1Password
  - type: SpectralRules
    url: rules/1password-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/1password-secrets-management.yaml
  - type: Vocabulary
    url: vocabulary/1password-vocabulary.yaml
  - type: Features
    data:
      - name: Secrets Management
        description: Programmatic access to 1Password vaults and items via Connect Server API
      - name: Security Monitoring
        description: Real-time audit log streaming of sign-in events, item usage, and audit trails
      - name: Partner Billing Management
        description: Provision and deprovision 1Password accounts for partner customers
      - name: SDKs
        description: Official SDKs for Python, JavaScript/TypeScript, Go, and Connect-specific clients
      - name: CLI
        description: 1Password CLI for command-line secrets management and automation
      - name: Kubernetes Integration
        description: Kubernetes operator and secrets injector for cloud-native deployments
      - name: Terraform Provider
        description: Terraform provider to manage 1Password vault items as infrastructure
      - name: GitHub Actions
        description: Load secrets from 1Password directly into GitHub Actions CI/CD pipelines
  - type: UseCases
    data:
      - name: Secrets Injection
        description: Inject secrets from 1Password into applications and containers at runtime
      - name: Security Audit
        description: Stream and analyze sign-in events and item usage for security incident response
      - name: Compliance Reporting
        description: Export audit trails for SOC2, GDPR, and other compliance frameworks
      - name: CI/CD Secrets
        description: Securely provide secrets to CI/CD pipelines without hardcoding credentials
      - name: Infrastructure as Code
        description: Manage secrets as part of Terraform or Ansible automation workflows
      - name: Partner Account Provisioning
        description: Automate provisioning of 1Password accounts for partner customer bases
  - type: Integrations
    data:
      - name: Kubernetes
        description: Native integration via operator and secrets injector for Kubernetes deployments
      - name: Terraform
        description: Terraform provider for managing 1Password items as infrastructure resources
      - name: Ansible
        description: Ansible collection for 1Password Connect integration
      - name: GitHub Actions
        description: GitHub Actions to load and install 1Password secrets in CI/CD workflows
      - name: Splunk
        description: Events API Splunk integration for security event streaming
      - name: HashiCorp Vault
        description: Vault plugin for 1Password Connect secrets retrieval
      - name: Helm Charts
        description: Official Helm charts for deploying 1Password Connect on Kubernetes
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
