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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viajanet-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/viajanet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/viajanet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/viajanet-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/viajanet-well-known.yml
- group: company
  title: ''
  type: Website
  url: http://www.viajanet.com.br/
created: '2026-07-17'
description: Viajanet is a Brazilian online travel agency (OTA) operated within the Despegar group, selling flights, hotels, vacation packages, car rentals and travel insurance to consumers in Brazil through www.viajanet.com.br. It was surfaced as a portfolio company of Redpoint Ventures and added to the API Evangelist network for enrichment. Viajanet publishes no public developer API, SDK, or developer portal; the enrichment pass captured its live security surface (a published security.txt with a Bugcrowd private bug bounty program run by the Despegar application-security team) and its domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/viajanet.png
layout: provider
modified: '2026-07-21'
name: Viajanet
nav: Providers
network: true
overview: Viajanet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Online Travel Agency, Flights, and Hotels.
random_paper: 10
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 6.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Viajanet Domain Security
  slug: viajanet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Viajanet Vulnerability Disclosure
  slug: viajanet-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: viajanet
tags:
- Company
- Travel
- Online Travel Agency
- Flights
- Hotels
- Booking
- Brazil
- E-Commerce
website: http://www.viajanet.com.br/
---
