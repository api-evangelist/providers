---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pepperi provides a unified B2B commerce platform with resources for items, accounts, transactions and more as documented in the developer portal.
  name: Pepperi API
  slug: pepperi-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.pepperi.com/security
- group: other
  href: https://artifacts.apis.io/pepperi/hosts/pepperi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pepperi-hosts.yml
- group: other
  href: https://artifacts.apis.io/pepperi/vendors/pepperi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pepperi-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pepperi.com/
- group: auth
  title: ''
  type: Security
  url: https://www.pepperi.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pepperi.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/pepperi/security/pepperi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pepperi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pepperi/security/pepperi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pepperi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pepperi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pepperi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pepperi.com/first-steps/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.pepperi.com/api-reference/
- group: company
  title: ''
  type: Blog
  url: https://www.pepperi.com/blog/
coverage:
  checked: '2026-10-27'
  detail: Developer portal pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developer.pepperi.com/api-reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Pepperi provides a unified B2B commerce platform that enables companies to plan, execute, and analyze their sales across channels. The solution offers mobile sales automation, e‑commerce, order management, and analytics, helping retailers and brands streamline B2B transactions and improve operational efficiency.
image: https://www.pepperi.com/wp-content/uploads/2023/10/pepperi-favicon_2x-transparent.png
layout: provider
modified: '2026-10-27'
name: Pepperi
nav: Providers
network: true
overview: 'Pepperi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B, Commerce, Retail, and Automation.


  Pepperi''s developer surface includes documentation, API reference, engineering blog, and 10 more developer resources.'
plans:
- name: Pepperi Plans Pricing
  plan_count: 0
  slug: pepperi-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Pepperi Rate Limits
  slug: pepperi-rate-limits
scopes:
- name: Pepperi Scopes
  scope_count: 0
  slug: pepperi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 44.7
  previous_composite: 27.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pepperi/pepperi-2026-11-03T141120.png
security:
- kind: authentication
  name: Pepperi Authentication
  slug: pepperi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pepperi Domain Security
  slug: pepperi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pepperi Trust Center
  slug: pepperi-trust-center
  summary_line: ISO 27001
slug: pepperi
tags:
- Company
- B2B
- Commerce
- Retail
- Automation
website: https://pepperi.com/
---
