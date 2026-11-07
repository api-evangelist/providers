---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
- description: Provides GDPR compliance scanning functionality as described on the website.
  name: DSGVO.pro API
  slug: dsgvo-pro-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dsgvo-pro/plans/dsgvo-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dsgvo-pro-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/dsgvo-pro/security/dsgvo-pro-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dsgvo-pro-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dsgvo-pro/llms/dsgvo-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dsgvo-pro-llms.txt
- group: auth
  href: https://artifacts.apis.io/dsgvo-pro/well-known/dsgvo-pro-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dsgvo-pro-security.txt
- group: agent
  href: https://artifacts.apis.io/dsgvo-pro/well-known/dsgvo-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dsgvo-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/dsgvo-pro/hosts/dsgvo-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dsgvo-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/dsgvo-pro/vendors/dsgvo-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dsgvo-pro-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://dsgvo.pro/pricing
- group: start
  title: ''
  type: Login
  url: https://dsgvo.pro/login
- group: company
  title: ''
  type: Blog
  url: https://dsgvo.pro/blog
- group: auth
  href: https://artifacts.apis.io/dsgvo-pro/security/dsgvo-pro-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dsgvo-pro-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dsgvo-pro/security/dsgvo-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dsgvo-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dsgvo.pro/
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite API reference pages.
  evidence:
  - status: 404
    url: https://dsgvo.pro/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: DSGVO.pro offers a free compliance scanner for German websites, checking up to 33 GDPR‑related modules such as DSGVO, TDDDG, KI‑VO, BFSG and BGB. The tool runs in about 60 seconds without registration, generating cookie‑banners and compliance reports. It aims to help site owners avoid fines by providing automated privacy audits and detailed legal references.
image: https://dsgvo.pro/images/og-cover.jpg
layout: provider
modified: '2026-11-06'
name: DSGVO.pro
nav: Providers
network: true
overview: 'DSGVO.pro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GDPR, Compliance, Privacy, and German.


  DSGVO.pro''s developer surface includes pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Dsgvo Pro Plans Pricing
  plan_count: 6
  slug: dsgvo-pro-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dsgvo Pro Domain Security
  slug: dsgvo-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dsgvo Pro Vulnerability Disclosure
  slug: dsgvo-pro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dsgvo-pro
tags:
- Company
- GDPR
- Compliance
- Privacy
- German
website: https://dsgvo.pro/
---
