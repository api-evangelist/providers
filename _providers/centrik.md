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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/centrik/llms/centrik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centrik-llms.txt
- group: other
  href: https://artifacts.apis.io/centrik/hosts/centrik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centrik-hosts.yml
- group: other
  href: https://artifacts.apis.io/centrik/vendors/centrik-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centrik-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustflight.com/terms-and-conditions/
- group: start
  title: ''
  type: SignUp
  url: https://reference.centrik.net/Login/RegisterMobilePhone.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustflight.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.trustflight.com/resource-type/newsroom/
- group: auth
  href: https://artifacts.apis.io/centrik/security/centrik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centrik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.centrik.net
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec is available.
  evidence:
  - status: 200
    url: https://reference.centrik.net/Login/Login.aspx?ReturnUrl=%2f
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Centrik provides the Centrik 5 Quality & Safety Management System, an integrated compliance, safety and risk management platform for aerospace operators, regulators and maintenance, repair and overhaul (MRO) organizations. The cloud‑based solution offers document control, dashboards, workflow automation, equipment tracking, training records and risk assessment tools. It is used by more than 200,000 active users in 120 countries.
image: https://www.trustflight.com/wp-content/uploads/2025/10/Yoast-Image.jpg
layout: provider
modified: '2026-11-03'
name: Centrik
nav: Providers
network: true
overview: 'Centrik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Quality Management, Safety Management, Risk Management, Compliance, and Aerospace.


  Centrik''s developer surface includes signup flow and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Centrik Domain Security
  slug: centrik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: centrik
tags:
- Quality Management
- Safety Management
- Risk Management
- Compliance
- Aerospace
- MRO
- Regulators
website: https://www.centrik.net
---
