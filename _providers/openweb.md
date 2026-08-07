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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'JWT-authenticated REST API for publishers on the OpenWeb platform: request an API token, export comments/users/ranks (v2 and v4), retrieve top comments and trending articles, manage SSO users (registe'
  name: OpenWeb Publisher API
  slug: openweb-publisher-api
artifact_total: 6
asyncapis:
- description: ''
  name: Openweb Notifications Webhooks
  slug: openweb-notifications-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openweb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openweb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.openweb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openweb.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.openweb.com/reference/post_v1-publisher-auth
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.openweb.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.openweb.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spotim
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openweb.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openweb.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.openweb.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.openweb.com
- group: build
  title: ''
  type: Packages
  url: packages/openweb-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openweb-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openweb-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openweb-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openweb-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.openweb.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openweb-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openweb-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/openweb-notifications-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/openweb-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openweb-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openweb-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openweb-llms.txt
created: '2026-07-17'
description: OpenWeb (formerly Spot.IM) is a community and audience-engagement platform for publishers, delivering OpenWebOS — a unified, end-to-end suite for building community, harnessing first-party data, and driving sustainable revenue. Its developer platform exposes a JWT-authenticated Publisher API (comment export, top comments, trending articles, SSO user management, moderation policy, and SEO markup services) at api.openweb.com, a notification webhook surface, and web, Android, iOS, and React Native SDKs for embedding Conversation, Reactions, Community Spotlight, Live Blog, and Standalone Ad experiences. Backed by Insight Partners.
image: https://www.openweb.com/wp-content/uploads/2025/09/favicon-32x32-1.png
layout: provider
mcp_servers:
- description: ''
  name: openweb-mcp.yml
  slug: openweb-mcpyml
modified: '2026-07-20'
name: OpenWeb
nav: Providers
network: true
overview: 'OpenWeb publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Community, Comments, and Audience Engagement.


  The OpenWeb catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenWeb''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 19 more developer resources.'
random_paper: 74
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 51.6
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 45.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Openweb Authentication
  slug: openweb-authentication
  summary_line: http/jwt/sso · 4 schemes
- kind: domain-security
  name: Openweb Domain Security
  slug: openweb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Openweb Trust Center
  slug: openweb-trust-center
  summary_line: SOC 2 Type II
slug: openweb
tags:
- Company
- Consumer
- Community
- Comments
- Audience Engagement
- Publishing
- Media
- Moderation
- Identity
- SSO
- Webhooks
website: https://www.openweb.com/
---
