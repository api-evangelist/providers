---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://teamsurfboard.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.dialpad.com/features/workforce-management-software/ — a different registrable domain (teamsurfboard.com -> dialpad.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/surfboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://teamsurfboard.com
created: '2026-07-17'
description: Surfboard (teamsurfboard.com) was a workforce management (WFM) SaaS for customer support teams — scheduling, forecasting, and real-time staffing for contact centers — backed by Seedcamp and Speedinvest. As of this enrichment pass the standalone product no longer operates independently; teamsurfboard.com returns an HTTP 301 permanent redirect to Dialpad's workforce management software page (dialpad.com/features/workforce-management-software), indicating Surfboard was acquired by / folded into Dialpad. No standalone Surfboard developer portal, API reference, or OpenAPI surface is publicly reachable; all probed /.well-known/ discovery endpoints return 404.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surfboard.png
layout: provider
modified: '2026-07-21'
name: Surfboard
nav: Providers
network: true
overview: Surfboard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Customer-Support, Contact Center, and Scheduling.
random_paper: 2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/surfboard/refs/heads/main/screenshots/surfboard-2026-09-02T161318.png
security:
- kind: domain-security
  name: Surfboard Domain Security
  slug: surfboard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: surfboard
tags:
- Company
- Workforce Management
- Customer-Support
- Contact Center
- Scheduling
- WFM
- Acquired
website: http://teamsurfboard.com
---
