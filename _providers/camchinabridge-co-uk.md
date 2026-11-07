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
  band: agent-aware
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
    mcp_server: documented
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Cambridge China Bridge services, documented at the Guides page.
  name: Cambridge China Bridge API
  slug: cambridge-china-bridge-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/camchinabridge-co-uk/plans/camchinabridge-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/camchinabridge-co-uk-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/camchinabridge-co-uk/llms/camchinabridge-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/camchinabridge-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/camchinabridge-co-uk/well-known/camchinabridge-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/camchinabridge-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/camchinabridge-co-uk/hosts/camchinabridge-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/camchinabridge-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/camchinabridge-co-uk/vendors/camchinabridge-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/camchinabridge-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://camchinabridge.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://camchinabridge.co.uk/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://camchinabridge.co.uk/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://camchinabridge.co.uk/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://camchinabridge.co.uk/tools/supplier-onboarding-checklist/
- group: auth
  href: https://artifacts.apis.io/camchinabridge-co-uk/security/camchinabridge-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/camchinabridge-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://camchinabridge.co.uk/
coverage:
  checked: '2026-11-04'
  detail: Provider documentation pages exist but no machine‑readable API contract was found.
  evidence:
  - status: 200
    url: https://camchinabridge.co.uk/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cambridge China Bridge is a UK‑based sourcing and supply management company that operates a dedicated team in China to help buyers worldwide find factories, conduct quality checks and coordinate shipping. Established in 2022, it serves clients across Europe, the Middle East and beyond, offering end‑to‑end procurement services and acting as the importer for buyer shipments.
image: https://camchinabridge.co.uk/og-default.jpg
layout: provider
modified: '2026-11-04'
name: Cambridge China Bridge
nav: Providers
network: true
overview: 'Cambridge China Bridge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sourcing, Supply Chain, China, and Procurement.


  Cambridge China Bridge''s developer surface includes pricing, documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Camchinabridge Co Uk Plans Pricing
  plan_count: 3
  slug: camchinabridge-co-uk-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Camchinabridge Co Uk Domain Security
  slug: camchinabridge-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: camchinabridge-co-uk
tags:
- Company
- Sourcing
- Supply Chain
- China
- Procurement
website: https://camchinabridge.co.uk/
---
