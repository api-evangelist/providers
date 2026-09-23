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
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-09-23'
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
  name: rtcStats API
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
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/agentic-access/rtcstats-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rtcstats-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/security/rtcstats-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rtcstats-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/authentication/rtcstats-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rtcstats-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/packages/rtcstats-packages.yml
  title: ''
  type: Packages
  url: packages/rtcstats-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/packages/rtcstats-packages.yml
  title: ''
  type: SDKs
  url: packages/rtcstats-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/mcp/rtcstats-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rtcstats-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/mcp/rtcstats-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rtcstats-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/llms/rtcstats-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rtcstats-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/overlays/rtcstats-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rtcstats-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/conformance/rtcstats-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rtcstats-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/errors/rtcstats-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rtcstats-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/lifecycle/rtcstats-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rtcstats-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/conventions/rtcstats-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rtcstats-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/changelog/rtcstats-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rtcstats-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/components/rtcstats-components.yml
  title: ''
  type: Components
  url: components/rtcstats-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/data-model/rtcstats-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rtcstats-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/rate-limits/rtcstats-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rtcstats-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/plans/rtcstats-plans.yml
  title: ''
  type: Plans
  url: plans/rtcstats-plans.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rtcstats/refs/heads/main/skills/_index.yml
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
modified: '2026-09-16'
name: rtcStats
nav: Providers
network: true
overview: 'rtcStats publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include WebRTC, Observability, Monitoring, Debugging, and Real-Time Communication.


  rtcStats'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 29 more developer resources.'
plans:
- name: Rtcstats Plans
  plan_count: 3
  slug: rtcstats-plans
random_paper: 8
rate_limits:
- limit_count: 3
  name: Rtcstats Rate Limits
  slug: rtcstats-rate-limits
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 25.0
  previous_composite: 53.1
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
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Real-Time Communication
- Video
- Voice
- Artificial Intelligence
- MCP
- Developer Tools
website: https://www.rtcstats.com/
---
