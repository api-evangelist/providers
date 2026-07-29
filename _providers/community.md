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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Community Agentic Access
  operation_count: 9
  slug: community-agentic-access
  summary_line: 9 operations · 9 acting
api_count: 4
apis:
- description: Community's Data Export API allows programmatic retrieval of account data in CSV or JSON formats, including member detail, campaign performance, link click performance, subscription state changes, and
  name: Community Data Export API
  slug: community-data-export-api
- description: The member-data API from Community — 4 operation(s) for member-data.
  name: Community member-data API
  slug: community-member-data-api
- description: The messaging API from Community — 1 operation(s) for messaging.
  name: Community messaging API
  slug: community-messaging-api
- description: The tags API from Community — 4 operation(s) for tags.
  name: Community tags API
  slug: community-tags-api
artifact_total: 11
asyncapis:
- description: ''
  name: Community Webhooks
  slug: community-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.community.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.community.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.community.com/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.community.com/reference/getting-started-with-your-api
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/community-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/community-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/community-async-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/community-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.community.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/community-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/community-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/community-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/community-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/community-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/community-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/community-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/community-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/community-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/community-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://community.com/blog
- group: operate
  title: ''
  type: Support
  url: https://community.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://community.com/pricing
- group: start
  title: ''
  type: Login
  url: https://community.com/login
- group: start
  title: ''
  type: SignUp
  url: https://community.com/signup/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://community.com/
created: '2026-07-17'
description: 'Community is a conversational messaging platform that lets brands, creators, artists, sports teams, media companies, and political organizations reach their audiences directly over SMS, MMS, WhatsApp, Apple Messages for Business, and RCS. Founded in 2019 and remote-first, Community pairs a campaign-and-flows product with a developer surface: an Async REST API to send Direct Messages, create and update members, set custom member data, manage subcommunities (tags), and opt members out; a Data Export API for member, campaign, and link analytics snapshots; and outbound webhooks for inbound/outbound messages and member lifecycle events. API access is provisioned per account by the Community team rather than self-serve.'
image: https://community.com/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: community-mcp.yml
  slug: community-mcpyml
modified: '2026-07-18'
name: Community
nav: Providers
network: true
overview: 'Community publishes 3 APIs on the [APIs.io](https://apis.io/) network: member-data API, messaging API, and tags API. Tagged areas include Messaging, SMS, Communications, Conversational, and Marketing.


  The Community catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Community''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 21 more developer resources.'
random_paper: 37
scopes:
- name: Community Scopes
  scope_count: 0
  slug: community-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.6
  delta: 0.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.4
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/community/refs/heads/main/screenshots/community-2026-07-25T210140.png
security:
- kind: authentication
  name: Community Authentication
  slug: community-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Community Domain Security
  slug: community-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Community Trust Center
  slug: community-trust-center
  summary_line: SOC 2, GDPR
slug: community
tags:
- Messaging
- SMS
- Communications
- Conversational
- Marketing
- Creators
- Webhooks
- Company
website: https://community.com/
---
