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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The New York Times Developer Network
  name: New York Times
  slug: new-york-times
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/new-york-times-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/new-york-times-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.nytimes.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: The New York Times Developer Network
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/new-york-times.png
layout: provider
modified: '2026-05-28'
name: New York Times
nav: Providers
network: true
overview: New York Times publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News and Public APIs.
random_paper: 12
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/new-york-times/refs/heads/main/screenshots/new-york-times-2026-06-20T190233.png
security:
- kind: domain-security
  name: New York Times Domain Security
  slug: new-york-times-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: New York Times Vulnerability Disclosure
  slug: new-york-times-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: new-york-times
tags:
- News
- Public APIs
website: https://developer.nytimes.com/
---
