---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Dev To Agentic Access
  operation_count: 42
  slug: dev-to-agentic-access
  summary_line: 42 operations · 15 acting
api_count: 1
apis:
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The Dev.to Webhooks API allows developers to subscribe to real-time notifications for events occurring on the Dev.to platform. By creating webhook subscriptions, applications can receive HTTP callback
  name: Dev.to Webhooks API
  slug: webhooks-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for creating, reading, updating, and managing articles (blog posts, discussions, help threads) on the platform.
  name: dev-to Articles API
  slug: dev-to-articles-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving comments on articles and podcast episodes, including threaded conversation views.
  name: dev-to Comments API
  slug: dev-to-comments-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for managing display advertisements on the platform. Requires admin-level API key.
  name: dev-to DisplayAds API
  slug: dev-to-displayads-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving the tags followed by the authenticated user.
  name: dev-to FollowedTags API
  slug: dev-to-followedtags-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving followers of the authenticated user.
  name: dev-to Followers API
  slug: dev-to-followers-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving organization details, members, and articles.
  name: dev-to Organizations API
  slug: dev-to-organizations-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for managing static pages on the platform. Requires admin-level API key.
  name: dev-to Pages API
  slug: dev-to-pages-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving published podcast episodes.
  name: dev-to PodcastEpisodes API
  slug: dev-to-podcastepisodes-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving profile images of users and organizations.
  name: dev-to ProfileImages API
  slug: dev-to-profileimages-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for creating and toggling reactions on articles, comments, and users.
  name: dev-to Reactions API
  slug: dev-to-reactions-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving the authenticated user's reading list.
  name: dev-to ReadingList API
  slug: dev-to-readinglist-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The Tags API from dev-to — 1 operation(s) for tags.
  name: dev-to Tags API
  slug: dev-to-tags-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving user profiles and managing user accounts.
  name: dev-to Users API
  slug: dev-to-users-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for creating, listing, retrieving, and deleting webhook subscriptions for real-time event notifications.
  name: dev-to Webhooks API
  slug: dev-to-webhooks-api
artifact_total: 42
asyncapis:
- description: The Dev.to Webhooks event-driven interface allows applications to receive real-time HTTP POST callbacks when specific events occur on the Dev.to platform. Webhook subscriptions are managed via the For
  name: Dev.to Webhooks Events
  slug: dev-to-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dev.to Forem Articles API
  slug: open-dev-to-articles-api
- collection_type: open
  name: Dev.to Forem Articles Comments API
  slug: open-dev-to-comments-api
- collection_type: open
  name: Dev.to Forem Articles DisplayAds API
  slug: open-dev-to-displayads-api
- collection_type: open
  name: Dev.to Forem Articles FollowedTags API
  slug: open-dev-to-followedtags-api
- collection_type: open
  name: Dev.to Forem Articles Followers API
  slug: open-dev-to-followers-api
- collection_type: open
  name: Dev.to Forem API
  slug: open-dev-to-forem-api
- collection_type: open
  name: Dev.to Forem Articles Organizations API
  slug: open-dev-to-organizations-api
- collection_type: open
  name: Dev.to Forem Articles Pages API
  slug: open-dev-to-pages-api
- collection_type: open
  name: Dev.to Forem Articles PodcastEpisodes API
  slug: open-dev-to-podcastepisodes-api
- collection_type: open
  name: Dev.to Forem Articles ProfileImages API
  slug: open-dev-to-profileimages-api
- collection_type: open
  name: Dev.to Forem Articles Reactions API
  slug: open-dev-to-reactions-api
- collection_type: open
  name: Dev.to Forem Articles ReadingList API
  slug: open-dev-to-readinglist-api
- collection_type: open
  name: Dev.to Forem Articles Tags API
  slug: open-dev-to-tags-api
- collection_type: open
  name: Dev.to Forem Articles Users API
  slug: open-dev-to-users-api
- collection_type: open
  name: Dev.to Forem Articles Webhooks API
  slug: open-dev-to-webhooks-api
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
name: Dev To
nav: Providers
network: true
overview: 'Dev To publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Dev.to Webhooks API, dev-to Articles API, dev-to Comments API, and 12 more.


  The Dev To catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Dev To''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Dev To Plans Pricing
  plan_count: 3
  slug: dev-to-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Dev To Rate Limits
  slug: dev-to-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Dev To API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: dev-to-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Dev To API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dev-to-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 65.4
    developer_ergonomics: 23.8
    discoverability: 53.7
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
