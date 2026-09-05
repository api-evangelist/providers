---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://www.vertosmed.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.stryker.com/us/en/interventional-spine.html — a different registrable domain (vertosmed.com -> stryker.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/vertos-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vertosmed.com/
- group: company
  title: ''
  type: About
  url: https://www.stryker.com/us/en/interventional-spine.html
- group: operate
  title: ''
  type: PressReleases
  url: https://www.stryker.com/us/en/about/news/2024/stryker-completes-acquisition-of-vertos-medical-inc-expanding-interventional-pain-management-solutions.html
coverage:
  checked: '2026-08-05'
  detail: Vertos Medical was acquired by Stryker on October 1, 2024, and vertosmed.com now answers every path — including /robots.txt, /llms.txt, /sitemap.xml and every /.well-known/* probe — with the same site-wide HTTP 301 to Stryker's Interventional Spine page, so no Vertos developer surface survives to profile.
  evidence:
  - status: 301
    url: https://www.vertosmed.com/
  - status: 301
    url: https://www.vertosmed.com/this-path-definitely-does-not-exist-9z8x7/
  - status: 301
    url: https://www.vertosmed.com/.well-known/agent-card.json
  - status: 301
    url: https://www.vertosmed.com/llms.txt
  - status: 0
    url: https://api.vertosmed.com/
  - status: 0
    url: https://developer.vertosmed.com/
  - status: 404
    url: https://api.github.com/orgs/vertos-medical
  reason: defunct
  state: none
created: '2026-08-05'
description: Vertos Medical, Inc. is a medical device company founded in 2005 and headquartered in Aliso Viejo, California, that developed the mild (minimally invasive lumbar decompression) procedure for treating lumbar spinal stenosis caused by hypertrophic ligamentum flavum. The mild device kit removes excess ligament tissue through a 5.1 mm treatment portal with no implants, no general anesthesia and no stitches; it received FDA clearance in 2006 and CE mark approval in 2019. Stryker announced a definitive agreement to acquire Vertos Medical in August 2024 and completed the acquisition on October 1, 2024, folding the mild procedure into its Interventional Spine business. The vertosmed.com domain now answers every path with a site-wide HTTP 301 redirect to Stryker, and Vertos Medical publishes no developer program, API, SDK or machine-readable specification of its own.
layout: provider
modified: '2026-08-05'
name: Vertos Medical
nav: Providers
network: true
overview: Vertos Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Spine, and Interventional Pain Management.
random_paper: 11
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vertos-medical/refs/heads/main/screenshots/vertos-medical-2026-09-02T165812.png
security:
- kind: domain-security
  name: Vertos Medical Domain Security
  slug: vertos-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vertos-medical
tags:
- Company
- Medical Devices
- Healthcare
- Spine
- Interventional Pain Management
- Minimally Invasive Surgery
- Acquired
website: https://www.vertosmed.com/
---
