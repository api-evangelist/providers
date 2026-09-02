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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Suunto Cloud API (also called the Integration API) gives approved partners OAuth2-authorized access to a Suunto App user's workout and daily-activity data. Workouts are delivered as FIT files carr
  name: Suunto Cloud API
  slug: suunto-cloud-api
- description: The HAYLOU brand storefront exposes an agent-facing commerce surface over the Universal Commerce Protocol, reachable as a live MCP endpoint. Agents can search the catalog, build a cart, create and upd
  name: HAYLOU Commerce (UCP/MCP)
  slug: haylou-ucp
artifact_total: 7
asyncapis:
- description: ''
  name: Liesheng Suunto Webhooks
  slug: liesheng-suunto-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://liesheng.cc
- group: company
  title: ''
  type: About
  url: https://liesheng.cc/about.html
- group: other
  title: ''
  type: ProductCatalog
  url: https://liesheng.cc/product.html
- group: operate
  title: ''
  type: Support
  url: https://liesheng.cc/support.html
- group: operate
  title: ''
  type: Community
  url: https://liesheng.cc/forum.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liesheng.cc/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liesheng.cc/privacy.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apizone.suunto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apizone.suunto.com/how-to-start
- group: docs
  title: ''
  type: APIReference
  url: https://apizone.suunto.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://apizone.suunto.com/how-to-start
- group: start
  title: ''
  type: SignUp
  url: https://www.suunto.com/welcomepartners
- group: auth
  title: ''
  type: Authentication
  url: authentication/liesheng-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/liesheng-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/liesheng-suunto-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liesheng-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/liesheng-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liesheng-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liesheng-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liesheng-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/liesheng-suunto-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/liesheng-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liesheng-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liesheng-haylou-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liesheng-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liesheng-domain-security.yml
created: '2026-07-17'
description: Liesheng Group (猎声集团 / Liesheng Technology) is a Dongguan, Guangdong based consumer-electronics company founded on 25 May 2015 as one of Xiaomi's first ecosystem-chain suppliers. It operates as a global ODM/OEM solution provider — it engineered the Redmi AirDots true-wireless earbuds — while building its own brand portfolio, and reaches customers in more than 100 countries and regions. Liesheng launched the HAYLOU brand of wireless audio, smart wearables, bone- conduction headphones and microphones in 2017, and in 2022 acquired SUUNTO, the 85-year-old Finnish premium sports-watch and outdoor-instrument brand, in the same year it raised a B round led by Cathay Capital and a B+ round led by Amer Sports. Liesheng publishes no corporate API of its own; its developer surface is the Suunto Cloud API (Integration API), a partner-gated OAuth2 workout and daily-activity data API served through the Suunto API Zone.
image: https://liesheng.cc/phone/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Liesheng Group MCP Server
  slug: liesheng-group-mcp-server
modified: '2026-07-19'
name: Liesheng Group
nav: Providers
network: true
overview: 'Liesheng Group publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, Wearables, Audio, and Sports.


  The Liesheng Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Liesheng Group''s developer surface includes support, documentation, API reference, getting-started guide, signup flow, authentication, sandbox, and 19 more developer resources.'
random_paper: 7
scopes:
- name: Liesheng Scopes
  scope_count: 1
  slug: liesheng-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 45.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liesheng/refs/heads/main/screenshots/liesheng-2026-07-25T225031.png
security:
- kind: authentication
  name: Liesheng Authentication
  slug: liesheng-authentication
  summary_line: oauth2/apiKey/http · 3 schemes
- kind: domain-security
  name: Liesheng Domain Security
  slug: liesheng-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: liesheng
tags:
- Company
- Consumer Electronics
- Wearables
- Audio
- Sports
- Fitness
- Health
- Internet of Things
- ODM
- OEM
- China
website: https://liesheng.cc
---
