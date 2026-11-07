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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/amalgament-com/plans/amalgament-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amalgament-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/amalgament-com/llms/amalgament-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amalgament-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/amalgament-com/well-known/amalgament-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amalgament-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/amalgament-com/hosts/amalgament-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amalgament-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/amalgament-com/vendors/amalgament-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amalgament-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amalgament.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amalgament.com/privacy
- group: auth
  href: https://artifacts.apis.io/amalgament-com/security/amalgament-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amalgament-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amalgament.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://amalgament.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://amalgament.com/what-we-do
coverage:
  checked: '2026-11-01'
  detail: The provider's documentation pages are HTML only and contain no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://amalgament.com/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Amalgament provides on-demand technical teams for small businesses, offering integration, automation, internal tools, and practical AI solutions for a flat monthly fee. They learn business processes, identify improvement opportunities, and build and maintain technology solutions, positioning themselves as a cost-effective alternative to hiring full‑time engineering staff.
image: https://amalgament.com/share/og-home.jpg
layout: provider
modified: '2026-11-01'
name: Amalgament
nav: Providers
network: true
overview: 'Amalgament is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, TechnicalTeam, Automation, Small Business, and Artificial Intelligence.


  Amalgament''s developer surface includes pricing, getting-started guide, and 9 more developer resources.'
plans:
- name: Amalgament Com Plans Pricing
  plan_count: 1
  slug: amalgament-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amalgament Com Domain Security
  slug: amalgament-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amalgament-com
tags:
- Company
- TechnicalTeam
- Automation
- Small Business
- Artificial Intelligence
website: https://amalgament.com/
---
