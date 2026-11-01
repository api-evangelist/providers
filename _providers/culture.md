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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation not publicly available; the provider's site offers consulting services.
  name: Culture API
  slug: culture-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/culture/llms/culture-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/culture-llms.txt
- group: other
  href: https://artifacts.apis.io/culture/hosts/culture-hosts.yml
  title: ''
  type: Hosts
  url: hosts/culture-hosts.yml
- group: other
  href: https://artifacts.apis.io/culture/vendors/culture-vendors.yml
  title: ''
  type: Vendors
  url: vendors/culture-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://culturepartners.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://culturepartners.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/culture/security/culture-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/culture-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://culturepartners.com/
coverage:
  checked: '2026-10-12'
  detail: The provider's host trust.culturepartners.com returns HTML for typical OpenAPI URLs, with no machine‑readable contract discovered.
  evidence:
  - status: 200
    url: https://trust.culturepartners.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Culture Partners provides organizational culture consulting, helping companies achieve better results through clarity, alignment, and accountability. Their services include strategic alignment, executive leadership consulting, change activation, and industry‑specific solutions such as healthcare and manufacturing. The firm leverages 37 years of research and proprietary IP to drive measurable outcomes like increased EBITDA and employee NPS.
image: https://culturepartners.com/favicon.ico
layout: provider
modified: '2026-10-11'
name: Culture
nav: Providers
network: true
overview: Culture is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, OrganizationalCulture, Change Management, and Leadership.
random_paper: 4
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 9.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Culture Domain Security
  slug: culture-domain-security
  summary_line: TLSv1.3 · DMARC
slug: culture
tags:
- Company
- Consulting
- OrganizationalCulture
- Change Management
- Leadership
website: https://culturepartners.com/
---
