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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Carry1St Agentic Access
  operation_count: 6
  slug: carry1st-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api-gateway.carry1st.com
  baseurl_source: declared
  description: Obtain and refresh access tokens for Gateway API requests.
  name: Carry1st Authentication API
  slug: carry1st-authentication-api
- baseURL: https://api-gateway.carry1st.com
  baseurl_source: declared
  description: Discover the local payment methods available per country.
  name: Carry1st Payment Methods API
  slug: carry1st-payment-methods-api
- baseURL: https://api-gateway.carry1st.com
  baseurl_source: declared
  description: Create payment requests and query their status.
  name: Carry1st Payments API
  slug: carry1st-payments-api
- baseURL: https://api-gateway.carry1st.com
  baseurl_source: declared
  description: Request refunds against processed transactions.
  name: Carry1st Refunds API
  slug: carry1st-refunds-api
arazzos:
- description: Authenticate, create a signed payment request, and confirm the payment status.
  name: Pay1st - collect a payment
  slug: carry1st-collect-payment
artifact_total: 14
asyncapis:
- description: ''
  name: Carry1St Pay1St Webhooks
  slug: carry1st-pay1st-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pay1st Gateway Authentication API
  slug: open-carry1st-authentication-api
- collection_type: open
  name: Pay1st Gateway Authentication Payment Methods API
  slug: open-carry1st-payment-methods-api
- collection_type: open
  name: Pay1st Gateway Authentication Payments API
  slug: open-carry1st-payments-api
- collection_type: open
  name: Pay1st Gateway Authentication Refunds API
  slug: open-carry1st-refunds-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/carry1st-pay1st-gateway-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pay1st-docs.carry1st.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pay1st-docs.carry1st.com/
- group: docs
  title: ''
  type: APIReference
  url: https://pay1st-docs.carry1st.com/reference/gateway-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://pay1st-docs.carry1st.com/reference/gateway-integration-step-by-step-checklist
- group: company
  title: ''
  type: Website
  url: https://www.carry1st.com/
- group: company
  title: ''
  type: Blog
  url: https://www.carry1st.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carry1st.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carry1st.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.carry1st.com/contact
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/carry1st-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carry1st-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/carry1st-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carry1st-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carry1st-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/carry1st-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carry1st-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://pay1st-docs.carry1st.com/reference/gateway-migration-guide
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carry1st-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carry1st-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carry1st-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/carry1st-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carry1st-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/carry1st-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/carry1st-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/carry1st-pay1st-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carry1st-agentic-access.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/carry1st-collect-payment.yml
created: '2026-07-17'
description: Carry1st is Africa's leading mobile games publisher and digital commerce platform, headquartered in South Africa and operating across high-growth African markets including Nigeria, South Africa, Kenya, Ghana, Egypt, and Morocco. Beyond publishing and distributing mobile games from partners such as Riot Games, Activision, and Supercell, Carry1st operates Pay1st, a payment gateway that lets digital-content and game developers accept payments through 120+ local payment methods across six African geographies. Pay1st offers a single unified API, acts as Merchant of Record (handling compliance, taxation, FX, and risk so businesses collect in USD), and supports hosted-payment, game-client, and Carry1st Shop marketplace integration styles. Carry1st is backed by a16z. This profile was enriched by the API Evangelist pipeline from the public Pay1st developer documentation.
image: https://www.carry1st.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Carry1st
nav: Providers
network: true
overview: 'Carry1st publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Payment Methods API, Payments API, and 1 more. Tagged areas include Company, Payments, Payment Gateway, Fintech, and Gaming.


  The Carry1st catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Carry1st''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 22 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 22.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 27.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carry1st/refs/heads/main/screenshots/carry1st-2026-07-25T204645.png
security:
- kind: authentication
  name: Carry1St Authentication
  slug: carry1st-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Carry1St Domain Security
  slug: carry1st-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carry1st
tags:
- Company
- Payments
- Payment Gateway
- Fintech
- Gaming
- Mobile Games
- Africa
- Digital Commerce
- Merchant of Record
- Games Publishing
website: https://www.carry1st.com/
---
