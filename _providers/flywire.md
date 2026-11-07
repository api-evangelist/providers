---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: REST API for integrating Flywire's global payment network — one-off, recurring, pre-authorization, refund and 529 payments, checkout sessions, payors, recipients, and documents, with real-time payment
  name: Flywire Payments API
  slug: flywire-payments-api
- description: REST API for the Flywire Invoicing Platform — contacts, invoices, credit notes and invoice payments for a company, with search, count and export on each resource. Authorized with OAuth 2.0 client cred
  name: Flywire Invoicing API
  slug: flywire-invoicing-api
- description: REST API for creating, retrieving, updating and removing payer-facing payment requests for a company, including instalment schedules. Requests are authenticated with an HMAC-SHA256 digest of the reque
  name: Flywire Payment Request API
  slug: flywire-payment-request-api
artifact_total: 13
asyncapis:
- description: ''
  name: Flywire Non Payment Webhooks
  slug: flywire-non-payment-webhooks
- description: ''
  name: Flywire Payments Webhooks
  slug: flywire-payments-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://www.flywire.com/company/news
- group: auth
  href: https://artifacts.apis.io/flywire/security/flywire-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flywire-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.flywire.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.flywire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.flywire.com/education/Content/home.htm
- group: docs
  title: ''
  type: APIReference
  url: https://developers.flywire.com/education/Content/api-reference.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.flywire.com/education/Content/api-basics.htm
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flywire.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flywire.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flywire.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flywirecorp
- group: auth
  title: ''
  type: Compliance
  url: https://www.flywire.com/company/security
- group: auth
  title: ''
  type: Security
  url: https://app.intigriti.com/programs/flywire/flywirevulnerabilitydiscloseprogram/
- group: build
  href: https://artifacts.apis.io/flywire/packages/flywire-packages.yml
  title: ''
  type: Packages
  url: packages/flywire-packages.yml
- group: build
  href: https://artifacts.apis.io/flywire/packages/flywire-packages.yml
  title: ''
  type: SDKs
  url: packages/flywire-packages.yml
- group: design
  href: https://artifacts.apis.io/flywire/components/flywire-components.yml
  title: ''
  type: Components
  url: components/flywire-components.yml
- group: start
  href: https://artifacts.apis.io/flywire/sandbox/flywire-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/flywire-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/flywire/authentication/flywire-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flywire-authentication.yml
- group: design
  href: https://artifacts.apis.io/flywire/conventions/flywire-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flywire-conventions.yml
- group: design
  href: https://artifacts.apis.io/flywire/errors/flywire-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flywire-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flywire/lifecycle/flywire-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flywire-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/flywire/asyncapi/flywire-payments-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/flywire-payments-webhooks.yml
- group: design
  href: https://artifacts.apis.io/flywire/conformance/flywire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flywire-conformance.yml
- group: design
  href: https://artifacts.apis.io/flywire/data-model/flywire-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flywire-data-model.yml
- group: agent
  href: https://artifacts.apis.io/flywire/well-known/flywire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flywire-well-known.yml
- group: auth
  href: https://artifacts.apis.io/flywire/well-known/flywire-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/flywire-security.txt
- group: auth
  href: https://artifacts.apis.io/flywire/security/flywire-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flywire-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/flywire/security/flywire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flywire-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/flywire/mcp/flywire-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/flywire-mcp.yml
- group: agent
  href: https://artifacts.apis.io/flywire/llms/flywire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flywire-llms.txt
- group: operate
  href: https://artifacts.apis.io/flywire/changelog/flywire-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flywire-changelog.yml
- group: operate
  href: https://artifacts.apis.io/flywire/rate-limits/flywire-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flywire-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/flywire/plans/flywire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flywire-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/flywire/scopes/flywire-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/flywire-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://www.flywire.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.flywire.com/
- group: start
  title: ''
  type: Login
  url: https://app.flywire.com/
created: '2026-07-17'
description: Flywire is a global payments enablement and software company that operates a proprietary cross-border payment network spanning more than 140 currencies and 240 countries and territories, serving the education, healthcare, travel, and business-to-business verticals. The Flywire Payments API is an HTTP-based REST API (JSON request/response bodies, API-Key authorization) that lets platforms integrate Flywire's payment network directly — creating and capturing one-off, recurring, pre-authorization, refund, and 529 payments, managing payors, recipients, checkout sessions and documents, and receiving real-time payment status callbacks (webhooks) signed with an HMAC-SHA256 shared secret. Flywire also ships client-side JavaScript and React libraries (Flywire Elements, Checkout, Pay-By-Link) for embedding hosted payment experiences.
finops:
- has_sources: true
  method: derived
  name: Flywire Finops
  primary_unit: ''
  service_category: ''
  slug: flywire-finops
  template: true
image: https://www.flywire.com/favicon.ico
layout: provider
modified: '2026-09-02'
name: Flywire
nav: Providers
network: true
overview: 'Flywire is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Fintech, and Education Payments.


  The Flywire catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Flywire''s developer surface includes engineering blog, documentation, API reference, getting-started guide, sandbox, authentication, changelog, and 30 more developer resources.'
plans:
- name: Flywire Plans Pricing
  plan_count: 0
  slug: flywire-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Flywire Rate Limits
  slug: flywire-rate-limits
scopes:
- name: Flywire Scopes
  scope_count: 16
  slug: flywire-scopes
  summary_line: 16 scopes
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 71.4
    discoverability: 78.6
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 55.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flywire/flywire-2026-07-25T214857.png
security:
- kind: authentication
  name: Flywire Authentication
  slug: flywire-authentication
  summary_line: apiKey/oauth2/http-signature · 3 schemes
- kind: domain-security
  name: Flywire Domain Security
  slug: flywire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flywire Vulnerability Disclosure
  slug: flywire-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Flywire Trust Center
  slug: flywire-trust-center
  summary_line: SOC 2, PCI DSS
slug: flywire
tags:
- Company
- Payments
- Cross-Border Payments
- Fintech
- Education Payments
- Healthcare Payments
- Travel Payments
- B2B Payments
- Checkout
- Webhook
website: https://www.flywire.com
---
