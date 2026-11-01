---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Unified social media API platform providing conversations, configurations, and authentication endpoints.
  name: Outstand API
  slug: outstand-api
artifact_total: 6
asyncapis:
- description: ''
  name: Outstand So Webhooks
  slug: outstand-so-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/outstand-so/plans/outstand-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/outstand-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/outstand-so/asyncapi/outstand-so-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/outstand-so-webhooks.yml
- group: design
  href: https://artifacts.apis.io/outstand-so/conventions/outstand-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/outstand-so-conventions.yml
- group: auth
  href: https://artifacts.apis.io/outstand-so/security/outstand-so-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/outstand-so-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/outstand-so/authentication/outstand-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/outstand-so-authentication.yml
- group: agent
  href: https://artifacts.apis.io/outstand-so/llms/outstand-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/outstand-so-llms.txt
- group: auth
  href: https://artifacts.apis.io/outstand-so/well-known/outstand-so-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/outstand-so-security.txt
- group: auth
  href: https://artifacts.apis.io/outstand-so/well-known/outstand-so-outstand-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/outstand-so-outstand-security.txt
- group: auth
  href: https://artifacts.apis.io/outstand-so/well-known/outstand-so-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/outstand-so-api-security.txt
- group: agent
  href: https://artifacts.apis.io/outstand-so/well-known/outstand-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/outstand-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/outstand-so/hosts/outstand-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outstand-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/outstand-so/vendors/outstand-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outstand-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outstand.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outstand.so/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.outstand.so/pricing.md
- group: start
  title: ''
  type: Login
  url: https://www.outstand.so/app/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/outstand-so
- group: docs
  title: ''
  type: Documentation
  url: https://www.outstand.so/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.outstand.so/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.outstand.so/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.outstand.so/docs/conversations/getting-started
- group: auth
  href: https://artifacts.apis.io/outstand-so/security/outstand-so-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/outstand-so-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/outstand-so/security/outstand-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outstand-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.outstand.so/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are served as a JavaScript‑rendered Next.js app, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://www.outstand.so/docs/getting-started
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Outstand is a unified social media API platform that enables agencies and businesses to publish, schedule, and analyze posts across twelve major social networks through a single integration. It offers an MCP server for AI agents, tiered pricing plans, reselling permissions, and detailed analytics, with a focus on flexibility and extensibility for developers.
image: https://www.outstand.so/opengraph-image?a533065c406647b1
layout: provider
modified: '2026-10-30'
name: outstand-so
nav: Providers
network: true
overview: 'outstand-so is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media, API, MCP, and SaaS.


  The outstand-so catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  outstand-so''s developer surface includes authentication, pricing, documentation, changelog, engineering blog, getting-started guide, and 18 more developer resources.'
plans:
- name: Outstand So Plans Pricing
  plan_count: 2
  slug: outstand-so-plans-pricing
random_paper: 1
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.2
    catalog_earned_first_party: 0.0
    catalog_gap: 75.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 39.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Outstand So Authentication
  slug: outstand-so-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Outstand So Domain Security
  slug: outstand-so-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Outstand So Vulnerability Disclosure
  slug: outstand-so-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: outstand-so
tags:
- Company
- Social Media
- API
- MCP
- SaaS
website: https://www.outstand.so/
---
