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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Moonchild AI developer platform for MCP integration and design automation.
  name: Moonchild API
  slug: moonchild-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/moonchild/plans/moonchild-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moonchild-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/moonchild/llms/moonchild-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moonchild-llms.txt
- group: auth
  href: https://artifacts.apis.io/moonchild/well-known/moonchild-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moonchild-www-security.txt
- group: auth
  href: https://artifacts.apis.io/moonchild/well-known/moonchild-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/moonchild-help-security.txt
- group: agent
  href: https://artifacts.apis.io/moonchild/well-known/moonchild-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moonchild-well-known.yml
- group: other
  href: https://artifacts.apis.io/moonchild/hosts/moonchild-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moonchild-hosts.yml
- group: other
  href: https://artifacts.apis.io/moonchild/vendors/moonchild-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moonchild-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moonchild.ai/terms_of_service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moonchild.ai/privacy_policy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://moonchild.ai/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://moonchild.ai/developers
- group: company
  title: ''
  type: Blog
  url: https://moonchild.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.moonchild.ai/
- group: auth
  href: https://artifacts.apis.io/moonchild/security/moonchild-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moonchild-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moonchild.ai
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API host.
  evidence:
  - status: unreachable
    url: https://api.moonchild.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Moonchild AI provides a chat‑based design assistant that transforms product requirement documents into production‑ready UI screens. By leveraging AI, it helps product managers, designers, and developers accelerate design workflows, generate prototypes, and export code directly from design systems. The platform offers a web interface, Discord community, and studio tools for collaborative design, aiming to close the gap between product vision and implementation without scaling design teams.
layout: provider
modified: '2026-10-29'
name: Moonchild
nav: Providers
network: true
overview: 'Moonchild is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Design, Product, Collaboration, and Automation.


  Moonchild''s developer surface includes pricing, engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Moonchild Plans Pricing
  plan_count: 4
  slug: moonchild-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Moonchild Domain Security
  slug: moonchild-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moonchild
tags:
- AI
- Design
- Product
- Collaboration
- Automation
- Platform
website: https://www.moonchild.ai
---
