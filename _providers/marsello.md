---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Marsello Agentic Access
  operation_count: 90
  slug: marsello-agentic-access
  summary_line: 90 operations · 44 acting
api_count: 3
apis:
- description: Marsello Loyalty API provides endpoints for account, activities, checkins, customers and other loyalty features as documented in the reference.
  name: Marsello Loyalty API
  slug: marsello-loyalty-api
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/marsello/plans/marsello-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/marsello-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.marsello.com/
- group: design
  href: https://artifacts.apis.io/marsello/conformance/marsello-conformance.yml
  title: ''
  type: Conformance
  url: conformance/marsello-conformance.yml
- group: other
  href: https://artifacts.apis.io/marsello/hosts/marsello-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marsello-hosts.yml
- group: other
  href: https://artifacts.apis.io/marsello/vendors/marsello-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marsello-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.marsello.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.marsello.com/
- group: start
  title: ''
  type: Login
  url: https://dashboard.marsello.com/account/login
- group: auth
  href: https://artifacts.apis.io/marsello/security/marsello-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/marsello-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/marsello/security/marsello-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marsello-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marsello.com/
- group: docs
  title: ''
  type: Documentation
  url: https://marsello.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://marsello.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://marsello.readme.io/reference/getting-started-with-marsello-api
- group: company
  title: ''
  type: Blog
  url: https://resources.marsello.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marsello.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marsello.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marsello.com/privacy
coverage:
  checked: '2026-10-28'
  detail: API reference pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://marsello.readme.io/reference/getting-started-with-marsello-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Marsello provides a loyalty and marketing platform for retail and hospitality brands, offering tools for customer loyalty programs, email and SMS campaigns, marketing automation, analytics, and digital wallet passes. The solution helps merchants attract, retain, and grow loyal customers through integrated loyalty, referral, and personalized marketing features.
json_schemas:
- name: AccountModel
  property_count: 9
  slug: marsello-account-model
- name: CustomerCreateModel
  property_count: 12
  slug: marsello-customer-create-model
- name: CustomerModel
  property_count: 24
  slug: marsello-customer-model
- name: DeviceCreateModel
  property_count: 13
  slug: marsello-device-create-model
- name: OrderCreateModel
  property_count: 6
  slug: marsello-order-create-model
- name: RewardModel
  property_count: 15
  slug: marsello-reward-model
jsonld:
- class_count: 35
  name: Marsello Context
  property_count: 245
  slug: marsello-context
layout: provider
modified: '2026-10-27'
name: Marsello
nav: Providers
network: true
overview: 'Marsello publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loyalty, Marketing, Retail, and Hospitality.


  The Marsello catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Marsello''s developer surface includes support, documentation, API reference, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Marsello Plans Pricing
  plan_count: 3
  slug: marsello-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Marsello Rate Limits
  slug: marsello-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Marsello API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: marsello-rules
scopes:
- name: Marsello Scopes
  scope_count: 2
  slug: marsello-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 60.5
    catalog_earned_first_party: 12.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 20.7
    developer_ergonomics: 17.9
    discoverability: 58.9
    operational_transparency: 7.9
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/marsello/marsello-2026-11-03T135341.png
security:
- kind: authentication
  name: Marsello Authentication
  slug: marsello-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Marsello Domain Security
  slug: marsello-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Marsello Trust Center
  slug: marsello-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 1
skills:
- name: getting-started
  slug: marsello-getting-started
slug: marsello
tags:
- Company
- Loyalty
- Marketing
- Retail
- Hospitality
website: https://marsello.com/
---
