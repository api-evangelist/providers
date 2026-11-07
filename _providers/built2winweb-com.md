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
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
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
  score: 20.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public agent-facing endpoints for built2winweb.com. All read endpoints are anonymous; OAuth optional.
  name: BuiltToWinWeb Agent API
  slug: builttowinweb-agent-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/built2winweb-com/plans/built2winweb-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/built2winweb-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://built2winweb.com/privacy
- group: design
  href: https://artifacts.apis.io/built2winweb-com/conformance/built2winweb-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/built2winweb-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/built2winweb-com/well-known/built2winweb-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/built2winweb-com-security.txt
- group: agent
  href: https://artifacts.apis.io/built2winweb-com/well-known/built2winweb-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/built2winweb-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/built2winweb-com/hosts/built2winweb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/built2winweb-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/built2winweb-com/vendors/built2winweb-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/built2winweb-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://built2winweb.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://freeaiboost.built2winweb.com/signup.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://built2winweb.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://built2winweb.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://built2winweb.com/news/
- group: company
  title: ''
  type: Blog
  url: https://built2winweb.com/blog/
- group: auth
  href: https://artifacts.apis.io/built2winweb-com/security/built2winweb-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/built2winweb-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/built2winweb-com/security/built2winweb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/built2winweb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://built2winweb.com/
created: '2026-11-03'
description: BuiltToWinWeb creates custom hand‑coded PHP websites for U.S. small businesses, offering flat‑fee projects with no monthly costs. Their services include SEO‑optimized landing pages in multiple languages, AI‑powered web building tools, and a suite of AI software such as AIWebBuilding and WebAgentScan. Founded by Jacob Campbell, the company emphasizes high performance, achieving Lighthouse scores of 96‑100, and provides full code ownership to clients.
image: https://built2winweb.com/designer.webp
layout: provider
modified: '2026-11-03'
name: BuiltToWinWeb
nav: Providers
network: true
overview: 'BuiltToWinWeb is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web Development, AI Tools, Small Business, SEO, and PHP.


  BuiltToWinWeb''s developer surface includes signup flow, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Built2Winweb Com Plans Pricing
  plan_count: 9
  slug: built2winweb-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 67.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Built2Winweb Com Domain Security
  slug: built2winweb-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Built2Winweb Com Vulnerability Disclosure
  slug: built2winweb-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: built2winweb-com
tags:
- Web Development
- AI Tools
- Small Business
- SEO
- PHP
website: https://built2winweb.com/
---
