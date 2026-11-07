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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Annsa Ai Agentic Access
  operation_count: 5
  slug: annsa-ai-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.annsa.ai
  baseurl_source: declared
  description: The MCP surface — ranked priorities, codebase-aware specs, search.
  name: Annsa Agents API
  slug: annsa-ai-agents-api
- baseURL: https://api.annsa.ai
  baseurl_source: declared
  description: Getting customer signal into Annsa.
  name: Annsa Ingest API
  slug: annsa-ai-ingest-api
- baseURL: https://api.annsa.ai
  baseurl_source: declared
  description: Liveness.
  name: Annsa Service API
  slug: annsa-ai-service-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/annsa-ai/agentic-access/annsa-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/annsa-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/annsa-ai/rate-limits/annsa-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/annsa-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/annsa-ai/plans/annsa-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/annsa-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/rules/annsa-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/annsa-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/json-ld/annsa-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/annsa-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/annsa-ai/vocabulary/annsa-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/annsa-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/annsa-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/data-model/annsa-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/annsa-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/annsa-ai/changelog/annsa-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/annsa-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/conventions/annsa-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/annsa-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/conventions/annsa-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/annsa-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/annsa-ai/authentication/annsa-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/annsa-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/annsa-ai/scopes/annsa-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/annsa-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/lifecycle/annsa-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/annsa-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/errors/annsa-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/annsa-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/annsa-ai/conformance/annsa-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/annsa-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/annsa-ai/llms/annsa-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/annsa-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/annsa-ai/mcp/annsa-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/annsa-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/annsa-ai/well-known/annsa-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/annsa-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/annsa-ai/well-known/annsa-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/annsa-ai-app-security.txt
- group: agent
  href: https://artifacts.apis.io/annsa-ai/well-known/annsa-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/annsa-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/annsa-ai/hosts/annsa-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/annsa-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/annsa-ai/vendors/annsa-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/annsa-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/annsa-ai/packages/annsa-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/annsa-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/annsa-ai/packages/annsa-ai-packages.yml
  title: ''
  type: Packages
  url: packages/annsa-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://annsa.ai/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://annsa.ai/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://annsa.ai/changelog
- group: start
  title: ''
  type: SignUp
  url: https://app.annsa.ai/signup
- group: auth
  href: https://artifacts.apis.io/annsa-ai/security/annsa-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/annsa-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/annsa-ai/security/annsa-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/annsa-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://annsa.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://annsa.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://annsa.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://annsa.ai/docs/quick-start
- group: operate
  title: ''
  type: Support
  url: https://annsa.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://annsa.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/annsa-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://annsa.ai/choose/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://annsa.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://annsa.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://annsa.ai/privacy
created: '2026-11-01'
description: Annsa is project and customer management for agent teams. Choose what to build from your customers, direct every agent from one plan and learn as you go. Based in Sydney, Australia, Annsa provides a source of direction for agent teams, offering features such as roadmaps, feedback integration, and AI-powered decision tools. It enables teams to prioritize work, share insights, and automate workflows across multiple platforms.
image: https://annsa.ai/og-home.jpg
json_schemas:
- name: FeedbackBatchResult
  property_count: 10
  slug: annsa-ai-feedback-batch-result
- name: FeedbackDuplicate
  property_count: 3
  slug: annsa-ai-feedback-duplicate
- name: FeedbackItem
  property_count: 8
  slug: annsa-ai-feedback-item
- name: HealthStatus
  property_count: 6
  slug: annsa-ai-health-status
- name: TranscriptUpload
  property_count: 11
  slug: annsa-ai-transcript-upload
- name: WidgetSubmission
  property_count: 9
  slug: annsa-ai-widget-submission
jsonld:
- class_count: 12
  name: Annsa Ai Context
  property_count: 47
  slug: annsa-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.annsa.ai.
  name: Annsa MCP Server
  slug: annsa-ai-mcp-yml
modified: '2026-11-01'
name: Annsa
nav: Providers
network: true
overview: 'Annsa publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agents API, Ingest API, and Service API. Tagged areas include Project Management, Customer Management, Agent Teams, Artificial Intelligence, and Software-as-a-Service.


  The Annsa catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Annsa''s developer surface includes changelog, authentication, signup flow, documentation, API reference, getting-started guide, support, and 35 more developer resources.'
plans:
- name: Annsa Ai Plans Pricing
  plan_count: 3
  slug: annsa-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Annsa Ai Rate Limits
  slug: annsa-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Annsa API Rules
  rule_count: 19
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 1
  slug: annsa-ai-rules
scopes:
- name: Annsa Ai Scopes
  scope_count: 2
  slug: annsa-ai-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.0
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 67.3
    developer_ergonomics: 48.1
    discoverability: 65.0
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 67.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Annsa Ai Authentication
  slug: annsa-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Annsa Ai Domain Security
  slug: annsa-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Annsa Ai Vulnerability Disclosure
  slug: annsa-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: health-check
  slug: health-check
- name: submit-feedback
  slug: submit-feedback
- name: submit-survey-feedback
  slug: submit-survey-feedback
- name: upload-transcript
  slug: upload-transcript
slug: annsa-ai
tags:
- Project Management
- Customer Management
- Agent Teams
- Artificial Intelligence
- Software-as-a-Service
website: https://annsa.ai/
---
