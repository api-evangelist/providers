---
access_model:
  confidence: low
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/foundation-software/security/foundation-software-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/foundation-software-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/foundation-software/llms/foundation-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/foundation-software-llms.txt
- group: other
  href: https://artifacts.apis.io/foundation-software/hosts/foundation-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foundation-software-hosts.yml
- group: other
  href: https://artifacts.apis.io/foundation-software/vendors/foundation-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/foundation-software-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.foundationsoft.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.foundationsoft.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.foundationsoft.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.foundationsoft.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.foundationsoft.com/
- group: auth
  href: https://artifacts.apis.io/foundation-software/security/foundation-software-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/foundation-software-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/foundation-software/security/foundation-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foundation-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.foundationsoft.com/
coverage:
  checked: '2026-10-28'
  detail: No machine‑readable API specification (OpenAPI/GraphQL/etc.) was found on any discovered host; only HTML placeholder pages were returned.
  evidence:
  - status: 200
    url: https://developer.foundationsoft.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Foundation Software provides construction accounting software designed for contractors, offering job costing, payroll, invoicing, vendor payments, and financial reporting in a unified cloud-based system. The platform enables real-time visibility into project expenses, streamlines payroll processing, and supports CPA tools, helping construction businesses manage finances from anywhere.
image: https://www.foundationsoft.com/wp-content/uploads/2021/04/2nd-Section.jpg
layout: provider
modified: '2026-10-28'
name: Foundation
nav: Providers
network: true
overview: 'Foundation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Accounting, Software, Contractors, and ERP.


  Foundation''s developer surface includes support, pricing, documentation, and 9 more developer resources.'
plans:
- name: Foundation Software Plans Pricing
  plan_count: 0
  slug: foundation-software-plans-pricing
random_paper: 7
scopes:
- name: Foundation Software Scopes
  scope_count: 0
  slug: foundation-software-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.2
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/foundation-software/foundation-software-2026-11-03T132309.png
security:
- kind: authentication
  name: Foundation Software Authentication
  slug: foundation-software-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Foundation Software Domain Security
  slug: foundation-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Foundation Software Vulnerability Disclosure
  slug: foundation-software-vulnerability-disclosure
  summary_line: no policy recorded
slug: foundation-software
tags:
- Construction
- Accounting
- Software
- Contractors
- ERP
website: https://www.foundationsoft.com/
---
