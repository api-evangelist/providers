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
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: RankHound is an SEO automation platform offering weekly keyword research, ranking checks, article generation, and AI visibility insights.
  name: RankHound API
  slug: rankhound-api
- baseURL: https://app.rankhound.ai
  baseurl_source: declared
  description: 'aimentiontracker-ai API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: aimentiontracker-ai API
  slug: aimentiontracker-ai-api
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/aimentiontracker-ai/vendors/aimentiontracker-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimentiontracker-ai-vendors.yml
- group: operate
  href: https://artifacts.apis.io/aimentiontracker-ai/rate-limits/aimentiontracker-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aimentiontracker-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aimentiontracker-ai/plans/aimentiontracker-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aimentiontracker-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aimentiontracker-ai/rules/aimentiontracker-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aimentiontracker-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aimentiontracker-ai/json-ld/aimentiontracker-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aimentiontracker-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/aimentiontracker-ai/vocabulary/aimentiontracker-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aimentiontracker-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aimentiontracker-ai/data-model/aimentiontracker-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aimentiontracker-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/aimentiontracker-ai/conventions/aimentiontracker-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aimentiontracker-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aimentiontracker-ai/authentication/aimentiontracker-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aimentiontracker-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/aimentiontracker-ai/errors/aimentiontracker-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aimentiontracker-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aimentiontracker-ai/conformance/aimentiontracker-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aimentiontracker-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aimentiontracker-ai/llms/aimentiontracker-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimentiontracker-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/aimentiontracker-ai/well-known/aimentiontracker-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aimentiontracker-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aimentiontracker-ai/hosts/aimentiontracker-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimentiontracker-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rankhound.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rankhound.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://rankhound.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.rankhound.ai/signin
- group: docs
  title: ''
  type: Documentation
  url: https://rankhound.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://rankhound.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://rankhound.ai/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aimentiontracker
- group: company
  title: ''
  type: Website
  url: https://aimentiontracker.ai/
- group: auth
  href: https://artifacts.apis.io/aimentiontracker-ai/security/aimentiontracker-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimentiontracker-ai-domain-security.yml
created: '2026-11-01'
description: aimentiontracker-ai is a stub entry in the API Evangelist catalog, originating from the MCP registry harvest. The company details are not publicly verifiable at this time, and no official website or documentation could be confirmed. This placeholder record includes basic metadata and will be updated when reliable information becomes available.
image: https://rankhound.ai/brand/og-e1c0889d8b.png
json_schemas:
- name: GetAgentResponse
  property_count: 9
  slug: aimentiontracker-ai-get-agent-response
- name: GetApiV1BrandsResponse
  property_count: 2
  slug: aimentiontracker-ai-get-api-v1-brands-response
- name: GetArticlesIdResponse
  property_count: 18
  slug: aimentiontracker-ai-get-articles-id-response
- name: GetArticlesResponse
  property_count: 13
  slug: aimentiontracker-ai-get-articles-response
- name: GetBrandsResponse
  property_count: 7
  slug: aimentiontracker-ai-get-brands-response
- name: GetMeResponse
  property_count: 6
  slug: aimentiontracker-ai-get-me-response
jsonld:
- class_count: 13
  name: Aimentiontracker Ai Context
  property_count: 56
  slug: aimentiontracker-ai-context
layout: provider
modified: '2026-11-01'
name: aimentiontracker-ai
nav: Providers
network: true
overview: 'aimentiontracker-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, SEO, Automation, and Marketing.


  The aimentiontracker-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aimentiontracker-ai''s developer surface includes authentication, pricing, documentation, engineering blog, getting-started guide, and 19 more developer resources.'
plans:
- name: Aimentiontracker Ai Plans Pricing
  plan_count: 4
  slug: aimentiontracker-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Aimentiontracker Ai Rate Limits
  slug: aimentiontracker-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: aimentiontracker-ai API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aimentiontracker-ai-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 27.1
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 23.7
  previous_composite: 43.0
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aimentiontracker Ai Authentication
  slug: aimentiontracker-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aimentiontracker Ai Domain Security
  slug: aimentiontracker-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aimentiontracker-ai
tags:
- Company
- Artificial Intelligence
- SEO
- Automation
- Marketing
website: https://aimentiontracker.ai/
---
