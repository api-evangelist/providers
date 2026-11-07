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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ICV Workflow Guides | Auditro Documentation
  name: Auditro API
  slug: auditro-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/auditro-co/llms/auditro-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auditro-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/auditro-co/well-known/auditro-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auditro-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/auditro-co/hosts/auditro-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auditro-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/auditro-co/vendors/auditro-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auditro-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/auditro-co/security/auditro-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auditro-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auditro.co/
- group: docs
  title: ''
  type: Documentation
  url: https://auditro.co/docs/
- group: start
  title: ''
  type: Login
  url: https://app.auditro.co/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auditro.co/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://app.auditro.co/suppliers/register
- group: operate
  title: ''
  type: Support
  url: https://auditro.co/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auditro.co/terms/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are JavaScript‑rendered and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://auditro.co/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Auditro provides ICV and Emiratisation planning software for UAE companies, helping finance, HR, and procurement teams understand how Emirati hires and supplier spend affect MoHRE quota and In‑Country Value scores. The platform offers forecasting, compliance tracking, and evidence management for multi‑entity groups across Abu Dhabi, Dubai, and the wider UAE market.
image: https://auditro.co/socials/auditro-og.png
layout: provider
modified: '2026-11-02'
name: Auditro
nav: Providers
network: true
overview: 'Auditro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ICV, Emiratisation, Procurement, Finance, and Human Resources.


  Auditro''s developer surface includes documentation, signup flow, support, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 15.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auditro Co Domain Security
  slug: auditro-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: auditro-co
tags:
- ICV
- Emiratisation
- Procurement
- Finance
- Human Resources
- United Arab Emirates
- Score Planning
website: https://auditro.co/
---
