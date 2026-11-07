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
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 64.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Apiosk Com Agentic Access
  operation_count: 20
  slug: apiosk-com-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 1
apis:
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Ask API from Apiosk — 3 operation(s) for ask.
  name: Apiosk Ask API
  slug: apiosk-com-ask-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Asks API from Apiosk — 3 operation(s) for asks.
  name: Apiosk Asks API
  slug: apiosk-com-asks-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Balance API from Apiosk — 1 operation(s) for balance.
  name: Apiosk Balance API
  slug: apiosk-com-balance-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Capabilities API from Apiosk — 2 operation(s) for capabilities.
  name: Apiosk Capabilities API
  slug: apiosk-com-capabilities-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Execute API from Apiosk — 3 operation(s) for execute.
  name: Apiosk Execute API
  slug: apiosk-com-execute-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Health API from Apiosk — 1 operation(s) for health.
  name: Apiosk Health API
  slug: apiosk-com-health-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Runs API from Apiosk — 1 operation(s) for runs.
  name: Apiosk Runs API
  slug: apiosk-com-runs-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Source Readiness API from Apiosk — 1 operation(s) for source readiness.
  name: Apiosk Source Readiness API
  slug: apiosk-com-source-readiness-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Sources API from Apiosk — 4 operation(s) for sources.
  name: Apiosk Sources API
  slug: apiosk-com-sources-api
- baseURL: https://gateway.apiosk.com
  baseurl_source: declared
  description: The Usage API from Apiosk — 1 operation(s) for usage.
  name: Apiosk Usage API
  slug: apiosk-com-usage-api
artifact_total: 25
common:
- group: start
  title: ''
  type: SignUp
  url: https://app.apiosk.com/signup
- group: agent
  href: https://artifacts.apis.io/apiosk-com/agentic-access/apiosk-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apiosk-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/apiosk-com/rules/apiosk-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apiosk-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apiosk-com/json-ld/apiosk-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apiosk-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/apiosk-com/vocabulary/apiosk-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apiosk-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apiosk-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apiosk-com/data-model/apiosk-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apiosk-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/apiosk-com/changelog/apiosk-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apiosk-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/apiosk-com/conventions/apiosk-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/apiosk-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/apiosk-com/conventions/apiosk-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apiosk-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/apiosk-com/authentication/apiosk-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiosk-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/apiosk-com/errors/apiosk-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apiosk-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apiosk-com/conformance/apiosk-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiosk-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apiosk-com/llms/apiosk-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiosk-com-llms.txt
- group: other
  href: https://artifacts.apis.io/apiosk-com/a2a/apiosk-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apiosk-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/apiosk-com/well-known/apiosk-com-gateway-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apiosk-com-gateway-security.txt
- group: agent
  href: https://artifacts.apis.io/apiosk-com/well-known/apiosk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiosk-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/apiosk-com/hosts/apiosk-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiosk-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/apiosk-com/vendors/apiosk-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiosk-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/apiosk-com/packages/apiosk-com-packages.yml
  title: ''
  type: SDKs
  url: packages/apiosk-com-packages.yml
- group: build
  href: https://artifacts.apis.io/apiosk-com/packages/apiosk-com-packages.yml
  title: ''
  type: Packages
  url: packages/apiosk-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.apiosk.com/overview/changelog
- group: company
  title: ''
  type: Blog
  url: https://apiosk.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Apiosk
- group: auth
  href: https://artifacts.apis.io/apiosk-com/security/apiosk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiosk-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiosk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apiosk.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apiosk.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://apiosk.com/use-cases/
- group: operate
  title: ''
  type: Support
  url: https://apiosk.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://apiosk.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiosk.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiosk.com/privacy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.apiosk.com/mcp
  - status: null
    url: https://gateway.apiosk.com/openapi.json
  - status: 401
    url: https://apiosk.com/mcp
  - status: 403
    url: https://gateway.apiosk.com/mcp
  - status: 200
    url: https://apiosk.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Apiosk provides AI-native compliance infrastructure, enabling verification of companies, tracing beneficial owners, screening against sanctions lists, and monitoring court records. The platform offers transparent source data and cost estimates before running checks, supporting both team workflows and AI agents.
image: https://apiosk.com/og-image-v11.png
json_schemas:
- name: BuyerRun
  property_count: 19
  slug: apiosk-com-buyer-run
- name: Continuation
  property_count: 2
  slug: apiosk-com-continuation
- name: ContinuationState
  property_count: 6
  slug: apiosk-com-continuation-state
- name: EuropeanCapabilityRequest
  property_count: 4
  slug: apiosk-com-european-capability-request
- name: EuropeanCapabilityResolution
  property_count: 4
  slug: apiosk-com-european-capability-resolution
- name: ExternalPurchase
  property_count: 10
  slug: apiosk-com-external-purchase
jsonld:
- class_count: 11
  name: Apiosk Com Context
  property_count: 63
  slug: apiosk-com-context
layout: provider
modified: '2026-11-01'
name: Apiosk
nav: Providers
network: true
overview: 'Apiosk publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ask API, Asks API, Balance API, and 7 more. Tagged areas include Artificial Intelligence, Compliance, Verification, Sanctions, and Monitoring.


  The Apiosk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apiosk''s developer surface includes signup flow, changelog, authentication, engineering blog, documentation, API reference, getting-started guide, and 26 more developer resources.'
plans:
- name: Apiosk Com Plans Pricing
  plan_count: 0
  slug: apiosk-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Apiosk Com Rate Limits
  slug: apiosk-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Apiosk API Rules
  rule_count: 57
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 5
  slug: apiosk-com-rules
scopes:
- name: Apiosk Com Scopes
  scope_count: 0
  slug: apiosk-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 64.1
    developer_ergonomics: 38.7
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apiosk Com Authentication
  slug: apiosk-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apiosk Com Domain Security
  slug: apiosk-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: apiosk-com-plan-and-run-ask
  slug: apiosk-com-plan-and-run-ask
slug: apiosk-com
tags:
- Artificial Intelligence
- Compliance
- Verification
- Sanctions
- Monitoring
- Company
website: https://apiosk.com/
---
