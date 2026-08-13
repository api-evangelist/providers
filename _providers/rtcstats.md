---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Rtcstats Agentic Access
  operation_count: 9
  slug: rtcstats-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: The rtcStats API API from rtcStats — 8 operation(s) for rtcstats api.
  name: rtcStats rtcStats API API
  slug: rtcstats-rtcstats-api-api
artifact_total: 7
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/rtcstats/rtcstats/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rtcstats-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rtcstats-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rtcstats-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/rtcstats-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rtcstats-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rtcstats-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rtcstats-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rtcstats-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rtcstats-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/rtcstats-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rtcstats-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rtcstats-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rtcstats-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rtcstats-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/rtcstats-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rtcstats-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rtcstats-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rtcstats-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rtcstats.com/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://rtcstats.com/kb
- group: docs
  title: ''
  type: APIReference
  url: https://rtcstats.com/api-docs.md
- group: start
  title: ''
  type: GettingStarted
  url: https://rtcstats.com/kb/getting-started
- group: operate
  title: ''
  type: Support
  url: https://rtcstats.com/support
- group: company
  title: ''
  type: Blog
  url: https://rtcstats.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://rtcstats.com/blog/category/release
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rtcstats
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/rtcstats/rtcstats
- group: commercial
  title: ''
  type: Pricing
  url: https://rtcstats.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://rtcstats.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rtcstats.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rtcstats.com/privacy
created: '2026-08-09'
description: SaaS for developers to troubleshoot and monitor WebRTC applications. Users upload webrtc-internals/rtcstats dumps or stream stats to receive metrics, Observations, Deductions, an Experience Score, and an AI root-cause summary. Offers a REST API, a hosted MCP server, and an open-source collection SDK/collector.
image: https://rtcstats.com/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: rtcstats-mcp.yml
  slug: rtcstats-mcpyml
modified: '2026-08-09'
name: rtcStats
nav: Providers
network: true
overview: 'rtcStats publishes 1 API on the [APIs.io](https://apis.io/) network: rtcStats API API. Tagged areas include webrtc, observability, monitoring, debugging, and real-time-communications.


  rtcStats'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
plans:
- name: Rtcstats Plans
  plan_count: 3
  slug: rtcstats-plans
random_paper: 48
rate_limits:
- limit_count: 3
  name: Rtcstats Rate Limits
  slug: rtcstats-rate-limits
score:
  band: strong
  composite: 59.5
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 58.5
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Rtcstats Authentication
  slug: rtcstats-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rtcstats Domain Security
  slug: rtcstats-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rtcstats
tags:
- webrtc
- observability
- monitoring
- debugging
- real-time-communications
- video
- voice
- ai
- mcp
- developer-tools
website: https://rtcstats.com/api-docs
---
