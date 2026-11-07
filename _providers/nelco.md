---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Nelco provides tax form and electronic filing integration APIs for software partners.
  name: Nelco API
  slug: nelco-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/nelco/hosts/nelco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nelco-hosts.yml
- group: other
  href: https://artifacts.apis.io/nelco/vendors/nelco-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nelco-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nelco/security/nelco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nelco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nelcosolutions.com/
- group: operate
  title: ''
  type: Support
  url: https://www.nelcosolutions.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nelcosolutions.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nelcosolutions.com/terms-of-use/
coverage:
  checked: '2026-10-28'
  detail: GraphQL endpoint https://www.nelcosolutions.com/graphql requires authentication, returning 401, preventing access to the schema.
  evidence:
  - status: 401
    url: https://www.nelcosolutions.com/graphql
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Nelco partners with over 100 software companies to provide compatible and compliant tax forms and electronic filing solutions. As your software’s authorized partner, Nelco offers a wide selection of W‑2, 1099, and other tax documents, ensuring users can file quickly and accurately. With a 100% satisfaction guarantee and a focus on saving time, Nelco helps software vendors integrate seamless filing capabilities for their customers.
image: https://cdn11.bigcommerce.com/s-fssudep34y/product_images/nelco-icon.png?t=1615822189
layout: provider
modified: '2026-10-28'
name: Nelco
nav: Providers
network: true
overview: 'Nelco is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tax Forms, Software Integration, Electronic Filing, Compliance, and Partners.


  Nelco''s developer surface includes support and 6 more developer resources.'
plans:
- name: Nelco Plans Pricing
  plan_count: 0
  slug: nelco-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Nelco Rate Limits
  slug: nelco-rate-limits
scopes:
- name: Nelco Scopes
  scope_count: 0
  slug: nelco-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nelco/nelco-2026-11-03T140108.png
security:
- kind: authentication
  name: Nelco Authentication
  slug: nelco-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nelco Domain Security
  slug: nelco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nelco
tags:
- Tax Forms
- Software Integration
- Electronic Filing
- Compliance
- Partners
website: https://nelcosolutions.com/
---
