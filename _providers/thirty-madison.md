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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thirty-madison-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://thirtymadison.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thirty-madison-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://thirtymadison.com
created: '2026-07-17'
description: Thirty Madison is a US direct-to-consumer telehealth and digital-health company founded in 2017 and headquartered in New York City. It operates a family of condition-focused virtual care brands, including Keeps (hair loss), Cove (migraine), Facet (dermatology), and Nurx (sexual and reproductive health), pairing online medical consultations with mail-order pharmacy fulfillment; the company merged with Nurx in 2022. Thirty Madison publishes no public developer API program, so this profile captures its public security-disclosure and domain-security posture rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thirty-madison.png
layout: provider
modified: '2026-07-21'
name: Thirty Madison
nav: Providers
network: true
overview: Thirty Madison is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Telemedicine, and Digital Health.
random_paper: 112
score:
  band: minimal
  composite: 7.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Thirty Madison Domain Security
  slug: thirty-madison-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Thirty Madison Vulnerability Disclosure
  slug: thirty-madison-vulnerability-disclosure
  summary_line: disclosure policy published
slug: thirty-madison
tags:
- Company
- Healthcare
- Telehealth
- Telemedicine
- Digital Health
- Direct-to-Consumer
- Pharmacy
website: http://thirtymadison.com
---
