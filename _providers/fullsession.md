---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/fullsession/llms/fullsession-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fullsession-llms.txt
- group: agent
  href: https://artifacts.apis.io/fullsession/well-known/fullsession-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fullsession-well-known.yml
- group: other
  href: https://artifacts.apis.io/fullsession/hosts/fullsession-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fullsession-hosts.yml
- group: other
  href: https://artifacts.apis.io/fullsession/vendors/fullsession-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fullsession-vendors.yml
- group: build
  href: https://artifacts.apis.io/fullsession/packages/fullsession-packages.yml
  title: ''
  type: SDKs
  url: packages/fullsession-packages.yml
- group: build
  href: https://artifacts.apis.io/fullsession/packages/fullsession-packages.yml
  title: ''
  type: Packages
  url: packages/fullsession-packages.yml
- group: auth
  href: https://artifacts.apis.io/fullsession/security/fullsession-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fullsession-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fullsession.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fullsession.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fullsession.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fullsession.io/api-developer-tools
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fullsession.io/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.fullsession.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fullsession.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fullsession.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fullsession.io/security-dpa
- group: operate
  title: ''
  type: Support
  url: https://www.fullsession.io/contact
coverage:
  checked: '2026-10-26'
  detail: Documentation is provided as HTML pages without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.fullsession.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: FullSession provides a comprehensive session replay and analytics platform that helps businesses understand user behavior across web and mobile applications. Leveraging AI-driven insights, FullSession captures detailed session data, heatmaps, funnel analysis, and real‑time feedback to improve conversion rates and product experience. The platform includes a managed cloud‑based MCP server, integrations with major tools, and robust security and compliance features for enterprise customers.
image: https://cdn.prod.website-files.com/6a574cc6f31722b01547fa25/6aceee0a938a23f2deb848cd_OG_Homepage.png
layout: provider
modified: '2026-10-26'
name: FullSession
nav: Providers
network: true
overview: 'FullSession is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Session Replay, AI, Web, and Mobile.


  FullSession''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fullsession Domain Security
  slug: fullsession-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fullsession
tags:
- Analytics
- Session Replay
- AI
- Web
- Mobile
website: https://fullsession.io/
---
