---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Electronic invoicing API for Ecuador SRI, providing async issuance of vouchers, catalogs, organization and operation endpoints.
  name: Contadeo API
  slug: contadeo-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/contadeo-com/plans/contadeo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contadeo-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://contadeo.com/seguridad
- group: design
  href: https://artifacts.apis.io/contadeo-com/conformance/contadeo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contadeo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contadeo-com/llms/contadeo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contadeo-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/contadeo-com/well-known/contadeo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contadeo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/contadeo-com/well-known/contadeo-com-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contadeo-com-portal-security.txt
- group: auth
  href: https://artifacts.apis.io/contadeo-com/well-known/contadeo-com-dash-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contadeo-com-dash-security.txt
- group: agent
  href: https://artifacts.apis.io/contadeo-com/well-known/contadeo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contadeo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/contadeo-com/hosts/contadeo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contadeo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/contadeo-com/vendors/contadeo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contadeo-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://contadeo.com/login
- group: company
  title: ''
  type: Blog
  url: https://contadeo.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://portal.contadeo.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/contadeo-com/security/contadeo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contadeo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contadeo-com/security/contadeo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contadeo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contadeo.com/
created: '2026-11-04'
description: Contadeo provides electronic invoicing solutions authorized by the Ecuadorian SRI, offering free plans up to 10 invoices per month and paid tiers for higher volume. The platform enables rapid invoice generation, compliance with the latest 2026 regulations, and integrates with accounting tools. It targets small to medium businesses in Ecuador seeking streamlined, cloud‑based billing without credit‑card requirements.
image: https://contadeo.com/img/og-social-v2.jpg
layout: provider
modified: '2026-11-04'
name: Contadeo
nav: Providers
network: true
overview: 'Contadeo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Invoicing, Ecuador, SRI, Fintech, and Small Business.


  Contadeo''s developer surface includes engineering blog, API reference, and 14 more developer resources.'
plans:
- name: Contadeo Com Plans Pricing
  plan_count: 4
  slug: contadeo-com-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contadeo Com Domain Security
  slug: contadeo-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Contadeo Com Vulnerability Disclosure
  slug: contadeo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: contadeo-com
tags:
- Invoicing
- Ecuador
- SRI
- Fintech
- Small Business
- Company
website: https://contadeo.com/
---
