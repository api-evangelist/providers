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
  url: security/rovi-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rovi.health
- group: start
  title: ''
  type: Login
  url: https://app.rovi.health
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rovi.health/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rovi.health/privacy-policy
created: '2026-07-17'
description: Rovi Health is a clinical navigation platform for employer health plans that puts "a clinician in every member's pocket." Members get text-based access to registered nurse care advisors who help them find high-quality, in-network doctors and specialists, navigate their insurance benefits and coverage, and coordinate care across every stage of treatment. The company also uses AI agents to search millions of pricing and quality data points to surface the best in-network providers for complex care and to handle appointment scheduling, aiming to help employers cut 10-20% of healthcare spend while improving employee outcomes. Rovi Health was a Y Combinator (Fall 2025) company operating in the digital health, health insurance navigation, and consumer health services space. As of this enrichment pass Rovi Health publishes no public API, SDK, or developer documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rovi-health.png
layout: provider
modified: '2026-07-21'
name: Rovi Health
nav: Providers
network: true
overview: Rovi Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Health Insurance.
random_paper: 80
score:
  band: minimal
  composite: 10.3
  delta: -2.4
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Rovi Health Domain Security
  slug: rovi-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rovi-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Health Insurance
- Care Navigation
- Employer Benefits
- Telehealth
website: https://www.rovi.health
---
