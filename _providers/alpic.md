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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Alpic Agentic Access
  operation_count: 24
  slug: alpic-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 2
apis:
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The analytics API from Alpic — 1 operation(s) for analytics.
  name: Alpic Analytics API
  slug: alpic-analytics-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The beacon API from Alpic — 2 operation(s) for beacon.
  name: Alpic Beacon API
  slug: alpic-beacon-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The deployments API from Alpic — 1 operation(s) for deployments.
  name: Alpic Deployments API
  slug: alpic-deployments-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The distribution API from Alpic — 2 operation(s) for distribution.
  name: Alpic Distribution API
  slug: alpic-distribution-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The environments API from Alpic — 8 operation(s) for environments.
  name: Alpic Environments API
  slug: alpic-environments-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The projects API from Alpic — 2 operation(s) for projects.
  name: Alpic Projects API
  slug: alpic-projects-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The teams API from Alpic — 1 operation(s) for teams.
  name: Alpic Teams API
  slug: alpic-teams-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The tunnels API from Alpic — 1 operation(s) for tunnels.
  name: Alpic Tunnels API
  slug: alpic-tunnels-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The insights API from Alpic — 6 operation(s) for insights.
  name: Alpic Insights API
  slug: alpic-insights-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The submissions API from Alpic — 3 operation(s) for submissions.
  name: Alpic Submissions API
  slug: alpic-submissions-api
- baseURL: https://api.alpic.ai
  baseurl_source: declared
  description: The telemetry API from Alpic — 2 operation(s) for telemetry.
  name: Alpic Telemetry API
  slug: alpic-telemetry-api
artifact_total: 29
collections:
- collection_type: open
  name: Alpic analytics API
  slug: open-alpic-analytics-api
- collection_type: open
  name: Alpic analytics beacon API
  slug: open-alpic-beacon-api
- collection_type: open
  name: Alpic analytics deployments API
  slug: open-alpic-deployments-api
- collection_type: open
  name: Alpic analytics distribution API
  slug: open-alpic-distribution-api
- collection_type: open
  name: Alpic analytics environments API
  slug: open-alpic-environments-api
- collection_type: open
  name: Alpic analytics projects API
  slug: open-alpic-projects-api
- collection_type: open
  name: Alpic analytics teams API
  slug: open-alpic-teams-api
- collection_type: open
  name: Alpic analytics tunnels API
  slug: open-alpic-tunnels-api
common:
- group: commercial
  href: https://artifacts.apis.io/alpic/plans/alpic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alpic-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/alpic/capabilities/alpic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/alpic-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/alpic/mcp/alpic-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alpic-mcp.yml
- group: other
  href: https://artifacts.apis.io/alpic/overlays/alpic-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alpic-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.alpic.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alpic.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alpic.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alpic.ai/quickstart
- group: build
  href: https://artifacts.apis.io/alpic/cli/alpic-cli.yml
  title: ''
  type: CLI
  url: cli/alpic-cli.yml
- group: build
  href: https://artifacts.apis.io/alpic/packages/alpic-packages.yml
  title: ''
  type: SDKs
  url: packages/alpic-packages.yml
- group: build
  href: https://artifacts.apis.io/alpic/packages/alpic-packages.yml
  title: ''
  type: Packages
  url: packages/alpic-packages.yml
- group: agent
  href: https://artifacts.apis.io/alpic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/alpic/well-known/alpic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpic-well-known.yml
- group: agent
  href: https://artifacts.apis.io/alpic/llms/alpic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpic-llms.txt
- group: auth
  href: https://artifacts.apis.io/alpic/authentication/alpic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alpic-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alpic/security/alpic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpic-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.alpic.ai/
- group: agent
  href: https://artifacts.apis.io/alpic/agentic-access/alpic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alpic-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alpic-ai
- group: company
  title: ''
  type: Blog
  url: https://alpic.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://alpic.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.alpic.ai
- group: operate
  title: ''
  type: Support
  url: https://alpic.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alpic.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alpic.ai/legal/privacy
- group: company
  title: ''
  type: Website
  url: https://alpic.ai/
created: '2026-07-17'
description: Alpic is the MCP-native cloud platform for building, deploying, monitoring, and distributing Model Context Protocol (MCP) servers and ChatGPT Apps. Its stack spans the open-source Skybridge TypeScript framework, the `alpic` CLI, Alpic Cloud (one-click deploy, multi-environment support, runtime and build logs, analytics, DCR proxy, Node.js/Python runtimes), Beacon compliance audits, and one-click distribution to the MCP registry. The Alpic REST API (https://api.alpic.ai, v1) programmatically manages teams, projects, environments, environment variables, deployments, analytics, playgrounds, tunnels, distribution, and Beacon audits, with an agentic self-registration path so AI agents can obtain an API key and ship MCP servers autonomously. Founded by the repeat team behind Streamroot; backed by Partech.
finops:
- has_sources: true
  method: derived
  name: Alpic Finops
  primary_unit: subscription
  service_category: ''
  slug: alpic-finops
  template: false
image: https://framerusercontent.com/images/WZiXUn1MVLa0eLUmTzKrnFH9tUs.png
layout: provider
modified: '2026-07-17'
name: Alpic
nav: Providers
network: true
overview: 'Alpic publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Beacon API, Deployments API, and 8 more. Tagged areas include Company, Artificial Intelligence, MCP, Cloud Platform, and Developer Tools.


  The Alpic catalog on APIs.io includes 1 Spectral governance ruleset.


  Alpic''s developer surface includes documentation, API reference, getting-started guide, CLI, authentication, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Alpic Plans Pricing
  plan_count: 3
  slug: alpic-plans-pricing
- name: Alpic Price Estimates
  plan_count: 0
  slug: alpic-price-estimates
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Alpic API Rules
  rule_count: 50
  severity_counts:
    error: 41
    hint: 0
    info: 3
    warn: 6
  slug: alpic-rules
scopes:
- name: Alpic Scopes
  scope_count: 3
  slug: alpic-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
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
    score: 22.2
screenshot: https://apis.io/screenshots/alpic/alpic-2026-07-25T195808.png
security:
- kind: authentication
  name: Alpic Authentication
  slug: alpic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alpic Domain Security
  slug: alpic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Alpic Trust Center
  slug: alpic-trust-center
  summary_line: trust center published
skill_count: 1
skills:
- name: Deploy and manage an MCP server on Alpic
  slug: alpic-deploy-mcp-server
slug: alpic
tags:
- Company
- Artificial Intelligence
- MCP
- Cloud Platform
- Developer Tools
- Deployment
- ChatGPT Apps
- AI Agents
- Platform-as-a-Service
website: https://alpic.ai/
---
