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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted, agent-native MCP server (streamable-http) exposing 23 published tools for creating grounded Audiences, planning and running multi-question Studies, asking standalone questions, heatmaps, summa
  name: Minds MCP Server
  slug: minds-mcp-server
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Agent Runs API from Minds — 3 operation(s) for agent runs.
  name: Minds Agent Runs API
  slug: getminds-agent-runs-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The API Keys API from Minds — 2 operation(s) for api keys.
  name: Minds API Keys API
  slug: getminds-api-keys-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Audiences API from Minds — 24 operation(s) for audiences.
  name: Minds Audiences API
  slug: getminds-audiences-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Auth API from Minds — 1 operation(s) for auth.
  name: Minds Auth API
  slug: getminds-auth-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Chat API from Minds — 4 operation(s) for chat.
  name: Minds Chat API
  slug: getminds-chat-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Knowledge API from Minds — 5 operation(s) for knowledge.
  name: Minds Knowledge API
  slug: getminds-knowledge-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Meta API from Minds — 1 operation(s) for meta.
  name: Minds Meta API
  slug: getminds-meta-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Minds API from Minds — 12 operation(s) for minds.
  name: Minds Minds API
  slug: getminds-minds-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Models API from Minds — 1 operation(s) for models.
  name: Minds Models API
  slug: getminds-models-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Research API from Minds — 5 operation(s) for research.
  name: Minds Research API
  slug: getminds-research-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Studies API from Minds — 18 operation(s) for studies.
  name: Minds Studies API
  slug: getminds-studies-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Study Drafts API from Minds — 3 operation(s) for study drafts.
  name: Minds Study Drafts API
  slug: getminds-study-drafts-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Study Runs API from Minds — 1 operation(s) for study runs.
  name: Minds Study Runs API
  slug: getminds-study-runs-api
- baseURL: https://getminds.ai/api/v1
  baseurl_source: declared
  description: The Study Templates API from Minds — 3 operation(s) for study templates.
  name: Minds Study Templates API
  slug: getminds-study-templates-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/getminds/capabilities/getminds-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/getminds-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/getminds/overlays/getminds-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getminds-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://getminds.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getminds.ai/docs/api/overview
- group: docs
  title: ''
  type: Documentation
  url: https://getminds.ai/docs/api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://getminds.ai/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://getminds.ai/docs/api/overview
- group: operate
  title: ''
  type: Support
  url: https://getminds.ai/guide
- group: company
  title: ''
  type: Blog
  url: https://getminds.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://getminds.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://getminds.ai/settings/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getminds.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getminds.ai/legal/dataprivacy
- group: operate
  href: https://artifacts.apis.io/getminds/lifecycle/getminds-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/getminds-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/getminds/mcp/getminds-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getminds-mcp.yml
- group: build
  href: https://artifacts.apis.io/getminds/mcp/getminds-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/getminds-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/getminds/scopes/getminds-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/getminds-scopes.yml
- group: agent
  href: https://artifacts.apis.io/getminds/llms/getminds-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getminds-llms.txt
- group: agent
  href: https://artifacts.apis.io/getminds/well-known/getminds-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getminds-well-known.yml
- group: auth
  href: https://artifacts.apis.io/getminds/authentication/getminds-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getminds-authentication.yml
- group: design
  href: https://artifacts.apis.io/getminds/conventions/getminds-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getminds-conventions.yml
- group: design
  href: https://artifacts.apis.io/getminds/conventions/getminds-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/getminds-conventions.yml
- group: design
  href: https://artifacts.apis.io/getminds/conformance/getminds-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getminds-conformance.yml
- group: design
  href: https://artifacts.apis.io/getminds/errors/getminds-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getminds-problem-types.yml
- group: design
  href: https://artifacts.apis.io/getminds/data-model/getminds-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getminds-data-model.yml
- group: design
  href: https://artifacts.apis.io/getminds/lifecycle/getminds-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getminds-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/getminds/security/getminds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getminds-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/getminds/rate-limits/getminds-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getminds-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/getminds/plans/getminds-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getminds-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/getminds/packages/getminds-packages.yml
  title: ''
  type: Packages
  url: packages/getminds-packages.yml
- group: agent
  href: https://artifacts.apis.io/getminds/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/getminds/regulatory/getminds-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/getminds-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/getminds/regulatory/getminds-regulatory-posture.yml
  title: ''
  type: DataResidency
  url: regulatory/getminds-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/getminds/regulatory/getminds-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/getminds-regulatory-posture.yml
created: '2026-09-20'
description: Minds (getminds.ai) is an end-to-end platform for commercial synthetic market research. Brand, agency, product and insights teams build reusable AI Audiences grounded in their own research and public sources, then run in-depth interviews, questionnaires, concept and message tests, MaxDiff/conjoint methods, and segment comparisons in a single Study — from audience creation through analysis and export. Minds ships a public v1 REST API (OpenAPI 3.1.0, 103 operations), a hosted MCP server (23 published tools, OAuth 2.0 / API key), and an agent integration guide. Operated by Art of X UG (Berlin, Germany) with EU (Frankfurt/ Stockholm) data residency and a full GDPR posture.
finops:
- has_sources: true
  method: derived
  name: Getminds Finops
  primary_unit: response
  service_category: ''
  slug: getminds-finops
  template: false
image: https://getminds.ai/images/preview.webp
layout: provider
mcp_servers:
- description: Build synthetic Audiences and run Studies for concept testing, message testing, and segment comparison.
  name: Minds MCP Server
  slug: minds-ai
modified: '2026-09-20'
name: Minds
nav: Providers
network: true
overview: 'Minds publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Runs API, API Keys API, Audiences API, and 12 more. Tagged areas include Synthetic Research, Market Research, Surveys, User Research, and Marketing Analytics.


  The Minds catalog on APIs.io includes 1 Spectral governance ruleset.


  Minds'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Getminds Plans Pricing
  plan_count: 3
  slug: getminds-plans-pricing
- name: Getminds Price Estimates
  plan_count: 0
  slug: getminds-price-estimates
random_paper: 19
rate_limits:
- limit_count: 1
  name: Getminds Rate Limits
  slug: getminds-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Minds API Rules
  rule_count: 63
  severity_counts:
    error: 42
    hint: 0
    info: 6
    warn: 15
  slug: getminds-rules
scopes:
- name: Getminds Scopes
  scope_count: 8
  slug: getminds-scopes
  summary_line: 8 scopes
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 53.1
    developer_ergonomics: 36.3
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 61.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 41.2
      total: 34
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 42.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/getminds/getminds-2026-10-11T104858.png
security:
- kind: authentication
  name: Getminds Authentication
  slug: getminds-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Getminds Domain Security
  slug: getminds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: getminds-ask-study
  slug: getminds-ask-study
- name: getminds-audience-to-study
  slug: getminds-audience-to-study
slug: getminds
tags:
- Synthetic Research
- Market Research
- Surveys
- User Research
- Marketing Analytics
- ai-personas
- MCP
- Agent-Native
- GDPR
website: https://getminds.ai
---
