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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The accounts API from Laka — 6 operation(s) for accounts.
  name: Laka accounts API
  slug: laka-accounts-api
- description: Claims API
  name: Laka claims API
  slug: laka-claims-api
- description: The deeplinks API from Laka — 1 operation(s) for deeplinks.
  name: Laka deeplinks API
  slug: laka-deeplinks-api
- description: The fleets API from Laka — 1 operation(s) for fleets.
  name: Laka fleets API
  slug: laka-fleets-api
- description: The policies API from Laka — 14 operation(s) for policies.
  name: Laka policies API
  slug: laka-policies-api
- description: The quote service gets quotes.
  name: Laka quote API
  slug: laka-quote-api
- description: The quotes API from Laka — 1 operation(s) for quotes.
  name: Laka quotes API
  slug: laka-quotes-api
- description: The reporting API from Laka — 3 operation(s) for reporting.
  name: Laka reporting API
  slug: laka-reporting-api
- description: The tasks API from Laka — 1 operation(s) for tasks.
  name: Laka tasks API
  slug: laka-tasks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Laka accounts API
  slug: open-laka-accounts-api
- collection_type: open
  name: Laka accounts claims API
  slug: open-laka-claims-api
- collection_type: open
  name: Laka accounts deeplinks API
  slug: open-laka-deeplinks-api
- collection_type: open
  name: Laka accounts fleets API
  slug: open-laka-fleets-api
- collection_type: open
  name: Laka accounts policies API
  slug: open-laka-policies-api
- collection_type: open
  name: Laka accounts quote API
  slug: open-laka-quote-api
- collection_type: open
  name: Laka accounts quotes API
  slug: open-laka-quotes-api
- collection_type: open
  name: Laka accounts reporting API
  slug: open-laka-reporting-api
- collection_type: open
  name: Laka accounts tasks API
  slug: open-laka-tasks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/laka-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laka-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/laka-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://laka.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.laka.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.laka.co/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.laka.co/reference/policycontroller_getpolicies
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.laka.co/docs/introduction
- group: start
  title: ''
  type: SignUp
  url: https://docs.laka.co/docs/request-access
- group: operate
  title: ''
  type: Support
  url: https://docs.laka.co/docs/request-access
- group: company
  title: ''
  type: Blog
  url: https://laka.co/gb/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://laka.co/gb/blog/feed
- group: commercial
  title: ''
  type: TermsOfService
  url: https://laka.co/gb/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://laka.co/gb/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.laka.co
- group: other
  title: ''
  type: Glossary
  url: https://docs.laka.co/docs/glossary
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laka-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/laka-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/laka-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/laka-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/laka-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/laka-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/laka-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/laka-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/laka-platform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/laka-quote-overlay.yaml
created: '2026-07-17'
description: 'Laka is a European InsurTech with deep micro-mobility expertise, insuring bikes, e-bikes, e-scooters and cycling gear against theft, accidental damage and loss, and providing riders and businesses with liability and personal accident cover. Laka exposes two partner-facing APIs. The Quote API is a lightweight integration for Introducer partners — retailers, e-commerce stores, bike brands and online communities — that returns pricing to riders, shares rider information to pre-fill onboarding, hands customers directly into Laka onboarding, and checks whether a rider has taken out cover. The Platform API supports Group partnerships where Laka issues the partner a Group policy whose benefits are extended to the partner''s members: partners can list policies, add and remove beneficiaries, manage products and documents, and create, submit and track claims. Both APIs run as regional instances across the UK (gb) and EU (nl), are secured with API keys, and require x-api-region and x-api-language
  headers so the insured party is attributed to the correct regulatory region.'
image: https://laka.co/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Laka MCP Server
  slug: laka-mcp-server
modified: '2026-07-19'
name: Laka
nav: Providers
network: true
overview: 'Laka publishes 9 APIs on the [APIs.io](https://apis.io/) network, including accounts API, claims API, deeplinks API, and 6 more. Tagged areas include Company, Insurance, Insurtech, Cycling, and Micromobility.


  Laka''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 20 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 51.6
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 39.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laka/refs/heads/main/screenshots/laka-2026-07-25T224431.png
security:
- kind: authentication
  name: Laka Authentication
  slug: laka-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Laka Domain Security
  slug: laka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: laka
tags:
- Company
- Insurance
- Insurtech
- Cycling
- Micromobility
- Bicycle Insurance
- Claims
- Policies
- Quotes
- Embedded Insurance
- Europe
website: https://laka.co
---
