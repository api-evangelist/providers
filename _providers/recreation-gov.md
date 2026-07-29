---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Recreation Gov Agentic Access
  operation_count: 25
  slug: recreation-gov-agentic-access
  summary_line: 25 operations
api_count: 10
apis:
- description: The Activities API from Recreation.gov — 2 operation(s) for activities.
  name: Recreation.gov Activities API
  slug: recreation-gov-activities-api
- description: The Campsites API from Recreation.gov — 2 operation(s) for campsites.
  name: Recreation.gov Campsites API
  slug: recreation-gov-campsites-api
- description: The Events API from Recreation.gov — 2 operation(s) for events.
  name: Recreation.gov Events API
  slug: recreation-gov-events-api
- description: The Facilities API from Recreation.gov — 6 operation(s) for facilities.
  name: Recreation.gov Facilities API
  slug: recreation-gov-facilities-api
- description: The Links API from Recreation.gov — 1 operation(s) for links.
  name: Recreation.gov Links API
  slug: recreation-gov-links-api
- description: The Media API from Recreation.gov — 1 operation(s) for media.
  name: Recreation.gov Media API
  slug: recreation-gov-media-api
- description: The Organizations API from Recreation.gov — 2 operation(s) for organizations.
  name: Recreation.gov Organizations API
  slug: recreation-gov-organizations-api
- description: The Permitentrances API from Recreation.gov — 2 operation(s) for permitentrances.
  name: Recreation.gov Permitentrances API
  slug: recreation-gov-permitentrances-api
- description: The Recareas API from Recreation.gov — 5 operation(s) for recareas.
  name: Recreation.gov Recareas API
  slug: recreation-gov-recareas-api
- description: The Tours API from Recreation.gov — 2 operation(s) for tours.
  name: Recreation.gov Tours API
  slug: recreation-gov-tours-api
artifact_total: 18
collections:
- collection_type: open
  name: Recreation Information Database (RIDB) API
  slug: open-recreation-gov
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/recreation-gov-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recreation-gov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recreation-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recreation-gov-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.recreation.gov
- group: docs
  title: ''
  type: Documentation
  url: https://ridb.recreation.gov/docs
- group: agent
  title: ''
  type: LlmsText
  url: https://www.recreation.gov/llms.txt
created: '2025-03-01'
description: The Recreation Information Database (RIDB) provides data resources to citizens, offering a single point of access to information about recreational opportunities nationwide. The RIDB represents an authoritative source of information and services for millions of visitors to federal lands, historic sites, museums, and other attractions/resources.
finops:
- name: Recreation Gov Finops
  service_category: API
  slug: recreation-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recreation-gov.png
layout: provider
modified: '2026-05-19'
name: Recreation.gov
nav: Providers
network: true
overview: 'Recreation.gov publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Campsites API, Events API, and 7 more. Tagged areas include Recreation, Federal, Camping, Outdoors, and Public Lands.


  Recreation.gov''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Recreation Gov Plans Pricing
  plan_count: 3
  slug: recreation-gov-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Recreation Gov Rate Limits
  slug: recreation-gov-rate-limits
score:
  band: thin
  composite: 35.8
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 33.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recreation-gov/refs/heads/main/screenshots/recreation-gov-2026-06-20T192708.png
security:
- kind: authentication
  name: Recreation Gov Authentication
  slug: recreation-gov-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Recreation Gov Domain Security
  slug: recreation-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Recreation Gov Vulnerability Disclosure
  slug: recreation-gov-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: recreation-gov
tags:
- Recreation
- Federal
- Camping
- Outdoors
- Public Lands
website: https://www.recreation.gov
---
