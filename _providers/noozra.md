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
api_count: 1
apis:
- description: Provides aggregated news articles across categories with free 100/day limit and Pro plan.
  name: Noozra News API
  slug: noozra-news-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://noozra.com/security-policy
- group: design
  href: https://artifacts.apis.io/noozra/conformance/noozra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/noozra-conformance.yml
- group: agent
  href: https://artifacts.apis.io/noozra/llms/noozra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noozra-llms.txt
- group: auth
  href: https://artifacts.apis.io/noozra/well-known/noozra-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/noozra-security.txt
- group: agent
  href: https://artifacts.apis.io/noozra/well-known/noozra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/noozra-well-known.yml
- group: other
  href: https://artifacts.apis.io/noozra/hosts/noozra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noozra-hosts.yml
- group: other
  href: https://artifacts.apis.io/noozra/vendors/noozra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/noozra-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://noozra.com/news
- group: start
  title: ''
  type: Login
  url: https://noozra.com/login
- group: auth
  href: https://artifacts.apis.io/noozra/security/noozra-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/noozra-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/noozra/security/noozra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noozra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noozra.com
- group: docs
  title: ''
  type: Documentation
  url: https://noozra.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://noozra.com/api
- group: company
  title: ''
  type: About
  url: https://noozra.com/about
- group: operate
  title: ''
  type: FAQ
  url: https://noozra.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noozra.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noozra.com/privacy
created: '2026-10-28'
description: Noozra provides a free News API that aggregates articles across categories such as politics, science, world, weather, finance, sports, entertainment, health, and AI. Users can retrieve up to 100 articles per day with a bearer token, and a Pro plan offers higher limits for $9 per month. Each article includes headline, summary, source, URL, and publication date, and links back to the original publisher. The platform also hosts community features like forums and games.
image: https://noozra.com/static/og-image.png
layout: provider
modified: '2026-10-28'
name: Noozra
nav: Providers
network: true
overview: 'Noozra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Free, Community, and Artificial Intelligence.


  Noozra''s developer surface includes documentation, API reference, FAQ, and 15 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 65.2
    operational_transparency: 5.3
  previous_composite: 20.7
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/noozra/noozra-2026-11-03T140257.png
security:
- kind: domain-security
  name: Noozra Domain Security
  slug: noozra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Noozra Vulnerability Disclosure
  slug: noozra-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: noozra
tags:
- News
- Free
- Community
- Artificial Intelligence
website: https://noozra.com
---
