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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/goalieip-com/plans/goalieip-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goalieip-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/goalieip-com/security/goalieip-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/goalieip-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/goalieip-com/llms/goalieip-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goalieip-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/goalieip-com/well-known/goalieip-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goalieip-com-security.txt
- group: auth
  href: https://artifacts.apis.io/goalieip-com/well-known/goalieip-com-goalieip-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goalieip-com-goalieip-security.txt
- group: agent
  href: https://artifacts.apis.io/goalieip-com/well-known/goalieip-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/goalieip-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/goalieip-com/hosts/goalieip-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goalieip-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/goalieip-com/vendors/goalieip-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goalieip-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goalieip.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goalieip.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://www.goalieip.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.goalieip.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.goalieip.com/blog
- group: auth
  href: https://artifacts.apis.io/goalieip-com/security/goalieip-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/goalieip-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/goalieip-com/security/goalieip-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goalieip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goalieip.com/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via Next.js JavaScript, providing no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.goalieip.com/trademark-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Goalie IP provides intellectual property monitoring and enforcement services, built by registered patent attorneys. It offers continuous US trademark, copyright, and patent monitoring, reporting, and a developer API over USPTO trademark data, enabling AI assistants to search federal trademark records via a robust API and MCP.
image: https://www.goalieip.com/opengraph-image?b0a71330059ea528
layout: provider
modified: '2026-10-30'
name: goalieip-com
nav: Providers
network: true
overview: 'goalieip-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Intellectual Property, Trademarks, and Monitoring.


  goalieip-com''s developer surface includes documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Goalieip Com Plans Pricing
  plan_count: 2
  slug: goalieip-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 39.3
    operational_transparency: 10.5
  previous_composite: 21.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/goalieip-com/goalieip-com-2026-11-03T132902.png
security:
- kind: domain-security
  name: Goalieip Com Domain Security
  slug: goalieip-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Goalieip Com Vulnerability Disclosure
  slug: goalieip-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: goalieip-com
tags:
- Company
- Intellectual Property
- Trademarks
- Monitoring
website: https://www.goalieip.com/
---
