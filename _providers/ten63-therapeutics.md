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
  url: security/ten63-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ten63tx.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ten63tx.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ten63tx
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ten63-therapeutics-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Ten63 Therapeutics is a clinical-stage drug-design company, not a software vendor — its BEYOND Large Quantum Chemistry Model is run internally and licensed through pharma partnerships, and www.ten63tx.com is a two-page marketing site whose own sitemap.xml lists only the home page and /contact, with no developer portal, docs, SDK or spec anywhere on it.
  evidence:
  - status: 200
    url: https://www.ten63tx.com/sitemap.xml
  - status: 404
    url: https://www.ten63tx.com/openapi.json
  - status: 404
    url: https://www.ten63tx.com/docs
  - status: 404
    url: https://www.ten63tx.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/ten63tx
  - status: 200
    url: https://www.ten63tx.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-30'
description: 'Ten63 Therapeutics is an AI-driven drug-discovery company spun out of Duke University in 2019 and operating from San Francisco, Durham and Boston. It builds BEYOND, which the company describes as the world''s first Large Quantum Chemistry Model — pairing generative chemistry at scale (Move37) with a quantum-accurate forcefield and molecular-dynamics engine (Astrolabe) in an approach it calls Superlearning. BEYOND is used to design therapeutics for previously undruggable and under-drugged targets, with an internal pipeline focused on oncology and platform partnerships such as the multi-target collaboration with Boehringer Ingelheim. Ten63 is a therapeutics company, not a software vendor: it publishes no developer program, no public API, and no machine-readable API contract. It does publish an llms.txt describing the company and platform for AI agents.'
image: https://www.ten63tx.com/brand/White.webp
layout: provider
modified: '2026-08-30'
name: Ten63 Therapeutics
nav: Providers
network: true
overview: 'Ten63 Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Artificial Intelligence.


  Ten63 Therapeutics'' developer surface includes support and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 5.4
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ten63-therapeutics/refs/heads/main/screenshots/ten63-therapeutics-2026-09-02T163109.png
security:
- kind: domain-security
  name: Ten63 Therapeutics Domain Security
  slug: ten63-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: ten63-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Artificial Intelligence
- Machine-Learning
- Computational Chemistry
- Oncology
- Life Sciences
- Research
website: https://www.ten63tx.com/
---
