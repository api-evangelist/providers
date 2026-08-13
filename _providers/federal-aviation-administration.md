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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 6
apis:
- description: The FAA NOTAM API provides access to Notices to Air Missions (NOTAMs), which are time-critical aeronautical information that could affect a pilot's decision to make a flight. The API allows developers
  name: FAA NOTAM
  slug: notam-api
- description: The FAA Airport Status Web Service (ASWS) provides current airport conditions, including delays and ground stops, for major United States airports. Developers can use the service to retrieve real-time
  name: FAA Airport Status
  slug: airport-status
- description: The FAA National Airspace System Resources (NASR) Subscription provides authoritative aeronautical data covering airports, navigation aids, airways, fixes, and special-use airspace on a 28-day publica
  name: FAA NASR Subscription
  slug: nasr-subscription
- description: The FAA Airmen Registry provides downloadable data on certificated pilots and other airmen in the United States, including pilot certificates, ratings, and medical certificates. The dataset supports v
  name: FAA Airmen Registry
  slug: airmen-registry
- description: The FAA Aircraft Registry provides downloadable data on civil aircraft registered in the United States, including registration, ownership, and airworthiness information. The dataset is widely used for
  name: FAA Aircraft Registry
  slug: aircraft-registry
- description: The FAA System Wide Information Management (SWIM) program is a service-oriented information sharing platform that delivers real-time National Airspace System data to authorized consumers. SWIM publish
  name: FAA System Wide Information Management
  slug: swim
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-aviation-administration-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Federal-Aviation-Administration
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/faa
- group: company
  title: ''
  type: Website
  url: https://www.faa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.faa.gov/data_research
created: '2024-12-03'
description: The Federal Aviation Administration (FAA) is the U.S. Department of Transportation agency responsible for the regulation and oversight of civil aviation. The FAA publishes a range of public data products and APIs covering airport status, NOTAMs, aeronautical information, airmen and aircraft registries, and System Wide Information Management (SWIM) feeds for air traffic operations.
finops:
- name: Federal Aviation Administration Finops
  service_category: API
  slug: federal-aviation-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-aviation-administration.png
layout: provider
modified: '2026-04-28'
name: Federal Aviation Administration
nav: Providers
network: true
overview: 'Federal Aviation Administration publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation and Federal Government.


  Federal Aviation Administration''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Federal Aviation Administration Plans Pricing
  plan_count: 3
  slug: federal-aviation-administration-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Federal Aviation Administration Rate Limits
  slug: federal-aviation-administration-rate-limits
score:
  band: minimal
  composite: 12.0
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-aviation-administration/refs/heads/main/screenshots/federal-aviation-administration-2026-06-20T181109.png
security:
- kind: domain-security
  name: Federal Aviation Administration Domain Security
  slug: federal-aviation-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: federal-aviation-administration
tags:
- Aviation
- Federal Government
website: https://www.faa.gov/
---
