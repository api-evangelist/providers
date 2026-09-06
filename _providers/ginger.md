---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://ginger.com/'', ''status'': 301, ''note'': ''declared website redirects to https://organizations.headspace.com/ — a different registrable domain (ginger.com -> headspace.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/ginger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ginger.com/
created: '2026-07-17'
description: Ginger (formerly Ginger.io) was a behavioral and emotional health company offering on-demand mental health support — coaching, therapy, and psychiatry — delivered through a mobile app and an employer/health-plan benefits model. Surfaced in the API Evangelist network as a Techstars portfolio lead, Ginger merged with Headspace in 2021 to form Headspace Health; the ginger.com domain now redirects to Headspace for Organizations (organizations.headspace.com). Enrichment probing on 2026-07-19 found no independent public API, developer portal, OpenAPI, SDKs, or /.well-known discovery surface — every /.well-known path resolves to a soft-404 Headspace marketing page. This profile is retained as an acquired-company record; the only genuine machine-derivable artifact is the live domain-security posture of ginger.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ginger.png
layout: provider
modified: '2026-07-19'
name: Ginger
nav: Providers
network: true
overview: Ginger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Behavioral Health, Healthcare, and Wellness.
random_paper: 6
score:
  band: minimal
  composite: 3.3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ginger/refs/heads/main/screenshots/ginger-2026-07-25T215825.png
security:
- kind: domain-security
  name: Ginger Domain Security
  slug: ginger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ginger
tags:
- Company
- Mental Health
- Behavioral Health
- Healthcare
- Wellness
- Telehealth
- Coaching
- Acquired
website: https://ginger.com/
---
