---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Coremodels Io Agentic Access
  operation_count: 8
  slug: coremodels-io-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: CoreModels' HTTP REST API (placeholder) – documented inside the product at https://go.coremodels.io.
  name: CoreModels API
  slug: coremodels-api
- baseURL: https://go.coremodels.io
  baseurl_source: declared
  description: The IntegrationApi API from coremodels-io — 7 operation(s) for integrationapi.
  name: coremodels-io Integration API
  slug: coremodels-io-integrationapi-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/coremodels-io/agentic-access/coremodels-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coremodels-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/coremodels-io/plans/coremodels-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coremodels-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coremodels-io/rules/coremodels-io-rules.yml
  title: ''
  type: Spectral
  url: rules/coremodels-io-rules.yml
- group: agent
  href: https://artifacts.apis.io/coremodels-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coremodels-io/data-model/coremodels-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coremodels-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/coremodels-io/changelog/coremodels-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coremodels-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/coremodels-io/authentication/coremodels-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coremodels-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/coremodels-io/conformance/coremodels-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coremodels-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coremodels-io/llms/coremodels-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coremodels-io-llms.txt
- group: other
  href: https://artifacts.apis.io/coremodels-io/a2a/coremodels-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coremodels-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/coremodels-io/well-known/coremodels-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coremodels-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/coremodels-io/hosts/coremodels-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coremodels-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/coremodels-io/vendors/coremodels-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coremodels-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.coremodels.io/legal/security
- group: start
  title: ''
  type: Sandbox
  url: https://www.coremodels.io/playground
- group: start
  title: ''
  type: Login
  url: https://go.coremodels.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.coremodels.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.coremodels.io/recipe/airbyte/source-onboarding-review
- group: auth
  href: https://artifacts.apis.io/coremodels-io/security/coremodels-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coremodels-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coremodels.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coremodels.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coremodels.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coremodels.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coremodels.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coremodels.io/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coremodels
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://coremodels.io/openapi.json
  - status: null
    url: https://learn.coremodels.io/openapi.json
  - status: 401
    url: https://go.coremodels.io/mcp
  - status: 200
    url: https://coremodels.io/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: CoreModels provides a platform for importing, mapping, and exporting data schemas, enabling developers to build agents that understand and act on structured data. The service offers a low‑code environment for creating content models, integrates with various data sources, and exposes an MCP endpoint for agents to query. CoreModels aims to simplify data integration across applications, supporting schema versioning, transformation, and reuse.
image: https://www.coremodels.io/favicon.ico
layout: provider
modified: '2026-10-29'
name: coremodels-io
nav: Providers
network: true
overview: 'coremodels-io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Integration API, and 1 more. Tagged areas include Company, Data-Modeling, API-Platform, Integration, and Schema-Mapping.


  The coremodels-io catalog on APIs.io includes 1 Spectral governance ruleset.


  coremodels-io''s developer surface includes changelog, authentication, sandbox, getting-started guide, documentation, pricing, and 20 more developer resources.'
plans:
- name: Coremodels Io Plans Pricing
  plan_count: 3
  slug: coremodels-io-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Coremodels Io Rate Limits
  slug: coremodels-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: coremodels-io API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: coremodels-io-rules
scopes:
- name: Coremodels Io Scopes
  scope_count: 0
  slug: coremodels-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 32.4
    developer_ergonomics: 56.4
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coremodels Io Authentication
  slug: coremodels-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Coremodels Io Domain Security
  slug: coremodels-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: create-node
  slug: coremodels-io-create-node
- name: fetch-node
  slug: coremodels-io-fetch-node
- name: fetch-nodes
  slug: coremodels-io-fetch-nodes
- name: update-node
  slug: coremodels-io-update-node
slug: coremodels-io
tags:
- Company
- Data-Modeling
- API-Platform
- Integration
- Schema-Mapping
website: https://coremodels.io/
---
