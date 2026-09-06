---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://tubemogul.com/'', ''status'': 301, ''note'': ''declared website redirects to https://advertising.adobe.com/auth/login — a different registrable domain (tubemogul.com -> adobe.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/adobe/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tubemogul-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tubemogul.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tubemogul
- group: build
  title: ''
  type: Packages
  url: packages/tubemogul-packages.yml
coverage:
  checked: '2026-08-13'
  detail: TubeMogul was absorbed into Adobe Advertising Cloud after the 2016 acquisition — tubemogul.com now 301s to advertising.adobe.com/auth/login, and the old Ad Platform API host api.tubemogul.com answers HTTP 503 "No server is available to handle this request." on every path, so the API tier has no backend left to document.
  evidence:
  - status: 301
    url: https://tubemogul.com/
  - status: 503
    url: https://api.tubemogul.com/openapi.json
  - status: 503
    url: https://api.tubemogul.com/.well-known/agent-card.json
  - status: 404
    url: https://www.tubemogul.com/.well-known/security.txt
  - status: 404
    url: https://www.tubemogul.com/llms.txt
  reason: defunct
  state: none
created: '2026-07-17'
description: TubeMogul was an independent video advertising software platform — a demand-side platform for planning, buying, measuring and optimizing programmatic brand video campaigns across desktop, mobile, connected TV and out-of-home. Founded 2006 in Emeryville, California, it IPO'd on NASDAQ in 2014 and was acquired by Adobe in 2016, then folded into Adobe Advertising Cloud. It ran an Ad Platform API at api.tubemogul.com for partner reporting and campaign management; that host is now dark and no independent developer surface remains.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tubemogul.png
layout: provider
modified: '2026-08-13'
name: TubeMogul
nav: Providers
network: true
overview: TubeMogul is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, Video Advertising, and Demand-Side Platform.
random_paper: 14
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 4
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
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tubemogul/refs/heads/main/screenshots/tubemogul-2026-09-02T164451.png
security:
- kind: domain-security
  name: Tubemogul Domain Security
  slug: tubemogul-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: tubemogul
tags:
- Company
- Marketing
- Advertising
- Video Advertising
- Demand-Side Platform
- Programmatic Advertising
- AdTech
- Acquired
website: https://tubemogul.com/
---
