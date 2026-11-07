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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public RMM API documentation for Nizlo, describing endpoints for remote monitoring and management.
  name: Nizlo RMM API
  slug: nizlo-rmm-api
- baseURL: https://app.nizlo.com
  baseurl_source: declared
  description: 'Nizlo API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Nizlo API
  slug: nizlo-com-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/nizlo-com/plans/nizlo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nizlo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nizlo-com/rules/nizlo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/nizlo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/nizlo-com/vocabulary/nizlo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nizlo-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nizlo-com/conformance/nizlo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nizlo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nizlo-com/llms/nizlo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nizlo-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/nizlo-com/well-known/nizlo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nizlo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/nizlo-com/well-known/nizlo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nizlo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/nizlo-com/well-known/nizlo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nizlo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/nizlo-com/hosts/nizlo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nizlo-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nizlo.com/terms
- group: auth
  title: ''
  type: Security
  url: https://nizlo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nizlo.com/privacy
- group: start
  title: ''
  type: Login
  url: https://nizlo.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://nizlo.com/guides/msp-client-onboarding-checklist
- group: auth
  href: https://artifacts.apis.io/nizlo-com/security/nizlo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nizlo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nizlo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nizlo.com/rmm-api
- group: commercial
  title: ''
  type: Pricing
  url: https://nizlo.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://nizlo.com/support
- group: docs
  title: ''
  type: Documentation
  url: https://nizlo.com/rmm-api
coverage:
  checked: '2026-11-06'
  detail: Documentation pages exist but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract was found.
  evidence:
  - status: 200
    url: https://nizlo.com/rmm-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Nizlo is an earlier-stage, Windows-first remote monitoring and management (RMM) platform for MSPs and IT teams. It offers public flat monthly pricing, unlimited RMM endpoints, and a self‑serve 14‑day trial. The service enables monitoring, patching, automation, and remote support of Windows endpoints from a single console, targeting managed service providers and internal IT departments.
image: https://nizlo.com/opengraph-image
layout: provider
modified: '2026-11-05'
name: Nizlo
nav: Providers
network: true
overview: 'Nizlo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RMM, Remote Monitoring, MSP, and Windows.


  The Nizlo catalog on APIs.io includes 1 Spectral governance ruleset.


  Nizlo''s developer surface includes getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Nizlo Com Plans Pricing
  plan_count: 3
  slug: nizlo-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Nizlo API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: nizlo-com-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nizlo Com Domain Security
  slug: nizlo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nizlo-com
tags:
- Company
- RMM
- Remote Monitoring
- MSP
- Windows
website: https://nizlo.com/
---
