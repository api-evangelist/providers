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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Deployxa Agentic Access
  operation_count: 2
  slug: deployxa-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://deployxa.com/api/v1
  baseurl_source: spec
  description: The Deployments API from Deployxa — 1 operation(s) for deployments.
  name: Deployxa Deployments API
  slug: deployxa-deployments-api
- baseURL: https://deployxa.com/api/v1
  baseurl_source: spec
  description: The Projects API from Deployxa — 1 operation(s) for projects.
  name: Deployxa Projects API
  slug: deployxa-projects-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/deployxa/capabilities/deployxa-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/deployxa-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/deployxa/mcp/deployxa-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deployxa-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://deployxa.com
- group: agent
  href: https://artifacts.apis.io/deployxa/agentic-access/deployxa-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deployxa-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/deployxa/security/deployxa-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deployxa-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deployxa/security/deployxa-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deployxa-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deployxa/security/deployxa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deployxa-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://deployxa.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deployxa.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://deployxa.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://deployxa.com/contact
- group: company
  title: ''
  type: Blog
  url: https://deployxa.com/dispatch
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deployxa
- group: commercial
  title: ''
  type: Pricing
  url: https://deployxa.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://deployxa.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deployxa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deployxa.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://deployxa.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://deployxa.com/status
- group: design
  href: https://artifacts.apis.io/deployxa/lifecycle/deployxa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/deployxa-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/deployxa/lifecycle/deployxa-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/deployxa-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/deployxa/well-known/deployxa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deployxa-well-known.yml
- group: other
  href: https://artifacts.apis.io/deployxa/a2a/deployxa-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deployxa-a2a.yml
- group: agent
  href: https://artifacts.apis.io/deployxa/llms/deployxa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deployxa-llms.txt
- group: auth
  href: https://artifacts.apis.io/deployxa/authentication/deployxa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deployxa-authentication.yml
- group: auth
  href: https://artifacts.apis.io/deployxa/scopes/deployxa-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/deployxa-scopes.yml
- group: design
  href: https://artifacts.apis.io/deployxa/conformance/deployxa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deployxa-conformance.yml
- group: design
  href: https://artifacts.apis.io/deployxa/errors/deployxa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deployxa-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deployxa/conventions/deployxa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deployxa-conventions.yml
- group: build
  href: https://artifacts.apis.io/deployxa/packages/deployxa-packages.yml
  title: ''
  type: Packages
  url: packages/deployxa-packages.yml
- group: build
  href: https://artifacts.apis.io/deployxa/cli/deployxa-cli.yml
  title: ''
  type: CLI
  url: cli/deployxa-cli.yml
- group: commercial
  href: https://artifacts.apis.io/deployxa/plans/deployxa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deployxa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/deployxa/rate-limits/deployxa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deployxa-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/deployxa/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/deployxa/overlays/deployxa-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deployxa-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/deployxa/data-model/deployxa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deployxa-data-model.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@deployxa.com
created: '2026-09-05'
description: AI-first autonomous cloud deployment platform for deploying AI-built and containerized web apps to production, featuring a deployment intelligence engine, global edge deployment, managed databases, VPS clusters, and a CLI. Publishes an OpenAPI 3.0.3 contract at /openapi.json, an llms.txt, an A2A agent card with an AP2 agentic-payments extension, an RFC 9727 api-catalog, OAuth 2.0 discovery metadata, and an OAuth-gated hosted MCP server at mcp.deployxa.com — all verified live 2026-09-05.
finops:
- has_sources: true
  method: derived
  name: Deployxa Finops
  primary_unit: 25 gb bandwidth, 1 dedicated vcpu, 10 gb nvme storage
  service_category: ''
  slug: deployxa-finops
  template: false
image: https://deployxa.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.deployxa.com over HTTP requiring OAuth.
  name: Deployxa MCP Server
  slug: deployxa
modified: '2026-09-05'
name: Deployxa
nav: Providers
network: true
overview: 'Deployxa publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Deployments API and Projects API. Tagged areas include Platform-as-a-Service, Cloud Deployment, DevOps, CI/CD, and containers-docker.


  The Deployxa catalog on APIs.io includes 1 Spectral governance ruleset.


  Deployxa''s developer surface includes getting-started guide, support, engineering blog, pricing, signup flow, changelog, authentication, and 30 more developer resources.'
plans:
- name: Deployxa Plans Pricing
  plan_count: 7
  slug: deployxa-plans-pricing
- name: Deployxa Price Estimates
  plan_count: 0
  slug: deployxa-price-estimates
random_paper: 6
rate_limits:
- limit_count: 0
  name: Deployxa Rate Limits
  slug: deployxa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Deployxa API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: deployxa-rules
scopes:
- name: Deployxa Scopes
  scope_count: 11
  slug: deployxa-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 44.2
    developer_ergonomics: 66.1
    discoverability: 66.7
    operational_transparency: 52.6
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/deployxa/deployxa-2026-10-11T103656.png
security:
- kind: authentication
  name: Deployxa Authentication
  slug: deployxa-authentication
  summary_line: http-bearer/oauth2 · 3 schemes
- kind: domain-security
  name: Deployxa Domain Security
  slug: deployxa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deployxa Vulnerability Disclosure
  slug: deployxa-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Deployxa Trust Center
  slug: deployxa-trust-center
  summary_line: trust center published
skill_count: 1
skills:
- name: Deploy a Git repository on Deployxa
  slug: deployxa-deploy-a-repository
slug: deployxa
tags:
- Platform-as-a-Service
- Cloud Deployment
- DevOps
- CI/CD
- containers-docker
- edge-hosting
- Managed Database
- AIOps
- Developer Tools
- A2A
website: https://deployxa.com
---
