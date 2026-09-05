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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Facebook Pages Agentic Access
  operation_count: 18
  slug: facebook-pages-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- description: Graph API endpoints for reading and managing Facebook Pages, including publishing posts and stories, retrieving Page insights, managing comments and conversations, and configuring Page metadata. Authe
  name: Meta Graph API - Pages
  slug: graph-pages-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Comments API from Facebook Pages API — 1 operation(s) for comments.
  name: Facebook Pages API Comments API
  slug: facebook-pages-comments-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Conversations API from Facebook Pages API — 1 operation(s) for conversations.
  name: Facebook Pages API Conversations API
  slug: facebook-pages-conversations-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Feed API from Facebook Pages API — 1 operation(s) for feed.
  name: Facebook Pages API Feed API
  slug: facebook-pages-feed-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Insights API from Facebook Pages API — 1 operation(s) for insights.
  name: Facebook Pages API Insights API
  slug: facebook-pages-insights-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Me API from Facebook Pages API — 1 operation(s) for me.
  name: Facebook Pages API Me API
  slug: facebook-pages-me-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Meta Graph API Pages API from Facebook Pages API — 2 operation(s) for meta graph api pages.
  name: Facebook Pages API Meta Graph API Pages API
  slug: facebook-pages-meta-graph-api-pages-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Photos API from Facebook Pages API — 1 operation(s) for photos.
  name: Facebook Pages API Photos API
  slug: facebook-pages-photos-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Posts API from Facebook Pages API — 1 operation(s) for posts.
  name: Facebook Pages API Posts API
  slug: facebook-pages-posts-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Settings API from Facebook Pages API — 1 operation(s) for settings.
  name: Facebook Pages API Settings API
  slug: facebook-pages-settings-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Subscribed Apps API from Facebook Pages API — 1 operation(s) for subscribed apps.
  name: Facebook Pages API Subscribed Apps API
  slug: facebook-pages-subscribed-apps-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Tagged API from Facebook Pages API — 1 operation(s) for tagged.
  name: Facebook Pages API Tagged API
  slug: facebook-pages-tagged-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meta Graph API - Pages Comments API
  slug: open-facebook-pages-comments-api
- collection_type: open
  name: Meta Graph API - Pages Comments Conversations API
  slug: open-facebook-pages-conversations-api
- collection_type: open
  name: Meta Graph API - Pages Comments Feed API
  slug: open-facebook-pages-feed-api
- collection_type: open
  name: Meta Graph API - Pages Comments Insights API
  slug: open-facebook-pages-insights-api
- collection_type: open
  name: Meta Graph API - Pages Comments Me API
  slug: open-facebook-pages-me-api
- collection_type: open
  name: Meta Graph API - Pages Comments Meta Graph API Pages API
  slug: open-facebook-pages-meta-graph-api-pages-api
- collection_type: open
  name: Meta Graph API - Pages Comments Photos API
  slug: open-facebook-pages-photos-api
- collection_type: open
  name: Meta Graph API - Pages Comments Posts API
  slug: open-facebook-pages-posts-api
- collection_type: open
  name: Meta Graph API - Pages Comments Settings API
  slug: open-facebook-pages-settings-api
- collection_type: open
  name: Meta Graph API - Pages Comments Subscribed Apps API
  slug: open-facebook-pages-subscribed-apps-api
- collection_type: open
  name: Meta Graph API - Pages Comments Tagged API
  slug: open-facebook-pages-tagged-api
- collection_type: open
  name: Meta Graph API - Pages
  slug: open-facebook-pages
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/facebook-pages-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/facebook-pages-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/facebook-pages-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/facebook-pages-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://developers.facebook.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.facebook.com/docs/pages-api
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting
- group: start
  title: ''
  type: Signup
  url: https://developers.facebook.com/async/registration
- group: other
  title: ''
  type: App Dashboard
  url: https://developers.facebook.com/apps
- group: operate
  title: ''
  type: Support
  url: https://developers.facebook.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.facebook.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://developers.facebook.com/blog/
created: '2026-05-11'
description: The Facebook Pages API is part of the Meta Graph API and allows applications to manage Facebook Pages, including posting content, reading insights, moderating comments, managing tabs and settings, and receiving real-time webhook updates for Page events. Access is granted via OAuth 2.0 Page access tokens with permission scopes such as pages_manage_posts, pages_read_engagement, and pages_messaging.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/facebook-pages.png
layout: provider
modified: '2026-05-11'
name: Facebook Pages API
nav: Providers
network: true
overview: 'Facebook Pages API publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Conversations API, Feed API, and 8 more. Tagged areas include Social-Media, Facebook, Meta Graph API, Pages, and Content Publishing.


  Facebook Pages API''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 13
scopes:
- name: Facebook Pages Scopes
  scope_count: 7
  slug: facebook-pages-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/facebook-pages/refs/heads/main/screenshots/facebook-pages-2026-06-20T181006.png
security:
- kind: authentication
  name: Facebook Pages Authentication
  slug: facebook-pages-authentication
  summary_line: oauth2 · 1 scheme
slug: facebook-pages
tags:
- Social-Media
- Facebook
- Meta Graph API
- Pages
- Content Publishing
- Social Insights
website: https://developers.facebook.com
---
