---
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/swapp1990-org/llms/swapp1990-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swapp1990-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/swapp1990-org/well-known/swapp1990-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swapp1990-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/swapp1990-org/hosts/swapp1990-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swapp1990-org-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://swapp1990.org/ambience-maker/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swapp1990.org/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swapp1990
- group: company
  title: ''
  type: Website
  url: https://swapp1990.org/
- group: auth
  href: https://artifacts.apis.io/swapp1990-org/security/swapp1990-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swapp1990-org-domain-security.yml
coverage:
  checked: '2026-10-30'
  detail: All probed spec endpoints on discovered hosts returned HTML pages, not machine‑readable OpenAPI/AsyncAPI/GraphQL specifications.
  evidence:
  - status: 200
    url: https://cars.swapp1990.org/openapi.json
  - status: 404
    url: https://swapp1990.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Swapp1990-org is a placeholder company entry harvested from the MCP registry. Currently, no official website, API documentation, or developer portal has been identified for this entity. The profile remains a stub pending further discovery and verification of any publicly available resources or services associated with the organization.
image: https://assets.apievangelist.com/logo.png
layout: provider
modified: '2026-10-30'
name: swapp1990-org
nav: Providers
network: true
overview: 'swapp1990-org is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Data, API, and Placeholder.


  swapp1990-org''s developer surface includes support and 7 more developer resources.'
plans:
- name: Swapp1990 Org Plans Pricing
  plan_count: 0
  slug: swapp1990-org-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Swapp1990 Org Rate Limits
  slug: swapp1990-org-rate-limits
scopes:
- name: Swapp1990 Org Scopes
  scope_count: 0
  slug: swapp1990-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Swapp1990 Org Authentication
  slug: swapp1990-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Swapp1990 Org Domain Security
  slug: swapp1990-org-domain-security
  summary_line: TLSv1.3
slug: swapp1990-org
tags:
- Company
- Technology
- Data
- API
- Placeholder
website: https://swapp1990.org/
---
