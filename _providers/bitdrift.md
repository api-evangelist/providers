---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The bitdrift Capture public API — schema-first protobuf service definitions exposed over gRPC, Connect, and gRPC-over-JSON at api-public.bitdrift.io. Services under the bitdrift.public.unary.* package
  name: bitdrift Public API
  slug: bitdrift-public-api
artifact_total: 5
asyncapis:
- description: ''
  name: Bitdrift Webhooks
  slug: bitdrift-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://bitdrift.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bitdrift.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitdrift.io/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bitdrift.dev/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitdrift.io/quickstart.html
- group: start
  title: ''
  type: Quickstart
  url: https://docs.bitdrift.io/sdk/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.bitdrift.io/support/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.bitdrift.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitdriftlabs
- group: operate
  title: ''
  type: Roadmap
  url: https://bitdrift.io/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://bitdrift.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://bitdrift.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.bitdrift.io/support/tos-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.bitdrift.io/support/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitdrift.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://bitdrift.io/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://blog.bitdrift.io/post/soc-2-type-ii
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitdrift-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitdrift-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitdrift-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitdrift-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitdrift-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/bitdrift-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitdrift-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitdrift-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bitdrift-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitdrift-domain-security.yml
created: '2026-07-17'
description: bitdrift builds Capture, a cost-effective dynamic mobile observability platform for iOS, Android, and React Native. A lightweight on-device SDK stores high-volume telemetry locally and uploads only what is needed under real-time control from the bitdrift control plane, avoiding lengthy mobile release cycles to change what is collected. The platform surfaces Instant Insights dashboards, Workflows for custom metrics, funnels and session-capture rules, a Session Timeline for debugging, Issues & Crashes tracking, and Alerts. It is operated through a web portal and the `bd` CLI, and exposes a public, schema-first protobuf API over gRPC, Connect, and gRPC-over-JSON at api-public.bitdrift.io. bitdrift is a developer-tools company backed by Amplify Partners.
image: https://bitdrift.io/v/7280840156499158247/images/hero-block-poster-preview.png
layout: provider
mcp_servers:
- description: ''
  name: bitdrift MCP Server
  slug: bitdrift-mcp-server
modified: '2026-07-18'
name: bitdrift
nav: Providers
network: true
overview: 'bitdrift publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Observability, Mobile, and Monitoring.


  The bitdrift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  bitdrift''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 50.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitdrift/refs/heads/main/screenshots/bitdrift-2026-07-25T203143.png
security:
- kind: authentication
  name: Bitdrift Authentication
  slug: bitdrift-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bitdrift Domain Security
  slug: bitdrift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitdrift
tags:
- Company
- Developer Tools
- Observability
- Mobile
- Monitoring
- Logging
- Crash Reporting
- Session Replay
- SDK
- gRPC
- Telemetry
website: https://bitdrift.io
---
