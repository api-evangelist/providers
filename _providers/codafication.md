---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Unity Cloud (Unity Platform) developer surface, documented publicly at docs.unitycloud.io as the Unity Platform SDK reference. A single GraphQL endpoint collates the schemas of every installed ext
  name: Unity Platform API
  slug: unity-platform-api
artifact_total: 4
asyncapis:
- description: ''
  name: Codafication Unity Webhooks
  slug: codafication-unity-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://codafication.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unitycloud.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unitycloud.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unitycloud.io/#prerequisites-setup
- group: company
  title: ''
  type: Blog
  url: https://blog.codafication.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.codafication.com/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://support.codafication.com/en/
- group: operate
  title: ''
  type: SupportKnowledgeBase
  url: https://support.codafication.com/en/
- group: operate
  title: ''
  type: Contact
  url: https://codafication.com/get-in-touch/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codafication.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codafication.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Codafication
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codafication/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/codafication-unity-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codafication-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codafication-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/codafication-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/codafication-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/codafication-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/codafication-cli.yml
- group: design
  title: ''
  type: Components
  url: components/codafication-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/codafication-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codafication-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://blog.codafication.com/codafication-secures-soc-2-type-ii-certification
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codafication-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codafication-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codafication-domain-security.yml
created: '2026-07-25'
description: 'Codafication is a Brisbane, Australia insurtech founded in 2015 by Daniel Sandaver and Drew Butler out of a property claims and repair construction business, building software for the general insurance claims supply chain rather than for underwriting or policy administration. Its three products are Crunchwork, a cloud claims and project management platform that acts as a control tower across insurers, assessors, builders, restorers and trades (tasks and workflow, report writer, quotes and variations, catalog, asset manager, purchase orders, invoices, finance, analytics, vendor manager, zones, tenants and teams, and Pulse); Virtual Assist, a real-time video streaming and virtual assessment tool used for remote triage of property claims; and Unity Cloud, the GraphQL data, extension and integration platform the other two products are built on. Unity Cloud does publish a public developer reference at docs.unitycloud.io - the Unity Platform SDK documentation - covering the Portal
  SDK (React), the Node.js Unity SDK, the GraphQL client, setQueries and setMutations, GraphQL links and type extensions, public and private REST endpoints served under a tenant Cloud domain, GraphQL-payload webhooks, before/after logic hooks, and the Twilio, SendGrid and Bitly platform services. Authentication is Auth0-backed (SAML 2.0 and Active Directory connections) with tenant-scoped role-based access control, plus Unity API tokens issued from the in-product Developer Portal and pre-shared extension secrets. What is missing is the self-serve layer: no OpenAPI or AsyncAPI definition, no public GraphQL introspection endpoint, no Postman collection, no public npm distribution of the SDKs, no status page and no self-serve signup - access runs through named enterprise engagements. Customers and partners include Insurance Australia Group (IAG, announced December 2025), Suncorp, Urban Utilities and the Australian Building and Construction Group, alongside a Guidewire partnership and SOC 2
  Type II certification attained in January 2026. Australia has no live open-insurance obligation - the Consumer Data Right was designated to extend to general insurance and then deferred - so nothing forces this platform to open further than it already has.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Codafication
nav: Providers
network: true
overview: 'Codafication publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Insurtech, Claims, and Claims Management.


  The Codafication catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Codafication''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, CLI, and 20 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 63.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 35.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codafication/refs/heads/main/screenshots/codafication-2026-07-25T205858.png
security:
- kind: authentication
  name: Codafication Authentication
  slug: codafication-authentication
  summary_line: oauth2/openIdConnect/saml/apiKey/preSharedSecret · 4 schemes
- kind: domain-security
  name: Codafication Domain Security
  slug: codafication-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codafication
tags:
- Insurance
- Australia
- Insurtech
- Claims
- Claims Management
- Property and Casualty
- FNOL
- Supply Chain
- GraphQL
- Webhook
- SDK
- Extensions
- Multi-Tenant
- Partner Gated
website: https://codafication.com/
---
