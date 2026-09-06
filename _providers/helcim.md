---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Helcim Agentic Access
  operation_count: 48
  slug: helcim-agentic-access
  summary_line: 48 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The ACH Payment API from Helcim — 8 operation(s) for ach payment.
  name: Helcim ACH Payment API
  slug: helcim-ach-payment-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The Card Batch API from Helcim — 3 operation(s) for card batch.
  name: Helcim Card Batch API
  slug: helcim-card-batch-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The Card Terminal API from Helcim — 1 operation(s) for card terminal.
  name: Helcim Card Terminal API
  slug: helcim-card-terminal-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The Card Transaction API from Helcim — 2 operation(s) for card transaction.
  name: Helcim Card Transaction API
  slug: helcim-card-transaction-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The Customer API from Helcim — 11 operation(s) for customer.
  name: Helcim Customer API
  slug: helcim-customer-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The Device API from Helcim — 5 operation(s) for device.
  name: Helcim Device API
  slug: helcim-device-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The General API from Helcim — 1 operation(s) for general.
  name: Helcim General API
  slug: helcim-general-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The Invoice API from Helcim — 2 operation(s) for invoice.
  name: Helcim Invoice API
  slug: helcim-invoice-api
- baseURL: https://api.helcim.com/v2
  baseurl_source: declared
  description: The Payment API from Helcim — 7 operation(s) for payment.
  name: Helcim Payment API
  slug: helcim-payment-api
artifact_total: 16
asyncapis:
- description: ''
  name: Helcim Webhooks
  slug: helcim-webhooks
collections:
- collection_type: postman
  name: The Helcim API
  slug: postman-helcim-api
- collection_type: open
  name: The Helcim API
  slug: open-helcim-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/helcim/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/helcim-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helcim-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/helcim-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.helcim.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devdocs.helcim.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.helcim.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://devdocs.helcim.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://devdocs.helcim.com/docs/overview-of-helcim-api
- group: auth
  title: ''
  type: Authentication
  url: https://devdocs.helcim.com/docs/authentication-with-the-helcim-api-and-helcimpayjs
- group: design
  title: ''
  type: Webhooks
  url: https://devdocs.helcim.com/docs/connected-account-webhooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helcim
- group: operate
  title: ''
  type: StatusPage
  url: https://status.helcim.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.helcim.com/api-developer-documentation
- group: design
  title: ''
  type: Idempotency
  url: conventions/helcim-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/helcim-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/helcim-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/helcim-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/helcim-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/helcim-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://devdocs.helcim.com/docs/api-versions-and-deprecation
- group: start
  title: ''
  type: Sandbox
  url: sandbox/helcim-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/helcim-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/helcim-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/helcim-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/helcim-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://devdocs.helcim.com/docs/pci-compliance-scope
- group: build
  title: ''
  type: Packages
  url: packages/helcim-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/helcim-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/helcim-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helcim-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/helcim-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/helcim-webhooks.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.helcim.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://hub.helcim.com/signup/register/
- group: start
  title: ''
  type: Login
  url: https://hsso.helcim.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.helcim.com/ca/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.helcim.com/ca/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://devdocs.helcim.com/docs/get-help
created: '2026-07-24'
description: 'Helcim is a Calgary, Canada based payment processor and merchant services provider serving small and medium-sized businesses across Canada and the United States with interchange-plus pricing and no monthly fees. Beyond its merchant dashboard, Smart Terminal hardware, and online store, Helcim ships a genuine developer surface: the versioned Helcim API (v2) for taking card and ACH payments, managing customers, cards, bank accounts and pre-authorized debits (PADs), issuing invoices, settling card and ACH batches, and driving in-person Card Terminal devices, alongside HelcimPay.js hosted checkout and connected-account webhooks. Authentication is a permissioned API access token passed in an api-token header, and the public developer portal publishes a downloadable OpenAPI 3.0 definition. In Canada''s small, concentrated payments market, Helcim is one of the API-native SMB money-movement fintechs building above the incumbent acquiring and Interac rails.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Helcim
nav: Providers
network: true
overview: 'Helcim publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ACH Payment API, Card Batch API, Card Terminal API, and 6 more. Tagged areas include Payments, Canada, Payment Gateway, Payment Processing, and Acquiring.


  The Helcim catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Helcim''s developer surface includes authentication, documentation, API reference, getting-started guide, sandbox, changelog, pricing, and 33 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 3
  name: Helcim Rate Limits
  slug: helcim-rate-limits
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 45.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 77.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: first-party
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
    regime: Payments
    regime_id: payments
    score: 55.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helcim/refs/heads/main/screenshots/helcim-2026-07-25T220910.png
security:
- kind: authentication
  name: Helcim Authentication
  slug: helcim-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Helcim Domain Security
  slug: helcim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helcim
tags:
- Payments
- Canada
- Payment Gateway
- Payment Processing
- Acquiring
- Merchant Services
- ACH
- Invoicing
- Card Terminal
- Small Business
website: https://www.helcim.com/
---
