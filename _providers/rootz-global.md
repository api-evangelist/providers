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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Rootz developer dashboard (no public machine‑readable API contract found)
  name: Rootz API
  slug: rootz-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/rootz-global/plans/rootz-global-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rootz-global-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/rootz-global/llms/rootz-global-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rootz-global-llms.txt
- group: other
  href: https://artifacts.apis.io/rootz-global/hosts/rootz-global-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rootz-global-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://rootz.global/team
- group: docs
  title: ''
  type: Documentation
  url: https://dev.rootz.global/
- group: auth
  href: https://artifacts.apis.io/rootz-global/security/rootz-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rootz-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rootz.global/
- group: company
  title: ''
  type: Blog
  url: https://rootz.global/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rootz.global/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rootz.global/terms
coverage:
  checked: '2026-10-29'
  detail: All attempted OpenAPI endpoints (e.g., https://dashboard.rootz.global/openapi.json) returned HTML pages, not a machine‑readable spec.
  evidence:
  - status: 200
    url: https://dashboard.rootz.global/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'Rootz builds Measured AI: a quality system for the AI factory that consumes the output of TCG standards and confidential compute. Every AI output gets a stated quality level, a measured origin, and a signed owner — so a buyer can know which model, on which machine, under whose signed instruction, produced a given answer.'
image: https://rootz.global/assets/rootz-logo.svg
layout: provider
modified: '2026-10-29'
name: rootz-global
nav: Providers
network: true
overview: 'rootz-global is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Quality, DataOwnership, and ConfidentialComputing.


  rootz-global''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Rootz Global Plans Pricing
  plan_count: 7
  slug: rootz-global-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Rootz Global Rate Limits
  slug: rootz-global-rate-limits
scopes:
- name: Rootz Global Scopes
  scope_count: 0
  slug: rootz-global-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rootz Global Authentication
  slug: rootz-global-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rootz Global Domain Security
  slug: rootz-global-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rootz-global
tags:
- Company
- AI
- Quality
- DataOwnership
- ConfidentialComputing
website: https://rootz.global/
---
