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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/easecentral/hosts/easecentral-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easecentral-hosts.yml
- group: other
  href: https://artifacts.apis.io/easecentral/vendors/easecentral-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easecentral-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.easecentral.com/security/
- group: auth
  href: https://artifacts.apis.io/easecentral/security/easecentral-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easecentral-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.easecentral.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.easecentral.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.easecentral.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.easecentral.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.easecentral.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.easecentral.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.easecentral.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.easecentral.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.easecentral.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.easecentral.com/privacy
coverage:
  checked: '2026-10-24'
  detail: Home page renders a JavaScript shell with no machine‑readable spec discovered despite rendered attempts.
  evidence:
  - status: 200
    url: https://www.easecentral.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: EaseCentral provides an employee benefits administration platform designed for insurance brokers and employers. The web‑based solution enables online enrollment, benefits plan management, compliance tools, and HR resources, serving thousands of businesses across the United States. It integrates with payroll, offers document libraries, and supports multi‑employer portals, aiming to simplify benefits administration for modern broker workflows.
image: https://www.easecentral.com/easecentral.png
layout: provider
modified: '2026-10-24'
name: EaseCentral
nav: Providers
network: true
overview: 'EaseCentral is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Benefits, Human Resources, Insurance, Software-as-a-Service, and Brokerage.


  EaseCentral''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 20.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/easecentral/easecentral-2026-11-03T131223.png
security:
- kind: domain-security
  name: Easecentral Domain Security
  slug: easecentral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easecentral
tags:
- Benefits
- Human Resources
- Insurance
- Software-as-a-Service
- Brokerage
website: https://www.easecentral.com
---
