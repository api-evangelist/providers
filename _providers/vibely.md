---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://vibely.io'', ''status'': 301, ''note'': ''declared website redirects to https://www.kajabi.com/product/communities — a different registrable domain (vibely.io -> kajabi.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vibely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vibely.io
created: '2026-07-17'
description: Vibely was a creator-community platform (surfaced as a 500 Global portfolio company) that let creators host paid communities, challenges, and group chat. As of this enrichment pass the domain vibely.io no longer serves an independent product; every path — including all /.well-known/ discovery endpoints — 301-redirects to kajabi.com/features/communities, indicating Vibely was folded into Kajabi's Communities product. No standalone Vibely developer portal, API, OpenAPI, SDK, MCP server, or llms.txt could be found; the only artifact captured is a probed TLS/DNS domain-security profile of the surviving redirect domain. This profile is retained as a defunct/acquired portfolio lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vibely.png
layout: provider
modified: '2026-07-21'
name: Vibely
nav: Providers
network: true
overview: Vibely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Community Platform, Membership, and Acquired.
random_paper: 0
score:
  band: minimal
  composite: 5.0
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
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vibely/refs/heads/main/screenshots/vibely-2026-09-02T165843.png
security:
- kind: domain-security
  name: Vibely Domain Security
  slug: vibely-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vibely
tags:
- Company
- Creator Economy
- Community Platform
- Membership
- Acquired
- Kajabi
website: https://vibely.io
---
