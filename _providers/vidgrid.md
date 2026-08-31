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
    agent_skills: derived
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Vidgrid Agentic Access
  operation_count: 15
  slug: vidgrid-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 1
apis:
- description: The Caption API allows you to request and manage closed captioning on your Videos.
  name: VidGrid Caption API
  slug: vidgrid-caption-api
- description: The Folder API allows you to interact with folders on your VidGrid account.
  name: VidGrid Folder API
  slug: vidgrid-folder-api
- description: The Search API allows you to search for videos.
  name: VidGrid Search API
  slug: vidgrid-search-api
- description: The Video Creation Token API allows you to request a token that can be used to record or upload videos into your VidGrid account.
  name: VidGrid Token API
  slug: vidgrid-token-api
- description: The User API allows you to interact with users on your VidGrid account.
  name: VidGrid User API
  slug: vidgrid-user-api
- description: The Video API allows you to interact with videos on your VidGrid account.
  name: VidGrid Video API
  slug: vidgrid-video-api
- description: The Webhook API allows you to trigger webhook events.
  name: VidGrid Webhooks API
  slug: vidgrid-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Vidgrid Webhooks
  slug: vidgrid-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VidGrid API Reference Caption API
  slug: open-vidgrid-caption-api
- collection_type: open
  name: VidGrid API Reference Caption Folder API
  slug: open-vidgrid-folder-api
- collection_type: open
  name: VidGrid API Reference Caption Search API
  slug: open-vidgrid-search-api
- collection_type: open
  name: VidGrid API Reference Caption Token API
  slug: open-vidgrid-token-api
- collection_type: open
  name: VidGrid API Reference Caption User API
  slug: open-vidgrid-user-api
- collection_type: open
  name: VidGrid API Reference Caption Video API
  slug: open-vidgrid-video-api
- collection_type: open
  name: VidGrid API Reference Caption Webhooks API
  slug: open-vidgrid-webhooks-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/paylocity/
- group: other
  title: ''
  type: Overlay
  url: overlays/vidgrid-content-management-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://vidgrid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.vidgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vidgrid.com/docs/v2/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.vidgrid.com/docs/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.vidgrid.com/en/articles/2554249-api-docs-for-developers
- group: operate
  title: ''
  type: Support
  url: https://help.vidgrid.com/
- group: start
  title: ''
  type: Login
  url: https://app.vidgrid.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ilosvideos
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vidgrid-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vidgrid-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vidgrid-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vidgrid-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vidgrid-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vidgrid-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vidgrid-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vidgrid-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vidgrid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vidgrid-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vidgrid-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vidgrid-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/vidgrid-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vidgrid-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: VidGrid is an enterprise video platform for recording, hosting, captioning, and sharing interactive video, acquired by Paylocity and now branded VidGrid by Paylocity. Its Content Management API v2 is a JSON REST API for managing videos, captions, folders, users, and search on an account, plus record/upload tokens that launch the embeddable screen recorder and uploader, with webhook events for video and caption processing. API keys are Enterprise-restricted after a 14-day trial.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vidgrid.png
layout: provider
mcp_servers:
- description: ''
  name: VidGrid MCP Server
  slug: vidgrid-mcp-server
modified: '2026-07-21'
name: VidGrid
nav: Providers
network: true
overview: 'VidGrid publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Caption API, Folder API, Search API, and 4 more. Tagged areas include Video, Screen Recording, Captions, Video Hosting, and Webhook.


  The VidGrid catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VidGrid''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 20 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 1
  name: Vidgrid Rate Limits
  slug: vidgrid-rate-limits
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 64.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vidgrid/refs/heads/main/screenshots/vidgrid-2026-08-17T082745.png
security:
- kind: authentication
  name: Vidgrid Authentication
  slug: vidgrid-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Vidgrid Domain Security
  slug: vidgrid-domain-security
  summary_line: TLSv1.3 · HSTS
slug: vidgrid
tags:
- Video
- Screen Recording
- Captions
- Video Hosting
- Webhook
- Training
- HR
website: https://vidgrid.com/
---
