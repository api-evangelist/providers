---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CalendarBridge provides calendar syncing and scheduling features via its web application. No public machine‑readable API contract was found.
  name: CalendarBridge API
  slug: calendarbridge-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/calendarbridge/plans/calendarbridge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calendarbridge-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.calendarbridge.com/
- group: design
  href: https://artifacts.apis.io/calendarbridge/conformance/calendarbridge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calendarbridge-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calendarbridge/llms/calendarbridge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calendarbridge-llms.txt
- group: other
  href: https://artifacts.apis.io/calendarbridge/hosts/calendarbridge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calendarbridge-hosts.yml
- group: other
  href: https://artifacts.apis.io/calendarbridge/vendors/calendarbridge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calendarbridge-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calendarbridge.com/terms-and-privacy/
- group: operate
  title: ''
  type: Support
  url: https://help.calendarbridge.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calendarbridge.com/privacy-controls/
- group: start
  title: ''
  type: Login
  url: https://app.calendarbridge.com/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.calendarbridge.com/user-docs/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://help.calendarbridge.com/
- group: auth
  href: https://artifacts.apis.io/calendarbridge/security/calendarbridge-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/calendarbridge-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/calendarbridge/security/calendarbridge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calendarbridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calendarbridge.com
- group: company
  title: ''
  type: Blog
  url: https://calendarbridge.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://calendarbridge.com/pricing-individual/
- group: commercial
  title: ''
  type: Pricing
  url: https://calendarbridge.com/pricing-group/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are public HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered despite probing known paths.
  evidence:
  - status: 200
    url: https://app.calendarbridge.com/openapi.json
  - status: 404
    url: https://help.calendarbridge.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CalendarBridge syncs calendars together in real-time and provides scheduling pages built for people with multiple calendars. It enables seamless integration across Google, Outlook, and iCloud calendars, offering a unified view and automated scheduling to simplify coordination for individuals and teams.
image: https://calendarbridge.com/wp-content/uploads/2026/09/CalendarBridge.jpg
layout: provider
modified: '2026-11-03'
name: CalendarBridge
nav: Providers
network: true
overview: 'CalendarBridge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Calendar, Scheduling, and Integration.


  CalendarBridge''s developer surface includes support, getting-started guide, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Calendarbridge Plans Pricing
  plan_count: 8
  slug: calendarbridge-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calendarbridge Domain Security
  slug: calendarbridge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Calendarbridge Trust Center
  slug: calendarbridge-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: calendarbridge
tags:
- Company
- Calendar
- Scheduling
- Integration
website: https://calendarbridge.com
---
