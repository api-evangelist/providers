---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Zinc lets you search, buy, and return items from top online retailers via a single API.
  name: Zinc API
  slug: zinc-api
artifact_total: 4
asyncapis:
- description: ''
  name: Zinc Com Webhooks
  slug: zinc-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/zinc-com/asyncapi/zinc-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/zinc-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/zinc-com/changelog/zinc-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zinc-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/zinc-com/conventions/zinc-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/zinc-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/zinc-com/conventions/zinc-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zinc-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/zinc-com/authentication/zinc-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zinc-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/zinc-com/conformance/zinc-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zinc-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zinc-com/llms/zinc-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zinc-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/zinc-com/well-known/zinc-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zinc-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/zinc-com/hosts/zinc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zinc-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/zinc-com/vendors/zinc-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zinc-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/zinc-com/packages/zinc-com-packages.yml
  title: ''
  type: SDKs
  url: packages/zinc-com-packages.yml
- group: build
  href: https://artifacts.apis.io/zinc-com/packages/zinc-com-packages.yml
  title: ''
  type: Packages
  url: packages/zinc-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://app.zinc.com/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zinc.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://www.zinc.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zinc.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zinc.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zincio
- group: docs
  title: ''
  type: Documentation
  url: https://www.zinc.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.zinc.com/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.zinc.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.zinc.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://www.zinc.com/developers
- group: auth
  href: https://artifacts.apis.io/zinc-com/security/zinc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zinc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://zinc.com
created: '2026-10-24'
description: Zinc provides an API that enables developers, agents, and businesses to search, purchase, track, and return products across thousands of online retailers in a single integration. The service supports automated procurement, gift messaging, and returns, and operates with a prefunded Zinc Wallet for payment.
image: https://www.zinc.com/opengraph-image?9566a34c69128f2e
layout: provider
modified: '2026-10-24'
name: Zinc
nav: Providers
network: true
overview: 'Zinc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E‑commerce API, Product Search, Order Automation, Retail Integration, and Procurement.


  The Zinc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zinc''s developer surface includes changelog, authentication, pricing, documentation, engineering blog, getting-started guide, API reference, and 18 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 34.5
    discoverability: 73.2
    operational_transparency: 22.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zinc-com/zinc-com-2026-11-03T150530.png
security:
- kind: authentication
  name: Zinc Com Authentication
  slug: zinc-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zinc Com Domain Security
  slug: zinc-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zinc-com
tags:
- E‑commerce API
- Product Search
- Order Automation
- Retail Integration
- Procurement
website: http://zinc.com
---
