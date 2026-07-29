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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Maps, datasets, applications and more in the context of COVID-19
  name: Covid-19 Datenhub
  slug: covid-19-datenhub
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/covid-19-datenhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covid-19-datenhub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://npgeo-corona-npgeo-de.hub.arcgis.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Maps, datasets, applications and more in the context of COVID-19
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covid-19-datenhub.png
layout: provider
modified: '2026-05-28'
name: Covid-19 Datenhub
nav: Providers
network: true
overview: Covid-19 Datenhub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 71
score:
  band: minimal
  composite: 7.1
  delta: -2.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/covid-19-datenhub/refs/heads/main/screenshots/covid-19-datenhub-2026-06-20T175124.png
security:
- kind: domain-security
  name: Covid 19 Datenhub Domain Security
  slug: covid-19-datenhub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Covid 19 Datenhub Vulnerability Disclosure
  slug: covid-19-datenhub-vulnerability-disclosure
  summary_line: disclosure policy published
slug: covid-19-datenhub
tags:
- Health
- Public APIs
website: https://npgeo-corona-npgeo-de.hub.arcgis.com
---
