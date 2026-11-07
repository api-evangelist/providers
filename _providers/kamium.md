---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/kamium/plans/kamium-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kamium-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/kamium/conformance/kamium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kamium-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kamium/llms/kamium-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kamium-llms.txt
- group: other
  href: https://artifacts.apis.io/kamium/hosts/kamium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kamium-hosts.yml
- group: other
  href: https://artifacts.apis.io/kamium/vendors/kamium-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kamium-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kamium.de/
- group: auth
  href: https://artifacts.apis.io/kamium/security/kamium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kamium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kamium.de/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://kamium.de/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Zweitag GmbH offers kamium, an enterprise‑AI platform that enables companies to deploy generative AI in a data‑sovereign, scalable and flexible manner. Hosted in private cloud, the solution integrates with existing workflows across sales, IT, HR, legal and more, providing multimodal processing, RAG over corporate data, and AI assistants. Built in Germany, it emphasizes GDPR compliance, vendor‑agnostic architecture, and on‑premise deployment, allowing enterprises to retain control over their AI models and data while benefiting from modern AI capabilities.
layout: provider
modified: '2026-10-20'
name: Zweitag
nav: Providers
network: true
overview: 'Zweitag is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, GDPR, and Germany.


  Zweitag''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Kamium Plans Pricing
  plan_count: 3
  slug: kamium-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 14.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kamium/kamium-2026-11-03T134307.png
security:
- kind: domain-security
  name: Kamium Domain Security
  slug: kamium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kamium
tags:
- Company
- Artificial Intelligence
- Enterprise
- GDPR
- Germany
website: https://kamium.de/
---
