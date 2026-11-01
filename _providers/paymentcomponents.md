---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Payments orchestration lowers costs, reduces regulatory burdens, eliminates unnecessary chargebacks, and creates fast, ...
  name: Payment Components API
  slug: payment-components-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/paymentcomponents/vendors/paymentcomponents-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paymentcomponents-vendors.yml
- group: auth
  href: https://artifacts.apis.io/paymentcomponents/authentication/paymentcomponents-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paymentcomponents-authentication.yml
- group: design
  href: https://artifacts.apis.io/paymentcomponents/errors/paymentcomponents-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paymentcomponents-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/paymentcomponents/llms/paymentcomponents-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paymentcomponents-llms.txt
- group: other
  href: https://artifacts.apis.io/paymentcomponents/hosts/paymentcomponents-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paymentcomponents-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aciworldwide.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.aciworldwide.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aciworldwide.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.aciworldwide.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.aciworldwide.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aciworldwide.com/tutorials/mp-guide/quick-start-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aciworldwide.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaymentComponents
- group: auth
  href: https://artifacts.apis.io/paymentcomponents/security/paymentcomponents-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paymentcomponents-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: Documentation is public HTML but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://docs.aciworldwide.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'Payment Components is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://www.aciworldwide.com/wp-content/uploads/2024/07/ACI-Worldwide-Blue-No-Tagline.png
layout: provider
modified: '2026-10-28'
name: Payment Components
nav: Providers
network: true
overview: 'Payment Components is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Payment Components'' developer surface includes authentication, support, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
plans:
- name: Paymentcomponents Plans Pricing
  plan_count: 0
  slug: paymentcomponents-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Paymentcomponents Rate Limits
  slug: paymentcomponents-rate-limits
scopes:
- name: Paymentcomponents Scopes
  scope_count: 0
  slug: paymentcomponents-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 41.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Paymentcomponents Authentication
  slug: paymentcomponents-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Paymentcomponents Domain Security
  slug: paymentcomponents-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paymentcomponents
tags:
- Company
---
