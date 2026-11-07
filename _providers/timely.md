---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 55
  human_in_the_loop: 3
  name: Timely Agentic Access
  operation_count: 92
  slug: timely-agentic-access
  summary_line: 92 operations · 55 acting · 3 human-in-the-loop
api_count: 1
artifact_total: 19
asyncapis:
- description: ''
  name: Timely Webhooks
  slug: timely-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/timely/agentic-access/timely-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/timely-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/timely/rules/timely-rules.yml
  title: ''
  type: Spectral
  url: rules/timely-rules.yml
- group: design
  href: https://artifacts.apis.io/timely/json-ld/timely-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/timely-context.jsonld
- group: design
  href: https://artifacts.apis.io/timely/vocabulary/timely-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/timely-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/timely/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/timely/asyncapi/timely-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/timely-webhooks.yml
- group: design
  href: https://artifacts.apis.io/timely/data-model/timely-data-model.yml
  title: ''
  type: DataModel
  url: data-model/timely-data-model.yml
- group: operate
  href: https://artifacts.apis.io/timely/changelog/timely-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/timely-changelog.yml
- group: auth
  href: https://artifacts.apis.io/timely/authentication/timely-authentication.yml
  title: ''
  type: Authentication
  url: authentication/timely-authentication.yml
- group: auth
  href: https://artifacts.apis.io/timely/scopes/timely-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/timely-scopes.yml
- group: design
  href: https://artifacts.apis.io/timely/errors/timely-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/timely-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/timely/plans/timely-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/timely-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.timely.com/security/
- group: design
  href: https://artifacts.apis.io/timely/conformance/timely-conformance.yml
  title: ''
  type: Conformance
  url: conformance/timely-conformance.yml
- group: agent
  href: https://artifacts.apis.io/timely/llms/timely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/timely-llms.txt
- group: agent
  href: https://artifacts.apis.io/timely/well-known/timely-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/timely-well-known.yml
- group: other
  href: https://artifacts.apis.io/timely/hosts/timely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/timely-hosts.yml
- group: other
  href: https://artifacts.apis.io/timely/vendors/timely-vendors.yml
  title: ''
  type: Vendors
  url: vendors/timely-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.timely.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.timely.com/help/
- group: auth
  title: ''
  type: Security
  url: https://www.timely.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.timely.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.timely.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.timelyapp.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.timely.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.timely.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.timely.com/help/handbook/getting-started/quick-start-onboarding/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.timelyapp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.timely.com/
- group: auth
  href: https://artifacts.apis.io/timely/security/timely-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/timely-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/timely/security/timely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/timely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://timelyapp.com/
coverage:
  checked: '2026-10-28'
  detail: Timely's developer portal renders the API reference via JavaScript and does not expose a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://developer.timely.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Timely provides AI‑powered automatic time‑tracking software for consultancies, agencies and SaaS businesses. Its platform captures billable hours, improves utilization, and offers data‑driven insights to help teams work smarter and increase profitability.
image: https://www.timely.com/cdn/665734560acfe09755fa0223_opne.png
json_schemas:
- name: V1.Forecast
  property_count: 21
  slug: timely-v1-forecast
- name: V1.Hour
  property_count: 51
  slug: timely-v1-hour
- name: V1.InsightsResponse
  property_count: 35
  slug: timely-v1-insights-response
- name: V1.Project
  property_count: 55
  slug: timely-v1-project
- name: V1.Projects.Create
  property_count: 1
  slug: timely-v1-projects-create
- name: V1.Projects.Update
  property_count: 1
  slug: timely-v1-projects-update
jsonld:
- class_count: 67
  name: Timely Context
  property_count: 249
  slug: timely-context
layout: provider
modified: '2026-10-27'
name: Timely (Memory AS)
nav: Providers
network: true
overview: 'Timely (Memory AS) publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Time Tracking, Artificial Intelligence, Software-as-a-Service, and Productivity.


  The Timely (Memory AS) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Timely (Memory AS)''s developer surface includes changelog, authentication, support, pricing, engineering blog, getting-started guide, documentation, and 25 more developer resources.'
plans:
- name: Timely Plans Pricing
  plan_count: 7
  slug: timely-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Timely Rate Limits
  slug: timely-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Timely (Memory AS) API Rules
  rule_count: 64
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 14
  slug: timely-rules
scopes:
- name: Timely Scopes
  scope_count: 1
  slug: timely-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 55.8
    catalog_earned_first_party: 12.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 85.5
    contract_governance: 35.6
    contract_quality: 59.1
    developer_ergonomics: 41.1
    discoverability: 55.4
    operational_transparency: 26.3
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/timely/timely-2026-11-03T144756.png
security:
- kind: authentication
  name: Timely Authentication
  slug: timely-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Timely Domain Security
  slug: timely-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Timely Trust Center
  slug: timely-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 3
skills:
- name: create-project
  slug: timely-create-project
- name: list-projects
  slug: timely-list-projects
- name: log-time
  slug: timely-log-time
slug: timely
tags:
- Company
- Time Tracking
- Artificial Intelligence
- Software-as-a-Service
- Productivity
website: https://timelyapp.com/
---
