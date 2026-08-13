---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-12'
api_count: 7
apis:
- description: The Comments API from Sylvia API — 2 operation(s) for comments.
  name: Sylvia API Comments API
  slug: sylvia-api-comments-api
- description: The Datasets API from Sylvia API — 1 operation(s) for datasets.
  name: Sylvia API Datasets API
  slug: sylvia-api-datasets-api
- description: The Live API from Sylvia API — 1 operation(s) for live.
  name: Sylvia API Live API
  slug: sylvia-api-live-api
- description: The Posts API from Sylvia API — 2 operation(s) for posts.
  name: Sylvia API Posts API
  slug: sylvia-api-posts-api
- description: The Subreddits API from Sylvia API — 2 operation(s) for subreddits.
  name: Sylvia API Subreddits API
  slug: sylvia-api-subreddits-api
- description: The Usage API from Sylvia API — 1 operation(s) for usage.
  name: Sylvia API Usage API
  slug: sylvia-api-usage-api
- description: The Users API from Sylvia API — 3 operation(s) for users.
  name: Sylvia API Users API
  slug: sylvia-api-users-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://sylvia-api.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://sylvia-api.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/sylvia-api-authentication.yml
created: '2026-08-04'
description: Sylvia API is a third-party Reddit data API that serves Reddit content as JSON — posts, comments with full recursive threads, subreddit and user surfaces, and a live comment feed. Twelve read operations cover post and comment search, single-item lookup, subreddit and user timelines, a live comments stream, dataset torrents for bulk access, and a usage endpoint. Authentication is an API key. It occupies the gap left by Pushshift, giving researchers and developers queryable Reddit history without going through OAuth on the first-party API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sylvia-api.png
layout: provider
modified: '2026-08-04'
name: Sylvia API
nav: Providers
network: true
overview: 'Sylvia API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Datasets API, Live API, and 4 more. Tagged areas include Reddit, Social, Data, Search, and Comments.


  Sylvia API''s developer surface includes authentication and 2 more developer resources.'
random_paper: 63
score:
  band: emerging
  composite: 25.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 61.2
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Sylvia Api Authentication
  slug: sylvia-api-authentication
  summary_line: 1 scheme
slug: sylvia-api
tags:
- Reddit
- Social
- Data
- Search
- Comments
- Research
- Content
- Datasets
website: https://sylvia-api.com/
---
