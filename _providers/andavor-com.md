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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/andavor-com/llms/andavor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/andavor-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/andavor-com/well-known/andavor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/andavor-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/andavor-com/hosts/andavor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andavor-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/andavor-com/vendors/andavor-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andavor-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/andavor-com/security/andavor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andavor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://andavor.com/
- group: company
  title: ''
  type: Blog
  url: https://andavor.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://andavor.com/precos
- group: operate
  title: ''
  type: Support
  url: https://andavor.com/contato
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/andavor
coverage:
  checked: '2026-11-01'
  detail: The site provides no developer portal or API documentation, and no public API endpoints were discovered.
  evidence:
  - status: 200
    url: https://andavor.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Andavor is an international AI platform offering its own trained AI for sales and a subscription app for sales and customer service management. The AI runs on infrastructure operated by Andavor, and conversation content is not sent to third‑party AI providers. It accesses real data before responding and follows rules defined by the company. Site available in Portuguese and English.
image: https://andavor.com/marca/favicon-512.png
layout: provider
modified: '2026-11-01'
name: Andavor
nav: Providers
network: true
overview: 'Andavor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sales, Customer Service, Software-as-a-Service, and Brazil.


  Andavor''s developer surface includes engineering blog, pricing, support, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 8.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Andavor Com Domain Security
  slug: andavor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andavor-com
tags:
- Artificial Intelligence
- Sales
- Customer Service
- Software-as-a-Service
- Brazil
website: https://andavor.com/
---
