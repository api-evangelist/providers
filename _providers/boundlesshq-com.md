---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Boundless offers APIs for its platform, but they are gated behind authentication and not publicly documented.
  name: Boundless API
  slug: boundless-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/boundlesshq-com/plans/boundlesshq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boundlesshq-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/boundlesshq-com/llms/boundlesshq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boundlesshq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/boundlesshq-com/well-known/boundlesshq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boundlesshq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boundlesshq-com/hosts/boundlesshq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boundlesshq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boundlesshq-com/vendors/boundlesshq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boundlesshq-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://boundlesshq.com/guides/
- group: auth
  href: https://artifacts.apis.io/boundlesshq-com/security/boundlesshq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boundlesshq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boundlesshq.com
- group: commercial
  title: ''
  type: Pricing
  url: https://boundlesshq.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://boundlesshq.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boundlesshq.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://boundlesshq.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boundlesshq
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec endpoints on https://app.boundlesshq.com return 403 Access Denied, indicating authentication is required.
  evidence:
  - status: 403
    url: https://app.boundlesshq.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Boundless provides Employer of Record (EOR) services that enable companies to hire international employees seamlessly. Through a global network of fully owned legal entities, Boundless handles payroll, taxes, benefits, and HR compliance across dozens of countries, allowing businesses to expand their workforce without establishing local subsidiaries. The platform emphasizes people‑first values, secure and compliant employment, and expert leadership to simplify global hiring and workforce management.
image: https://boundlesshq.com/wp-content/uploads/2025/12/boundless_icon_black.png
layout: provider
modified: '2026-10-28'
name: Boundless
nav: Providers
network: true
overview: 'Boundless is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employer of Record, Global Hiring, Payroll, and HR Compliance.


  Boundless'' developer surface includes documentation, pricing, engineering blog, support, and 9 more developer resources.'
plans:
- name: Boundlesshq Com Plans Pricing
  plan_count: 2
  slug: boundlesshq-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Boundlesshq Com Rate Limits
  slug: boundlesshq-com-rate-limits
scopes:
- name: Boundlesshq Com Scopes
  scope_count: 0
  slug: boundlesshq-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/boundlesshq-com/boundlesshq-com-2026-11-03T122358.png
security:
- kind: authentication
  name: Boundlesshq Com Authentication
  slug: boundlesshq-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Boundlesshq Com Domain Security
  slug: boundlesshq-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boundlesshq-com
tags:
- Company
- Employer of Record
- Global Hiring
- Payroll
- HR Compliance
- International Employment
website: https://boundlesshq.com
---
