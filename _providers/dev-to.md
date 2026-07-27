---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Dev To Agentic Access
  operation_count: 42
  slug: dev-to-agentic-access
  summary_line: 42 operations · 15 acting
api_count: 15
apis:
- description: The Dev.to Webhooks API allows developers to subscribe to real-time notifications for events occurring on the Dev.to platform. By creating webhook subscriptions, applications can receive HTTP callback
  name: Dev.to Webhooks API
  slug: webhooks-api
- description: Endpoints for creating, reading, updating, and managing articles (blog posts, discussions, help threads) on the platform.
  name: dev-to Articles API
  slug: dev-to-articles-api
- description: Endpoints for retrieving comments on articles and podcast episodes, including threaded conversation views.
  name: dev-to Comments API
  slug: dev-to-comments-api
- description: Endpoints for managing display advertisements on the platform. Requires admin-level API key.
  name: dev-to DisplayAds API
  slug: dev-to-displayads-api
- description: Endpoints for retrieving the tags followed by the authenticated user.
  name: dev-to FollowedTags API
  slug: dev-to-followedtags-api
- description: Endpoints for retrieving followers of the authenticated user.
  name: dev-to Followers API
  slug: dev-to-followers-api
- description: Endpoints for retrieving organization details, members, and articles.
  name: dev-to Organizations API
  slug: dev-to-organizations-api
- description: Endpoints for managing static pages on the platform. Requires admin-level API key.
  name: dev-to Pages API
  slug: dev-to-pages-api
- description: Endpoints for retrieving published podcast episodes.
  name: dev-to PodcastEpisodes API
  slug: dev-to-podcastepisodes-api
- description: Endpoints for retrieving profile images of users and organizations.
  name: dev-to ProfileImages API
  slug: dev-to-profileimages-api
- description: Endpoints for creating and toggling reactions on articles, comments, and users.
  name: dev-to Reactions API
  slug: dev-to-reactions-api
- description: Endpoints for retrieving the authenticated user's reading list.
  name: dev-to ReadingList API
  slug: dev-to-readinglist-api
- description: The Tags API from dev-to — 1 operation(s) for tags.
  name: dev-to Tags API
  slug: dev-to-tags-api
- description: Endpoints for retrieving user profiles and managing user accounts.
  name: dev-to Users API
  slug: dev-to-users-api
- description: Endpoints for creating, listing, retrieving, and deleting webhook subscriptions for real-time event notifications.
  name: dev-to Webhooks API
  slug: dev-to-webhooks-api
artifact_total: 27
asyncapis:
- description: The Dev.to Webhooks event-driven interface allows applications to receive real-time HTTP POST callbacks when specific events occur on the Dev.to platform. Webhook subscriptions are managed via the For
  name: Dev.to Webhooks Events
  slug: dev-to-webhooks-asyncapi
collections:
- collection_type: open
  name: Dev.to Forem API
  slug: open-dev-to-forem-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dev-to-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dev-to-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dev-to-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forem
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thepracticaldev
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dev-to-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/dev-to-article-schema.json
- group: company
  title: ''
  type: Blog
  url: https://dev.to/feed/devteam
description: Access Forem articles, users and other resources via API. For a real-world example of Forem in action, check out [DEV](https://www.dev.to). All endpoints can be accessed with the 'api-key' header and a accept header, but some of them are accessible publicly without authentication. Dates and date times, unless otherwise specified, must be in the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.
finops:
- name: Dev To Finops
  service_category: API
  slug: dev-to-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dev-to.png
json_schemas:
- name: Dev.to Article
  property_count: 29
  slug: dev-to-article
jsonld:
- class_count: 0
  name: Dev To Context
  property_count: 7
  slug: dev-to-context
layout: provider
modified: '2026-05-19'
name: dev-to
nav: Providers
network: true
overview: 'dev-to publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Dev.to Webhooks API, Articles API, Comments API, and 12 more.


  The dev-to catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  dev-to''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Dev To Plans Pricing
  plan_count: 3
  slug: dev-to-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Dev To Rate Limits
  slug: dev-to-rate-limits
rules:
- name: dev-to API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: dev-to-asyncapi-spectral-rules
- name: dev-to API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dev-to-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.9
  delta: 2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.3
    developer_ergonomics: 13.0
    discoverability: 80.0
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 44.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dev-to/refs/heads/main/screenshots/dev-to-2026-06-20T175954.png
security:
- kind: authentication
  name: Dev To Authentication
  slug: dev-to-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dev To Domain Security
  slug: dev-to-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dev-to
---
