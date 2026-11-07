---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Dev To Agentic Access
  operation_count: 167
  slug: dev-to-agentic-access
  summary_line: 167 operations · 54 acting
api_count: 20
apis:
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The Dev.to Webhooks API allows developers to subscribe to real-time notifications for events occurring on the Dev.to platform. By creating webhook subscriptions, applications can receive HTTP callback
  name: Dev.to Webhooks API
  slug: webhooks-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for creating, listing, retrieving, and deleting webhook subscriptions for real-time event notifications.
  name: dev-to Webhooks API
  slug: dev-to-webhooks-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The admin API from DEV Community — 16 operation(s) for admin.
  name: DEV Community Admin API
  slug: dev-to-admin-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The agent_sessions API from DEV Community — 4 operation(s) for agent_sessions.
  name: DEV Community Agent Sessions API
  slug: dev-to-agent-sessions-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The analytics API from DEV Community — 8 operation(s) for analytics.
  name: DEV Community Analytics API
  slug: dev-to-analytics-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for creating, reading, updating, and managing articles (blog posts, discussions, help threads) on the platform.
  name: DEV Community Articles API
  slug: dev-to-articles-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The badge_achievements API from DEV Community — 2 operation(s) for badge_achievements.
  name: DEV Community Badge Achievements API
  slug: dev-to-badge-achievements-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The badges API from DEV Community — 2 operation(s) for badges.
  name: DEV Community Badges API
  slug: dev-to-badges-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The billboards API from DEV Community — 3 operation(s) for billboards.
  name: DEV Community Billboards API
  slug: dev-to-billboards-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving comments on articles and podcast episodes, including threaded conversation views.
  name: DEV Community Comments API
  slug: dev-to-comments-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The concepts API from DEV Community — 7 operation(s) for concepts.
  name: DEV Community Concepts API
  slug: dev-to-concepts-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The events API from DEV Community — 2 operation(s) for events.
  name: DEV Community Events API
  slug: dev-to-events-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The feedback_messages API from DEV Community — 1 operation(s) for feedback_messages.
  name: DEV Community Feedback Messages API
  slug: dev-to-feedback-messages-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The followed_tags API from DEV Community — 2 operation(s) for followed_tags.
  name: DEV Community Followed Tags API
  slug: dev-to-followed-tags-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving followers of the authenticated user.
  name: DEV Community Followers API
  slug: dev-to-followers-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The follows API from DEV Community — 1 operation(s) for follows.
  name: DEV Community Follows API
  slug: dev-to-follows-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The health_checks API from DEV Community — 3 operation(s) for health_checks.
  name: DEV Community Health Checks API
  slug: dev-to-health-checks-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The instance API from DEV Community — 1 operation(s) for instance.
  name: DEV Community Instance API
  slug: dev-to-instance-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving organization details, members, and articles.
  name: DEV Community Organizations API
  slug: dev-to-organizations-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for managing static pages on the platform. Requires admin-level API key.
  name: DEV Community Pages API
  slug: dev-to-pages-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The podcast_episodes API from DEV Community — 2 operation(s) for podcast_episodes.
  name: DEV Community Podcast Episodes API
  slug: dev-to-podcast-episodes-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The profile images API from DEV Community — 2 operation(s) for profile images.
  name: DEV Community profile images API
  slug: dev-to-profile-images-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for creating and toggling reactions on articles, comments, and users.
  name: DEV Community Reactions API
  slug: dev-to-reactions-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The Reading List API from DEV Community — 2 operation(s) for reading list.
  name: DEV Community Reading List API
  slug: dev-to-reading-list-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The recommended_articles_lists API from DEV Community — 2 operation(s) for recommended_articles_lists.
  name: DEV Community Recommended Articles Lists API
  slug: dev-to-recommended-articles-lists-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The request_redirects API from DEV Community — 2 operation(s) for request_redirects.
  name: DEV Community Request Redirects API
  slug: dev-to-request-redirects-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The segments API from DEV Community — 5 operation(s) for segments.
  name: DEV Community Segments API
  slug: dev-to-segments-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The subforems API from DEV Community — 1 operation(s) for subforems.
  name: DEV Community Subforems API
  slug: dev-to-subforems-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The surveys API from DEV Community — 4 operation(s) for surveys.
  name: DEV Community Surveys API
  slug: dev-to-surveys-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The Tags API from DEV Community — 4 operation(s) for tags.
  name: DEV Community Tags API
  slug: dev-to-tags-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The trends API from DEV Community — 3 operation(s) for trends.
  name: DEV Community Trends API
  slug: dev-to-trends-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for retrieving user profiles and managing user accounts.
  name: DEV Community Users API
  slug: dev-to-users-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The videos API from DEV Community — 2 operation(s) for videos.
  name: DEV Community Videos API
  slug: dev-to-videos-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: Endpoints for managing display advertisements on the platform. Requires admin-level API key.
  name: DEV Community Display Ads API
  slug: dev-to-display-ads-api
- baseURL: https://dev.to/api
  baseurl_source: declared
  description: The Open API API from DEV Community — 1 operation(s) for open api.
  name: DEV Community Open API
  slug: dev-to-open-api-api
artifact_total: 65
asyncapis:
- description: The Dev.to Webhooks event-driven interface allows applications to receive real-time HTTP POST callbacks when specific events occur on the Dev.to platform. Webhook subscriptions are managed via the For
  name: Dev.to Webhooks Events
  slug: dev-to-webhooks-asyncapi
collections:
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
- group: commercial
  href: https://artifacts.apis.io/dev-to/finops/dev-to-finops.yml
  title: ''
  type: FinOps
  url: finops/dev-to-finops.yml
- group: other
  href: https://artifacts.apis.io/dev-to/capabilities/dev-to-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dev-to-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/dev-to/overlays/dev-to-display-ads-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dev-to-display-ads-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dev-to/agentic-access/dev-to-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dev-to-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dev-to/security/dev-to-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dev-to-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dev-to/authentication/dev-to-authentication.yml
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
  href: https://artifacts.apis.io/dev-to/json-ld/dev-to-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dev-to-context.jsonld
- group: docs
  href: https://artifacts.apis.io/dev-to/json-schema/dev-to-article-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/dev-to-article-schema.json
- group: company
  title: ''
  type: Blog
  url: https://dev.to/feed/devteam
- group: company
  title: ''
  type: Website
  url: https://dev.to
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.forem.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.forem.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.forem.com/api/v1
- group: operate
  title: ''
  type: Support
  url: https://dev.to/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.to/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dev.to/privacy
- group: start
  title: ''
  type: SignUp
  url: https://dev.to/enter
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.to
- group: operate
  href: https://artifacts.apis.io/dev-to/lifecycle/dev-to-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dev-to-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dev-to/lifecycle/dev-to-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dev-to-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://dev.to/security
- group: auth
  href: https://artifacts.apis.io/dev-to/security/dev-to-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dev-to-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dev-to/llms/dev-to-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dev-to-llms.txt
- group: agent
  href: https://artifacts.apis.io/dev-to/well-known/dev-to-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dev-to-well-known.yml
- group: build
  href: https://artifacts.apis.io/dev-to/packages/dev-to-packages.yml
  title: ''
  type: Packages
  url: packages/dev-to-packages.yml
- group: build
  href: https://artifacts.apis.io/dev-to/packages/dev-to-packages.yml
  title: ''
  type: SDKs
  url: packages/dev-to-packages.yml
- group: design
  href: https://artifacts.apis.io/dev-to/conventions/dev-to-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dev-to-conventions.yml
- group: design
  href: https://artifacts.apis.io/dev-to/conventions/dev-to-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dev-to-conventions.yml
- group: design
  href: https://artifacts.apis.io/dev-to/errors/dev-to-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dev-to-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dev-to/conformance/dev-to-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dev-to-conformance.yml
- group: design
  href: https://artifacts.apis.io/dev-to/data-model/dev-to-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dev-to-data-model.yml
- group: agent
  href: https://artifacts.apis.io/dev-to/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/dev-to/rate-limits/dev-to-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dev-to-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dev-to/plans/dev-to-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dev-to-plans-pricing.yml
created: '2026-05-03'
description: Access Forem articles, users and other resources via API. For a real-world example of Forem in action, check out [DEV](https://www.dev.to). All endpoints can be accessed with the 'api-key' header and a accept header, but some of them are accessible publicly without authentication. Dates and date times, unless otherwise specified, must be in the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.
finops:
- has_sources: true
  method: derived
  name: Dev To Finops
  primary_unit: ''
  service_category: ''
  slug: dev-to-finops
  template: true
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
modified: '2026-09-17'
name: DEV Community
nav: Providers
network: true
overview: 'DEV Community publishes 35 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dev.to Webhooks API, dev-to Webhooks API, Admin API, and 32 more. Tagged areas include Developer Community, Content, Publishing, Social, and Blogging.


  The DEV Community catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  DEV Community''s developer surface includes authentication, engineering blog, documentation, API reference, support, signup flow, and 30 more developer resources.'
plans:
- name: Dev To Plans Pricing
  plan_count: 0
  slug: dev-to-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Dev To Rate Limits
  slug: dev-to-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: DEV Community — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: dev-to-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: DEV Community — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dev-to-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 57.5
    catalog_earned_first_party: 8.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 66.5
    developer_ergonomics: 54.2
    discoverability: 78.6
    operational_transparency: 65.8
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 58.8
      total: 34
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/dev-to/dev-to-2026-06-20T175954.png
security:
- kind: authentication
  name: Dev To Authentication
  slug: dev-to-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dev To Domain Security
  slug: dev-to-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dev To Vulnerability Disclosure
  slug: dev-to-vulnerability-disclosure
  summary_line: contact published
skill_count: 3
skills:
- name: dev-to-manage-webhooks
  slug: dev-to-manage-webhooks
- name: dev-to-publish-article
  slug: dev-to-publish-article
- name: dev-to-read-community
  slug: dev-to-read-community
slug: dev-to
tags:
- Developer Community
- Content
- Publishing
- Social
- Blogging
- Open Source
- Articles
- Webhook
website: https://dev.to
---
