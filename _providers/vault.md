---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 17
  human_in_the_loop: 3
  name: Vault Agentic Access
  operation_count: 25
  slug: vault-agentic-access
  summary_line: 25 operations · 17 acting · 3 human-in-the-loop
api_count: 9
apis:
- description: The complete Vault HTTP API gives full access to all Vault operations via REST. Includes authentication method APIs (AppRole, LDAP, JWT, Kubernetes, AWS, Azure), secrets engine APIs (Database, AWS, PK
  name: Vault HTTP API
  slug: vault-api
- description: Enable, disable, list, and configure authentication methods.
  name: HashiCorp Vault Auth Methods API
  slug: vault-auth-methods-api
- description: Check Vault health and initialization status.
  name: HashiCorp Vault Health API
  slug: vault-health-api
- description: Look up, renew, and revoke leases for secrets and tokens.
  name: HashiCorp Vault Leases API
  slug: vault-leases-api
- description: Create, read, update, delete, and list ACL policies.
  name: HashiCorp Vault Policies API
  slug: vault-policies-api
- description: Configure KV v2 engine settings such as max versions and CAS required.
  name: HashiCorp Vault Secrets Config API
  slug: vault-secrets-config-api
- description: Read, write, patch, and delete secret data versions in the KV v2 engine.
  name: HashiCorp Vault Secrets Data API
  slug: vault-secrets-data-api
- description: Mount, unmount, list, and configure secrets engines.
  name: HashiCorp Vault Secrets Engines API
  slug: vault-secrets-engines-api
- description: Manage metadata and version history for KV v2 secrets.
  name: HashiCorp Vault Secrets Metadata API
  slug: vault-secrets-metadata-api
artifact_total: 132
collections:
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods API
  slug: postman-vault-auth-methods-api
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods Health API
  slug: postman-vault-health-api
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods Leases API
  slug: postman-vault-leases-api
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods Policies API
  slug: postman-vault-policies-api
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Config API
  slug: postman-vault-secrets-config-api
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Data API
  slug: postman-vault-secrets-data-api
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Engines API
  slug: postman-vault-secrets-engines-api
- collection_type: postman
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Metadata API
  slug: postman-vault-secrets-metadata-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods API
  slug: open-vault-auth-methods-api
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods Health API
  slug: open-vault-health-api
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine API
  slug: open-vault-kv
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods Leases API
  slug: open-vault-leases-api
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods Policies API
  slug: open-vault-policies-api
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Config API
  slug: open-vault-secrets-config-api
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Data API
  slug: open-vault-secrets-data-api
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Engines API
  slug: open-vault-secrets-engines-api
- collection_type: open
  name: HashiCorp Vault KV Secrets Engine Auth Methods Secrets Metadata API
  slug: open-vault-secrets-metadata-api
- collection_type: open
  name: HashiCorp Vault System Backend API
  slug: open-vault-sys
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hashicorp-vault/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vault-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vault-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vault-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.hashicorp.com/vault
- group: company
  title: ''
  type: Website
  url: https://www.vaultproject.io
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog/products/vault
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hashicorp.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hashicorp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hashicorp.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hashicorp/vault
- group: operate
  title: ''
  type: Forums
  url: https://discuss.hashicorp.com/c/vault
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/vault
- group: learn
  title: ''
  type: Training
  url: https://developer.hashicorp.com/vault/tutorials
- group: design
  title: ''
  type: SpectralRules
  url: rules/vault-spectral-rules.yml
created: '2024-01-01'
description: HashiCorp Vault is an open source tool for securely storing and accessing secrets. A secret is anything you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret while providing tight access control via policies and recording a detailed audit log. It supports dynamic secrets, data encryption, PKI, SSH certificate issuance, and identity-based access through a comprehensive REST HTTP API.
examples:
- key_count: 3
  name: Vault Kv Kv Config Request Example
  slug: vault-kv-kv-config-request-example
- key_count: 1
  name: Vault Kv Kv Config Response Example
  slug: vault-kv-kv-config-response-example
- key_count: 2
  name: Vault Kv Secret Data Request Example
  slug: vault-kv-secret-data-request-example
- key_count: 1
  name: Vault Kv Secret Data Response Example
  slug: vault-kv-secret-data-response-example
- key_count: 4
  name: Vault Kv Secret Metadata Request Example
  slug: vault-kv-secret-metadata-request-example
- key_count: 1
  name: Vault Kv Secret Metadata Response Example
  slug: vault-kv-secret-metadata-response-example
- key_count: 4
  name: Vault Kv Secret Version Metadata Example
  slug: vault-kv-secret-version-metadata-example
- key_count: 1
  name: Vault Kv Secret Write Response Example
  slug: vault-kv-secret-write-response-example
- key_count: 1
  name: Vault Kv Versions Request Example
  slug: vault-kv-versions-request-example
- key_count: 3
  name: Vault Sys Auth Method Config Example
  slug: vault-sys-auth-method-config-example
- key_count: 1
  name: Vault Sys Auth Methods Response Example
  slug: vault-sys-auth-methods-response-example
- key_count: 2
  name: Vault Sys Enable Auth Method Request Example
  slug: vault-sys-enable-auth-method-request-example
- key_count: 3
  name: Vault Sys Enable Mount Request Example
  slug: vault-sys-enable-mount-request-example
- key_count: 6
  name: Vault Sys Health Response Example
  slug: vault-sys-health-response-example
- key_count: 1
  name: Vault Sys Lease Id Request Example
  slug: vault-sys-lease-id-request-example
- key_count: 3
  name: Vault Sys Lease Renew Response Example
  slug: vault-sys-lease-renew-response-example
- key_count: 1
  name: Vault Sys Lease Response Example
  slug: vault-sys-lease-response-example
- key_count: 4
  name: Vault Sys Mount Config Example
  slug: vault-sys-mount-config-example
- key_count: 1
  name: Vault Sys Mounts Response Example
  slug: vault-sys-mounts-response-example
- key_count: 1
  name: Vault Sys Policies List Response Example
  slug: vault-sys-policies-list-response-example
- key_count: 1
  name: Vault Sys Policy Request Example
  slug: vault-sys-policy-request-example
- key_count: 1
  name: Vault Sys Policy Response Example
  slug: vault-sys-policy-response-example
- key_count: 2
  name: Vault Sys Renew Lease Request Example
  slug: vault-sys-renew-lease-request-example
features:
- description: Versioned key-value secret storage with soft delete, undelete, and permanent destruction.
  name: KV Secrets Engine
- description: On-demand, time-limited credentials for databases, AWS, Azure, GCP, and other backends.
  name: Dynamic Secrets
- description: Encryption-as-a-Service for application data without storing plaintext in Vault.
  name: Data Encryption (Transit)
- description: Built-in PKI secrets engine for issuing X.509 certificates with configurable TTLs.
  name: PKI Certificate Authority
- description: Dynamic SSH certificates and OTPs for secure machine access management.
  name: SSH Certificate Issuance
- description: Fine-grained HCL-based policies controlling access to any secret path with capabilities.
  name: ACL Policies
- description: Pluggable authentication supporting AppRole, LDAP, JWT/OIDC, Kubernetes, AWS, and more.
  name: Auth Methods
- description: All dynamic secrets have TTL-bound leases that can be renewed or revoked on demand.
  name: Lease Management
- description: Comprehensive audit trail of all API requests and responses for compliance.
  name: Audit Logging
- description: Official HashiCorp Vault MCP server enabling AI-assisted secrets management workflows.
  name: MCP Server
finops:
- name: Vault Finops
  service_category: API
  slug: vault-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vault.png
integrations:
- description: Terraform Vault provider for managing Vault configuration and policies as code.
  name: Terraform
- description: Vault Secrets Operator and Vault Agent Injector for native Kubernetes integration.
  name: Kubernetes
- description: OIDC-based authentication from GitHub Actions workflows without static credentials.
  name: GitHub Actions
- description: Dynamic AWS IAM credentials and EC2/IAM-based authentication methods.
  name: AWS
- description: Native HashiCorp Consul integration for service mesh secrets and ACL tokens.
  name: Consul
- description: Dynamic database credentials for PostgreSQL with configurable role TTLs.
  name: PostgreSQL
- description: Native HashiCorp Nomad integration for workload identity and secrets.
  name: Nomad
- description: HashiCorp Vault lookup plugin for Ansible playbook secret retrieval.
  name: Ansible
json_schemas:
- name: KvConfigRequest
  property_count: 3
  slug: vault-kv-kv-config-request
- name: KvConfigResponse
  property_count: 1
  slug: vault-kv-kv-config-response
- name: SecretDataRequest
  property_count: 2
  slug: vault-kv-secret-data-request
- name: SecretDataResponse
  property_count: 1
  slug: vault-kv-secret-data-response
- name: SecretMetadataRequest
  property_count: 4
  slug: vault-kv-secret-metadata-request
- name: SecretMetadataResponse
  property_count: 1
  slug: vault-kv-secret-metadata-response
- name: SecretVersionMetadata
  property_count: 4
  slug: vault-kv-secret-version-metadata
- name: SecretWriteResponse
  property_count: 1
  slug: vault-kv-secret-write-response
- name: VersionsRequest
  property_count: 1
  slug: vault-kv-versions-request
- name: AuthMethodConfig
  property_count: 3
  slug: vault-sys-auth-method-config
- name: AuthMethodsResponse
  property_count: 1
  slug: vault-sys-auth-methods-response
- name: EnableAuthMethodRequest
  property_count: 2
  slug: vault-sys-enable-auth-method-request
- name: EnableMountRequest
  property_count: 3
  slug: vault-sys-enable-mount-request
- name: HealthResponse
  property_count: 6
  slug: vault-sys-health-response
- name: LeaseIdRequest
  property_count: 1
  slug: vault-sys-lease-id-request
- name: LeaseRenewResponse
  property_count: 3
  slug: vault-sys-lease-renew-response
- name: LeaseResponse
  property_count: 1
  slug: vault-sys-lease-response
- name: MountConfig
  property_count: 4
  slug: vault-sys-mount-config
- name: MountsResponse
  property_count: 1
  slug: vault-sys-mounts-response
- name: PoliciesListResponse
  property_count: 1
  slug: vault-sys-policies-list-response
- name: PolicyRequest
  property_count: 1
  slug: vault-sys-policy-request
- name: PolicyResponse
  property_count: 1
  slug: vault-sys-policy-response
- name: RenewLeaseRequest
  property_count: 2
  slug: vault-sys-renew-lease-request
json_structures:
- name: Vault Kv Kv Config Request Structure
  property_count: 3
  slug: vault-kv-kv-config-request-structure
- name: Vault Kv Kv Config Response Structure
  property_count: 1
  slug: vault-kv-kv-config-response-structure
- name: Vault Kv Secret Data Request Structure
  property_count: 2
  slug: vault-kv-secret-data-request-structure
- name: Vault Kv Secret Data Response Structure
  property_count: 1
  slug: vault-kv-secret-data-response-structure
- name: Vault Kv Secret Metadata Request Structure
  property_count: 4
  slug: vault-kv-secret-metadata-request-structure
- name: Vault Kv Secret Metadata Response Structure
  property_count: 1
  slug: vault-kv-secret-metadata-response-structure
- name: Vault Kv Secret Version Metadata Structure
  property_count: 4
  slug: vault-kv-secret-version-metadata-structure
- name: Vault Kv Secret Write Response Structure
  property_count: 1
  slug: vault-kv-secret-write-response-structure
- name: Vault Kv Versions Request Structure
  property_count: 1
  slug: vault-kv-versions-request-structure
- name: Vault Sys Auth Method Config Structure
  property_count: 3
  slug: vault-sys-auth-method-config-structure
- name: Vault Sys Auth Methods Response Structure
  property_count: 1
  slug: vault-sys-auth-methods-response-structure
- name: Vault Sys Enable Auth Method Request Structure
  property_count: 2
  slug: vault-sys-enable-auth-method-request-structure
- name: Vault Sys Enable Mount Request Structure
  property_count: 3
  slug: vault-sys-enable-mount-request-structure
- name: Vault Sys Health Response Structure
  property_count: 6
  slug: vault-sys-health-response-structure
- name: Vault Sys Lease Id Request Structure
  property_count: 1
  slug: vault-sys-lease-id-request-structure
- name: Vault Sys Lease Renew Response Structure
  property_count: 3
  slug: vault-sys-lease-renew-response-structure
- name: Vault Sys Lease Response Structure
  property_count: 1
  slug: vault-sys-lease-response-structure
- name: Vault Sys Mount Config Structure
  property_count: 4
  slug: vault-sys-mount-config-structure
- name: Vault Sys Mounts Response Structure
  property_count: 1
  slug: vault-sys-mounts-response-structure
- name: Vault Sys Policies List Response Structure
  property_count: 1
  slug: vault-sys-policies-list-response-structure
- name: Vault Sys Policy Request Structure
  property_count: 1
  slug: vault-sys-policy-request-structure
- name: Vault Sys Policy Response Structure
  property_count: 1
  slug: vault-sys-policy-response-structure
- name: Vault Sys Renew Lease Request Structure
  property_count: 2
  slug: vault-sys-renew-lease-request-structure
jsonld:
- class_count: 10
  name: Vault Kv Context
  property_count: 15
  slug: vault-kv-context
- class_count: 17
  name: Vault Sys Context
  property_count: 19
  slug: vault-sys-context
layout: provider
modified: '2026-05-19'
name: HashiCorp Vault
nav: Providers
network: true
overview: 'HashiCorp Vault publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth Methods API, Health API, Leases API, and 5 more. Tagged areas include DevOps, Encryption, Open-Source, PKI, and Secrets Management.


  The HashiCorp Vault catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  HashiCorp Vault''s developer surface includes authentication, developer portal, engineering blog, Stack Overflow tag, training material, and 11 more developer resources.'
plans:
- name: Vault Plans Pricing
  plan_count: 3
  slug: vault-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Vault Rate Limits
  slug: vault-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: HashiCorp Vault API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vault-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: HashiCorp Vault API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 17
  slug: vault-spectral-rules
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 28.9
    developer_ergonomics: 32.1
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vault/refs/heads/main/screenshots/vault-2026-06-20T200835.png
security:
- kind: authentication
  name: Vault Authentication
  slug: vault-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vault Domain Security
  slug: vault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vault
tags:
- DevOps
- Encryption
- Open-Source
- PKI
- Secrets Management
- Security
use_cases:
- description: Inject database credentials, API keys, and config into applications at runtime via Vault Agent.
  name: Application Secret Injection
- description: Replace Kubernetes secrets with Vault-managed secrets using the Vault Secrets Operator.
  name: Kubernetes Secrets Management
- description: Automatically rotate database credentials with dynamic secrets engine for zero-knowledge security.
  name: Database Credential Rotation
- description: Automate certificate lifecycle management for internal services and mutual TLS.
  name: PKI Automation
- description: Provide short-lived credentials to CI/CD pipelines via AppRole or GitHub Actions OIDC.
  name: CI/CD Secret Injection
- description: Manage Vault configuration as code using the Terraform Vault provider.
  name: Secrets as Code
- description: Meet SOC 2, PCI-DSS, HIPAA, and FedRAMP requirements with immutable audit logs.
  name: Compliance and Audit
website: https://www.vaultproject.io
---
