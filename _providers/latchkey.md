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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.latchkey.dev
  baseurl_source: declared
  description: Create, submit, observe and cancel runner jobs.
  name: Latchkey Jobs API Jobs API
  slug: latchkey-jobs-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/latchkey/capabilities/latchkey-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/latchkey-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://latchkey.dev/blog/rss.xml
- group: agent
  title: ''
  type: MCPServer
  url: https://latchkey.dev/mcp
- group: agent
  href: https://artifacts.apis.io/latchkey/mcp/latchkey-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/latchkey-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://latchkey.dev/
- group: auth
  href: https://artifacts.apis.io/latchkey/security/latchkey-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/latchkey-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/latchkey/security/latchkey-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/latchkey-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/latchkey/authentication/latchkey-authentication.yml
  title: ''
  type: Authentication
  url: authentication/latchkey-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://latchkey.dev/documentation/security-architecture
- group: auth
  href: https://artifacts.apis.io/latchkey/well-known/latchkey-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/latchkey-security.txt
- group: agent
  href: https://artifacts.apis.io/latchkey/well-known/latchkey-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/latchkey-well-known.yml
- group: build
  href: https://artifacts.apis.io/latchkey/packages/latchkey-packages.yml
  title: ''
  type: Packages
  url: packages/latchkey-packages.yml
- group: build
  href: https://artifacts.apis.io/latchkey/cli/latchkey-cli.yml
  title: ''
  type: CLI
  url: cli/latchkey-cli.yml
- group: design
  href: https://artifacts.apis.io/latchkey/conventions/latchkey-conventions.yml
  title: ''
  type: Conventions
  url: conventions/latchkey-conventions.yml
- group: design
  href: https://artifacts.apis.io/latchkey/conventions/latchkey-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/latchkey-conventions.yml
- group: design
  href: https://artifacts.apis.io/latchkey/errors/latchkey-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/latchkey-problem-types.yml
- group: design
  href: https://artifacts.apis.io/latchkey/lifecycle/latchkey-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/latchkey-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/latchkey/conformance/latchkey-conformance.yml
  title: ''
  type: Conformance
  url: conformance/latchkey-conformance.yml
- group: design
  href: https://artifacts.apis.io/latchkey/data-model/latchkey-data-model.yml
  title: ''
  type: DataModel
  url: data-model/latchkey-data-model.yml
- group: other
  href: https://artifacts.apis.io/latchkey/overlays/latchkey-jobs-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/latchkey-jobs-api-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/latchkey/plans/latchkey-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/latchkey-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/latchkey/rate-limits/latchkey-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/latchkey-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/latchkey/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://latchkey.dev/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://latchkey.dev/documentation/quickstart
- group: operate
  title: ''
  type: Support
  url: https://latchkey.dev/support
- group: company
  title: ''
  type: Blog
  url: https://latchkey.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://latchkey.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://latchkey.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latchkey.dev/privacy
- group: start
  title: ''
  type: Login
  url: https://latchkey.dev/dashboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/latchkey-dev
created: '2026-09-06'
description: Managed ephemeral GitHub Actions runners that repair failing builds mid-run. The Jobs API gives coding agents and CI systems direct access to a fresh Ubuntu 24.04 x86_64 runner that runs one command and is then destroyed, with a hosted MCP server, CLI, and llms.txt for agent-native access.
finops:
- has_sources: true
  method: derived
  name: Latchkey Finops
  primary_unit: minute (2 vcpu, 8 gb)
  service_category: ''
  slug: latchkey-finops
  template: false
image: https://latchkey.dev/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Latchkey Jobs API MCP Server
  slug: mcp
modified: '2026-10-06'
name: Latchkey Jobs API
nav: Providers
network: true
overview: 'Latchkey Jobs API publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Jobs API. Tagged areas include CI/CD, DevOps, GitHub Actions, Ephemeral Compute, and Build & Test Infrastructure.


  The Latchkey Jobs API catalog on APIs.io includes 1 Spectral governance ruleset.


  Latchkey Jobs API''s developer surface includes authentication, CLI, documentation, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Latchkey Plans Pricing
  plan_count: 9
  slug: latchkey-plans-pricing
- name: Latchkey Price Estimates
  plan_count: 0
  slug: latchkey-price-estimates
random_paper: 13
rate_limits:
- limit_count: 3
  name: Latchkey Rate Limits
  slug: latchkey-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Latchkey Jobs API API Rules
  rule_count: 65
  severity_counts:
    error: 63
    hint: 0
    info: 1
    warn: 1
  slug: latchkey-rules
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 50.2
    developer_ergonomics: 54.8
    discoverability: 75.0
    operational_transparency: 44.7
  previous_composite: 54.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/latchkey/latchkey-2026-10-11T110327.png
security:
- kind: authentication
  name: Latchkey Authentication
  slug: latchkey-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Latchkey Domain Security
  slug: latchkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Latchkey Vulnerability Disclosure
  slug: latchkey-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: ci-doctor
  slug: latchkey-ci-doctor
- name: latchkey-cli
  slug: latchkey-cli-skill
- name: latchkey-run-and-verify-job
  slug: latchkey-run-and-verify-job
slug: latchkey
tags:
- CI/CD
- DevOps
- GitHub Actions
- Ephemeral Compute
- Build & Test Infrastructure
- Agent-Native
- AI Coding Agents
- Developer Tools
website: https://latchkey.dev/
---
