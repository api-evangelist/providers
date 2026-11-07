---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1032
  human_in_the_loop: 7
  name: Apibase Pro Agentic Access
  operation_count: 1385
  slug: apibase-pro-agentic-access
  summary_line: 1385 operations · 1032 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://apibase.pro
  baseurl_source: declared
  description: The Tools API from APIbase — 1385 operation(s) for tools.
  name: APIbase Tools API
  slug: apibase-pro-tools-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/apibase-pro/agentic-access/apibase-pro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apibase-pro-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/apibase-pro/rate-limits/apibase-pro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apibase-pro-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apibase-pro/plans/apibase-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apibase-pro-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apibase-pro/rules/apibase-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/apibase-pro-rules.yml
- group: design
  href: https://artifacts.apis.io/apibase-pro/json-ld/apibase-pro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apibase-pro-context.jsonld
- group: design
  href: https://artifacts.apis.io/apibase-pro/vocabulary/apibase-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apibase-pro-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apibase-pro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apibase-pro/data-model/apibase-pro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apibase-pro-data-model.yml
- group: operate
  href: https://artifacts.apis.io/apibase-pro/changelog/apibase-pro-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apibase-pro-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/whiteknightonhorse/APIbase/blob/main/SECURITY.md
- group: auth
  href: https://artifacts.apis.io/apibase-pro/authentication/apibase-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apibase-pro-authentication.yml
- group: design
  href: https://artifacts.apis.io/apibase-pro/errors/apibase-pro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apibase-pro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apibase-pro/conformance/apibase-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apibase-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apibase-pro/llms/apibase-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apibase-pro-llms.txt
- group: other
  href: https://artifacts.apis.io/apibase-pro/a2a/apibase-pro-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apibase-pro-a2a.yml
- group: auth
  href: https://artifacts.apis.io/apibase-pro/well-known/apibase-pro-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apibase-pro-security.txt
- group: agent
  href: https://artifacts.apis.io/apibase-pro/well-known/apibase-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apibase-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/apibase-pro/hosts/apibase-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apibase-pro-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://apibase.pro/llms.txt
- group: auth
  href: https://artifacts.apis.io/apibase-pro/security/apibase-pro-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apibase-pro-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/apibase-pro/security/apibase-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apibase-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apibase.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://apibase.pro/guides/
- group: commercial
  title: ''
  type: Pricing
  url: https://apibase.pro/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apibase.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apibase.pro/privacy
- group: operate
  title: ''
  type: Support
  url: https://apibase.pro/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whiteknightonhorse/APIbase
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/whiteknightonhorse/APIbase/releases/tag/v2.2.0
- group: start
  title: ''
  type: SignUp
  url: https://apibase.pro/onboard
created: '2026-11-01'
description: 'APIbase.pro is an MCP gateway: one endpoint that gives AI agents access to a catalog of third‑party API tools, with pay‑per‑call pricing. The Integrator lets online stores accept payments from AI agents. Some pages on this site, in particular the guides, are written and reviewed with the help of AI. Facts about APIbase itself (fees, minimum order, payment rails, prices) are not written by the AI: they are inserted from the live product data and checked automatically before a page is published. Editorial responsibility for all content rests with the Operator.'
image: https://apibase.pro/og-image.png?v=20260928
jsonld:
- class_count: 1
  name: Apibase Pro Context
  property_count: 2
  slug: apibase-pro-context
layout: provider
modified: '2026-11-01'
name: APIbase
nav: Providers
network: true
overview: 'APIbase publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Tools API. Tagged areas include Gateways, Artificial Intelligence, MCP, and Payments.


  The APIbase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIbase''s developer surface includes changelog, authentication, API reference, documentation, pricing, support, signup flow, and 23 more developer resources.'
plans:
- name: Apibase Pro Plans Pricing
  plan_count: 3
  slug: apibase-pro-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Apibase Pro Rate Limits
  slug: apibase-pro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: APIbase API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: apibase-pro-rules
scopes:
- name: Apibase Pro Scopes
  scope_count: 0
  slug: apibase-pro-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 46.9
    developer_ergonomics: 29.0
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 30.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apibase Pro Authentication
  slug: apibase-pro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apibase Pro Domain Security
  slug: apibase-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Apibase Pro Vulnerability Disclosure
  slug: apibase-pro-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: weather-get-current
  slug: apibase-pro-weather-get-current
slug: apibase-pro
tags:
- Gateways
- Artificial Intelligence
- MCP
- Payments
website: https://apibase.pro/
---
