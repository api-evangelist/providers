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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Reddit Agentic Access
  operation_count: 84
  slug: reddit-agentic-access
  summary_line: 84 operations · 34 acting
api_count: 2
apis:
- description: Reddit's OAuth 2.0 authorization system provides authentication for all Reddit API access. Developers register applications at reddit.com/prefs/apps to obtain client credentials. Supported grant types
  name: Reddit OAuth 2.0 Authorization
  slug: oauth
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints related to the authenticated user account, including identity, preferences, karma, trophies, and friend management.
  name: Reddit Account API
  slug: reddit-account-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for managing user and link flair within subreddits, including flair templates, assignments, and configuration.
  name: Reddit Flair API
  slug: reddit-flair-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for interacting with submissions (links) and comments, including voting, saving, hiding, reporting, and submitting content.
  name: Reddit Links & Comments API
  slug: reddit-links-comments-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for retrieving sorted listings of content from subreddits, including hot, new, rising, top, and controversial posts.
  name: Reddit Listings API
  slug: reddit-listings-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for managing private messages, including inbox, sent, unread messages, composing, and message actions.
  name: Reddit Messages API
  slug: reddit-messages-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for subreddit moderation tasks, including approving and removing content, managing bans, moderation logs, and modqueue.
  name: Reddit Moderation API
  slug: reddit-moderation-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints implementing the oEmbed protocol for embedding Reddit content in external websites and applications.
  name: Reddit oEmbed API
  slug: reddit-oembed-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for searching Reddit content including submissions, subreddits, and users across the platform.
  name: Reddit Search API
  slug: reddit-search-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for managing and retrieving information about subreddits, including subscription, creation, rules, and settings.
  name: Reddit Subreddits API
  slug: reddit-subreddits-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for retrieving information about Reddit users, including profiles, post history, comment history, and trophies.
  name: Reddit Users API
  slug: reddit-users-api
- baseURL: https://oauth.reddit.com
  baseurl_source: declared
  description: Endpoints for managing subreddit wikis, including reading and editing wiki pages, revision history, and permissions.
  name: Reddit Wiki API
  slug: reddit-wiki-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reddit Ads Account API
  slug: open-reddit-account-api
- collection_type: open
  name: Reddit Ads Account Accounts API
  slug: open-reddit-accounts-api
- collection_type: open
  name: Reddit Ads Account Ad Groups API
  slug: open-reddit-ad-groups-api
- collection_type: open
  name: Reddit Account Ads API
  slug: open-reddit-ads-api
- collection_type: open
  name: Reddit Ads Account Campaigns API
  slug: open-reddit-campaigns-api
- collection_type: open
  name: Reddit Ads Account Conversions API
  slug: open-reddit-conversions-api
- collection_type: open
  name: Reddit Ads Account Custom Audiences API
  slug: open-reddit-custom-audiences-api
- collection_type: open
  name: Reddit Data API
  slug: open-reddit-data-api
- collection_type: open
  name: Reddit Embeds
  slug: open-reddit-embeds
- collection_type: open
  name: Reddit Ads Account Flair API
  slug: open-reddit-flair-api
- collection_type: open
  name: Reddit Ads Account Funding API
  slug: open-reddit-funding-api
- collection_type: open
  name: Reddit Ads Account Links & Comments API
  slug: open-reddit-links-comments-api
- collection_type: open
  name: Reddit Ads Account Listings API
  slug: open-reddit-listings-api
- collection_type: open
  name: Reddit Ads Account Messages API
  slug: open-reddit-messages-api
- collection_type: open
  name: Reddit Ads Account Moderation API
  slug: open-reddit-moderation-api
- collection_type: open
  name: Reddit Ads Account oEmbed API
  slug: open-reddit-oembed-api
- collection_type: open
  name: Reddit Ads Account Reporting API
  slug: open-reddit-reporting-api
- collection_type: open
  name: Reddit Ads Account Search API
  slug: open-reddit-search-api
- collection_type: open
  name: Reddit Ads Account Subreddits API
  slug: open-reddit-subreddits-api
- collection_type: open
  name: Reddit Ads Account Targeting API
  slug: open-reddit-targeting-api
- collection_type: open
  name: Reddit Ads Account Users API
  slug: open-reddit-users-api
- collection_type: open
  name: Reddit Ads Account Wiki API
  slug: open-reddit-wiki-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/reddit-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reddit-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/reddit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reddit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reddit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/reddit-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reddit-com
- group: company
  title: ''
  type: Website
  url: https://www.reddit.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.reddit.com/dev/api
- group: docs
  title: ''
  type: Documentation
  url: https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reddit-archive
- group: company
  title: ''
  type: Blog
  url: https://www.redditinc.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reddit.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redditinc.com/policies/user-agreement
- group: operate
  title: ''
  type: StatusPage
  url: https://www.redditstatus.com/
- group: operate
  title: ''
  type: Support
  url: https://support.reddithelp.com/hc/en-us
- group: start
  title: ''
  type: Signup
  url: https://www.reddit.com/register
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/reddit-data-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/reddit-ads-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/reddit-embeds-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/reddit-post-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/reddit-comment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/reddit-subreddit-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/reddit-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/reddit-post-structure.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/reddit-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/reddit-vocabulary.yml
created: '2026-01-01'
description: Reddit is a social news aggregation, discussion, and community platform where users submit, vote, and comment on content organized into topic-based communities called subreddits. Reddit provides developer APIs for accessing platform data, managing communities, running advertising campaigns, and embedding content. The Reddit Data API provides access to posts, comments, subreddits, user profiles, and moderation tools via OAuth 2.0. The Reddit Ads API enables programmatic management of advertising campaigns, audiences, and conversion tracking. All API access requires OAuth 2.0 authentication via the oauth.reddit.com server at 60 requests per minute.
examples:
- key_count: 2
  name: Reddit Ads Api Create Campaign Example
  slug: reddit-ads-api-create-campaign-example
- key_count: 2
  name: Reddit Data Api Get Subreddit Hot Example
  slug: reddit-data-api-get-subreddit-hot-example
finops:
- name: Reddit Finops
  service_category: Social Media Data
  slug: reddit-finops
graphqls:
- description: This conceptual GraphQL schema represents the Reddit platform's data model, derived from the official Reddit Data API (https://www.reddit.com/dev/api/) and Reddit's OAuth 2.0 authentication system. Re
  name: Reddit GraphQL Schema
  slug: reddit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reddit.png
json_schemas:
- name: Reddit Comment
  property_count: 29
  slug: reddit-comment
- name: Reddit Post (Submission)
  property_count: 37
  slug: reddit-post
- name: Reddit Subreddit
  property_count: 30
  slug: reddit-subreddit
json_structures:
- name: Reddit Post Structure
  property_count: 0
  slug: reddit-post-structure
jsonld:
- class_count: 0
  name: Reddit Context
  property_count: 7
  slug: reddit-context
layout: provider
modified: '2026-05-19'
name: Reddit
nav: Providers
network: true
overview: 'Reddit publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Flair API, Links & Comments API, and 8 more. Tagged areas include Advertising, Communities, Content, Social-Media, and Social News.


  The Reddit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Reddit''s developer surface includes authentication, documentation, engineering blog, support, signup flow, and 22 more developer resources.'
plans:
- name: Reddit Plans Pricing
  plan_count: 2
  slug: reddit-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Reddit Rate Limits
  slug: reddit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Reddit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: reddit-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Reddit API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 8
  slug: reddit-rules
scopes:
- name: Reddit Scopes
  scope_count: 20
  slug: reddit-scopes
  summary_line: 20 scopes · authorizationCode
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 60.3
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reddit/refs/heads/main/screenshots/reddit-2026-08-17T081506.png
security:
- kind: authentication
  name: Reddit Authentication
  slug: reddit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Reddit Domain Security
  slug: reddit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Reddit Vulnerability Disclosure
  slug: reddit-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: reddit
tags:
- Advertising
- Communities
- Content
- Social-Media
- Social News
website: https://www.reddit.com
---
