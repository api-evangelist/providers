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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snips-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snipsco
- group: company
  title: ''
  type: Website
  url: https://snips.ai
created: '2026-07-17'
description: Snips was a Paris-based artificial intelligence company that built a private-by-design, on-device voice assistant platform and natural language understanding (NLU) technology, letting developers add offline voice interfaces to connected devices without sending audio to the cloud. Snips was acquired by Sonos in November 2019 and its team became the Sonos Voice Experience group; the developer platform, hosted APIs, and console were subsequently discontinued. snips.ai now serves only a static acquisition-announcement page, and the company's open-source libraries (notably the Snips NLU engine) remain archived under the github.com/snipsco organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snips.png
layout: provider
modified: '2026-07-21'
name: Snips
nav: Providers
network: true
overview: Snips is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Voice, Artificial Intelligence, Natural Language Understanding, and Voice Assistant.
random_paper: 11
score:
  band: minimal
  composite: 5.3
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snips/refs/heads/main/screenshots/snips-2026-09-02T160014.png
security:
- kind: domain-security
  name: Snips Domain Security
  slug: snips-domain-security
  summary_line: TLSv1.3 · DMARC
slug: snips
tags:
- Company
- Voice
- Artificial Intelligence
- Natural Language Understanding
- Voice Assistant
- On-Device AI
- Privacy
- Acquired
website: https://snips.ai
---
