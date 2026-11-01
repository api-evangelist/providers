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
- description: Booking API for local services across the United States, enabling AI agents to book tradespeople such as plumbers, electricians, HVAC technicians, and other categories.
  name: Sunrays Booking API
  slug: booking-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/sunrays-dev/llms/sunrays-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sunrays-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/sunrays-dev/well-known/sunrays-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sunrays-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/sunrays-dev/hosts/sunrays-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sunrays-dev-hosts.yml
- group: auth
  href: https://artifacts.apis.io/sunrays-dev/security/sunrays-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sunrays-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sunrays.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://sunrays.dev/llms-full.txt
- group: docs
  title: ''
  type: APIReference
  url: https://sunrays.dev/llms-full.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sunrays.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sunrays.dev/privacy
coverage:
  checked: '2026-10-31'
  detail: OpenAPI and other contract URLs on sunrays.dev and its subdomains return 404, and no documentation host is provided.
  evidence:
  - status: 404
    url: https://sunrays.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Sunrays.dev provides an agent-callable booking API for local services across the United States. It enables AI agents to deterministically and idempotently book tradespeople such as plumbers, electricians, HVAC technicians, and many other categories via MCP tool calls. The service is transactional, integrates with Stripe for payment capture, and returns confirmed bookings with receipts. All endpoints are public HTTP APIs without requiring DOM scraping, and the platform supplies full documentation via llms-full.txt.
image: https://sunrays.dev/logo.svg
layout: provider
modified: '2026-10-31'
name: sunrays-dev
nav: Providers
network: true
overview: 'sunrays-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Booking, Local-Services, MCP, and Agent-Callable.


  sunrays-dev''s developer surface includes documentation, API reference, and 7 more developer resources.'
random_paper: 1
scopes:
- name: Sunrays Dev Scopes
  scope_count: 0
  slug: sunrays-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sunrays Dev Authentication
  slug: sunrays-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sunrays Dev Domain Security
  slug: sunrays-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sunrays-dev
tags:
- Company
- Booking
- Local-Services
- MCP
- Agent-Callable
- API
website: https://sunrays.dev/
---
