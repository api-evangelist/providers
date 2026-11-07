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
  href: https://artifacts.apis.io/clausely-co-uk/plans/clausely-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clausely-co-uk-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/clausely-co-uk/llms/clausely-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clausely-co-uk-llms.txt
- group: other
  href: https://artifacts.apis.io/clausely-co-uk/hosts/clausely-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clausely-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/clausely-co-uk/vendors/clausely-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clausely-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/clausely-co-uk/security/clausely-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clausely-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clausely.co.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://clausely.co.uk/pricing
- group: company
  title: ''
  type: Blog
  url: https://clausely.co.uk/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clausely.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clausely.co.uk/privacy
coverage:
  detail: Provider offers pricing and documentation pages but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract was found.
  evidence:
  - status: 200
    url: https://clausely.co.uk/pricing
  - status: 404
    url: https://clausely.co.uk/openapi.json
  - status: 404
    url: https://clausely.co.uk/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Clausely provides UK compliance packs for SMEs, covering AI, GDPR, and workplace regulations. Their platform offers a range of ready‑made compliance packages, white‑label services, and a free risk check tool. Targeted at small and medium businesses, they aim to simplify adherence to the EU AI Act, the Worker Protection Act 2023, and UK GDPR without hiring a dedicated compliance team.
image: https://clausely.co.uk/og-image.png
layout: provider
modified: '2026-11-03'
name: Clausely
nav: Providers
network: true
overview: 'Clausely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Artificial Intelligence, GDPR, and Small Business.


  Clausely''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Clausely Co Uk Plans Pricing
  plan_count: 8
  slug: clausely-co-uk-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clausely Co Uk Domain Security
  slug: clausely-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clausely-co-uk
tags:
- Company
- Compliance
- Artificial Intelligence
- GDPR
- Small Business
website: https://clausely.co.uk/
---
