---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Flashalpha Agentic Access
  operation_count: 1
  slug: flashalpha-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Options Analytics API
  name: Flashalpha API
  slug: flashalpha-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/agentic-access/flashalpha-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flashalpha-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/plans/flashalpha-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flashalpha-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/rules/flashalpha-rules.yml
  title: ''
  type: Spectral
  url: rules/flashalpha-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/changelog/flashalpha-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flashalpha-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/authentication/flashalpha-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flashalpha-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/conformance/flashalpha-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flashalpha-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/llms/flashalpha-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flashalpha-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/well-known/flashalpha-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flashalpha-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/hosts/flashalpha-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flashalpha-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/vendors/flashalpha-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flashalpha-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/packages/flashalpha-packages.yml
  title: ''
  type: SDKs
  url: packages/flashalpha-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/packages/flashalpha-packages.yml
  title: ''
  type: Packages
  url: packages/flashalpha-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flashalpha.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flashalpha.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://flashalpha.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlashAlpha-lab
- group: operate
  title: ''
  type: ChangeLog
  url: https://flashalpha.com/docs/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flashalpha/refs/heads/main/security/flashalpha-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flashalpha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flashalpha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://flashalpha.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://flashalpha.com/docs/lab-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://flashalpha.com/docs/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://flashalpha.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://flashalpha.com/status
- group: company
  title: ''
  type: Blog
  url: https://flashalpha.com/articles/
created: '2026-10-16'
description: Flashalpha provides an Options Analytics API delivering real-time Greeks, exposure, and volatility surfaces for equities, ETFs, and CME futures. The platform offers REST endpoints and WebSocket streams, supporting over 1.8 million option contracts and multi‑Greek exposure calculations. It serves quantitative researchers, fund desks, and systematic traders worldwide, with free and paid tiers, detailed documentation, and interactive playgrounds for testing.
image: https://flashalpha.com/images/hero-image-2.jpg
layout: provider
modified: '2026-10-16'
name: Flashalpha
nav: Providers
network: true
overview: 'Flashalpha is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Options, and Analytics.


  The Flashalpha catalog on APIs.io includes 1 Spectral governance ruleset.


  Flashalpha''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 18 more developer resources.'
plans:
- name: Flashalpha Plans Pricing
  plan_count: 4
  slug: flashalpha-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 45
  extends:
  - spectral:oas
  name: Flashalpha API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 1
  slug: flashalpha-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Flashalpha Authentication
  slug: flashalpha-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Flashalpha Domain Security
  slug: flashalpha-domain-security
  summary_line: TLSv1.3
slug: flashalpha
tags:
- Company
- Finance
- Options
- Analytics
website: https://flashalpha.com/
---
