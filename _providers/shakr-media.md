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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 30.8
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: 'REST API for programmatic, end-to-end video creation and automated delivery. OAuth 2.0 client-credentials + bearer auth. Resources: TemplateStyleVersion, Mapping, RenderSession.'
  name: Shakr Video API
  slug: shakr-video-api
- description: Embeddable, white-labeled drag-and-drop video editor for the browser (npm @shakrmedia/editor-sdk).
  name: Shakr Video Editor SDK
  slug: shakr-video-editor-sdk
artifact_total: 7
asyncapis:
- description: ''
  name: Shakr Media Webhooks
  slug: shakr-media-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shakr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.shakr.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shakr.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.shakr.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.shakr.com/docs/quickstart/getting-server-token/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shakrmedia
- group: auth
  title: ''
  type: Authentication
  url: authentication/shakr-media-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shakr-media-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shakr-media-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shakr-media-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/shakr-media-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shakr-media-packages.yml
- group: design
  title: ''
  type: Components
  url: components/shakr-media-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shakr-media-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shakr-media-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shakr-media-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shakr-media-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shakr-media-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shakr-media-domain-security.yml
created: '2026-07-17'
description: 'Shakr is a video creation platform that helps businesses produce and automate video at scale. The Shakr Video API (v2) offers programmatic end-to-end video production: create a versioned creative template (TemplateStyleVersion), map input content (text, images, video, audio, fonts) onto its editable spec, kick off a render session, and automatically deliver the finished video to destinations such as Amazon S3, Microsoft Azure Blob Storage, and Facebook Ad Accounts — with completion webhooks. The Shakr Video Editor SDK embeds a white-labeled drag-and-drop video editor directly inside a customer''s product. Authentication uses the OAuth 2.0 Client Credentials Grant with scoped bearer tokens. Shakr is a 500 Global portfolio company.'
image: https://avatars.githubusercontent.com/shakrmedia
layout: provider
mcp_servers:
- description: ''
  name: shakr-media-mcp.yml
  slug: shakr-media-mcpyml
modified: '2026-07-21'
name: Shakr Media
nav: Providers
network: true
overview: 'Shakr Media publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Video Creation, Video Editing, and Video API.


  The Shakr Media catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shakr Media''s developer surface includes documentation, API reference, getting-started guide, authentication, and 15 more developer resources.'
random_paper: 23
scopes:
- name: Shakr Media Scopes
  scope_count: 6
  slug: shakr-media-scopes
  summary_line: 6 scopes
score:
  band: emerging
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 22.6
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 28.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Shakr Media Authentication
  slug: shakr-media-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Shakr Media Domain Security
  slug: shakr-media-domain-security
  summary_line: TLSv1.3
slug: shakr-media
tags:
- Company
- Video
- Video Creation
- Video Editing
- Video API
- Media
- SDK
- Automation
- Advertising
- White Label
website: https://shakr.com
---
