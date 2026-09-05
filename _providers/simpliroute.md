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
  score: 23.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for delivery visits, route plans, route optimization, vehicles, drivers, clients, invoices and lifecycle webhooks. Token-header authenticated, JSON over HTTPS, versioned at /v1.
  name: SimpliRoute API
  slug: simpliroute-api
artifact_total: 4
asyncapis:
- description: ''
  name: Simpliroute Webhooks
  slug: simpliroute-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://simpliroute.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://simpliroute.com/en/development
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.simpliroute.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.simpliroute.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.simpliroute.com/#introduction
- group: operate
  title: ''
  type: Support
  url: https://help.simpliroute.com/en
- group: company
  title: ''
  type: Blog
  url: https://simpliroute.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simpliroute
- group: start
  title: ''
  type: SignUp
  url: https://app2.simpliroute.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://app2.simpliroute.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simpliroute.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simpliroute.com/en/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/simpliroute-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simpliroute-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simpliroute-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simpliroute-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simpliroute-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simpliroute-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/simpliroute-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/simpliroute-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/simpliroute-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/simpliroute-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simpliroute-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simpliroute-llms.txt
created: '2026-07-17'
description: SimpliRoute is an AI-powered last-mile route optimization and delivery management platform, founded in Chile and operating across Latin America and beyond. Its REST API (base URL https://api.simpliroute.com/v1, authenticated with an Authorization Token header) lets developers create delivery and pickup visits, build daily plans, run the route-optimization engine over vehicles and deliveries, manage vehicles, drivers, couriers, clients, skills, zones and fleets, handle invoices, and subscribe to lifecycle webhooks (route started, on its way, checkout, route finished). First-party Node/TypeScript and Python SDKs are published under the github.com/simpliroute organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simpliroute.png
layout: provider
modified: '2026-07-21'
name: Simpliroute
nav: Providers
network: true
overview: 'Simpliroute publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Route Optimization, Last Mile Delivery, and Delivery Management.


  The Simpliroute catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Simpliroute''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 14
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
    contract_quality: 41.6
    developer_ergonomics: 60.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simpliroute/refs/heads/main/screenshots/simpliroute-2026-09-02T155548.png
security:
- kind: authentication
  name: Simpliroute Authentication
  slug: simpliroute-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Simpliroute Domain Security
  slug: simpliroute-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: simpliroute
tags:
- Company
- Logistics
- Route Optimization
- Last Mile Delivery
- Delivery Management
- Fleet Management
- Transportation
- Webhook
website: https://simpliroute.com
---
