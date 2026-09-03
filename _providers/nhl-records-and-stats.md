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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: NHL historical data and statistics
  name: NHL Records and Stats
  slug: nhl-records-and-stats
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/nhl-records-and-stats-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nhl-records-and-stats-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nhl-records-and-stats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gitlab.com/dword4/nhlapi
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: NHL historical data and statistics
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nhl-records-and-stats.png
layout: provider
modified: '2026-05-28'
name: NHL Records and Stats
nav: Providers
network: true
overview: NHL Records and Stats publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sports And Fitness and Public APIs.
random_paper: 19
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nhl-records-and-stats/refs/heads/main/screenshots/nhl-records-and-stats-2026-06-20T190310.png
security:
- kind: domain-security
  name: Nhl Records And Stats Domain Security
  slug: nhl-records-and-stats-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nhl Records And Stats Vulnerability Disclosure
  slug: nhl-records-and-stats-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Nhl Records And Stats Trust Center
  slug: nhl-records-and-stats-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR, CSA STAR
slug: nhl-records-and-stats
tags:
- Sports And Fitness
- Public APIs
website: https://gitlab.com/dword4/nhlapi
---
