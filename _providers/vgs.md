---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Vgs Agentic Access
  operation_count: 15
  slug: vgs-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 4
apis:
- description: Tokenization operations on the VGS Vault HTTP API.
  name: Very Good Security aliases API
  slug: vgs-aliases-api
- description: Organization resources on the VGS Accounts API.
  name: Very Good Security organizations API
  slug: vgs-organizations-api
- description: Inbound / outbound proxy route resources on the VGS Accounts API.
  name: Very Good Security routes API
  slug: vgs-routes-api
- description: Vault resources on the VGS Accounts API.
  name: Very Good Security vaults API
  slug: vgs-vaults-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Very Good Security (VGS) aliases API
  slug: open-vgs-aliases-api
- collection_type: open
  name: Very Good Security (VGS) aliases organizations API
  slug: open-vgs-organizations-api
- collection_type: open
  name: Very Good Security (VGS) aliases routes API
  slug: open-vgs-routes-api
- collection_type: open
  name: Very Good Security (VGS) aliases vaults API
  slug: open-vgs-vaults-api
- collection_type: open
  name: Very Good Security (VGS) API
  slug: open-vgs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vgs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vgs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vgs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vgs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verygoodsecurity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verygoodsecurity
- group: company
  title: ''
  type: Website
  url: https://www.verygoodsecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verygoodsecurity.com
- group: commercial
  title: ''
  type: Plans
  url: plans/vgs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vgs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vgs-finops.yml
created: '2026-06-20'
description: Very Good Security (VGS) is a data security and tokenization platform that lets companies collect, protect, and exchange sensitive data (cards, PII, bank accounts, credentials) without it touching their own systems, reducing PCI DSS and compliance scope. The platform exposes a Vault HTTP API for tokenization (aliases / redact / reveal), an Accounts management API for vaults, routes, and organizations, and a forward/reverse Proxy that aliases and de-aliases data in transit.
finops:
- name: Vgs Finops
  service_category: Security and Identity
  slug: vgs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vgs.png
layout: provider
modified: '2026-06-20'
name: Very Good Security
nav: Providers
network: true
overview: 'Very Good Security publishes 4 APIs on the [APIs.io](https://apis.io/) network, including aliases API, organizations API, routes API, and 1 more. Tagged areas include Security, Tokenization, Data Privacy, PCI Compliance, and Vault.


  Very Good Security''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Vgs Plans Pricing
  plan_count: 3
  slug: vgs-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 4
  name: Vgs Rate Limits
  slug: vgs-rate-limits
score:
  band: developing
  composite: 39.4
  delta: 1.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 58.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vgs/refs/heads/main/screenshots/vgs-2026-06-20T201107.png
security:
- kind: authentication
  name: Vgs Authentication
  slug: vgs-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Vgs Domain Security
  slug: vgs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vgs Trust Center
  slug: vgs-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: vgs
tags:
- Security
- Tokenization
- Data Privacy
- PCI Compliance
- Vault
website: https://www.verygoodsecurity.com
---
