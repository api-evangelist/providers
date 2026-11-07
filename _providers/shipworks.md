---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/shipworks/authentication/shipworks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shipworks-authentication.yml
- group: auth
  href: https://artifacts.apis.io/shipworks/well-known/shipworks-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shipworks-status-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shipworks.com/terms-of-service/
- group: company
  title: ''
  type: Newsroom
  url: https://www.shipworks.com/company-info/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.shipworks.com/company-info/team/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shipworks.com/privacy-policy/
- group: commercial
  href: https://artifacts.apis.io/shipworks/plans/shipworks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shipworks-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/shipworks/well-known/shipworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shipworks-well-known.yml
- group: other
  href: https://artifacts.apis.io/shipworks/hosts/shipworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shipworks-hosts.yml
- group: other
  href: https://artifacts.apis.io/shipworks/vendors/shipworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shipworks-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shipworks.com/
- group: start
  title: ''
  type: Login
  url: https://www.shipworks.com/login/
- group: auth
  href: https://artifacts.apis.io/shipworks/security/shipworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shipworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipworks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.shipworks.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.shipworks.com/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://www.shipworks.com/developer/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.shipworks.com/developer/
- group: company
  title: ''
  type: Blog
  url: https://www.shipworks.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.shipworks.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shipworks.com/pricing/
coverage:
  checked: '2026-10-27'
  detail: The developer portal pages are rendered HTML with no machine‑readable OpenAPI or other contract available.
  evidence:
  - status: 200
    url: https://www.shipworks.com/developer/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: ShipWorks provides multi-carrier shipping software that helps e‑commerce businesses automate order fulfillment, print shipping labels, and manage high‑volume shipments. The platform integrates with major marketplaces, shopping carts, and ERP/WMS systems, offering features like batch label printing, rate shopping, and customizable workflows to reduce shipping costs and improve efficiency.
image: https://www.shipworks.com/wp-content/uploads/2021/10/Works-Graphics-How-to-Avoid-8-Common-Shipping-Mistakes-Feature-956x478-2.jpg
layout: provider
modified: '2026-10-27'
name: ShipWorks
nav: Providers
network: true
overview: 'ShipWorks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, E-Commerce, Logistics, Software, and Integration.


  ShipWorks'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 14 more developer resources.'
plans:
- name: Shipworks Plans Pricing
  plan_count: 4
  slug: shipworks-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Shipworks Rate Limits
  slug: shipworks-rate-limits
scopes:
- name: Shipworks Scopes
  scope_count: 0
  slug: shipworks-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 51.8
    operational_transparency: 18.4
  previous_composite: 31.1
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shipworks/shipworks-2026-11-03T143135.png
security:
- kind: authentication
  name: Shipworks Authentication
  slug: shipworks-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shipworks Domain Security
  slug: shipworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipworks
tags:
- Shipping
- E-Commerce
- Logistics
- Software
- Integration
website: https://www.shipworks.com/
---
