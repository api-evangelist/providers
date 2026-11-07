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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/kiwop/llms/kiwop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kiwop-llms.txt
- group: other
  href: https://artifacts.apis.io/kiwop/hosts/kiwop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kiwop-hosts.yml
- group: other
  href: https://artifacts.apis.io/kiwop/vendors/kiwop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kiwop-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kiwop.com/de/privacy-engineering
- group: company
  title: ''
  type: Blog
  url: https://www.kiwop.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.kiwop.com/
- group: auth
  href: https://artifacts.apis.io/kiwop/security/kiwop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kiwop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kiwop.com/
coverage:
  checked: '2026-10-18'
  detail: The provider's documentation site renders content via JavaScript, preventing retrieval of a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.kiwop.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-17'
description: Kiwop LLMOps is a Spanish‑based company offering AI‑powered services for enterprises, including large language model (LLM) integration, Retrieval‑Augmented Generation (RAG), autonomous AI agents, and consulting. Their portfolio spans AI strategy, governance, compliance with the AI Act, custom chatbot development, cloud architecture on AWS, Azure and GCP, and cybersecurity audits. Kiwop provides end‑to‑end solutions from model fine‑tuning to production deployment, helping businesses unlock the value of generative AI while ensuring regulatory and security standards are met.
image: https://www.kiwop.com/og-image.png
layout: provider
modified: '2026-10-17'
name: Kiwop LLMOps
nav: Providers
network: true
overview: 'Kiwop LLMOps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, LLM, RAG, and Consulting.


  Kiwop LLMOps'' developer surface includes engineering blog, documentation, and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 9.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kiwop/kiwop-2026-11-03T134436.png
security:
- kind: domain-security
  name: Kiwop Domain Security
  slug: kiwop-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kiwop
tags:
- Company
- Artificial Intelligence
- LLM
- RAG
- Consulting
website: https://kiwop.com/
---
