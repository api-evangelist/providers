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
- acting_count: 51
  human_in_the_loop: 0
  name: Canny Agentic Access
  operation_count: 51
  slug: canny-agentic-access
  summary_line: 51 operations · 51 acting
api_count: 16
apis:
- description: 'REST API for retrieving and managing Canny boards, posts, comments, votes, status changes, users, companies, categories, tags, and changelog entries. Requests authenticate using a secret API key sent '
  name: Canny REST API
  slug: v1-api
- description: The Autopilot API from Canny — 1 operation(s) for autopilot.
  name: Canny Autopilot API
  slug: canny-autopilot-api
- description: The Boards API from Canny — 2 operation(s) for boards.
  name: Canny Boards API
  slug: canny-boards-api
- description: The Categories API from Canny — 4 operation(s) for categories.
  name: Canny Categories API
  slug: canny-categories-api
- description: The ChangelogEntries API from Canny — 2 operation(s) for changelogentries.
  name: Canny ChangelogEntries API
  slug: canny-changelogentries-api
- description: The Comments API from Canny — 4 operation(s) for comments.
  name: Canny Comments API
  slug: canny-comments-api
- description: The Companies API from Canny — 3 operation(s) for companies.
  name: Canny Companies API
  slug: canny-companies-api
- description: The Groups API from Canny — 2 operation(s) for groups.
  name: Canny Groups API
  slug: canny-groups-api
- description: The Ideas API from Canny — 4 operation(s) for ideas.
  name: Canny Ideas API
  slug: canny-ideas-api
- description: The Insights API from Canny — 2 operation(s) for insights.
  name: Canny Insights API
  slug: canny-insights-api
- description: The Opportunities API from Canny — 1 operation(s) for opportunities.
  name: Canny Opportunities API
  slug: canny-opportunities-api
- description: The Posts API from Canny — 13 operation(s) for posts.
  name: Canny Posts API
  slug: canny-posts-api
- description: The StatusChanges API from Canny — 1 operation(s) for statuschanges.
  name: Canny StatusChanges API
  slug: canny-statuschanges-api
- description: The Tags API from Canny — 3 operation(s) for tags.
  name: Canny Tags API
  slug: canny-tags-api
- description: The Users API from Canny — 5 operation(s) for users.
  name: Canny Users API
  slug: canny-users-api
- description: The Votes API from Canny — 4 operation(s) for votes.
  name: Canny Votes API
  slug: canny-votes-api
artifact_total: 20
collections:
- collection_type: open
  name: Canny REST API
  slug: open-canny
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canny-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canny-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canny-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Canny
- group: company
  title: ''
  type: Website
  url: https://canny.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.canny.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.canny.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://canny.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://canny.io/signup
- group: operate
  title: ''
  type: Help Center
  url: https://help.canny.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canny-io
- group: agent
  title: ''
  type: LlmsText
  url: https://canny.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://canny.io/blog/feed
created: '2026-05-11'
description: Canny is a customer feedback and product management platform that collects, organizes, and prioritizes feature requests from users and internal teams, ties them to roadmaps and changelogs, and surfaces product analytics. The Canny REST API exposes boards, posts, comments, votes, users, companies, categories, status changes, and tags so product teams can integrate feedback with CRMs, support tools, and issue trackers. Requests use a secret API key sent as a POST parameter apiKey or in the x-api-key header against the base URL https://canny.io/api/v1.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canny.png
layout: provider
modified: '2026-05-11'
name: Canny
nav: Providers
network: true
overview: 'Canny publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Autopilot API, Boards API, Categories API, and 12 more. Tagged areas include Customer Feedback, Product Management, Feature Requests, Roadmap, and Changelog.


  Canny''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 29.7
  delta: -2.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.0
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canny/refs/heads/main/screenshots/canny-2026-06-20T173923.png
security:
- kind: authentication
  name: Canny Authentication
  slug: canny-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Canny Domain Security
  slug: canny-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canny
tags:
- Customer Feedback
- Product Management
- Feature Requests
- Roadmap
- Changelog
- Voice of Customer
- SaaS
website: https://canny.io
---
