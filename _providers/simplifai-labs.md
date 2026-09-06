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
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://simplifailabs.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simplifailabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplifailabs
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/simplifai-labs
coverage:
  checked: '2026-08-12'
  detail: simplifailabs.com lapsed and was re-registered on 2025-08-18 (GoDaddy, NS1/NS2.CYBERFUEL.COM) and now returns a Spanish-language Cyberfuel "this site has no published content" hosting placeholder, so every /.well-known/, /openapi.json and /llms.txt probe 404s against a host the company no longer operates; no api/docs/developer subdomain resolves and the simplifailabs GitHub org contains only a react-native-elements fork.
  evidence:
  - status: 200
    url: https://simplifailabs.com/
  - status: 404
    url: https://simplifailabs.com/openapi.json
  - status: 404
    url: https://simplifailabs.com/.well-known/agent-card.json
  - status: 404
    url: https://simplifailabs.com/.well-known/security.txt
  - status: 404
    url: https://simplifailabs.com/llms.txt
  - status: 200
    url: https://github.com/simplifailabs
  reason: defunct
  state: none
created: '2026-07-17'
description: Simplifai Labs is a Dubai-based artificial intelligence and marketing-technology company founded in 2018 by Sachin Rathnaraj Jain. Its deep-learning platform combines image recognition, computer vision, sentiment and emotion analysis, and natural language processing to place brand advertising alongside highly relevant, brand-safe content in real time, without relying on stored user cookie data. Simplifai Labs completed the 500 Global (Misk 500 MENA) accelerator in Riyadh and is a 500 Global portfolio company. As of this enrichment pass the company publishes no public API, developer documentation, or SDKs. Its simplifailabs.com domain lapsed and was re-registered on 2025-08-18, and now serves a Cyberfuel hosting placeholder rather than any Simplifai Labs content; no API, docs, or developer subdomain resolves, and the simplifailabs GitHub organization holds a single forked UI repository and no first-party libraries. The founder's subsequent venture, Smartifai (Dubai, 2022), is
  a separate company and is not profiled here. No API artifacts could be harvested.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplifai-labs.png
layout: provider
modified: '2026-08-12'
name: Simplifai Labs
nav: Providers
network: true
overview: Simplifai Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Marketing Technology, and Advertising.
random_paper: 14
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 1
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
    - middle-east
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simplifai-labs/refs/heads/main/screenshots/simplifai-labs-2026-09-02T155543.png
slug: simplifai-labs
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Marketing Technology
- Advertising
- Brand Safety
- Contextual Advertising
- Computer-Vision
- Natural Language Processing
website: https://simplifailabs.com
---
