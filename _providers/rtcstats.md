---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Rtcstats Agentic Access
  operation_count: 9
  slug: rtcstats-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 2
apis:
- baseURL: https://api.rtcstats.com/v1.0
  baseurl_source: declared
  description: The rtcStats API API from rtcStats — 8 operation(s) for rtcstats api.
  name: rtcStats rtcStats API API
  slug: rtcstats-rtcstats-api-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: rtcStats rtcStats API API
  slug: open-rtcstats-rtcstats-api-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.rtcstats.com/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/rtcstats/rtcstats/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/rtcstats/rtcstats/releases
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
- description: rtcStats operates a first-party hosted MCP server over Streamable HTTP at https://api.rtcstats.com/v1.0/mcp. It is stateless JSON-RPC 2.0 and is also declared in the OpenAPI as the mcpStreamablePost o
  name: rtcStats MCP Server
  slug: rtcstats-mcp-server
modified: '2026-08-09'
name: rtcStats
nav: Providers
network: true
overview: 'rtcStats publishes 1 API on the [APIs.io](https://apis.io/) network: rtcStats API API. Tagged areas include WebRTC, Observability, Monitoring, Debugging, and Real-Time Communications.


  rtcStats'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 29 more developer resources.'
plans:
- name: Rtcstats Plans
  plan_count: 3
  slug: rtcstats-plans
random_paper: 6
rate_limits:
- limit_count: 3
  name: Rtcstats Rate Limits
  slug: rtcstats-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/screenshots/rtcstats-2026-08-17T081649.png
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
- WebRTC
- Observability
- Monitoring
- Debugging
- Real-Time Communications
- Video
- Voice
- Artificial Intelligence
- MCP
- Developer Tools
website: https://www.rtcstats.com/
---
