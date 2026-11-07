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
  href: https://artifacts.apis.io/auroraconcierge-com-br/llms/auroraconcierge-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auroraconcierge-com-br-llms.txt
- group: other
  href: https://artifacts.apis.io/auroraconcierge-com-br/hosts/auroraconcierge-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auroraconcierge-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/auroraconcierge-com-br/vendors/auroraconcierge-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auroraconcierge-com-br-vendors.yml
- group: auth
  href: https://artifacts.apis.io/auroraconcierge-com-br/security/auroraconcierge-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auroraconcierge-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auroraconcierge.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auroraconcierge.com.br/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.auroraconcierge.com.br/precos
- group: company
  title: ''
  type: Blog
  url: https://www.auroraconcierge.com.br/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auroraconcierge.com.br/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auroraconcierge.com.br/privacidade
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.com.br/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Aurora Concierge provides specialized home care services in São Paulo, offering personalized nursing, technical, and caregiver support. Clients receive tailored care plans with nursing supervision, flexible scheduling, and transparent pricing. The service includes virtual assistance via the Aura chatbot, detailed proposals sent by email, and digital contracts. Aurora aims to ensure dignified, high-quality care for loved ones at home.
image: https://www.auroraconcierge.com.br/images/og-image.jpg
layout: provider
modified: '2026-11-02'
name: Aurora Concierge
nav: Providers
network: true
overview: 'Aurora Concierge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Home Care, Healthcare, Brazil, Nursing, and Concierge.


  Aurora Concierge''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 13.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auroraconcierge Com Br Domain Security
  slug: auroraconcierge-com-br-domain-security
  summary_line: TLSv1.3
slug: auroraconcierge-com-br
tags:
- Home Care
- Healthcare
- Brazil
- Nursing
- Concierge
- Company
website: https://auroraconcierge.com.br/
---
