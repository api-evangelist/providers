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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/787daily-com/security/787daily-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/787daily-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/787daily-com/llms/787daily-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/787daily-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/787daily-com/well-known/787daily-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/787daily-com-security.txt
- group: agent
  href: https://artifacts.apis.io/787daily-com/well-known/787daily-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/787daily-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/787daily-com/hosts/787daily-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/787daily-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/787daily-com/vendors/787daily-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/787daily-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://787daily.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://787daily.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://787daily.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://787daily.com/news/
- group: auth
  href: https://artifacts.apis.io/787daily-com/security/787daily-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/787daily-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/787daily-com/security/787daily-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/787daily-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://787daily.com/
coverage:
  checked: '2026-10-31'
  detail: No API contract or documentation found; the site provides news content only.
  evidence:
  - status: 404
    url: https://787daily.com/api
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: 787daily provides English-language news, guides, and real-time alerts about Puerto Rico, covering power outages, water rationing, weather, and local conditions. The site offers live updates, detailed town-by-town information, and resources for residents and visitors, aiming to keep the community informed and safe.
image: https://787daily.com/og-pinned.jpg
layout: provider
modified: '2026-10-31'
name: 787daily
nav: Providers
network: true
overview: '787daily is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include News, Puerto Rico, Alerts, Guides, and Community.


  787daily''s developer surface includes support and 12 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 10.5
  previous_composite: 12.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 787Daily Com Domain Security
  slug: 787daily-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 787Daily Com Vulnerability Disclosure
  slug: 787daily-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 787daily-com
tags:
- News
- Puerto Rico
- Alerts
- Guides
- Community
website: https://787daily.com/
---
