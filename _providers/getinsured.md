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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getinsured-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://company.getinsured.com/
- group: company
  title: ''
  type: Blog
  url: https://company.getinsured.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://company.getinsured.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://company.getinsured.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://company.getinsured.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getinsured-llms.txt
created: '2026-07-17'
description: GetInsured (Vimo, Inc.) is a SaaS technology provider for public-sector healthcare that powers state-based health insurance marketplaces (SBMs). Its platform handles eligibility and enrollment, plan shopping and comparison, and consumer-assistance contact-center operations for state ACA exchanges. GetInsured powers ten state marketplaces (including Idaho, Illinois, Minnesota, Nevada, New Jersey, New Mexico, Pennsylvania, Georgia, Virginia, and Oregon, with Oregon launching in 2027) and supported the migration of roughly 4.5 million people off Healthcare.gov. It sells to state governments, insurance carriers, agents/brokers, and enrollment assisters. GetInsured does not publish a public self-serve developer portal or API; integrations are delivered under contract. Backed by Bessemer Venture Partners. This profile was enriched by the API Evangelist pipeline.
image: https://company.getinsured.com/wp-content/uploads/2021/10/GetInsured-By-Vimo-white.png
layout: provider
modified: '2026-07-19'
name: GetInsured
nav: Providers
network: true
overview: 'GetInsured is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Insurance, Government, and Insurance.


  GetInsured''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 39
score:
  band: minimal
  composite: 7.5
  delta: -2.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getinsured/refs/heads/main/screenshots/getinsured-2026-07-25T215735.png
security:
- kind: domain-security
  name: Getinsured Domain Security
  slug: getinsured-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: getinsured
tags:
- Company
- Healthcare
- Health Insurance
- Government
- Insurance
- Marketplace
- ACA
- SaaS
- Enrollment
website: https://company.getinsured.com/
---
