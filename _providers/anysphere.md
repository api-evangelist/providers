---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Anysphere Agentic Access
  operation_count: 18
  slug: anysphere-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: The Agents API from Anysphere — 11 operation(s) for agents.
  name: Anysphere Agents API
  slug: anysphere-agents-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: The Me API from Anysphere — 1 operation(s) for me.
  name: Anysphere Me API
  slug: anysphere-me-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: The Models API from Anysphere — 1 operation(s) for models.
  name: Anysphere Models API
  slug: anysphere-models-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: The Repositories API from Anysphere — 1 operation(s) for repositories.
  name: Anysphere Repositories API
  slug: anysphere-repositories-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: The Sub Tokens API from Anysphere — 1 operation(s) for sub tokens.
  name: Anysphere Sub Tokens API
  slug: anysphere-sub-tokens-api
artifact_total: 27
collections:
- collection_type: postman
  name: Cursor Cloud Agents API
  slug: postman-anysphere-agents-api
- collection_type: postman
  name: Cursor Cloud Agents Me API
  slug: postman-anysphere-me-api
- collection_type: postman
  name: Cursor Cloud Agents Models API
  slug: postman-anysphere-models-api
- collection_type: postman
  name: Cursor Cloud Agents Repositories API
  slug: postman-anysphere-repositories-api
- collection_type: postman
  name: Cursor Cloud Agents Sub Tokens API
  slug: postman-anysphere-sub-tokens-api
- collection_type: open
  name: Cursor Cloud Agents API
  slug: open-anysphere-agents-api
- collection_type: open
  name: Cursor Cloud Agents Me API
  slug: open-anysphere-me-api
- collection_type: open
  name: Cursor Cloud Agents Models API
  slug: open-anysphere-models-api
- collection_type: open
  name: Cursor Cloud Agents Repositories API
  slug: open-anysphere-repositories-api
- collection_type: open
  name: Cursor Cloud Agents Sub Tokens API
  slug: open-anysphere-sub-tokens-api
common:
- group: commercial
  href: https://artifacts.apis.io/anysphere/plans/anysphere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anysphere-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/anysphere/overview
- group: auth
  href: https://artifacts.apis.io/anysphere/security/anysphere-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anysphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cursor.com/security
- group: auth
  href: https://artifacts.apis.io/anysphere/security/anysphere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anysphere-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/anysphere/security/anysphere-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/anysphere-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cursor.com/security
- group: agent
  href: https://artifacts.apis.io/anysphere/agentic-access/anysphere-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anysphere-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/anysphere/authentication/anysphere-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anysphere-authentication.yml
- group: design
  href: https://artifacts.apis.io/anysphere/conventions/anysphere-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anysphere-conventions.yml
- group: design
  href: https://artifacts.apis.io/anysphere/errors/anysphere-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/anysphere-error-codes.yml
- group: design
  href: https://artifacts.apis.io/anysphere/conformance/anysphere-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anysphere-conformance.yml
- group: design
  href: https://artifacts.apis.io/anysphere/data-model/anysphere-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anysphere-data-model.yml
- group: operate
  href: https://artifacts.apis.io/anysphere/rate-limits/anysphere-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anysphere-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/anysphere/lifecycle/anysphere-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anysphere-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cursor.com
- group: operate
  href: https://artifacts.apis.io/anysphere/changelog/anysphere-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/anysphere-changelog.yml
- group: agent
  href: https://artifacts.apis.io/anysphere/well-known/anysphere-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anysphere-well-known.yml
- group: auth
  href: https://artifacts.apis.io/anysphere/well-known/anysphere-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-security.txt
- group: build
  href: https://artifacts.apis.io/anysphere/packages/anysphere-packages.yml
  title: ''
  type: Packages
  url: packages/anysphere-packages.yml
- group: build
  href: https://artifacts.apis.io/anysphere/cli/anysphere-cli.yml
  title: ''
  type: CLI
  url: cli/anysphere-cli.yml
- group: agent
  href: https://artifacts.apis.io/anysphere/mcp/anysphere-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/anysphere-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anysphere/llms/anysphere-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anysphere-llms.txt
- group: other
  href: https://artifacts.apis.io/anysphere/overlays/anysphere-cloud-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anysphere-cloud-agents-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/anysphere/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cursor.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cursor.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cursor.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cursor.com/docs/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://forum.cursor.com
- group: company
  title: ''
  type: Blog
  url: https://cursor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cursor
- group: commercial
  title: ''
  type: Pricing
  url: https://cursor.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cursor.com/dashboard/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cursor.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cursor.com/privacy
- group: company
  title: ''
  type: Website
  url: https://anysphere.inc
created: '2026-07-17'
description: Anysphere is the applied-research company behind Cursor, the AI-native code editor and agent platform. Beyond the desktop app, Cursor ships a public Cloud Agents REST API (https://api.cursor.com) that lets developers programmatically create autonomous coding agents, submit prompt runs, stream run events over SSE, and retrieve produced artifacts, plus an Admin API for team member/usage/spend management and a first-party terminal CLI (the `agent` binary). Authentication is a dashboard-issued API key over HTTP Basic/Bearer. This profile was surfaced as a Thrive Capital portfolio company and enriched from Cursor's public developer surface.
finops:
- has_sources: true
  method: derived
  name: Anysphere Finops
  primary_unit: user
  service_category: ''
  slug: anysphere-finops
  template: false
image: https://cursor.com/apple-touch-icon.png
layout: provider
modified: '2026-07-17'
name: Anysphere
nav: Providers
network: true
overview: 'Anysphere publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Me API, Models API, and 2 more. Tagged areas include Company, Developer Tools, Artificial Intelligence, Code Editor, and Coding Agents.


  The Anysphere catalog on APIs.io includes 1 Spectral governance ruleset.


  Anysphere''s developer surface includes authentication, changelog, CLI, documentation, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Anysphere Plans Pricing
  plan_count: 4
  slug: anysphere-plans-pricing
- name: Anysphere Price Estimates
  plan_count: 0
  slug: anysphere-price-estimates
random_paper: 15
rate_limits:
- limit_count: 7
  name: Anysphere Rate Limits
  slug: anysphere-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Anysphere API Rules
  rule_count: 63
  severity_counts:
    error: 54
    hint: 0
    info: 4
    warn: 5
  slug: anysphere-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 51.5
    developer_ergonomics: 38.7
    discoverability: 73.2
    operational_transparency: 65.8
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/anysphere/anysphere-2026-07-25T200524.png
security:
- kind: authentication
  name: Anysphere Authentication
  slug: anysphere-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Anysphere Domain Security
  slug: anysphere-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anysphere Vulnerability Disclosure
  slug: anysphere-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anysphere Trust Center
  slug: anysphere-trust-center
  summary_line: SOC 2 Type II
skill_count: 2
skills:
- name: Create and monitor a Cursor Cloud Agent
  slug: anysphere-create-cloud-agent
- name: Send a follow-up prompt and reconcile agent usage
  slug: anysphere-follow-up-run
slug: anysphere
tags:
- Company
- Developer Tools
- Artificial Intelligence
- Code Editor
- Coding Agents
- Cloud Agents
- Developer Productivity
- IDE
website: https://anysphere.inc
---
