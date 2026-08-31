---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-30'
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
- group: auth
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
  title: ''
  type: Packages
  url: packages/poynt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/poynt-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/poynt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/poynt-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/poynt-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/poynt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/poynt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/poynt-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/poynt-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/poynt-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/poynt-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poynt-llms.txt
created: '2026-07-17'
description: 'Poynt (GoDaddy Poynt) is an open commerce platform for merchants built around smart payment terminals and a cloud API. Its Poynt Cloud API (services.poynt.net) lets developers build and distribute business apps that read and write orders, transactions, customers, products, catalogs, inventory, taxes and businesses, register webhooks for real-time events, and tokenize card data in the browser with Poynt Collect. Authentication is OAuth 2.0 using a self-signed JWT bearer grant that is exchanged for a short-lived access token. The platform serves three integration audiences: payment processors, terminal OEMs, and independent app developers.'
image: https://poynt.com/wp-content/uploads/2021/09/poynt-logo.png
layout: provider
modified: '2026-07-20'
name: Poynt
nav: Providers
network: true
overview: 'Poynt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Payments, Point-of-Sale, and Commerce.


  The Poynt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Poynt''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 17 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 37.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
