---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Enzo Health Agentic Access
  operation_count: 2
  slug: enzo-health-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://app.enzo.health
  baseurl_source: declared
  description: The Workflow Runs API from Enzo Health — 2 operation(s) for workflow runs.
  name: Enzo Health Workflow Runs API
  slug: enzo-health-workflow-runs-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/enzo-health/agentic-access/enzo-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enzo-health-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/enzo-health/rules/enzo-health-rules.yml
  title: ''
  type: Spectral
  url: rules/enzo-health-rules.yml
- group: design
  href: https://artifacts.apis.io/enzo-health/json-ld/enzo-health-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/enzo-health-context.jsonld
- group: design
  href: https://artifacts.apis.io/enzo-health/vocabulary/enzo-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/enzo-health-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/enzo-health/data-model/enzo-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/enzo-health-data-model.yml
- group: design
  href: https://artifacts.apis.io/enzo-health/errors/enzo-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/enzo-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/enzo-health/conformance/enzo-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enzo-health-conformance.yml
- group: agent
  href: https://artifacts.apis.io/enzo-health/llms/enzo-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enzo-health-llms.txt
- group: other
  href: https://artifacts.apis.io/enzo-health/a2a/enzo-health-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/enzo-health-a2a.yml
- group: auth
  href: https://artifacts.apis.io/enzo-health/well-known/enzo-health-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/enzo-health-help-security.txt
- group: agent
  href: https://artifacts.apis.io/enzo-health/well-known/enzo-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enzo-health-well-known.yml
- group: other
  href: https://artifacts.apis.io/enzo-health/hosts/enzo-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enzo-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/enzo-health/vendors/enzo-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enzo-health-vendors.yml
- group: auth
  href: https://artifacts.apis.io/enzo-health/authentication/enzo-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/enzo-health-authentication.yml
- group: auth
  href: https://artifacts.apis.io/enzo-health/security/enzo-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enzo-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enzo.health/
- group: docs
  title: ''
  type: Documentation
  url: https://www.enzo.health/
- group: docs
  title: ''
  type: APIReference
  url: https://www.enzo.health/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.enzo.health/signup
- group: company
  title: ''
  type: Blog
  url: https://www.enzo.health/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enzo.health/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enzo.health/privacy
created: '2026-10-24'
description: Enzo Health provides a cloud‑based home health electronic health record (EHR) platform that automates patient episode management, eligibility verification, scheduling, documentation, and billing. The solution integrates with payer systems, supports OASIS and QA workflows, and offers tools for care coordination, intake, and reporting, aiming to reduce manual overhead for home health agencies.
image: https://cdn.sanity.io/images/jmsbw5z6/production/05062c06ab5be317095f467ed800feb6c5f7702c-4800x2400.jpg?rect=104,0,4593,2400&w=1200&h=627&fit=crop&auto=format
jsonld:
- class_count: 2
  name: Enzo Health Context
  property_count: 4
  slug: enzo-health-context
layout: provider
modified: '2026-10-24'
name: Enzo Health
nav: Providers
network: true
overview: 'Enzo Health publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Workflow Runs API. Tagged areas include Company, Home Health, EHR, Healthcare, and SaaS.


  The Enzo Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Enzo Health''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, and 17 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Enzo Health API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: enzo-health-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.5
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Enzo Health Authentication
  slug: enzo-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Enzo Health Domain Security
  slug: enzo-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enzo-health
tags:
- Company
- Home Health
- EHR
- Healthcare
- SaaS
website: https://www.enzo.health/
---
