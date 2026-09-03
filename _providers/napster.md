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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Music
  name: Napster
  slug: napster
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/napster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.napster.com/api/v2.2
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Music
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/napster.png
layout: provider
modified: '2026-05-28'
name: Napster
nav: Providers
network: true
overview: Napster publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music and Public APIs.
random_paper: 9
score:
  band: minimal
  composite: 6.7
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/napster/refs/heads/main/screenshots/napster-2026-08-07T184629.png
security:
- kind: domain-security
  name: Napster Domain Security
  slug: napster-domain-security
  summary_line: TLSv1.3 · DMARC
slug: napster
tags:
- Music
- Public APIs
website: https://developer.napster.com/api/v2.2
---
