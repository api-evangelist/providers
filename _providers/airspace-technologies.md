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
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Airspace Technologies Agentic Access
  operation_count: 33
  slug: airspace-technologies-agentic-access
  summary_line: 33 operations · 15 acting
api_count: 2
apis:
- baseURL: https://api.airspace.com/api/public/v3
  baseurl_source: declared
  description: We support listing reusable address entries.
  name: Airspace Technologies Address Books API
  slug: airspace-technologies-address-books-api
- baseURL: https://api.airspace.com/api/public/v3
  baseurl_source: declared
  description: We support listing invoices for Orders. Please reach out to account manager for setup
  name: Airspace Technologies Invoices API
  slug: airspace-technologies-invoices-api
- baseURL: https://api.airspace.com/api/public/v3
  baseurl_source: declared
  description: We support generating labels for Orders.
  name: Airspace Technologies Labels API
  slug: airspace-technologies-labels-api
- baseURL: https://api.airspace.com/api/public/v3
  baseurl_source: declared
  description: We support order creation, updates, cancellation, information, and document upload.
  name: Airspace Technologies Orders API
  slug: airspace-technologies-orders-api
- baseURL: https://api.airspace.com/api/public/v3
  baseurl_source: declared
  description: We support listing reusable piece entries.
  name: Airspace Technologies Piece Libraries API
  slug: airspace-technologies-piece-libraries-api
- baseURL: https://api.airspace.com/api/public/v3
  baseurl_source: declared
  description: We support generating a Quote for a potential Order as well as confirming that Quote to place an Order.
  name: Airspace Technologies Quotes API
  slug: airspace-technologies-quotes-api
artifact_total: 20
asyncapis:
- description: ''
  name: Airspace Technologies Webhooks
  slug: airspace-technologies-webhooks
collections:
- collection_type: open
  name: Airspace API Documentation Address Books API
  slug: open-airspace-technologies-address-books-api
- collection_type: open
  name: Airspace API Documentation Address Books Invoices API
  slug: open-airspace-technologies-invoices-api
- collection_type: open
  name: Airspace API Documentation Address Books Labels API
  slug: open-airspace-technologies-labels-api
- collection_type: open
  name: Airspace API Documentation Address Books Orders API
  slug: open-airspace-technologies-orders-api
- collection_type: open
  name: Airspace API Documentation Address Books Piece Libraries API
  slug: open-airspace-technologies-piece-libraries-api
- collection_type: open
  name: Airspace API Documentation Address Books Quotes API
  slug: open-airspace-technologies-quotes-api
common:
- group: other
  href: https://artifacts.apis.io/airspace-technologies/capabilities/airspace-technologies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/airspace-technologies-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/airspace-technologies/overlays/airspace-technologies-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/airspace-technologies-v3-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.airspace.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.airspace.com/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.airspace.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.airspace.com/api-docs/v3
- group: start
  title: ''
  type: GettingStarted
  url: https://api.airspace.com/api-docs/v3
- group: start
  title: ''
  type: Login
  url: https://app.airspacetechnologies.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: https://www.airspace.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airspace.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AirspaceTechnologies
- group: operate
  title: ''
  type: StatusPage
  url: https://airspace.statuspage.io
- group: auth
  href: https://artifacts.apis.io/airspace-technologies/security/airspace-technologies-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/airspace-technologies-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.airspace.com/
- group: auth
  href: https://artifacts.apis.io/airspace-technologies/security/airspace-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airspace-technologies-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/airspace-technologies/authentication/airspace-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airspace-technologies-authentication.yml
- group: design
  href: https://artifacts.apis.io/airspace-technologies/conventions/airspace-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/airspace-technologies-conventions.yml
- group: design
  href: https://artifacts.apis.io/airspace-technologies/errors/airspace-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airspace-technologies-problem-types.yml
- group: design
  href: https://artifacts.apis.io/airspace-technologies/lifecycle/airspace-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/airspace-technologies-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/airspace-technologies/conformance/airspace-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airspace-technologies-conformance.yml
- group: design
  href: https://artifacts.apis.io/airspace-technologies/data-model/airspace-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airspace-technologies-data-model.yml
- group: start
  href: https://artifacts.apis.io/airspace-technologies/sandbox/airspace-technologies-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/airspace-technologies-sandbox.yml
- group: design
  href: https://artifacts.apis.io/airspace-technologies/asyncapi/airspace-technologies-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/airspace-technologies-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/airspace-technologies/mcp/airspace-technologies-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/airspace-technologies-mcp.yml
- group: agent
  href: https://artifacts.apis.io/airspace-technologies/llms/airspace-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airspace-technologies-llms.txt
- group: agent
  href: https://artifacts.apis.io/airspace-technologies/agentic-access/airspace-technologies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airspace-technologies-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/airspace-technologies/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Airspace Technologies is a time-critical logistics provider that uses AI-driven routing to move urgent, high-value freight via Next Flight Out (NFO), on-demand ground, charter, and specialty services across 80+ countries. Its public REST API (current V3, prior V2) supports order creation, quote generation, and active shipment monitoring. The API is asynchronous, authenticates with a non-expiring bearer token, paginates lists with page/page_limit, and pushes milestone, delay, and cancellation updates over webhooks correlated by request_id.
image: https://www.airspacetechnologies.com/hubfs/Updated%20logos/Airspace%20horizontal%20logotype%20black%20and%20green%20no%20background%20011321%20(1).png
layout: provider
modified: '2026-07-17'
name: Airspace Technologies
nav: Providers
network: true
overview: 'Airspace Technologies publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Address Books API, Invoices API, Labels API, and 3 more. Tagged areas include Company, Logistics, Shipping, Freight, and Supply Chain.


  The Airspace Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airspace Technologies'' developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 58.2
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/airspace-technologies/airspace-technologies-2026-07-25T195443.png
security:
- kind: authentication
  name: Airspace Technologies Authentication
  slug: airspace-technologies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airspace Technologies Domain Security
  slug: airspace-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Airspace Technologies Trust Center
  slug: airspace-technologies-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
skill_count: 3
skills:
- name: Create and track a shipment order
  slug: airspace-technologies-create-and-track-order
- name: Generate a shipping quote
  slug: airspace-technologies-generate-quote
- name: Monitor active shipments
  slug: airspace-technologies-monitor-shipments
slug: airspace-technologies
tags:
- Company
- Logistics
- Shipping
- Freight
- Supply Chain
- Transportation
- Webhook
- Order
website: https://www.airspace.com/
---
