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
    consent_identity: true
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
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blink-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.blinkhealth.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blink-health-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blink-health-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/blink-health-security.txt
- group: operate
  title: ''
  type: Support
  url: https://www.blinkhealth.com/faq
- group: start
  title: ''
  type: Login
  url: https://www.blinkhealth.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blinkhealth.com/legal
- group: company
  title: ''
  type: Website
  url: https://blinkhealth.com
created: '2026-07-17'
description: Blink Health is a healthcare technology company that operates BlinkRx, a digital pharmacy platform connecting patients, prescribers, and pharmaceutical manufacturers to simplify prescription access, fulfillment, and affordability. The platform streamlines the path from a provider writing a prescription to a patient receiving medication at a transparent price, with copay support, home delivery, and manufacturer-sponsored programs. Backed by 8vc, Blink Health runs consumer-facing prescription-savings tools and a provider/pharma-facing BlinkRx offering. No public developer API program or documentation was found during enrichment; a live undocumented API host exists at api.blinkhealth.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blink-health.png
layout: provider
modified: '2026-07-18'
name: Blink Health
nav: Providers
network: true
overview: 'Blink Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pharmacy, Prescriptions, and Digital Health.


  Blink Health''s developer surface includes support and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.4
  delta: -2.7
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blink-health/refs/heads/main/screenshots/blink-health-2026-07-25T203321.png
security:
- kind: domain-security
  name: Blink Health Domain Security
  slug: blink-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blink Health Vulnerability Disclosure
  slug: blink-health-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blink-health
tags:
- Company
- Healthcare
- Pharmacy
- Prescriptions
- Digital Health
- Medications
- Health Tech
website: https://blinkhealth.com
---
