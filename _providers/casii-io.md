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
    agent_skills: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Illustrated guides for connecting Casii remote MCP from various AI clients.
  name: Casii MCP API
  slug: casii-mcp-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/casii-io/plans/casii-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/casii-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/casii-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/casii-io/security/casii-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/casii-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/casii-io/well-known/casii-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/casii-io-security.txt
- group: agent
  href: https://artifacts.apis.io/casii-io/well-known/casii-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/casii-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/casii-io/hosts/casii-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/casii-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/casii-io/vendors/casii-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/casii-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://casii.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://casii.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://casii.io/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://casii.io/docs/mcp/
- group: auth
  href: https://artifacts.apis.io/casii-io/security/casii-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/casii-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/casii-io/security/casii-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casii-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://casii.io/
coverage:
  checked: '2026-11-04'
  detail: MCP documentation is rendered via JavaScript, no machine‑readable spec is available.
  evidence:
  - status: 200
    url: https://casii.io/docs/mcp/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Casii provides a sales‑enablement platform that helps teams find prospects, manage leads and run multilingual, multi‑account outreach from a single desktop workspace. It mines buyer data from Google Maps, automates WhatsApp outreach, translates messages and nurtures global customers, offering a comprehensive solution for worldwide sales prospecting and customer acquisition.
image: https://casii.io/og.png
layout: provider
modified: '2026-11-04'
name: Casii
nav: Providers
network: true
overview: 'Casii is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales, Lead Management, Multilingual, Outreach, and Prospecting.


  Casii''s developer surface includes pricing, documentation, and 12 more developer resources.'
plans:
- name: Casii Io Plans Pricing
  plan_count: 3
  slug: casii-io-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Casii Io Domain Security
  slug: casii-io-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Casii Io Vulnerability Disclosure
  slug: casii-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: casii-io
tags:
- Sales
- Lead Management
- Multilingual
- Outreach
- Prospecting
website: https://casii.io/
---
