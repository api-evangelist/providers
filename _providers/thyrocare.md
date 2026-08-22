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
api_count: 1
apis:
- description: Partner order-booking API used by Thyrocare's DSA (Direct Selling Agent) franchise network for booking diagnostic tests and retrieving reports. A Swashbuckle (.NET) Swagger UI is publicly reachable, b
  name: Thyrocare TechSo Partner API (BTS)
  slug: thyrocare-techso-partner-api-bts
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thyrocare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thyrocare.com
- group: operate
  title: ''
  type: Support
  url: https://thyrocare.freshdesk.com/support/solutions
- group: start
  title: ''
  type: Login
  url: https://client.thyrocare.com/
- group: start
  title: ''
  type: SignUp
  url: https://lead.thyrocare.com/dsa-affiliate/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://b2capi.thyrocare.com/privacy_policy.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thyrocare-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thyrocare-llms.txt
created: '2026-07-17'
description: Thyrocare Technologies Limited is an Indian chain of diagnostic and preventive-care laboratories headquartered in Navi Mumbai, founded in 1996. Built around a centralized, highly automated laboratory model, it focuses on affordable preventive health checkups, thyroid and pathology testing, and sells through a nationwide network of DSA (Direct Selling Agent) franchise partners. Norwest Venture Partners invested pre-IPO, and PharmEasy (API Holdings) acquired a majority stake in 2021. Its partner order-booking API (TechSo/BTS) is gated behind the DSA program and publishes no public OpenAPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thyrocare.png
layout: provider
modified: '2026-07-21'
name: Thyrocare
nav: Providers
network: true
overview: 'Thyrocare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Laboratory, and Pathology.


  Thyrocare''s developer surface includes support, signup flow, and 6 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.4
  delta: -1.7
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Thyrocare Domain Security
  slug: thyrocare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thyrocare
tags:
- Company
- Healthcare
- Diagnostics
- Laboratory
- Pathology
- Preventive Care
- India
website: https://thyrocare.com
---
