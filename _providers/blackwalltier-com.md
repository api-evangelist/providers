---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Blackwalltier Com Agentic Access
  operation_count: 7
  slug: blackwalltier-com-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://blackwalltier.com/api
  baseurl_source: declared
  description: The Forecast API from blackwalltier-com — 2 operation(s) for forecast.
  name: blackwalltier-com Forecast API
  slug: blackwalltier-com-forecast-api
- baseURL: https://blackwalltier.com/api
  baseurl_source: declared
  description: The Keys API from blackwalltier-com — 1 operation(s) for keys.
  name: blackwalltier-com Keys API
  slug: blackwalltier-com-keys-api
- baseURL: https://blackwalltier.com/api
  baseurl_source: declared
  description: The Receipts API from blackwalltier-com — 2 operation(s) for receipts.
  name: blackwalltier-com Receipts API
  slug: blackwalltier-com-receipts-api
- baseURL: https://blackwalltier.com/api
  baseurl_source: declared
  description: The Usage API from blackwalltier-com — 1 operation(s) for usage.
  name: blackwalltier-com Usage API
  slug: blackwalltier-com-usage-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/blackwalltier-com/agentic-access/blackwalltier-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blackwalltier-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blackwalltier-com/rules/blackwalltier-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blackwalltier-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blackwalltier-com/json-ld/blackwalltier-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blackwalltier-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blackwalltier-com/vocabulary/blackwalltier-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blackwalltier-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blackwalltier-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blackwalltier-com/data-model/blackwalltier-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blackwalltier-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/blackwalltier-com/conventions/blackwalltier-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blackwalltier-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://blackwalltier.com/security
- group: auth
  href: https://artifacts.apis.io/blackwalltier-com/authentication/blackwalltier-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blackwalltier-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/blackwalltier-com/errors/blackwalltier-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blackwalltier-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blackwalltier-com/conformance/blackwalltier-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blackwalltier-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blackwalltier-com/llms/blackwalltier-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blackwalltier-com-llms.txt
- group: other
  href: https://artifacts.apis.io/blackwalltier-com/hosts/blackwalltier-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackwalltier-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blackwalltier-com/vendors/blackwalltier-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackwalltier-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/blackwalltier-com/packages/blackwalltier-com-packages.yml
  title: ''
  type: SDKs
  url: packages/blackwalltier-com-packages.yml
- group: build
  href: https://artifacts.apis.io/blackwalltier-com/packages/blackwalltier-com-packages.yml
  title: ''
  type: Packages
  url: packages/blackwalltier-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://blackwalltier.com/security
- group: docs
  title: ''
  type: APIReference
  url: https://blackwalltier.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/blackwalltier-com/security/blackwalltier-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blackwalltier-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/blackwalltier-com/security/blackwalltier-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blackwalltier-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blackwalltier-com/security/blackwalltier-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackwalltier-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackwalltier.com/
created: '2026-10-29'
description: Black_Wall provides a pre‑action outcome API for AI agents, reasoning about each AI‑agent action and catching risks that policy rules may miss, such as prompt injection, anomalies, and inadvertent exposure of personally identifiable information. The service offers a free tier and aims to gate actions with decisions like GO, CAUTION, or STOP before they run, helping organizations prevent damage from unexpected AI behavior.
image: https://blackwalltier.com/og.png
json_schemas:
- name: ApiKey
  property_count: 5
  slug: blackwalltier-com-api-key
- name: ForecastRequest
  property_count: 4
  slug: blackwalltier-com-forecast-request
- name: ForecastResponse
  property_count: 18
  slug: blackwalltier-com-forecast-response
- name: OutcomeReport
  property_count: 2
  slug: blackwalltier-com-outcome-report
- name: Receipt
  property_count: 9
  slug: blackwalltier-com-receipt
- name: UsageSummary
  property_count: 5
  slug: blackwalltier-com-usage-summary
jsonld:
- class_count: 7
  name: Blackwalltier Com Context
  property_count: 44
  slug: blackwalltier-com-context
layout: provider
modified: '2026-10-29'
name: blackwalltier-com
nav: Providers
network: true
overview: 'blackwalltier-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Forecast API, Keys API, Receipts API, and 1 more. Tagged areas include Company, AI, Security, Policy, and RiskManagement.


  The blackwalltier-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  blackwalltier-com''s developer surface includes authentication, API reference, and 20 more developer resources.'
plans:
- name: Blackwalltier Com Plans Pricing
  plan_count: 0
  slug: blackwalltier-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Blackwalltier Com Rate Limits
  slug: blackwalltier-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: blackwalltier-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: blackwalltier-com-rules
scopes:
- name: Blackwalltier Com Scopes
  scope_count: 0
  slug: blackwalltier-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 60.3
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blackwalltier Com Authentication
  slug: blackwalltier-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blackwalltier Com Domain Security
  slug: blackwalltier-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Blackwalltier Com Vulnerability Disclosure
  slug: blackwalltier-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Blackwalltier Com Trust Center
  slug: blackwalltier-com-trust-center
  summary_line: SOC 2, HIPAA
skill_count: 1
skills:
- name: blackwalltier-com-default-skill
  slug: blackwalltier-com-default-skill
slug: blackwalltier-com
tags:
- Company
- AI
- Security
- Policy
- RiskManagement
website: https://blackwalltier.com/
---
