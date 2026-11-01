---
agent_readiness:
  band: agent-ready
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/easyweek-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/easyweek-io/conventions/easyweek-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/easyweek-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/easyweek-io/authentication/easyweek-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/easyweek-io-authentication.yml
- group: agent
  href: https://artifacts.apis.io/easyweek-io/llms/easyweek-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easyweek-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/easyweek-io/well-known/easyweek-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easyweek-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/easyweek-io/hosts/easyweek-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easyweek-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/easyweek-io/vendors/easyweek-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easyweek-io-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://easyweek.io/business/features/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easyweek.io/business/terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://security-investment.easyweek.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://easyweek.io/business/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.easyweek.io
- group: docs
  title: ''
  type: APIReference
  url: https://developers.easyweek.io/docs/api-reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.easyweek.io/docs/getting-started/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.easyweek.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/easyweek
- group: auth
  href: https://artifacts.apis.io/easyweek-io/security/easyweek-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easyweek-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easyweek.io/
- group: company
  title: ''
  type: Blog
  url: https://easyweek.io/business/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://easyweek.io/business/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.easyweek.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.easyweek.io/
coverage:
  checked: '2026-10-30'
  detail: Docs site returns JavaScript-rendered pages preventing machine reading.
  evidence:
  - status: 200
    url: https://docs.easyweek.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: EasyWeek is an online marketplace that lets consumers book a wide range of services such as beauty, health, automotive, and home services. Users can browse categories, select providers, schedule appointments, and manage bookings through a web portal and mobile app. The platform supports multiple cities across the United States and offers a seamless experience for both customers and service businesses.
image: https://imprx.easyweek.io/_/rs:fill:1200:630:1:0/gravity:sm/dpr:1/q:80/aHR0cHM6Ly91c2Vyc3RhdGljLmNvbS9mLzYxZTMxOGE4LWZkYmQtNGNiMy04YmM3LTZjOTFmN2U2YjUzYi5wbmc.jpg
layout: provider
modified: '2026-10-30'
name: easyweek-io
nav: Providers
network: true
overview: 'easyweek-io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Booking, Services, US, and Consumer.


  easyweek-io''s developer surface includes authentication, API reference, getting-started guide, documentation, engineering blog, pricing, support, and 15 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 63.6
    discoverability: 50.0
    operational_transparency: 28.9
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Easyweek Io Authentication
  slug: easyweek-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Easyweek Io Domain Security
  slug: easyweek-io-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: easyweek-io
tags:
- Marketplace
- Booking
- Services
- US
- Consumer
website: https://easyweek.io/
---
