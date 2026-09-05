---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  url: security/powder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.powder.gg/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/powder-lifecycle.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://powderapp.notion.site/POWDER-T-C-fb5f1576921f4ec9a7fb9d243786ace3
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://powderapp.notion.site/POWDER-T-C-fb5f1576921f4ec9a7fb9d243786ace3
coverage:
  checked: '2026-08-17'
  detail: Powder shipped only a consumer Windows desktop clipping app with no public API, portal or SDK, and the company has since wound down — its apex host powder.gg now 301-redirects every path, including /openapi.json and every /.well-known/ path, to a first-party notice saying the app is no longer updated or maintained.
  evidence:
  - status: 301
    url: https://powder.gg/openapi.json
  - status: 200
    url: https://docs.google.com/document/d/1p8TjN7bCRdOnhrD5DjG02pmoGi4ylsGKmdCS-YV4jrg/export?format=txt
  - status: 404
    url: https://www.powder.gg/.well-known/agent-card.json
  - status: 404
    url: https://www.powder.gg/llms.txt
  reason: defunct
  state: none
created: '2026-08-17'
description: 'Powder was a Paris-based gaming company, founded in 2018 and backed by a $14M Series A led by Serena with General Catalyst, Slow Ventures, Alven, Bpifrance Digital Venture and Secocha Ventures. It built AI-powered clipping software for gamers and content creators: a low-resource Windows screen recorder plus on-device machine learning that detected highlight moments in gameplay recordings and long Twitch, YouTube and Kick streams and turned them into short vertical clips, AutoEdits and automontages, with per-title models for 40-plus games including Fortnite, Valorant, Counter-Strike 2 and League of Legends, and NPU-accelerated local inference on AMD XDNA hardware. It was distributed as an end-user desktop app through Steam, the Microsoft Store and Razer Cortex, on a free tier with a $9.99/month Powder Pro subscription. Powder published no public API, developer portal, SDK or machine-readable contract. The company has since wound down: its own apex domain now redirects every
  path to a first-party notice stating the app is no longer updated or maintained and that all subscriptions have been cancelled.'
image: https://www.powder.gg/_next/static/media/og.fecfbdd8.jpg
layout: provider
modified: '2026-08-17'
name: Powder
nav: Providers
network: true
overview: Powder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Video, Artificial Intelligence, and Content Creation.
random_paper: 6
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/powder/refs/heads/main/screenshots/powder-2026-09-02T151836.png
security:
- kind: domain-security
  name: Powder Domain Security
  slug: powder-domain-security
  summary_line: TLSv1.3 · HSTS
slug: powder
tags:
- Company
- Gaming
- Video
- Artificial Intelligence
- Content Creation
- Streaming
- Media
- Desktop Application
- Discontinued
website: https://www.powder.gg/
---
