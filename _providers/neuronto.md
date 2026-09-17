---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Adoption API from Neuronto ARD Registry — 1 operation(s) for adoption.
  name: Neuronto ARD Registry Adoption API
  slug: neuronto-adoption-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Agents API from Neuronto ARD Registry — 1 operation(s) for agents.
  name: Neuronto ARD Registry Agents API
  slug: neuronto-agents-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Analytics API from Neuronto ARD Registry — 1 operation(s) for analytics.
  name: Neuronto ARD Registry Analytics API
  slug: neuronto-analytics-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Audit API from Neuronto ARD Registry — 1 operation(s) for audit.
  name: Neuronto ARD Registry Audit API
  slug: neuronto-audit-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Bench API from Neuronto ARD Registry — 1 operation(s) for bench.
  name: Neuronto ARD Registry Bench API
  slug: neuronto-bench-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Claim API from Neuronto ARD Registry — 2 operation(s) for claim.
  name: Neuronto ARD Registry Claim API
  slug: neuronto-claim-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Demand API from Neuronto ARD Registry — 1 operation(s) for demand.
  name: Neuronto ARD Registry Demand API
  slug: neuronto-demand-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Doctor API from Neuronto ARD Registry — 1 operation(s) for doctor.
  name: Neuronto ARD Registry Doctor API
  slug: neuronto-doctor-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Explore API from Neuronto ARD Registry — 1 operation(s) for explore.
  name: Neuronto ARD Registry Explore API
  slug: neuronto-explore-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Health API from Neuronto ARD Registry — 1 operation(s) for health.
  name: Neuronto ARD Registry Health API
  slug: neuronto-health-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Insights API from Neuronto ARD Registry — 1 operation(s) for insights.
  name: Neuronto ARD Registry Insights API
  slug: neuronto-insights-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Liveness API from Neuronto ARD Registry — 1 operation(s) for liveness.
  name: Neuronto ARD Registry Liveness API
  slug: neuronto-liveness-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Manifest API from Neuronto ARD Registry — 1 operation(s) for manifest.
  name: Neuronto ARD Registry Manifest API
  slug: neuronto-manifest-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Me API from Neuronto ARD Registry — 1 operation(s) for me.
  name: Neuronto ARD Registry Me API
  slug: neuronto-me-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Plan API from Neuronto ARD Registry — 1 operation(s) for plan.
  name: Neuronto ARD Registry Plan API
  slug: neuronto-plan-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Private API from Neuronto ARD Registry — 1 operation(s) for private.
  name: Neuronto ARD Registry Private API
  slug: neuronto-private-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Reliability API from Neuronto ARD Registry — 1 operation(s) for reliability.
  name: Neuronto ARD Registry Reliability API
  slug: neuronto-reliability-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Search API from Neuronto ARD Registry — 1 operation(s) for search.
  name: Neuronto ARD Registry Search API
  slug: neuronto-search-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The State Of Mcp API from Neuronto ARD Registry — 1 operation(s) for state of mcp.
  name: Neuronto ARD Registry State Of Mcp API
  slug: neuronto-state-of-mcp-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Stats API from Neuronto ARD Registry — 1 operation(s) for stats.
  name: Neuronto ARD Registry Stats API
  slug: neuronto-stats-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Submit API from Neuronto ARD Registry — 3 operation(s) for submit.
  name: Neuronto ARD Registry Submit API
  slug: neuronto-submit-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Tool Safety API from Neuronto ARD Registry — 1 operation(s) for tool safety.
  name: Neuronto ARD Registry Tool Safety API
  slug: neuronto-tool-safety-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Tools API from Neuronto ARD Registry — 1 operation(s) for tools.
  name: Neuronto ARD Registry Tools API
  slug: neuronto-tools-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Usage API from Neuronto ARD Registry — 1 operation(s) for usage.
  name: Neuronto ARD Registry Usage API
  slug: neuronto-usage-api
- baseURL: https://neuronto.com
  baseurl_source: declared
  description: The Web Position API from Neuronto ARD Registry — 1 operation(s) for web position.
  name: Neuronto ARD Registry Web Position API
  slug: neuronto-web-position-api
artifact_total: 30
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/mcp/neuronto-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/neuronto-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/overlays/neuronto-ard-registry-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/neuronto-ard-registry-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/security/neuronto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neuronto-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/packages/neuronto-packages.yml
  title: ''
  type: Packages
  url: packages/neuronto-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/packages/neuronto-packages.yml
  title: ''
  type: SDKs
  url: packages/neuronto-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/cli/neuronto-cli.yml
  title: ''
  type: CLI
  url: cli/neuronto-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/well-known/neuronto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/neuronto-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/llms/neuronto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neuronto-llms.txt
- group: company
  title: ''
  type: Website
  url: https://neuronto.com
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/conformance/neuronto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/neuronto-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/authentication/neuronto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/neuronto-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/conventions/neuronto-conventions.yml
  title: ''
  type: Conventions
  url: conventions/neuronto-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/conventions/neuronto-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/neuronto-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/lifecycle/neuronto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/neuronto-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/plans/neuronto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neuronto-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://neuronto.com/pricing
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/rate-limits/neuronto-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/neuronto-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/neuronto/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://neuronto.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://neuronto.com/feed.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neuronto.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://neuronto.com/publish
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neuronto
created: '2026-08-31'
description: Agentic Resource Discovery (ARD) index. One search covers this index and every other public ARD registry, and results carry the tools each MCP server actually exposes, read from its own tools/list. The index holds 15,412 resources from 6,926 publishers, 14,522 verified to respond, and answers over REST, MCP and A2A with no key and no signup.
image: https://neuronto.com/icon.svg
layout: provider
mcp_servers:
- description: Official hosted MCP server for the Neuronto ARD Registry. tools/list answered a live anonymous POST on 2026-09-07 (HTTP 200, application/json) with 4 tools; the response is saved verbatim in neuronto-
  name: Neuronto ARD Registry MCP Server
  slug: neuronto-ard-registry-mcp-server
modified: '2026-09-07'
name: Neuronto ARD Registry
nav: Providers
network: true
overview: 'Neuronto ARD Registry publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Adoption API, Agents API, Analytics API, and 22 more. Tagged areas include Agentic Resource Discovery, ARD, MCP, A2A, and API Discovery.


  Neuronto ARD Registry''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, and 18 more developer resources.'
plans:
- name: Neuronto Plans Pricing
  plan_count: 4
  slug: neuronto-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Neuronto Rate Limits
  slug: neuronto-rate-limits
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.0
    catalog_earned_first_party: 24.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 48.0
    developer_ergonomics: 51.8
    discoverability: 70.4
    operational_transparency: 34.2
  previous_composite: 43.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Neuronto Authentication
  slug: neuronto-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Neuronto Domain Security
  slug: neuronto-domain-security
  summary_line: TLSv1.3 · HSTS
slug: neuronto
tags:
- Agentic Resource Discovery
- ARD
- MCP
- A2A
- API Discovery
- Registry
website: https://neuronto.com
---
