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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Disqus Agentic Access
  operation_count: 25
  slug: disqus-agentic-access
  summary_line: 25 operations · 13 acting
api_count: 5
apis:
- description: The Categories API from Disqus — 2 operation(s) for categories.
  name: Disqus Categories API
  slug: disqus-categories-api
- description: The Forums API from Disqus — 10 operation(s) for forums.
  name: Disqus Forums API
  slug: disqus-forums-api
- description: The Posts API from Disqus — 6 operation(s) for posts.
  name: Disqus Posts API
  slug: disqus-posts-api
- description: The Threads API from Disqus — 4 operation(s) for threads.
  name: Disqus Threads API
  slug: disqus-threads-api
- description: The Users API from Disqus — 3 operation(s) for users.
  name: Disqus Users API
  slug: disqus-users-api
artifact_total: 10
collections:
- collection_type: open
  name: Disqus Public API
  slug: open-disqus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/disqus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/disqus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/disqus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/disqus-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://disqus.com
- group: docs
  title: ''
  type: Documentation
  url: https://disqus.com/api/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://disqus.com/api/applications/
- group: auth
  title: ''
  type: Authentication
  url: https://disqus.com/api/docs/auth/
- group: commercial
  title: ''
  type: Pricing
  url: https://disqus.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://disqus.com/profile/signup/
- group: start
  title: ''
  type: Login
  url: https://disqus.com/profile/login/
- group: operate
  title: ''
  type: Help
  url: https://help.disqus.com/
- group: operate
  title: ''
  type: Support
  url: https://help.disqus.com/en/articles/1717104-contacting-disqus
- group: company
  title: ''
  type: Blog
  url: https://blog.disqus.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.disqus.com/en/articles/1717103-disqus-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.disqus.com/en/articles/1717102-terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/disqus
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/disqus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/disqus
created: '2026-05-11'
description: Disqus is a hosted web comments and community discussion service used by publishers and bloggers to add threaded commenting, social sharing, and audience engagement features to their sites without running their own backend. The Disqus Public API lets developers read and write comments, threads, forums, users, and category data and integrate Disqus communities into custom applications. Authentication uses OAuth 2.0 plus an API key and secret, with all REST endpoints served from disqus.com/api/3.0/.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/disqus.png
layout: provider
modified: '2026-05-11'
name: Disqus
nav: Providers
network: true
overview: 'Disqus publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Forums API, Posts API, and 2 more. Tagged areas include Comments, Community, Discussions, Publishing, and Audience Engagement.


  Disqus'' developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 13 more developer resources.'
random_paper: 25
scopes:
- name: Disqus Scopes
  scope_count: 3
  slug: disqus-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 36.5
  delta: -2.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 50.0
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/disqus/refs/heads/main/screenshots/disqus-2026-06-20T180049.png
security:
- kind: authentication
  name: Disqus Authentication
  slug: disqus-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Disqus Domain Security
  slug: disqus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: disqus
tags:
- Comments
- Community
- Discussions
- Publishing
- Audience Engagement
- Social
website: https://disqus.com
---
