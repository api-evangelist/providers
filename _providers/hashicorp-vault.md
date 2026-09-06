---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.vaultproject.io/'', ''status'': 308, ''note'': ''declared website redirects to https://developer.hashicorp.com/vault — a different registrable domain (vaultproject.io -> hashicorp.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 39
  human_in_the_loop: 6
  name: Hashicorp Vault Agentic Access
  operation_count: 54
  slug: hashicorp-vault-agentic-access
  summary_line: 54 operations · 39 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: AppRole auth method
  name: HashiCorp Vault Auth - AppRole API
  slug: hashicorp-vault-auth-approle-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: Token auth method
  name: HashiCorp Vault Auth - Token API
  slug: hashicorp-vault-auth-token-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: Username/password auth method
  name: HashiCorp Vault Auth - Userpass API
  slug: hashicorp-vault-auth-userpass-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: Identity secrets engine
  name: HashiCorp Vault Identity API
  slug: hashicorp-vault-identity-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: Lease management
  name: HashiCorp Vault Leases API
  slug: hashicorp-vault-leases-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: ACL policy management
  name: HashiCorp Vault Policy API
  slug: hashicorp-vault-policy-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: Key/Value secrets engine version 2
  name: HashiCorp Vault Secrets - KV v2 API
  slug: hashicorp-vault-secrets-kv-v2-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: Transit secrets engine (encryption as a service)
  name: HashiCorp Vault Secrets - Transit API
  slug: hashicorp-vault-secrets-transit-api
- baseURL: https://127.0.0.1:8200/v1
  baseurl_source: declared
  description: System backend operations (init, seal, mounts, auth, audit)
  name: HashiCorp Vault System API
  slug: hashicorp-vault-system-api
- description: The complete Vault HTTP API gives full access to all Vault operations via REST. Includes authentication method APIs (AppRole, LDAP, JWT, Kubernetes, AWS, Azure), secrets engine APIs (Database, AWS, PK
  name: Vault HTTP API
  slug: vault-api
- baseURL: https://vault.example.com/v1
  baseurl_source: declared
  description: Enable, disable, list, and configure authentication methods.
  name: HashiCorp Vault Auth Methods API
  slug: vault-auth-methods-api
- baseURL: https://vault.example.com/v1
  baseurl_source: declared
  description: Check Vault health and initialization status.
  name: HashiCorp Vault Health API
  slug: vault-health-api
- baseURL: https://vault.example.com/v1
  baseurl_source: declared
  description: Create, read, update, delete, and list ACL policies.
  name: HashiCorp Vault Policies API
  slug: vault-policies-api
- baseURL: https://vault.example.com/v1
  baseurl_source: declared
  description: Configure KV v2 engine settings such as max versions and CAS required.
  name: HashiCorp Vault Secrets Config API
  slug: vault-secrets-config-api
- baseURL: https://vault.example.com/v1
  baseurl_source: declared
  description: Read, write, patch, and delete secret data versions in the KV v2 engine.
  name: HashiCorp Vault Secrets Data API
  slug: vault-secrets-data-api
- baseURL: https://vault.example.com/v1
  baseurl_source: declared
  description: Mount, unmount, list, and configure secrets engines.
  name: HashiCorp Vault Secrets Engines API
  slug: vault-secrets-engines-api
- baseURL: https://vault.example.com/v1
  baseurl_source: declared
  description: Manage metadata and version history for KV v2 secrets.
  name: HashiCorp Vault Secrets Metadata API
  slug: vault-secrets-metadata-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole API
  slug: open-hashicorp-vault-auth-approle-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole Auth - Token API
  slug: open-hashicorp-vault-auth-token-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole Auth - Userpass API
  slug: open-hashicorp-vault-auth-userpass-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole Identity API
  slug: open-hashicorp-vault-identity-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole Leases API
  slug: open-hashicorp-vault-leases-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole Policy API
  slug: open-hashicorp-vault-policy-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole Secrets - KV v2 API
  slug: open-hashicorp-vault-secrets-kv-v2-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole Secrets - Transit API
  slug: open-hashicorp-vault-secrets-transit-api
- collection_type: open
  name: HashiCorp Vault HTTP Auth - AppRole System API
  slug: open-hashicorp-vault-system-api
- collection_type: open
  name: HashiCorp Vault HTTP API
  slug: open-hashicorp-vault
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hashicorp-vault-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hashicorp-vault-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hashicorp-vault-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hashicorp
- group: company
  title: ''
  type: Website
  url: https://www.vaultproject.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/vault/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hashicorp.com/vault/tutorials
- group: operate
  title: ''
  type: Support
  url: https://support.hashicorp.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hashicorp.com
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hashicorp.com/products/vault/pricing
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
  url: https://github.com/hashicorp/vault
- group: build
  title: ''
  type: SDKs
  url: https://developer.hashicorp.com/vault/docs/libraries
created: '2024-01-15'
description: HashiCorp Vault is a secrets management tool that provides secure storage, access control, and distribution of tokens, passwords, certificates, and encryption keys. It provides a unified interface to any secret while providing tight access control and recording a detailed audit log.
examples:
- key_count: 1
  name: Vault Kv Secret Data Response Example
  slug: vault-kv-secret-data-response-example
- key_count: 6
  name: Vault Sys Health Response Example
  slug: vault-sys-health-response-example
finops:
- name: Hashicorp Vault Finops
  service_category: API
  slug: hashicorp-vault-finops
image: https://www.datocms-assets.com/2885/1620155116-brandhcvaultprimaryattributedcolor.svg
json_schemas:
- name: SecretDataRequest
  property_count: 2
  slug: vault-kv-secret-data-request
- name: SecretDataResponse
  property_count: 1
  slug: vault-kv-secret-data-response
- name: HealthResponse
  property_count: 6
  slug: vault-sys-health-response
json_structures:
- name: Vault Kv Secret Data Request Structure
  property_count: 2
  slug: vault-kv-secret-data-request-structure
- name: Vault Sys Health Response Structure
  property_count: 6
  slug: vault-sys-health-response-structure
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
overview: 'HashiCorp Vault publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Auth - AppRole API, Auth - Token API, Auth - Userpass API, and 13 more. Tagged areas include DevOps, Encryption, Infrastructure, Secrets Management, and Security.


  The HashiCorp Vault catalog on APIs.io includes 2 JSON-LD contexts.


  HashiCorp Vault''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Hashicorp Vault Plans Pricing
  plan_count: 3
  slug: hashicorp-vault-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Hashicorp Vault Rate Limits
  slug: hashicorp-vault-rate-limits
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.1
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 51.3
    developer_ergonomics: 46.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 43.8
      total: 16
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hashicorp-vault/refs/heads/main/screenshots/hashicorp-vault-2026-06-20T182532.png
security:
- kind: authentication
  name: Hashicorp Vault Authentication
  slug: hashicorp-vault-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hashicorp Vault Domain Security
  slug: hashicorp-vault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hashicorp-vault
tags:
- DevOps
- Encryption
- Infrastructure
- Secrets Management
- Security
website: https://www.vaultproject.io/
---
