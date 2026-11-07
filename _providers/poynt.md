---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The Poynt Cloud API lets developers manage a merchant business''s orders, transactions, customers, products, catalogs, inventory and taxes, register webhooks for real-time events, and collect/tokenize '
  name: Poynt Cloud API
  slug: poynt-cloud-api
artifact_total: 4
asyncapis:
- description: ''
  name: Poynt Webhooks
  slug: poynt-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://www.poynt.com/press
- group: auth
  href: https://artifacts.apis.io/poynt/security/poynt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/poynt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.poynt.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.poynt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.poynt.com/app-integration/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.poynt.com/api-reference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.poynt.com/app-integration/
- group: operate
  title: ''
  type: Support
  url: https://support.poynt.com
- group: operate
  title: ''
  type: Support
  url: https://discuss.poynt.net
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/poynt
- group: operate
  title: ''
  type: StatusPage
  url: https://poynt.statuspage.io
- group: build
  href: https://artifacts.apis.io/poynt/packages/poynt-packages.yml
  title: ''
  type: Packages
  url: packages/poynt-packages.yml
- group: build
  href: https://artifacts.apis.io/poynt/packages/poynt-packages.yml
  title: ''
  type: SDKs
  url: packages/poynt-packages.yml
- group: auth
  href: https://artifacts.apis.io/poynt/authentication/poynt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/poynt-authentication.yml
- group: design
  href: https://artifacts.apis.io/poynt/conventions/poynt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/poynt-conventions.yml
- group: design
  href: https://artifacts.apis.io/poynt/conventions/poynt-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/poynt-conventions.yml
- group: design
  href: https://artifacts.apis.io/poynt/conformance/poynt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/poynt-conformance.yml
- group: design
  href: https://artifacts.apis.io/poynt/errors/poynt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/poynt-problem-types.yml
- group: design
  href: https://artifacts.apis.io/poynt/lifecycle/poynt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/poynt-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/poynt/asyncapi/poynt-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/poynt-webhooks.yml
- group: design
  href: https://artifacts.apis.io/poynt/data-model/poynt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/poynt-data-model.yml
- group: design
  href: https://artifacts.apis.io/poynt/components/poynt-components.yml
  title: ''
  type: Components
  url: components/poynt-components.yml
- group: agent
  href: https://artifacts.apis.io/poynt/llms/poynt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/poynt-llms.txt
created: '2026-07-17'
description: 'Poynt (GoDaddy Poynt) is an open commerce platform for merchants built around smart payment terminals and a cloud API. Its Poynt Cloud API (services.poynt.net) lets developers build and distribute business apps that read and write orders, transactions, customers, products, catalogs, inventory, taxes and businesses, register webhooks for real-time events, and tokenize card data in the browser with Poynt Collect. Authentication is OAuth 2.0 using a self-signed JWT bearer grant that is exchanged for a short-lived access token. The platform serves three integration audiences: payment processors, terminal OEMs, and independent app developers.'
image: https://poynt.com/wp-content/uploads/2021/09/poynt-logo.png
layout: provider
modified: '2026-10-06'
name: Poynt
nav: Providers
network: true
overview: 'Poynt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Payments, Point-of-Sale, and Commerce.


  The Poynt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Poynt''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, authentication, and 17 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 36.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/poynt/poynt-2026-09-02T151849.png
security:
- kind: authentication
  name: Poynt Authentication
  slug: poynt-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Poynt Domain Security
  slug: poynt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: poynt
tags:
- Company
- Consumer
- Payments
- Point-of-Sale
- Commerce
- Merchant Services
- Payment Processing
- Developer Platform
website: https://www.poynt.com
---
