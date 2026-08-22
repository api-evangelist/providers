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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Zencoder Agentic Access
  operation_count: 16
  slug: zencoder-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 5
apis:
- description: Operations for managing accounts.
  name: Zencoder Accounts API
  slug: zencoder-accounts-api
- description: Operations for getting input details and progress.
  name: Zencoder Inputs API
  slug: zencoder-inputs-api
- description: Operations for managing Zencoder encoding jobs.
  name: Zencoder Jobs API
  slug: zencoder-jobs-api
- description: Operations for getting output details and progress.
  name: Zencoder Outputs API
  slug: zencoder-outputs-api
- description: Operations for getting reports.
  name: Zencoder Reports API
  slug: zencoder-reports-api
artifact_total: 16
asyncapis:
- description: ''
  name: Zencoder Notifications Webhooks
  slug: zencoder-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zencoder Accounts API
  slug: open-zencoder-accounts-api
- collection_type: open
  name: Zencoder Accounts Inputs API
  slug: open-zencoder-inputs-api
- collection_type: open
  name: Zencoder Accounts Jobs API
  slug: open-zencoder-jobs-api
- collection_type: open
  name: Zencoder Accounts Outputs API
  slug: open-zencoder-outputs-api
- collection_type: open
  name: Zencoder Accounts Reports API
  slug: open-zencoder-reports-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zencoder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zencoder.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zencoder.support.brightcove.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zencoder.support.brightcove.com/
- group: docs
  title: ''
  type: APIReference
  url: https://zencoder.support.brightcove.com/references/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://zencoder.support.brightcove.com/getting-started/quick-start-zencoder.html
- group: operate
  title: ''
  type: Support
  url: https://zencoder.support.brightcove.com/support/index.html
- group: start
  title: ''
  type: SignUp
  url: https://app.zencoder.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.zencoder.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightcove.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightcove.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zencoder
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brightcove.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zencoder-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/zencoder-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zencoder-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zencoder-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zencoder-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zencoder-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zencoder-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zencoder-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zencoder-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zencoder-notifications-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zencoder-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zencoder-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zencoder-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zencoder-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zencoder-llms.txt
created: '2026-07-17'
description: Zencoder is a cloud-based video and audio encoding (transcoding) platform, now part of Brightcove, that turns source media into web-, mobile-, and broadcast-ready outputs at scale. Its REST API lets developers submit encoding jobs, generate multiple simultaneous outputs (MP4, HLS, DASH, HEVC/H.265, VP9, 4K/UHD, HDR10), apply captions, watermarks, clips, and thumbnails, protect content with DRM and encryption, and receive completion notifications via webhooks. Zencoder is known for its Emmy Award-winning Context Aware Encoding (CAE), no queue time, and per-minute usage-based pricing. The v2 API is organized around Jobs, Inputs, Outputs, Accounts, and Reports resources and authenticates with a Zencoder-Api-Key header (also accepted as an api_key query parameter). Originally an a16z / GV / 500 Global-backed startup, Zencoder was acquired by Brightcove and its API is documented and supported under the Brightcove developer surface.
image: https://zencoder.support.brightcove.com/assets/s-site-assets-favicons/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: zencoder-mcp.yml
  slug: zencoder-mcpyml
modified: '2026-07-21'
name: Zencoder
nav: Providers
network: true
overview: 'Zencoder publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Inputs API, Jobs API, and 2 more. Tagged areas include Company, Video, Video Encoding, Transcoding, and Media.


  The Zencoder catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zencoder''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, authentication, and 22 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 51.3
  delta: 0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 58.5
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 51.0
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zencoder/refs/heads/main/screenshots/zencoder-2026-08-17T083039.png
security:
- kind: authentication
  name: Zencoder Authentication
  slug: zencoder-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zencoder Domain Security
  slug: zencoder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zencoder
tags:
- Company
- Video
- Video Encoding
- Transcoding
- Media
- Streaming
- Video Processing
- Cloud
- Brightcove
- Captions
- DRM
- HLS
website: https://zencoder.com
---
