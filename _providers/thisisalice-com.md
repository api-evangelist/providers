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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/thisisalice-com/vendors/thisisalice-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thisisalice-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/thisisalice-com/llms/thisisalice-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thisisalice-com-llms.txt
- group: other
  href: https://artifacts.apis.io/thisisalice-com/hosts/thisisalice-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thisisalice-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thisisalice.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thisisalice.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.thisisalice.com/press/
- group: start
  title: ''
  type: Login
  url: https://app.thisisalice.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://help.thisisalice.com/category/11-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.thisisalice.com/
- group: auth
  href: https://artifacts.apis.io/thisisalice-com/security/thisisalice-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thisisalice-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thisisalice.com
coverage:
  checked: '2026-10-25'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable contract extraction.
  evidence:
  - status: 200
    url: https://www.thisisalice.com/select/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Alice provides a modern pretax spending platform that automates employee benefits, helping users keep more of their earnings. The service offers a seamless experience for managing pretax contributions, expense tracking, and compliance, targeting both employers and employees seeking efficient benefit administration.
layout: provider
modified: '2026-10-25'
name: Alice
nav: Providers
network: true
overview: 'Alice is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Benefits, Payroll, and Employee Experience.


  Alice''s developer surface includes getting-started guide, documentation, and 9 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 52.7
    operational_transparency: 0.0
  previous_composite: 15.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thisisalice-com/thisisalice-com-2026-11-03T144658.png
security:
- kind: domain-security
  name: Thisisalice Com Domain Security
  slug: thisisalice-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thisisalice-com
tags:
- Company
- Fintech
- Benefits
- Payroll
- Employee Experience
website: https://thisisalice.com
---
