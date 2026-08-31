---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The SOPS decrypt Go package provides programmatic access to SOPS-encrypted files from Go applications. It supports decryption of YAML, JSON, ENV, INI, and binary formats using configured key managemen
  name: SOPS Go Library
  slug: sops-go-library
artifact_total: 10
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/getsops/sops/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/getsops/sops/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/getsops/sops/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getsops.io/
- group: docs
  title: ''
  type: Documentation
  url: https://getsops.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/getsops
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/getsops/sops
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/getsops/sops/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/getsops/sops/blob/main/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/getsops/sops/blob/main/CHANGELOG.rst
- group: start
  title: ''
  type: CNCF Sandbox
  url: https://www.cncf.io/projects/sops/
- group: other
  title: ''
  type: Homebrew
  url: https://formulae.brew.sh/formula/sops
- group: build
  title: ''
  type: Flux Integration
  url: https://fluxcd.io/flux/guides/mozilla-sops/
- group: company
  title: ''
  type: Blog
  url: https://getsops.io/blog/
- group: auth
  title: ''
  type: Security
  url: https://github.com/getsops/sops/blob/main/SECURITY.md
created: '2025'
description: SOPS (Secrets OPerationS) is a CNCF Sandbox encrypted file editor that supports YAML, JSON, ENV, INI, and binary formats. SOPS encrypts file values while leaving keys in cleartext, enabling secure storage of secrets in version control systems. Supports AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud KMS, age, and PGP for key management. Originally created at Mozilla and donated to the CNCF in 2023.
examples:
- key_count: 8
  name: Sops Encrypt File Example
  slug: sops-encrypt-file-example
finops:
- name: Sops Finops
  service_category: API
  slug: sops-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sops.png
json_schemas:
- name: SOPS Encrypted File
  property_count: 1
  slug: sops-encrypted-file
json_structures:
- name: Sops Config Structure
  property_count: 0
  slug: sops-config-structure
jsonld:
- class_count: 4
  name: Sops Context
  property_count: 11
  slug: sops-context
layout: provider
modified: '2026-05-02'
name: SOPS
nav: Providers
network: true
overview: 'SOPS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Secrets Management, Encryption, Configuration Management, DevOps, and Security.


  The SOPS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SOPS''s developer surface includes documentation, release notes, changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Sops Plans Pricing
  plan_count: 3
  slug: sops-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Sops Rate Limits
  slug: sops-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SOPS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sops-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 65.0
  previous_composite: 24.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sops/refs/heads/main/screenshots/sops-2026-06-20T194211.png
security:
- kind: domain-security
  name: Sops Domain Security
  slug: sops-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sops
tags:
- Secrets Management
- Encryption
- Configuration Management
- DevOps
- Security
- Kubernetes
- CNCF
website: https://getsops.io/
---
