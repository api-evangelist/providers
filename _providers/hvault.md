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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 76
  human_in_the_loop: 5
  name: Hvault Agentic Access
  operation_count: 116
  slug: hvault-agentic-access
  summary_line: 116 operations · 76 acting · 5 human-in-the-loop
api_count: 28
apis:
- description: AppRole auth method for machine-to-machine authentication
  name: HashiCorp Vault AppRole API
  slug: hvault-approle-api
- description: Audit device management
  name: HashiCorp Vault Audit API
  slug: hvault-audit-api
- description: Auth method management
  name: HashiCorp Vault Auth API
  slug: hvault-auth-api
- description: AWS dynamic credentials secrets engine
  name: HashiCorp Vault AWS API
  slug: hvault-aws-api
- description: General Vault configuration
  name: HashiCorp Vault Configuration API
  slug: hvault-configuration-api
- description: Database dynamic credentials secrets engine
  name: HashiCorp Vault Database API
  slug: hvault-database-api
- description: Identity entity alias management
  name: HashiCorp Vault Entity Alias API
  slug: hvault-entity-alias-api
- description: Identity entity management
  name: HashiCorp Vault Entity API
  slug: hvault-entity-api
- description: GitHub auth method for organization-based authentication
  name: HashiCorp Vault GitHub API
  slug: hvault-github-api
- description: Identity group alias management
  name: HashiCorp Vault Group Alias API
  slug: hvault-group-alias-api
- description: Identity group management
  name: HashiCorp Vault Group API
  slug: hvault-group-api
- description: Health and status endpoints
  name: HashiCorp Vault Health API
  slug: hvault-health-api
- description: Vault initialization
  name: HashiCorp Vault Init API
  slug: hvault-init-api
- description: JWT/OIDC auth method for identity provider authentication
  name: HashiCorp Vault JWT/OIDC API
  slug: hvault-jwt-oidc-api
- description: Kubernetes auth method for pod authentication
  name: HashiCorp Vault Kubernetes API
  slug: hvault-kubernetes-api
- description: Key/Value version 2 secrets engine
  name: HashiCorp Vault KV V2 API
  slug: hvault-kv-v2-api
- description: LDAP auth method for directory-based authentication
  name: HashiCorp Vault LDAP API
  slug: hvault-ldap-api
- description: HA leader status
  name: HashiCorp Vault Leader API
  slug: hvault-leader-api
- description: Identity lookup operations
  name: HashiCorp Vault Lookup API
  slug: hvault-lookup-api
- description: Secrets engine mount management
  name: HashiCorp Vault Mounts API
  slug: hvault-mounts-api
- description: OIDC identity provider operations
  name: HashiCorp Vault OIDC API
  slug: hvault-oidc-api
- description: PKI certificate management secrets engine
  name: HashiCorp Vault PKI API
  slug: hvault-pki-api
- description: Policy management
  name: HashiCorp Vault Policy API
  slug: hvault-policy-api
- description: Seal and unseal operations
  name: HashiCorp Vault Seal API
  slug: hvault-seal-api
- description: SSH certificate signing secrets engine
  name: HashiCorp Vault SSH API
  slug: hvault-ssh-api
- description: Token auth method for token lifecycle management
  name: HashiCorp Vault Token API
  slug: hvault-token-api
- description: Transit encryption-as-a-service secrets engine
  name: HashiCorp Vault Transit API
  slug: hvault-transit-api
- description: Username and password auth method
  name: HashiCorp Vault Userpass API
  slug: hvault-userpass-api
artifact_total: 46
collections:
- collection_type: open
  name: HashiCorp Vault Vault Auth Methods API
  slug: open-hvault-auth-methods
- collection_type: open
  name: HashiCorp Vault Vault Identity API
  slug: open-hvault-identity
- collection_type: open
  name: HashiCorp Vault Vault Secrets Engines API
  slug: open-hvault-secrets-engines
- collection_type: open
  name: HashiCorp Vault Vault System Backend API
  slug: open-hvault-system-backend
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hvault-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hvault-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hvault-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hashicorp
- group: company
  title: ''
  type: X-website
  url: https://www.vaultproject.io/
- group: docs
  title: ''
  type: X-documentation
  url: https://developer.hashicorp.com/vault/docs
- group: docs
  title: ''
  type: X-api-documentation
  url: https://developer.hashicorp.com/vault/api-docs
- group: build
  title: ''
  type: X-github
  url: https://github.com/hashicorp/vault
- group: learn
  title: ''
  type: X-tutorials
  url: https://developer.hashicorp.com/vault/tutorials
- group: operate
  title: ''
  type: X-support
  url: https://support.hashicorp.com/
- group: commercial
  title: ''
  type: X-terms-of-service
  url: https://www.hashicorp.com/terms-of-service
- group: commercial
  title: ''
  type: X-privacy-policy
  url: https://www.hashicorp.com/privacy
- group: commercial
  title: ''
  type: X-pricing
  url: https://www.hashicorp.com/products/vault/pricing
- group: company
  title: ''
  type: X-blog
  url: https://www.hashicorp.com/blog
- group: operate
  title: ''
  type: X-status
  url: https://status.hashicorp.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hvault-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hvault-secret-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hvault-entity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hvault-entity-alias-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hvault-token-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hvault-policy-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hvault-group-schema.json
created: '2024-01-15'
description: HashiCorp Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing. Vault handles leasing, key revocation, key rolling, and auditing. Through a unified API, users can access an encrypted Key/Value store and network encryption-as-a-service, or generate AWS IAM/STS credentials, SQL/NoSQL databases, X.509 certificates, SSH credentials, and more.
finops:
- name: Hvault Finops
  service_category: Security & Identity
  slug: hvault-finops
image: https://www.vaultproject.io/img/logo-hashicorp.svg
json_schemas:
- name: Vault Entity Alias
  property_count: 9
  slug: hvault-entity-alias
- name: Vault Identity Entity
  property_count: 10
  slug: hvault-entity
- name: Vault Identity Group
  property_count: 10
  slug: hvault-group
- name: Vault ACL Policy
  property_count: 2
  slug: hvault-policy
- name: Vault Secret
  property_count: 2
  slug: hvault-secret
- name: Vault Token
  property_count: 17
  slug: hvault-token
jsonld:
- class_count: 0
  name: Hvault Context
  property_count: 10
  slug: hvault-context
layout: provider
modified: '2026-05-19'
name: HashiCorp Vault
nav: Providers
network: true
overview: 'HashiCorp Vault publishes 28 APIs on the [APIs.io](https://apis.io/) network, including AppRole API, Audit API, Auth API, and 25 more. Tagged areas include Encryption, Identity, Infrastructure, Secrets Management, and Security.


  The HashiCorp Vault catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HashiCorp Vault''s developer surface includes authentication and 21 more developer resources.'
plans:
- name: Hvault Plans Pricing
  plan_count: 4
  slug: hvault-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 5
  name: Hvault Rate Limits
  slug: hvault-rate-limits
rules:
- name: HashiCorp Vault API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hvault-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.1
  delta: -8.4
  facets:
    commercial_clarity: 15.8
    contract_quality: 64.4
    developer_ergonomics: 10.9
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
security:
- kind: authentication
  name: Hvault Authentication
  slug: hvault-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hvault Domain Security
  slug: hvault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hvault
tags:
- Encryption
- Identity
- Infrastructure
- Secrets Management
- Security
website: https://www.vaultproject.io/api-docs
---
