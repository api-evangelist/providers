---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gorilladesk Agentic Access
  operation_count: 9
  slug: gorilladesk-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.gorilladesk.com/v1
  baseurl_source: declared
  description: The Company API from GorillaDesk — 1 operation(s) for company.
  name: GorillaDesk Company API
  slug: gorilladesk-company-api
- baseURL: https://api.gorilladesk.com/v1
  baseurl_source: declared
  description: The Customer API from GorillaDesk — 2 operation(s) for customer.
  name: GorillaDesk Customer API
  slug: gorilladesk-customer-api
- baseURL: https://api.gorilladesk.com/v1
  baseurl_source: declared
  description: The Note API from GorillaDesk — 1 operation(s) for note.
  name: GorillaDesk Note API
  slug: gorilladesk-note-api
- baseURL: https://api.gorilladesk.com/v1
  baseurl_source: declared
  description: The Phone Type API from GorillaDesk — 1 operation(s) for phone type.
  name: GorillaDesk Phone Type API
  slug: gorilladesk-phone-type-api
- baseURL: https://api.gorilladesk.com/v1
  baseurl_source: declared
  description: The User API from GorillaDesk — 2 operation(s) for user.
  name: GorillaDesk User API
  slug: gorilladesk-user-api
artifact_total: 19
collections:
- collection_type: open
  name: GorillaDesk Company API
  slug: open-gorilladesk-company-api
- collection_type: open
  name: GorillaDesk Company Customer API
  slug: open-gorilladesk-customer-api
- collection_type: open
  name: GorillaDesk Company Note API
  slug: open-gorilladesk-note-api
- collection_type: open
  name: GorillaDesk Company Phone Type API
  slug: open-gorilladesk-phone-type-api
- collection_type: open
  name: GorillaDesk Company User API
  slug: open-gorilladesk-user-api
- collection_type: open
  name: GorillaDesk Company Users API
  slug: open-gorilladesk-users-api
- collection_type: open
  name: GorillaDesk v1 API
  slug: open-gorilladesk
common:
- group: company
  title: ''
  type: Blog
  url: https://gorilladesk.com/blog/
- group: other
  href: https://artifacts.apis.io/gorilladesk/capabilities/gorilladesk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gorilladesk-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gorilladesk/agentic-access/gorilladesk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gorilladesk-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gorilladesk/security/gorilladesk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gorilladesk-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gorilladesk/authentication/gorilladesk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gorilladesk-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gorilladesk
- group: company
  title: ''
  type: Website
  url: https://gorilladesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.gorilladesk.com/
- group: start
  title: ''
  type: SignUp
  url: https://beta.gorilladesk.com/addons/api
- group: commercial
  href: https://artifacts.apis.io/gorilladesk/plans/gorilladesk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gorilladesk-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gorilladesk/rate-limits/gorilladesk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gorilladesk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gorilladesk/finops/gorilladesk-finops.yml
  title: ''
  type: FinOps
  url: finops/gorilladesk-finops.yml
created: '2026-07-04'
description: GorillaDesk is field service management software for pest control, lawn care, pool service, and other home-service businesses, covering scheduling, routing, invoicing, payments, customer records, and technician management. GorillaDesk exposes a real, self-serve public REST API - the GorillaDesk v1 API at https://api.gorilladesk.com/v1 - documented with a public OpenAPI 3.0.3 specification (rendered via Redoc at https://api.gorilladesk.com/). Access uses per-company API keys (Bearer token authentication) generated on the in-app Addons page; there is no separate developer signup or API pricing tier - any paying account can mint a key. The documented public surface is intentionally narrow (Company, Users, Customers, Customer Notes, and Phone Types); broader automation (invoices, jobs, work orders, payments) is offered through Zapier connectors and out-of-the-box integrations (QuickBooks, Square, Stripe, Google) rather than through the public v1 REST spec. A newer, auth-gated v2
  API surface (apiv2.gdesk.io) exists but is not publicly documented.
finops:
- has_sources: true
  method: generated
  name: Gorilladesk Finops
  primary_unit: ''
  service_category: Field Service Management Software
  slug: gorilladesk-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gorilladesk.png
layout: provider
modified: '2026-10-06'
name: GorillaDesk
nav: Providers
network: true
overview: 'GorillaDesk publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Company API, Customer API, Note API, and 2 more. Tagged areas include Field Service Management, Pest Control, Lawn Care, Scheduling, and Invoicing.


  The GorillaDesk catalog on APIs.io includes 1 Spectral governance ruleset.


  GorillaDesk''s developer surface includes engineering blog, authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Gorilladesk Plans Pricing
  plan_count: 4
  slug: gorilladesk-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Gorilladesk Rate Limits
  slug: gorilladesk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: GorillaDesk API Rules
  rule_count: 50
  severity_counts:
    error: 41
    hint: 0
    info: 2
    warn: 7
  slug: gorilladesk-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 45.4
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 27.6
      total: 29
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gorilladesk/gorilladesk-2026-07-25T220117.png
security:
- kind: authentication
  name: Gorilladesk Authentication
  slug: gorilladesk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gorilladesk Domain Security
  slug: gorilladesk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gorilladesk
tags:
- Field Service Management
- Pest Control
- Lawn Care
- Scheduling
- Invoicing
- Customers
- Software-as-a-Service
website: https://gorilladesk.com/
---
