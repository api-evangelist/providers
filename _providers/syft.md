---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://syftapp.com'', ''status'': 302, ''note'': ''declared website redirects to https://indeedflex.co.uk/ — a different registrable domain (syftapp.com -> indeedflex.co.uk), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/indeed/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syftapp.com
- group: other
  title: ''
  type: Company
  url: https://creandum.com/commitments/syft/
created: '2026-07-17'
description: Syft (originally Syft Online Ltd, later branded "Syft by Indeed") is a UK-founded flexible-staffing marketplace launched in London in 2015 by Jack Beaman and Novo Abakare. Its platform connects employers across hospitality, retail, industrial, care and facilities-management directly with vetted, rated temporary and part-time workers, removing the traditional recruitment agency and charging a flat fee on top of worker wages. Creandum led Syft's Series A in 2017; the company was acquired by Indeed in 2019 and now operates as part of Indeed Flex. Syft is a consumer/employer staffing marketplace and exposes no public developer API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/syft.png
layout: provider
modified: '2026-07-21'
name: Syft
nav: Providers
network: true
overview: Syft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Recruitment, Hospitality, and Workforce.
random_paper: 13
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
screenshot: https://raw.githubusercontent.com/api-evangelist/syft/refs/heads/main/screenshots/syft-2026-09-02T161435.png
security:
- kind: domain-security
  name: Syft Domain Security
  slug: syft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: syft
tags:
- Company
- Staffing
- Recruitment
- Hospitality
- Workforce
- Marketplace
- Gig Economy
website: https://syftapp.com
---
