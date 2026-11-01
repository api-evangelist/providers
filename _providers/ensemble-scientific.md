---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Talk to Ensemble Scientific about autonomous irrigation for your farm. Get in touch to book a demo or ask about PulseLogic and RadSum deployments.
  name: Ensemble Scientific API
  slug: ensemble-scientific-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/ensemble-scientific/hosts/ensemble-scientific-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ensemble-scientific-hosts.yml
- group: other
  href: https://artifacts.apis.io/ensemble-scientific/vendors/ensemble-scientific-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ensemble-scientific-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.esci.io/
- group: auth
  href: https://artifacts.apis.io/ensemble-scientific/security/ensemble-scientific-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ensemble-scientific-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://esci.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.esci.io/
- group: operate
  title: ''
  type: Support
  url: https://www.esci.io/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.esci.io/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esci.io/privacy
coverage:
  checked: '2026-10-28'
  detail: Spec URLs on app.esci.io return HTML pages, not machine‑readable OpenAPI documents.
  evidence:
  - status: 200
    url: https://app.esci.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Ensemble Scientific combines real-time sensors, forecasting, and autonomous irrigation systems for efficient water management. Based in British Columbia, they provide smart irrigation control for modern farms, offering hardware and a cloud platform to monitor, optimize, and automate watering across zones, reducing water use and improving yields for crops such as berries, strawberries, and other field produce.
image: https://www.esci.io/og/og-default.jpg
layout: provider
modified: '2026-10-28'
name: Ensemble Scientific (ESCI)
nav: Providers
network: true
overview: 'Ensemble Scientific (ESCI) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Irrigation, Smart Farming, IoT, and Water Management.


  Ensemble Scientific (ESCI)''s developer surface includes support, signup flow, and 7 more developer resources.'
plans:
- name: Ensemble Scientific Plans Pricing
  plan_count: 0
  slug: ensemble-scientific-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Ensemble Scientific Rate Limits
  slug: ensemble-scientific-rate-limits
scopes:
- name: Ensemble Scientific Scopes
  scope_count: 0
  slug: ensemble-scientific-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ensemble Scientific Authentication
  slug: ensemble-scientific-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ensemble Scientific Domain Security
  slug: ensemble-scientific-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ensemble-scientific
tags:
- Agriculture
- Irrigation
- Smart Farming
- IoT
- Water Management
- Canada
website: https://esci.io/
---
