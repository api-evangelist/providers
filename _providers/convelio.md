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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Convelio Agentic Access
  operation_count: 9
  slug: convelio-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.convelio.com/v2
  baseurl_source: declared
  description: Shipping API allow you to request a shipping estimate from our system
  name: Convelio Shipping API
  slug: convelio-shipping-api
- baseURL: https://api.convelio.com/v2
  baseurl_source: declared
  description: The Webhook API allows an API partner to create and manage webhooks.
  name: Convelio Webhook API
  slug: convelio-webhook-api
artifact_total: 9
asyncapis:
- description: ''
  name: Convelio Webhooks
  slug: convelio-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Convelio Public Shipping API
  slug: open-convelio-shipping-api
- collection_type: open
  name: Convelio Public Webhook API
  slug: open-convelio-webhook-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/convelio-capability-edges.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/convelio-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/convelio-shipping-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/convelio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convelio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/convelio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.convelio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.convelio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.convelio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.convelio.com/#tag/shipping
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.convelio.com/#section/API-key
- group: operate
  title: ''
  type: Support
  url: https://help.convelio.com/en
- group: company
  title: ''
  type: Blog
  url: https://www.convelio.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/convelio
- group: start
  title: ''
  type: SignUp
  url: https://web.convelio.com/auth/signup-email
- group: start
  title: ''
  type: Login
  url: https://web.convelio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.convelio.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.convelio.com/en/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.convelio.com/status
- group: design
  title: ''
  type: Conventions
  url: conventions/convelio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/convelio-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/convelio-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/convelio-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/convelio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/convelio-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/convelio-llms.txt
created: '2026-08-09'
description: Convelio is a Paris- and London-based tech-enabled fine art logistics company that moves high-value, fragile and oversized objects — paintings, sculpture, antiques and design — for galleries, auction houses, art fairs, dealers, collectors and online marketplaces. Its differentiator is an instant-pricing engine that returns an all-inclusive door-to-door shipping price (packing, crating, customs, road/air/sea freight, insurance and white-glove delivery) in place of the multi-day manual quoting the art-handling trade traditionally runs on. Convelio exposes that engine to partners as the Convelio Public API — a REST Shipping API (v2.0) documented with OpenAPI 3.1 at developers.convelio.com — plus an embeddable checkout widget, a web dashboard and a tracking surface, so marketplaces and auction platforms can price, book and track fine art shipments inside their own product.
image: https://www.convelio.com/favicon.ico
layout: provider
modified: '2026-08-09'
name: Convelio
nav: Providers
network: true
overview: 'Convelio publishes 2 APIs on the [APIs.io](https://apis.io/) network: Shipping API and Webhook API. Tagged areas include Company, Logistics, Shipping, Fine Art, and Freight.


  The Convelio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Convelio''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 69.7
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convelio/refs/heads/main/screenshots/convelio-2026-08-17T080832.png
security:
- kind: authentication
  name: Convelio Authentication
  slug: convelio-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Convelio Domain Security
  slug: convelio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: convelio
tags:
- Company
- Logistics
- Shipping
- Fine Art
- Freight
- E-Commerce
- Quotes
- Webhook
- Customs
- Insurance
website: https://www.convelio.com/
---
