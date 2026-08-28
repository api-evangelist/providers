---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: OffenderList provides security and information-focused organizations API access, batch requests, remote access, and internal access to a national sex offender database.
  name: OffenderList
  slug: offenderlist
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offenderlist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://offenderlist.us/
- group: company
  title: ''
  type: Blog
  url: https://offenderlist.us/feed/
created: '2024-11-13'
description: OffenderList is a comprehensive online platform that provides information about individuals who have been convicted of criminal offenses. The website allows users to search for offenders based on various criteria such as name, location, or offense type. OffenderList provides important details about each offender, including their mugshot, charges, conviction date, and sentence length. OffenderList provides security and information-focused organizations API access, batch requests, remote access, and internal access to a national sex offender database.
finops:
- name: Offenderlist Finops
  service_category: API
  slug: offenderlist-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/offenderlist.png
layout: provider
modified: '2026-04-28'
name: OffenderList
nav: Providers
network: true
overview: 'OffenderList publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sex Offenders, Public Safety, and Criminal Records.


  OffenderList''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Offenderlist Plans Pricing
  plan_count: 3
  slug: offenderlist-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Offenderlist Rate Limits
  slug: offenderlist-rate-limits
score:
  band: minimal
  composite: 9.7
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/offenderlist/refs/heads/main/screenshots/offenderlist-2026-06-20T190626.png
security:
- kind: domain-security
  name: Offenderlist Domain Security
  slug: offenderlist-domain-security
  summary_line: TLSv1.3 · DMARC
slug: offenderlist
tags:
- Sex Offenders
- Public Safety
- Criminal Records
website: https://offenderlist.us/
---
