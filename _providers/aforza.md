---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Manage your organization's users - create, update and manage the lifecycle of users.
  name: User Management API
  slug: user-management-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/aforza/conformance/aforza-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aforza-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aforza/well-known/aforza-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aforza-well-known.yml
- group: other
  href: https://artifacts.apis.io/aforza/hosts/aforza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aforza-hosts.yml
- group: other
  href: https://artifacts.apis.io/aforza/vendors/aforza-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aforza-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://aforza.com/create-account-objectives/
- group: auth
  href: https://artifacts.apis.io/aforza/security/aforza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aforza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aforza.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aforza.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aforza.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.aforza.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.aforza.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://aforza.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aforza.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aforza.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/aforza/workspace
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://aforza.com/api/mcp
  - status: 403
    url: https://blog.aforza.com/mcp
  - status: 200
    url: https://aforza.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Aforza is a cloud‑based fintech platform that helps enterprises and startups integrate financial services, payments, analytics, and route‑to‑market solutions through a unified set of APIs. The company offers secure, scalable, developer‑friendly endpoints for transaction processing, account management, reporting, and a suite of AI‑driven tools such as Ava. Backed by Bonfire Ventures, Aforza provides extensive documentation, SDKs, and support to accelerate product development and improve profitability across retail, distribution, and B2B commerce.
image: https://aforza.com/wp-content/uploads/2024/04/Aforza-Homepage-Social-tile-10-04-24.png
layout: provider
modified: '2026-10-25'
name: Aforza
nav: Providers
network: true
overview: 'Aforza is listed with 1 API on the [APIs.io](https://apis.io/) network: User Management API. Tagged areas include Company, Fintech, Payments, and Cloud.


  Aforza''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 11.8
    contract_governance: 4.5
    contract_quality: 29.0
    developer_ergonomics: 25.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 29.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/aforza/aforza-2026-11-03T120331.png
security:
- kind: domain-security
  name: Aforza Domain Security
  slug: aforza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aforza
tags:
- Company
- Fintech
- Payments
- Cloud
website: https://aforza.com
---
