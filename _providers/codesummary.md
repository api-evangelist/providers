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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Code Summary API provides endpoints for managing documentation, knowledge extraction, and integration with code repositories.
  name: Code Summary API
  slug: code-summary-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/codesummary/refs/heads/main/plans/codesummary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codesummary-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/codesummary/refs/heads/main/llms/codesummary-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/codesummary-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/codesummary/refs/heads/main/well-known/codesummary-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/codesummary-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codesummary/refs/heads/main/hosts/codesummary-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codesummary-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codesummary/refs/heads/main/vendors/codesummary-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codesummary-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://dashboard.codesummary.io/auth/signin
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codesummary/refs/heads/main/security/codesummary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codesummary-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codesummary.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://codesummary.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://codesummary.io/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codesummary.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codesummary.io/privacy/
coverage:
  checked: '2026-10-16'
  detail: OpenAPI endpoints return HTML pages instead of machine‑readable JSON/YAML, preventing contract discovery.
  evidence:
  - status: 200
    url: https://codesummary.io/openapi.json
  - status: 200
    url: https://codesummary.io/openapi.yaml
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Code Summary provides a platform that synthesizes source code repositories into structured, reviewed knowledge systems. It offers hosted documentation, AI‑agent context, and team workflow tools, enabling developers to generate, edit, and publish living documentation that stays in sync with code changes. Users can start a free trial, explore pricing plans, and integrate the service with their repositories for continuous knowledge updates.
layout: provider
modified: '2026-10-16'
name: Code Summary
nav: Providers
network: true
overview: 'Code Summary is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Documentation, Artificial Intelligence, Knowledge, and Platform.


  Code Summary''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Codesummary Plans Pricing
  plan_count: 3
  slug: codesummary-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Codesummary Domain Security
  slug: codesummary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codesummary
tags:
- Company
- Documentation
- Artificial Intelligence
- Knowledge
- Platform
website: https://codesummary.io/
---
