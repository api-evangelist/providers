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
- description: API for managing battery swapping stations and operator integration.
  name: Swap API
  slug: swap-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/swap-id/llms/swap-id-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swap-id-llms.txt
- group: other
  href: https://artifacts.apis.io/swap-id/hosts/swap-id-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swap-id-hosts.yml
- group: other
  href: https://artifacts.apis.io/swap-id/vendors/swap-id-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swap-id-vendors.yml
- group: auth
  href: https://artifacts.apis.io/swap-id/security/swap-id-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swap-id-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swap.id
- group: company
  title: ''
  type: Blog
  url: https://www.swap.id/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swap.id/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swap.id/terms-and-conditions
coverage:
  checked: '2026-10-29'
  detail: The provider's website returns HTTP 400 for standard OpenAPI spec URLs, and no machine‑readable API documentation is available.
  evidence:
  - status: 400
    url: https://www.swap.id/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Swap provides city‑based infrastructure of battery swapping stations for e‑motorcycle riders, enabling rapid battery exchange in 9 seconds. This service reduces range anxiety, supports sustainable urban mobility, and offers a platform for operators to manage stations, monitor usage, and integrate with smart city initiatives, fostering a greener transportation ecosystem across multiple cities.
image: https://static.parastorage.com/media/dc3d7c_210906a34eff431fae1fec2d75663b80%7Emv2.jpg/v1/fill/w_192%2Ch_192%2Clg_1%2Cusm_0.66_1.00_0.01/dc3d7c_210906a34eff431fae1fec2d75663b80%7Emv2.jpg
layout: provider
modified: '2026-10-28'
name: swap
nav: Providers
network: true
overview: 'swap is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Mobility, Battery, and Infrastructure.


  swap''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Swap Id Plans Pricing
  plan_count: 0
  slug: swap-id-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Swap Id Rate Limits
  slug: swap-id-rate-limits
scopes:
- name: Swap Id Scopes
  scope_count: 0
  slug: swap-id-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Swap Id Authentication
  slug: swap-id-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Swap Id Domain Security
  slug: swap-id-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swap-id
tags:
- Company
- Energy
- Mobility
- Battery
- Infrastructure
- IoT
website: https://swap.id
---
