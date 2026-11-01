---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Invokera provides a platform that turns a project URL into tools usable by AI agents, offering a REST API documented at the public docs site.
  name: Invokera API
  slug: invokera-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/invokera-com/plans/invokera-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/invokera-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/invokera-com/llms/invokera-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/invokera-com-llms.txt
- group: other
  href: https://artifacts.apis.io/invokera-com/hosts/invokera-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/invokera-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/invokera-com/vendors/invokera-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/invokera-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/invokera-com/security/invokera-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invokera-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://invokera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://invokera.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://invokera.com/app/
- group: commercial
  title: ''
  type: Pricing
  url: https://invokera.com/pricing
- group: other
  title: ''
  type: Directory
  url: https://invokera.com/directory
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the documented API host.
  evidence:
  - status: 0
    url: https://api.invokera.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Invokera provides a platform that turns a project URL into tools usable by AI agents. It offers a Claude Skill, an MCP server, and a REST API, enabling agents like Claude and Cursor to interact with projects via generated APIs. Users can import OpenAPI specs, curl commands, or Postman collections, and obtain hosted or self‑hosted endpoints. The service includes a public directory, pricing plans, and documentation for quick start, import, domain verification, and automation.
layout: provider
modified: '2026-10-29'
name: invokera-com
nav: Providers
network: true
overview: 'invokera-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Automation, Platform, Tools, and Integration.


  invokera-com''s developer surface includes documentation, pricing, and 8 more developer resources.'
plans:
- name: Invokera Com Plans Pricing
  plan_count: 3
  slug: invokera-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Invokera Com Rate Limits
  slug: invokera-com-rate-limits
scopes:
- name: Invokera Com Scopes
  scope_count: 0
  slug: invokera-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Invokera Com Authentication
  slug: invokera-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Invokera Com Domain Security
  slug: invokera-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: invokera-com
tags:
- AI
- Automation
- Platform
- Tools
- Integration
- Company
website: https://invokera.com/
---
