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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Duo Security Agentic Access
  operation_count: 32
  slug: duo-security-agentic-access
  summary_line: 32 operations · 19 acting
api_count: 7
apis:
- description: Batched operations
  name: Duo Security Bulk API
  slug: duo-security-bulk-api
- description: Bypass code generation and listing
  name: Duo Security Bypass Codes API
  slug: duo-security-bypass-codes-api
- description: Group management and membership
  name: Duo Security Groups API
  slug: duo-security-groups-api
- description: Phone device management
  name: Duo Security Phones API
  slug: duo-security-phones-api
- description: Hardware token management
  name: Duo Security Tokens API
  slug: duo-security-tokens-api
- description: User account management
  name: Duo Security Users API
  slug: duo-security-users-api
- description: WebAuthn credential management
  name: Duo Security WebAuthn API
  slug: duo-security-webauthn-api
artifact_total: 16
collections:
- collection_type: open
  name: Duo Admin API
  slug: open-duo-admin-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/duo-security-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/duo-security-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/duo-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duo-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duo-security-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/duosec
- group: company
  title: ''
  type: Website
  url: https://duo.com
- group: docs
  title: ''
  type: Documentation
  url: https://duo.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duosecurity
- group: company
  title: ''
  type: Blog
  url: https://duo.com/feed
created: '2026-03-25'
description: Duo Security is a multi-factor authentication and zero trust security platform from Cisco for securing access to applications and APIs.
finops:
- name: Duo Security Finops
  service_category: API
  slug: duo-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duo-security.png
layout: provider
modified: '2026-05-19'
name: Duo Security
nav: Providers
network: true
overview: 'Duo Security publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Bypass Codes API, Groups API, and 4 more. Tagged areas include Authentication, MFA, Zero Trust, and Identity.


  Duo Security''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Duo Security Plans Pricing
  plan_count: 3
  slug: duo-security-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 5
  name: Duo Security Rate Limits
  slug: duo-security-rate-limits
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.7
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duo-security/refs/heads/main/screenshots/duo-security-2026-06-20T180323.png
security:
- kind: authentication
  name: Duo Security Authentication
  slug: duo-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duo Security Domain Security
  slug: duo-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Duo Security Vulnerability Disclosure
  slug: duo-security-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Duo Security Trust Center
  slug: duo-security-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: duo-security
tags:
- Authentication
- MFA
- Zero Trust
- Identity
website: https://duo.com
---
