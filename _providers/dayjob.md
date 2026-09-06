---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.getdayjob.ai'', ''status'': 301, ''note'': ''declared website redirects to https://www.dayjob.ai/ — a different registrable domain (getdayjob.ai -> dayjob.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dayjob-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getdayjob.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getdayjob.ai/privacy-policy
created: '2026-07-17'
description: Dayjob is an AI-powered scheduling agent built for waste management and skip hire fleets, operated by Gaea Technology Ltd and backed by Y Combinator (Spring 2026). Its autonomous agents analyze millions of potential route combinations to build optimized daily schedules that factor in travel times, skip sizes, driver availability and priority job assignments, then continuously re-optimize in real time as new jobs, driver changes and exceptions arrive. Dayjob integrates with existing ERP and telematics systems (Weighsoft, PurGo, Wastelogics, plus custom report setups) and claims customers see revenue and efficiency gains, tighter time-window hit rates and materially less planning admin. It is a vertical logistics application rather than an API platform - no public developer portal, API reference or SDKs are published at this time. This profile has been enriched from the company's public website.
image: https://www.getdayjob.ai/favicon.ico
layout: provider
modified: '2026-07-18'
name: Dayjob
nav: Providers
network: true
overview: Dayjob is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Transportation, Waste Management, and Fleet Management.
random_paper: 3
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dayjob/refs/heads/main/screenshots/dayjob-2026-07-25T211445.png
security:
- kind: domain-security
  name: Dayjob Domain Security
  slug: dayjob-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dayjob
tags:
- Company
- Logistics
- Transportation
- Waste Management
- Fleet Management
- Scheduling
- Route Optimization
- Artificial Intelligence
website: https://www.getdayjob.ai
---
