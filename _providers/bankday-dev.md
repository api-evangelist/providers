---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bankday Dev Agentic Access
  operation_count: 16
  slug: bankday-dev-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Account API from bankday-dev — 1 operation(s) for account.
  name: bankday-dev Account API
  slug: bankday-dev-account-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Ach API from bankday-dev — 1 operation(s) for ach.
  name: bankday-dev Ach API
  slug: bankday-dev-ach-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Business Day API from bankday-dev — 1 operation(s) for business day.
  name: bankday-dev Business Day API
  slug: bankday-dev-business-day-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Business Days API from bankday-dev — 5 operation(s) for business days.
  name: bankday-dev Business Days API
  slug: bankday-dev-business-days-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Calendars API from bankday-dev — 1 operation(s) for calendars.
  name: bankday-dev Calendars API
  slug: bankday-dev-calendars-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Fx API from bankday-dev — 1 operation(s) for fx.
  name: bankday-dev Fx API
  slug: bankday-dev-fx-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Holidays API from bankday-dev — 1 operation(s) for holidays.
  name: bankday-dev Holidays API
  slug: bankday-dev-holidays-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Minimum Wage API from bankday-dev — 3 operation(s) for minimum wage.
  name: bankday-dev Minimum Wage API
  slug: bankday-dev-minimum-wage-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Payroll API from bankday-dev — 1 operation(s) for payroll.
  name: bankday-dev Payroll API
  slug: bankday-dev-payroll-api
- baseURL: https://bankday.dev
  baseurl_source: declared
  description: The Today API from bankday-dev — 1 operation(s) for today.
  name: bankday-dev Today API
  slug: bankday-dev-today-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/bankday-dev/agentic-access/bankday-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bankday-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bankday-dev/plans/bankday-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bankday-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bankday-dev/rules/bankday-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/bankday-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/bankday-dev/errors/bankday-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bankday-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bankday-dev/conformance/bankday-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bankday-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bankday-dev/llms/bankday-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankday-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/bankday-dev/hosts/bankday-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankday-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/bankday-dev/vendors/bankday-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankday-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bankday.dev/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://bankday.dev/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bankday.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bankday.dev/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://bankday.dev/docs
- group: auth
  href: https://artifacts.apis.io/bankday-dev/authentication/bankday-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bankday-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bankday-dev/security/bankday-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankday-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankday.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://bankday.dev/openapi.json
  - status: 401
    url: https://bankday.dev/mcp
  - status: 200
    url: https://bankday.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Bankday provides a Business Day & Bank Holiday API covering ACH, Fedwire, NYSE, and over 240 countries. It offers calendar data, settlement dates, and value date calculations for payments, payroll, lending, and trading systems. The service includes a free tier with 1,000 requests per month and paid plans starting at $19/mo, delivering low-latency responses from a global edge network.
image: https://bankday.dev/assets/og.png
layout: provider
modified: '2026-10-30'
name: bankday-dev
nav: Providers
network: true
overview: 'bankday-dev publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Ach API, Business Day API, and 7 more. Tagged areas include Company, Finance, Calendar, API, and Payments.


  The bankday-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  bankday-dev''s developer surface includes pricing, API reference, authentication, and 13 more developer resources.'
plans:
- name: Bankday Dev Plans Pricing
  plan_count: 5
  slug: bankday-dev-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: bankday-dev API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: bankday-dev-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 65.5
    contract_quality: 49.2
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bankday Dev Authentication
  slug: bankday-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bankday Dev Domain Security
  slug: bankday-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bankday-dev
tags:
- Company
- Finance
- Calendar
- API
- Payments
website: https://bankday.dev/
---
