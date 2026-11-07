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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/antofagasta/hosts/antofagasta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antofagasta-hosts.yml
- group: other
  href: https://artifacts.apis.io/antofagasta/vendors/antofagasta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/antofagasta-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.antofagasta.co.uk/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.antofagasta.co.uk/privacy-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://www.antofagasta.co.uk/media/news/
- group: auth
  href: https://artifacts.apis.io/antofagasta/security/antofagasta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antofagasta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.antofagasta.co.uk/
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or machine‑readable contract was found on the company’s website.
  evidence:
  - status: 200
    url: https://www.antofagasta.co.uk/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Antofagasta PLC is a multinational mining company focused on the extraction and processing of copper, gold, and other minerals. It operates globally with a strong emphasis on sustainable practices, community engagement, and technological innovation. The company provides data services and investor information through its corporate website, offering insights into operations, financial performance, and environmental stewardship.
layout: provider
modified: '2026-11-01'
name: Antofagasta PLC
nav: Providers
network: true
overview: Antofagasta PLC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Copper, Gold, Sustainable, and Investor Relations.
plans:
- name: Antofagasta Plans Pricing
  plan_count: 0
  slug: antofagasta-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Antofagasta Rate Limits
  slug: antofagasta-rate-limits
scopes:
- name: Antofagasta Scopes
  scope_count: 0
  slug: antofagasta-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 10.1
  provenance:
    conformance: unknown
    mcp: unknown
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
security:
- kind: authentication
  name: Antofagasta Authentication
  slug: antofagasta-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Antofagasta Domain Security
  slug: antofagasta-domain-security
  summary_line: TLSv1.3
slug: antofagasta
tags:
- Mining
- Copper
- Gold
- Sustainable
- Investor Relations
website: https://www.antofagasta.co.uk/
---
