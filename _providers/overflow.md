---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 8
  name: Overflow Agentic Access
  operation_count: 38
  slug: overflow-agentic-access
  summary_line: 38 operations · 8 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Campaigns API from Overflow — 2 operation(s) for campaigns.
  name: Overflow Campaigns API
  slug: overflow-campaigns-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Chargebacks API from Overflow — 2 operation(s) for chargebacks.
  name: Overflow Chargebacks API
  slug: overflow-chargebacks-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Contributions API from Overflow — 3 operation(s) for contributions.
  name: Overflow Contributions API
  slug: overflow-contributions-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Deposits API from Overflow — 3 operation(s) for deposits.
  name: Overflow Deposits API
  slug: overflow-deposits-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Donors API from Overflow — 2 operation(s) for donors.
  name: Overflow Donors API
  slug: overflow-donors-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Locations API from Overflow — 2 operation(s) for locations.
  name: Overflow Locations API
  slug: overflow-locations-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Payment Methods API from Overflow — 1 operation(s) for payment methods.
  name: Overflow Payment Methods API
  slug: overflow-payment-methods-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Payments API from Overflow — 1 operation(s) for payments.
  name: Overflow Payments API
  slug: overflow-payments-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Refunds API from Overflow — 2 operation(s) for refunds.
  name: Overflow Refunds API
  slug: overflow-refunds-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Status API from Overflow — 1 operation(s) for status.
  name: Overflow Status API
  slug: overflow-status-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Subscriptions API from Overflow — 3 operation(s) for subscriptions.
  name: Overflow Subscriptions API
  slug: overflow-subscriptions-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Tap API from Overflow — 7 operation(s) for tap.
  name: Overflow Tap API
  slug: overflow-tap-api
- baseURL: https://server.overflow.co
  baseurl_source: declared
  description: The Webhooks API from Overflow — 3 operation(s) for webhooks.
  name: Overflow Webhooks API
  slug: overflow-webhooks-api
artifact_total: 37
asyncapis:
- description: ''
  name: Overflow Webhooks
  slug: overflow-webhooks
collections:
- collection_type: open
  name: Overflow Open Campaigns API
  slug: open-overflow-campaigns-api
- collection_type: open
  name: Overflow Open Campaigns Chargebacks API
  slug: open-overflow-chargebacks-api
- collection_type: open
  name: Overflow Open Campaigns Contributions API
  slug: open-overflow-contributions-api
- collection_type: open
  name: Overflow Open Campaigns Deposits API
  slug: open-overflow-deposits-api
- collection_type: open
  name: Overflow Open Campaigns Donors API
  slug: open-overflow-donors-api
- collection_type: open
  name: Overflow Open Campaigns Locations API
  slug: open-overflow-locations-api
- collection_type: open
  name: Overflow Open Campaigns Payment Methods API
  slug: open-overflow-payment-methods-api
- collection_type: open
  name: Overflow Open Campaigns Payments API
  slug: open-overflow-payments-api
- collection_type: open
  name: Overflow Open Campaigns Refunds API
  slug: open-overflow-refunds-api
- collection_type: open
  name: Overflow Open Campaigns Status API
  slug: open-overflow-status-api
- collection_type: open
  name: Overflow Open Campaigns Subscriptions API
  slug: open-overflow-subscriptions-api
- collection_type: open
  name: Overflow Open Campaigns Tap API
  slug: open-overflow-tap-api
- collection_type: open
  name: Overflow Open Campaigns Webhooks API
  slug: open-overflow-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/overflow/plans/overflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/overflow-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/overflow/capabilities/overflow-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/overflow-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.overflow.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.overflow.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.overflow.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.overflow.co/api-reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.overflow.co/api-reference/quickstart
- group: auth
  href: https://artifacts.apis.io/overflow/authentication/overflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/overflow-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.overflow.co/api-reference/rate-limiting
- group: design
  href: https://artifacts.apis.io/overflow/asyncapi/overflow-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/overflow-webhooks.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.overflow.co
- group: company
  title: ''
  type: Blog
  url: https://www.overflow.co/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/overflow-co
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.overflow.co/login
- group: start
  title: ''
  type: Login
  url: https://dashboard.overflow.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.overflow.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.overflow.co/privacy
- group: agent
  href: https://artifacts.apis.io/overflow/llms/overflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/overflow-llms.txt
- group: agent
  href: https://artifacts.apis.io/overflow/mcp/overflow-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/overflow-mcp.yml
- group: other
  href: https://artifacts.apis.io/overflow/overlays/overflow-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/overflow-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/overflow/conformance/overflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/overflow-conformance.yml
- group: design
  href: https://artifacts.apis.io/overflow/errors/overflow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/overflow-problem-types.yml
- group: design
  href: https://artifacts.apis.io/overflow/lifecycle/overflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/overflow-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/overflow/security/overflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/overflow-domain-security.yml
- group: design
  href: https://artifacts.apis.io/overflow/conventions/overflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/overflow-conventions.yml
- group: start
  href: https://artifacts.apis.io/overflow/sandbox/overflow-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/overflow-sandbox.yml
- group: design
  href: https://artifacts.apis.io/overflow/data-model/overflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/overflow-data-model.yml
- group: agent
  href: https://artifacts.apis.io/overflow/agentic-access/overflow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/overflow-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/overflow/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Overflow is a fintech giving platform for churches and nonprofits that lets organizations accept and reconcile donations across many asset types — card and ACH, Apple Pay and Google Pay, stock, cryptocurrency, RoundUps, and Donor Advised Funds (DAFs) — through a single unified platform. Overflow also offers Overflow Tap (NFC tap-to-give hardware) and Generosity University donor education. Its public Overflow Open API (v3) is a REST interface over contributions, donors, subscriptions (recurring gifts), payments, campaigns, deposits, refunds, chargebacks, locations, tap devices/events, and webhooks, authenticated with header API keys and used to sync giving data into CRMs and accounting/reconciliation workflows. Overflow is backed by Uncork Capital.
finops:
- has_sources: true
  method: derived
  name: Overflow Finops
  primary_unit: organization
  service_category: ''
  slug: overflow-finops
  template: false
image: https://cdn.prod.website-files.com/661982b7ce6b433411c6e0c8/661986ff805671631abc51f8_Open%20Graph%20Image.webp
layout: provider
modified: '2026-07-20'
name: Overflow
nav: Providers
network: true
overview: 'Overflow publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Campaigns API, Chargebacks API, Contributions API, and 10 more. Tagged areas include Company, Fintech, Payments, Donations, and Fundraising.


  The Overflow catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Overflow''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, sandbox, and 22 more developer resources.'
plans:
- name: Overflow Plans Pricing
  plan_count: 3
  slug: overflow-plans-pricing
- name: Overflow Price Estimates
  plan_count: 0
  slug: overflow-price-estimates
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Overflow API Rules
  rule_count: 60
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 6
  slug: overflow-rules
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/overflow/overflow-2026-08-07T191125.png
security:
- kind: authentication
  name: Overflow Authentication
  slug: overflow-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Overflow Domain Security
  slug: overflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Reconcile Overflow deposits
  slug: overflow-reconcile-deposits
- name: Record a donation with Overflow
  slug: overflow-record-contribution
- name: Set up a recurring gift with Overflow
  slug: overflow-recurring-gift
slug: overflow
tags:
- Company
- Fintech
- Payments
- Donations
- Fundraising
- Non-Profit
- Giving
- Recurring Payments
- Webhook
- Cryptocurrency
website: https://www.overflow.co/
---
