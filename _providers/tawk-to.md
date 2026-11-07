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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer portal for Tawk.to offering JavaScript API integration and documentation.
  name: Tawk.to Developer API
  slug: tawk-to-developer-api
artifact_total: 3
asyncapis:
- description: ''
  name: Tawk To Webhooks
  slug: tawk-to-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/tawk-to/well-known/tawk-to-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tawk-to-status-security.txt
- group: design
  href: https://artifacts.apis.io/tawk-to/asyncapi/tawk-to-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tawk-to-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/tawk-to/llms/tawk-to-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tawk-to-llms.txt
- group: agent
  href: https://artifacts.apis.io/tawk-to/well-known/tawk-to-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tawk-to-well-known.yml
- group: other
  href: https://artifacts.apis.io/tawk-to/hosts/tawk-to-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tawk-to-hosts.yml
- group: other
  href: https://artifacts.apis.io/tawk-to/vendors/tawk-to-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tawk-to-vendors.yml
- group: build
  href: https://artifacts.apis.io/tawk-to/packages/tawk-to-packages.yml
  title: ''
  type: SDKs
  url: packages/tawk-to-packages.yml
- group: build
  href: https://artifacts.apis.io/tawk-to/packages/tawk-to-packages.yml
  title: ''
  type: Packages
  url: packages/tawk-to-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tawk.to/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: http://status.tawk.to
- group: auth
  title: ''
  type: Security
  url: https://www.tawk.to/security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tawk.to
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tawk
- group: auth
  href: https://artifacts.apis.io/tawk-to/security/tawk-to-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tawk-to-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tawk.to/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tawk.to/resources/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tawk.to/
- group: start
  title: ''
  type: GettingStarted
  url: https://dashboard.tawk.to/signup
- group: company
  title: ''
  type: Blog
  url: https://www.tawk.to/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tawk.to/why-free/
- group: operate
  title: ''
  type: Support
  url: https://help.tawk.to/
coverage:
  checked: '2026-10-27'
  detail: Developer portal loads content via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.tawk.to/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Tawk.to provides a free live chat software platform that enables businesses to communicate with website visitors in real time. It offers a suite of products including live chat, inbox, chat pages, knowledge base, CRM, pipeline automation, and various add‑ons. Millions of companies use tawk.to to deliver customer support, capture leads, and integrate chat into their tech stack via JavaScript APIs, webhooks, and Zapier integrations. The service is free‑forever with optional paid add‑ons, and it emphasizes ease of use, multilingual support, and extensive documentation for developers.
image: https://www.tawk.to/share-card.png
layout: provider
modified: '2026-10-27'
name: Tawk.to
nav: Providers
network: true
overview: 'Tawk.to is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Live Chat, Customer Service, FreeSoftware, and Developer Tools.


  The Tawk.to catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tawk.to''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, and 15 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tawk-to/tawk-to-2026-11-03T144329.png
security:
- kind: domain-security
  name: Tawk To Domain Security
  slug: tawk-to-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tawk-to
tags:
- Company
- Live Chat
- Customer Service
- FreeSoftware
- Developer Tools
website: https://tawk.to/
---
