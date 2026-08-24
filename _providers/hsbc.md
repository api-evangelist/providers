---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The HSBC Developer Portal exposes a catalogue of APIs covering Open Banking (UK/EU PSD2 Account Information, Payment Initiation, Confirmation of Funds), global payments solutions, and corporate bankin
  name: HSBC Developer Portal APIs
  slug: hsbc-developer-portal
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hsbc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hsbc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hsbc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hsbc
- group: company
  title: ''
  type: Website
  url: https://www.hsbc.com/
- group: start
  title: ''
  type: Portal
  url: https://develop.hsbc.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hsbc.com/
created: '2026-05-05'
description: One of the world's largest banking and financial services organizations headquartered in London. Serves over 40 million customers globally with a strong presence in Asia, Europe, and the Americas. Operates a public Developer Portal (develop.hsbc.com) exposing Open Banking, payments, accounts, and global payments solutions APIs for partners and third-party providers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hsbc.png
layout: provider
modified: '2026-05-16'
name: HSBC
nav: Providers
network: true
overview: 'HSBC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Banks, Global Banking, Open Banking, and PSD2.


  HSBC''s developer surface includes developer portal and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 5.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hsbc/refs/heads/main/screenshots/hsbc-2026-06-20T182858.png
security:
- kind: domain-security
  name: Hsbc Domain Security
  slug: hsbc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hsbc Vulnerability Disclosure
  slug: hsbc-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: hsbc
tags:
- Financial
- Banks
- Global Banking
- Open Banking
- PSD2
website: https://www.hsbc.com/
---
