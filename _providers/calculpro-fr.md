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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CalculPro offers a suite of calculation tools accessible via a web interface; no public machine‑readable API specification was found.
  name: CalculPro API
  slug: calculpro-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/calculpro-fr/plans/calculpro-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calculpro-fr-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/calculpro-fr/hosts/calculpro-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calculpro-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/calculpro-fr/vendors/calculpro-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calculpro-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/calculpro-fr/security/calculpro-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calculpro-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calculpro.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://calculpro.fr/outils
- group: commercial
  title: ''
  type: Pricing
  url: https://calculpro.fr/pricing
- group: start
  title: ''
  type: SignUp
  url: https://calculpro.fr/register?redirect=/
- group: start
  title: ''
  type: Login
  url: https://calculpro.fr/login?redirect=/
coverage:
  checked: '2026-11-03'
  detail: No public OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were discovered despite documentation pages.
  evidence:
  - status: 200
    url: https://calculpro.fr/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CalculPro provides professional online calculation tools for the building industry, offering over 120 calculators covering heating, plumbing, ventilation, electricity, structure, and more. The platform follows French DTU, NF, and Eurocode standards, delivering detailed formulas, references, and calculation notes to help architects, engineers, and tradespeople justify designs and generate client proposals.
layout: provider
modified: '2026-11-03'
name: CalculPro
nav: Providers
network: true
overview: 'CalculPro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Engineering, Calculators, BuildingTools, and FrenchStandards.


  CalculPro''s developer surface includes documentation, pricing, signup flow, and 6 more developer resources.'
plans:
- name: Calculpro Fr Plans Pricing
  plan_count: 2
  slug: calculpro-fr-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calculpro Fr Domain Security
  slug: calculpro-fr-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: calculpro-fr
tags:
- Construction
- Engineering
- Calculators
- BuildingTools
- FrenchStandards
website: https://calculpro.fr/
---
