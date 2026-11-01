---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/tubebuddy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/tubebuddy/security/tubebuddy-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tubebuddy-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/tubebuddy/llms/tubebuddy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tubebuddy-llms.txt
- group: auth
  href: https://artifacts.apis.io/tubebuddy/well-known/tubebuddy-tubebuddy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tubebuddy-tubebuddy-security.txt
- group: auth
  href: https://artifacts.apis.io/tubebuddy/well-known/tubebuddy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tubebuddy-security.txt
- group: agent
  href: https://artifacts.apis.io/tubebuddy/well-known/tubebuddy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tubebuddy-well-known.yml
- group: other
  href: https://artifacts.apis.io/tubebuddy/hosts/tubebuddy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tubebuddy-hosts.yml
- group: other
  href: https://artifacts.apis.io/tubebuddy/vendors/tubebuddy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tubebuddy-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tubebuddy/security/tubebuddy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tubebuddy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tubebuddy/security/tubebuddy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tubebuddy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tubebuddy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.tubebuddy.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tubebuddy.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.tubebuddy.com/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://mcp.tubebuddy.com/openapi.json
  - status: 401
    url: https://mcp.tubebuddy.com/mcp
  - status: 401
    url: https://support.tubebuddy.com/mcp
  - status: 301
    url: https://tubebuddy.com/
  reason: partner-login
  state: gated
created: '2026-10-27'
description: TubeBuddy provides a suite of tools that help YouTube creators grow their channels, optimize video SEO, and manage content. The platform offers keyword research, thumbnail generation, bulk editing, analytics, and monetization calculators, all accessible through a browser extension and web dashboard. It serves creators of all sizes, from newcomers to established channels, aiming to increase visibility, subscriber growth, and revenue on YouTube.
layout: provider
modified: '2026-10-27'
name: TubeBuddy
nav: Providers
network: true
overview: 'TubeBuddy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, YouTube, SEO, VideoTools, and CreatorGrowth.


  TubeBuddy''s developer surface includes documentation, pricing, engineering blog, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tubebuddy Domain Security
  slug: tubebuddy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tubebuddy Vulnerability Disclosure
  slug: tubebuddy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tubebuddy
tags:
- Company
- YouTube
- SEO
- VideoTools
- CreatorGrowth
website: https://tubebuddy.com/
---
