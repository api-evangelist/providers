---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'CleanSlice API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CleanSlice API
  slug: cleanslice-org-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/cleanslice-org/rules/cleanslice-org-rules.yml
  title: ''
  type: Spectral
  url: rules/cleanslice-org-rules.yml
- group: design
  href: https://artifacts.apis.io/cleanslice-org/json-ld/cleanslice-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cleanslice-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/cleanslice-org/vocabulary/cleanslice-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cleanslice-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cleanslice-org/data-model/cleanslice-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cleanslice-org-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cleanslice-org/authentication/cleanslice-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cleanslice-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/cleanslice-org/conformance/cleanslice-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleanslice-org-conformance.yml
- group: other
  href: https://artifacts.apis.io/cleanslice-org/hosts/cleanslice-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleanslice-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/cleanslice-org/vendors/cleanslice-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleanslice-org-vendors.yml
- group: build
  href: https://artifacts.apis.io/cleanslice-org/packages/cleanslice-org-packages.yml
  title: ''
  type: SDKs
  url: packages/cleanslice-org-packages.yml
- group: build
  href: https://artifacts.apis.io/cleanslice-org/packages/cleanslice-org-packages.yml
  title: ''
  type: Packages
  url: packages/cleanslice-org-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cleanslice
- group: start
  title: ''
  type: GettingStarted
  url: https://cleanslice.org/backend/getting-started.html
- group: auth
  href: https://artifacts.apis.io/cleanslice-org/security/cleanslice-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleanslice-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleanslice.org/
created: '2026-11-03'
description: CleanSlice provides an AI‑first full‑stack architecture framework built on NestJS and Nuxt. It enables developers to compose vertical slices—self‑contained feature modules—following clean‑architecture principles, with built‑in guidance via the Model Context Protocol (MCP). The platform offers tooling, standards, and examples for TypeScript, Prisma, Tailwind, and more, helping teams build scalable applications without AI drift.
json_schemas:
- name: GetUsersIdResponse
  property_count: 2
  slug: cleanslice-org-get-users-id-response
- name: GetUsersResponse
  property_count: 2
  slug: cleanslice-org-get-users-response
- name: PostUsersRequest
  property_count: 1
  slug: cleanslice-org-post-users-request
- name: PostUsersResponse
  property_count: 5
  slug: cleanslice-org-post-users-response
- name: PutUsersIdRequest
  property_count: 1
  slug: cleanslice-org-put-users-id-request
- name: PutUsersIdResponse
  property_count: 1
  slug: cleanslice-org-put-users-id-response
jsonld:
- class_count: 6
  name: Cleanslice Org Context
  property_count: 7
  slug: cleanslice-org-context
layout: provider
modified: '2026-11-03'
name: CleanSlice
nav: Providers
network: true
overview: 'CleanSlice is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, Full‑Stack Framework, NestJS, Nuxt, and AI Agents.


  The CleanSlice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CleanSlice''s developer surface includes authentication, getting-started guide, and 12 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: CleanSlice API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: cleanslice-org-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 22.6
    developer_ergonomics: 25.0
    discoverability: 53.6
    operational_transparency: 2.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cleanslice Org Authentication
  slug: cleanslice-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cleanslice Org Domain Security
  slug: cleanslice-org-domain-security
  summary_line: TLSv1.3
slug: cleanslice-org
tags:
- Architecture
- Full‑Stack Framework
- NestJS
- Nuxt
- AI Agents
- Deployment Platform
- TypeScript
website: https://cleanslice.org/
---
