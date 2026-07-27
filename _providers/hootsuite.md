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
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Hootsuite Agentic Access
  operation_count: 13
  slug: hootsuite-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 5
apis:
- description: REST API for managing social media profiles, scheduling messages, reading and posting to connected networks, and pulling analytics across Hootsuite-managed accounts. Authentication uses OAuth 2.0 auth
  name: Hootsuite REST API
  slug: rest-api
- description: The Me API from Hootsuite — 1 operation(s) for me.
  name: Hootsuite Me API
  slug: hootsuite-me-api
- description: The Media API from Hootsuite — 2 operation(s) for media.
  name: Hootsuite Media API
  slug: hootsuite-media-api
- description: The Messages API from Hootsuite — 5 operation(s) for messages.
  name: Hootsuite Messages API
  slug: hootsuite-messages-api
- description: The SocialProfiles API from Hootsuite — 3 operation(s) for socialprofiles.
  name: Hootsuite SocialProfiles API
  slug: hootsuite-socialprofiles-api
artifact_total: 12
collections:
- collection_type: open
  name: Hootsuite Platform API
  slug: open-hootsuite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hootsuite-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hootsuite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hootsuite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hootsuite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hootsuite-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hootsuite
- group: company
  title: ''
  type: Website
  url: https://www.hootsuite.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hootsuite.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hootsuite.com/docs/api
- group: start
  title: ''
  type: Signup
  url: https://hootsuite.com/plans
- group: commercial
  title: ''
  type: Pricing
  url: https://hootsuite.com/plans
- group: start
  title: ''
  type: Login
  url: https://hootsuite.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.hootsuite.com
- group: company
  title: ''
  type: Blog
  url: https://blog.hootsuite.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hootsuite
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.hootsuite.com/llms.txt
created: '2026-05-11'
description: Hootsuite is a social media management platform that lets organizations schedule posts, monitor conversations, run paid campaigns, and analyze performance across LinkedIn, X (Twitter), Facebook, Instagram, TikTok, YouTube, and Pinterest from a single dashboard. The platform serves marketers, agencies, and enterprises with collaboration, approval, and governance workflows. The Hootsuite REST API uses OAuth 2.0 and provides programmatic access to social profiles, messages, scheduling, and analytics through the platform.hootsuite.com endpoint.
graphqls:
- description: This conceptual GraphQL schema represents the Hootsuite social media management platform API surface. Hootsuite provides a REST API at `https://platform.hootsuite.com/v1` with OAuth 2.0 authentication
  name: Hootsuite GraphQL Schema
  slug: hootsuite-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hootsuite.png
layout: provider
modified: '2026-05-11'
name: Hootsuite
nav: Providers
network: true
overview: 'Hootsuite publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Me API, Media API, Messages API, and 1 more. Tagged areas include Social Media, Social Media Management, Marketing, Content Scheduling, and Analytics.


  Hootsuite''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, and 10 more developer resources.'
random_paper: 44
scopes:
- name: Hootsuite Scopes
  scope_count: 1
  slug: hootsuite-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 35.2
  delta: 3.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 51.3
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hootsuite/refs/heads/main/screenshots/hootsuite-2026-06-20T182835.png
security:
- kind: authentication
  name: Hootsuite Authentication
  slug: hootsuite-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hootsuite Domain Security
  slug: hootsuite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hootsuite Vulnerability Disclosure
  slug: hootsuite-vulnerability-disclosure
  summary_line: Intigriti
slug: hootsuite
tags:
- Social Media
- Social Media Management
- Marketing
- Content Scheduling
- Analytics
- Engagement
website: https://www.hootsuite.com
---
