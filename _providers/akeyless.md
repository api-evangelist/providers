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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 256
  human_in_the_loop: 4
  name: Akeyless Agentic Access
  operation_count: 256
  slug: akeyless-agentic-access
  summary_line: 256 operations · 256 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: The v2 API from Akeyless — 256 operation(s) for v2.
  name: Akeyless v2 API
  slug: akeyless-v2-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akeyless-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/akeyless-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akeyless-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akeyless.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akeyless.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/akeylesslabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akeyless
- group: company
  title: ''
  type: Blog
  url: https://www.akeyless.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.akeyless.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.akeyless.io/
- group: other
  title: ''
  type: X
  url: https://x.com/akeylessio
- group: commercial
  title: ''
  type: Plans
  url: plans/akeyless-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/akeyless-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/akeyless-finops.yml
created: '2026-06-13'
description: Akeyless is a cloud-native identity security platform that unifies secrets management, machine identity, and privileged access for AI agents, machines, and humans at scale. The platform provides a REST API with 200+ endpoints covering secrets vaulting, dynamic secrets generation, certificate lifecycle management, encryption and multi-cloud KMS, and SSH access governance. Built on patented Distributed Fragments Cryptography (DFC) technology, Akeyless delivers zero-knowledge, quantum-safe security without requiring central key storage. The API supports multiple authentication methods including AWS IAM, Azure AD, GCP, Kubernetes, SAML, OIDC, LDAP, and API key authentication.
examples:
- key_count: 4
  name: Akeyless Auth Example
  slug: akeyless-auth-example
- key_count: 4
  name: Akeyless Create Secret Example
  slug: akeyless-create-secret-example
- key_count: 6
  name: Akeyless Encrypt Decrypt Example
  slug: akeyless-encrypt-decrypt-example
- key_count: 4
  name: Akeyless Get Secret Value Example
  slug: akeyless-get-secret-value-example
finops:
- name: Akeyless Finops
  service_category: ''
  slug: akeyless-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akeyless.png
json_schemas:
- name: Akeyless Auth Request
  property_count: 13
  slug: akeyless-auth
- name: Akeyless Dynamic Secret
  property_count: 10
  slug: akeyless-dynamic-secret
- name: Akeyless Secret
  property_count: 11
  slug: akeyless-secret
jsonld:
- class_count: 43
  name: Akeyless Context
  property_count: 20
  slug: akeyless-context
layout: provider
modified: '2026-06-13'
name: Akeyless
nav: Providers
network: true
overview: 'Akeyless publishes 1 API on the [APIs.io](https://apis.io/) network: v2 API. Tagged areas include Secrets Management, Zero Trust, Cloud Security, Identity Security, and Machine Identity.


  The Akeyless catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Akeyless'' developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Akeyless Plans Pricing
  plan_count: 2
  slug: akeyless-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 0
  name: Akeyless Rate Limits
  slug: akeyless-rate-limits
rules:
- name: Akeyless API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: akeyless-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.9
  delta: -3.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.5
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akeyless/refs/heads/main/screenshots/akeyless-2026-06-20T171453.png
security:
- kind: domain-security
  name: Akeyless Domain Security
  slug: akeyless-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Akeyless Trust Center
  slug: akeyless-trust-center
  summary_line: SOC 2, ISO 27001, FIPS 140
slug: akeyless
tags:
- Secrets Management
- Zero Trust
- Cloud Security
- Identity Security
- Machine Identity
- Certificate Management
- PKI
- KMS
- Encryption
- SSH Access
- Dynamic Secrets
- Privileged Access Management
- DevSecOps
website: https://www.akeyless.io/
---
