---
aid: vault
name: HashiCorp Vault
description: HashiCorp Vault is an open source tool for securely storing and accessing secrets. A secret is anything you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret while providing tight access control via policies and recording a detailed audit log. It supports dynamic secrets, data encryption, PKI, SSH certificate issuance, and identity-based access through a comprehensive REST HTTP API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - DevOps
  - Encryption
  - Open Source
  - PKI
  - Secrets Management
  - Security
url: https://raw.githubusercontent.com/api-evangelist/vault/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vault:vault-kv
    name: HashiCorp Vault KV Secrets Engine API
    description: The KV v2 secrets engine provides key-value secret storage with versioning, metadata management, soft delete, and permanent destruction of secret versions. Essential for storing static secrets like API keys, passwords, and configuration values with full version history and access control.
    humanURL: https://developer.hashicorp.com/vault/api-docs/secret/kv/kv-v2
    baseURL: https://vault.example.com/v1
    tags:
      - KV Secrets
      - Secrets Management
      - Versioning
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/vault/api-docs/secret/kv/kv-v2
      - type: OpenAPI
        url: openapi/vault-kv-openapi.yml
      - type: JSONSchema
        url: json-schema/vault-kv-secret-data-request-schema.json
        title: Secret Data Request Schema
      - type: JSONSchema
        url: json-schema/vault-kv-secret-data-response-schema.json
        title: Secret Data Response Schema
      - type: JSONStructure
        url: json-structure/vault-kv-secret-data-request-structure.json
        title: Secret Data Request Structure
      - type: Example
        url: examples/vault-kv-secret-data-response-example.json
        title: Secret Data Response Example
      - type: JSON-LD
        url: json-ld/vault-kv-context.jsonld
  - aid: vault:vault-sys
    name: HashiCorp Vault System Backend API
    description: The Vault system backend provides management operations for authentication methods, secrets engine mounts, ACL policies, token lifecycle, and lease management. All sys/ endpoints control the core operational behavior of Vault.
    humanURL: https://developer.hashicorp.com/vault/api-docs
    baseURL: https://vault.example.com/v1
    tags:
      - Auth Methods
      - Leases
      - Policies
      - Secrets Engines
      - System Administration
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/vault/api-docs
      - type: OpenAPI
        url: openapi/vault-sys-openapi.yml
      - type: JSONSchema
        url: json-schema/vault-sys-health-response-schema.json
        title: Health Response Schema
      - type: JSONStructure
        url: json-structure/vault-sys-health-response-structure.json
        title: Health Response Structure
      - type: Example
        url: examples/vault-sys-health-response-example.json
        title: Health Response Example
      - type: JSON-LD
        url: json-ld/vault-sys-context.jsonld
  - aid: vault:vault-api
    name: Vault HTTP API
    description: The complete Vault HTTP API gives full access to all Vault operations via REST. Includes authentication method APIs (AppRole, LDAP, JWT, Kubernetes, AWS, Azure), secrets engine APIs (Database, AWS, PKI, SSH, Transit), and the system backend. The OpenAPI spec is dynamically generated from a running Vault instance at /v1/sys/internal/specs/openapi.
    humanURL: https://developer.hashicorp.com/vault/api-docs
    baseURL: https://vault.example.com/v1
    tags:
      - Auth Methods
      - Dynamic Secrets
      - Secrets Management
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/vault/api-docs
      - type: Authentication
        url: https://developer.hashicorp.com/vault/docs/auth
      - type: GettingStarted
        url: https://developer.hashicorp.com/vault/tutorials/get-started
      - type: ChangeLog
        url: https://github.com/hashicorp/vault/blob/main/CHANGELOG.md
common:
  - type: Portal
    url: https://developer.hashicorp.com/vault
  - type: Website
    url: https://www.vaultproject.io
  - type: Blog
    url: https://www.hashicorp.com/blog/products/vault
  - type: StatusPage
    url: https://status.hashicorp.com
  - type: TermsOfService
    url: https://www.hashicorp.com/terms-of-service
  - type: PrivacyPolicy
    url: https://www.hashicorp.com/privacy
  - type: GitHubOrganization
    url: https://github.com/hashicorp
  - type: GitHubRepository
    url: https://github.com/hashicorp/vault
  - type: Forum
    url: https://discuss.hashicorp.com/c/vault
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/vault
  - type: Training
    url: https://developer.hashicorp.com/vault/tutorials
  - type: SpectralRules
    url: rules/vault-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/secrets-management.yaml
    title: Secrets Management
  - type: Features
    data:
      - name: KV Secrets Engine
        description: Versioned key-value secret storage with soft delete, undelete, and permanent destruction.
      - name: Dynamic Secrets
        description: On-demand, time-limited credentials for databases, AWS, Azure, GCP, and other backends.
      - name: Data Encryption (Transit)
        description: Encryption-as-a-Service for application data without storing plaintext in Vault.
      - name: PKI Certificate Authority
        description: Built-in PKI secrets engine for issuing X.509 certificates with configurable TTLs.
      - name: SSH Certificate Issuance
        description: Dynamic SSH certificates and OTPs for secure machine access management.
      - name: ACL Policies
        description: Fine-grained HCL-based policies controlling access to any secret path with capabilities.
      - name: Auth Methods
        description: Pluggable authentication supporting AppRole, LDAP, JWT/OIDC, Kubernetes, AWS, and more.
      - name: Lease Management
        description: All dynamic secrets have TTL-bound leases that can be renewed or revoked on demand.
      - name: Audit Logging
        description: Comprehensive audit trail of all API requests and responses for compliance.
      - name: MCP Server
        description: Official HashiCorp Vault MCP server enabling AI-assisted secrets management workflows.
  - type: UseCases
    data:
      - name: Application Secret Injection
        description: Inject database credentials, API keys, and config into applications at runtime via Vault Agent.
      - name: Kubernetes Secrets Management
        description: Replace Kubernetes secrets with Vault-managed secrets using the Vault Secrets Operator.
      - name: Database Credential Rotation
        description: Automatically rotate database credentials with dynamic secrets engine for zero-knowledge security.
      - name: PKI Automation
        description: Automate certificate lifecycle management for internal services and mutual TLS.
      - name: CI/CD Secret Injection
        description: Provide short-lived credentials to CI/CD pipelines via AppRole or GitHub Actions OIDC.
      - name: Secrets as Code
        description: Manage Vault configuration as code using the Terraform Vault provider.
      - name: Compliance and Audit
        description: Meet SOC 2, PCI-DSS, HIPAA, and FedRAMP requirements with immutable audit logs.
  - type: Integrations
    data:
      - name: Terraform
        description: Terraform Vault provider for managing Vault configuration and policies as code.
      - name: Kubernetes
        description: Vault Secrets Operator and Vault Agent Injector for native Kubernetes integration.
      - name: GitHub Actions
        description: OIDC-based authentication from GitHub Actions workflows without static credentials.
      - name: AWS
        description: Dynamic AWS IAM credentials and EC2/IAM-based authentication methods.
      - name: Consul
        description: Native HashiCorp Consul integration for service mesh secrets and ACL tokens.
      - name: PostgreSQL
        description: Dynamic database credentials for PostgreSQL with configurable role TTLs.
      - name: Nomad
        description: Native HashiCorp Nomad integration for workload identity and secrets.
      - name: Ansible
        description: HashiCorp Vault lookup plugin for Ansible playbook secret retrieval.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
