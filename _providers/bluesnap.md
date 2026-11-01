---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: start
  href: https://artifacts.apis.io/bluesnap/sandbox/bluesnap-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bluesnap-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/bluesnap/authentication/bluesnap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bluesnap-authentication.yml
- group: agent
  href: https://artifacts.apis.io/bluesnap/llms/bluesnap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bluesnap-llms.txt
- group: agent
  href: https://artifacts.apis.io/bluesnap/well-known/bluesnap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluesnap-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluesnap/hosts/bluesnap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluesnap-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluesnap/vendors/bluesnap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluesnap-vendors.yml
- group: build
  href: https://artifacts.apis.io/bluesnap/packages/bluesnap-packages.yml
  title: ''
  type: SDKs
  url: packages/bluesnap-packages.yml
- group: build
  href: https://artifacts.apis.io/bluesnap/packages/bluesnap-packages.yml
  title: ''
  type: Packages
  url: packages/bluesnap-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bluesnap.com/
- group: auth
  href: https://artifacts.apis.io/bluesnap/security/bluesnap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluesnap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluesnap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bluesnap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bluesnap.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bluesnap.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bluesnap.com/v8976-Embedded-Payments/reference/overview
- group: operate
  title: ''
  type: Support
  url: https://support.bluesnap.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bluesnap.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bluesnap.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.bluesnap.com/ecommerce/legal/terms_and_conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.bluesnap.com/ecommerce/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/bluesnap/workspace/bluesnap-api
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://developers.bluesnap.com/mcp
  - status: 403
    url: https://api.bluesnap.com/mcp
  - status: 403
    url: https://cp.bluesnap.com/mcp
  - status: 403
    url: https://go.bluesnap.com/mcp
  - status: 200
    url: https://home.bluesnap.com/
  reason: partner-login
  state: gated
created: '2026-10-26'
description: BlueSnap provides a Global Payment Orchestration Platform that enables businesses to accept payments worldwide through a single integration. It supports multiple payment methods, currencies, and regions, offering tools for fraud prevention, chargeback management, and compliance. BlueSnap also offers embedded payment solutions, subscription billing, invoicing, and robust reporting APIs for developers to integrate and automate payment workflows.
image: https://www.bluesnap.com/wp-content/uploads/2024/10/bluesnap-logo-header.jpeg
layout: provider
modified: '2026-10-26'
name: BlueSnap
nav: Providers
network: true
overview: 'BlueSnap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, FinTech, API, and GlobalPayments.


  BlueSnap''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 76.2
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bluesnap Authentication
  slug: bluesnap-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bluesnap Domain Security
  slug: bluesnap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bluesnap
tags:
- Company
- Payments
- FinTech
- API
- GlobalPayments
website: https://www.bluesnap.com/
---
