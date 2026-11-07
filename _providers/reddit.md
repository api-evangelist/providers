---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Reddit Agentic Access
  operation_count: 56
  slug: reddit-agentic-access
  summary_line: 56 operations · 19 acting
api_count: 3
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
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: The Reddit Advertising API (v3) lets advertisers and partners programmatically manage ad accounts, businesses, campaigns, ad groups, ads, creative assets, custom and saved audiences, pixels, product c
  name: Reddit Ads API
  slug: reddit-ads-api
- description: 'Protocol Buffer service definitions for the Reddit API as exposed to Devvit apps (Reddit''s Developer Platform): Flair, GraphQL, LinksAndComments, Listings, Moderation, ModNote, NewModmail, PrivateMess'
  name: Reddit Devvit Reddit API Plugin (gRPC)
  slug: devvit-reddit-api-plugin
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about ad account history.
  name: Reddit Ad Account History API
  slug: reddit-ad-account-history-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about ad accounts.
  name: Reddit Ad Accounts API
  slug: reddit-ad-accounts-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about ad groups.
  name: Reddit Ad Groups API
  slug: reddit-ad-groups-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about apps.
  name: Reddit App API
  slug: reddit-app-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Suggest bids.
  name: Reddit Bid Suggestions API
  slug: reddit-bid-suggestions-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about businesses.
  name: Reddit Businesses API
  slug: reddit-businesses-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about campaigns.
  name: Reddit Campaigns API
  slug: reddit-campaigns-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about creative assets stored in the asset library.
  name: Reddit Creative Assets API
  slug: reddit-creative-assets-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about creative generator.
  name: Reddit Creative Generator API
  slug: reddit-creative-generator-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about custom audiences. > **Note:** We're updating custom audience estimates during the week of October 14, 2026. Advertisers may see lower estimates after these updates roll out. [Learn m
  name: Reddit Custom Audiences API
  slug: reddit-custom-audiences-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about data deletion jobs.
  name: Reddit Data Deletion API
  slug: reddit-data-deletion-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about forecasting.
  name: Reddit Forecasting API
  slug: reddit-forecasting-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about funding instruments.
  name: Reddit Funding Instruments API
  slug: reddit-funding-instruments-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about lead generation forms.
  name: Reddit Lead Generation Forms API
  slug: reddit-lead-generation-forms-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about members.
  name: Reddit Members API
  slug: reddit-members-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about Pixels.
  name: Reddit Pixels API
  slug: reddit-pixels-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about posts. > **Note:** This is a legacy API. Use [Structured Posts API](/docs/v3/api/structured-posts) instead.
  name: Reddit Posts API
  slug: reddit-posts-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about product catalogs.
  name: Reddit Product Catalogs API
  slug: reddit-product-catalogs-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about profiles.
  name: Reddit Profiles API
  slug: reddit-profiles-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about reports.
  name: Reddit Reports API
  slug: reddit-reports-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about saved audiences.
  name: Reddit Saved Audiences API
  slug: reddit-saved-audiences-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about SKAdNetwork.
  name: Reddit SK Ad Network API
  slug: reddit-skadnetwork-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about structured posts.
  name: Reddit Structured Posts API
  slug: reddit-structured-posts-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about targeting.
  name: Reddit Targeting API
  slug: reddit-targeting-api
- baseURL: https://www.reddit.com
  baseurl_source: declared
  description: Endpoints implementing the oEmbed protocol for embedding Reddit content in external websites and applications.
  name: Reddit o Embed API
  slug: reddit-o-embed-api
- baseURL: https://ads-api.reddit.com/api/v3
  baseurl_source: declared
  description: Information about time zones.
  name: Reddit Timezones API
  slug: reddit-timezones-api
artifact_total: 99
asyncapis:
- description: ''
  name: Reddit Webhooks
  slug: reddit-webhooks
collections:
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
- group: operate
  href: https://artifacts.apis.io/reddit/rate-limits/reddit-ads-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reddit-ads-api-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/reddit/rules/reddit-rules.yml
  title: ''
  type: Spectral
  url: rules/reddit-rules.yml
- group: design
  href: https://artifacts.apis.io/reddit/rules/reddit-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/reddit-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/reddit/json-ld/reddit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/reddit-context.jsonld
- group: agent
  href: https://artifacts.apis.io/reddit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/reddit/asyncapi/reddit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/reddit-webhooks.yml
- group: design
  href: https://artifacts.apis.io/reddit/data-model/reddit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reddit-data-model.yml
- group: build
  href: https://artifacts.apis.io/reddit/cli/reddit-cli.yml
  title: ''
  type: CLI
  url: cli/reddit-cli.yml
- group: operate
  href: https://artifacts.apis.io/reddit/changelog/reddit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/reddit-changelog.yml
- group: design
  href: https://artifacts.apis.io/reddit/conventions/reddit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reddit-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/reddit?type=team
- group: operate
  href: https://artifacts.apis.io/reddit/lifecycle/reddit-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/reddit-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reddit/lifecycle/reddit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reddit-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reddit/errors/reddit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reddit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reddit/conformance/reddit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reddit-conformance.yml
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-wiki_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-wiki_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-widgets_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-widgets_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-users_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-users_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-subreddits_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-subreddits_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-privatemessages_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-privatemessages_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-newmodmail_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-newmodmail_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-modnote_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-modnote_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-moderation_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-moderation_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-listings_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-listings_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-linksandcomments_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-linksandcomments_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-graphql_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-graphql_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-flair_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-flair_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/grpc/reddit-devvit-common_msg.proto
  title: ''
  type: Protobuf
  url: grpc/reddit-devvit-common_msg.proto
- group: other
  href: https://artifacts.apis.io/reddit/overlays/reddit-account-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/reddit-account-api-overlay.yaml
- group: build
  href: https://artifacts.apis.io/reddit/mcp/reddit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/reddit-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/reddit/mcp/reddit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reddit-mcp.yml
- group: auth
  href: https://artifacts.apis.io/reddit/well-known/reddit-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/reddit-www-security.txt
- group: auth
  href: https://artifacts.apis.io/reddit/well-known/reddit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/reddit-security.txt
- group: auth
  href: https://artifacts.apis.io/reddit/well-known/reddit-oauth-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/reddit-oauth-security.txt
- group: auth
  href: https://artifacts.apis.io/reddit/well-known/reddit-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/reddit-api-security.txt
- group: agent
  href: https://artifacts.apis.io/reddit/well-known/reddit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reddit-well-known.yml
- group: other
  href: https://artifacts.apis.io/reddit/hosts/reddit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reddit-hosts.yml
- group: build
  href: https://artifacts.apis.io/reddit/integrations/reddit-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/reddit-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/reddit/vendors/reddit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reddit-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/reddit/plans/reddit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reddit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/reddit/rate-limits/reddit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reddit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/reddit/finops/reddit-finops.yml
  title: ''
  type: FinOps
  url: finops/reddit-finops.yml
- group: other
  href: https://artifacts.apis.io/reddit/vendor-facets/reddit-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/reddit-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/reddit/capabilities/reddit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/reddit-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/reddit/agentic-access/reddit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reddit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/reddit/security/reddit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/reddit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/reddit/security/reddit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reddit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/reddit/authentication/reddit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reddit-authentication.yml
- group: auth
  href: https://artifacts.apis.io/reddit/scopes/reddit-scopes.yml
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
  url: https://developers.reddit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.reddit.com/dev/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.reddit.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.reddit.com/docs/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.reddit.com/docs/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developers.reddit.com/docs/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://ads-api.reddit.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reddit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reddit-archive
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redditinc.com/policies/developer-terms
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
  href: https://artifacts.apis.io/reddit/openapi/_original/reddit-data-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/reddit-data-api-openapi.yml
- group: docs
  href: https://artifacts.apis.io/reddit/openapi/_original/reddit-embeds-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/reddit-embeds-openapi.yml
- group: docs
  href: https://artifacts.apis.io/reddit/json-schema/reddit-post-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/reddit-post-schema.json
- group: docs
  href: https://artifacts.apis.io/reddit/json-schema/reddit-comment-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/reddit-comment-schema.json
- group: docs
  href: https://artifacts.apis.io/reddit/json-schema/reddit-subreddit-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/reddit-subreddit-schema.json
- group: design
  href: https://artifacts.apis.io/reddit/json-ld/reddit-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/reddit-context.jsonld
- group: design
  href: https://artifacts.apis.io/reddit/json-structure/reddit-post-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/reddit-post-structure.json
- group: design
  href: https://artifacts.apis.io/reddit/rules/reddit-rules.yml
  title: ''
  type: SpectralRuleset
  url: rules/reddit-rules.yml
- group: design
  href: https://artifacts.apis.io/reddit/vocabulary/reddit-vocabulary.yml
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
- has_sources: true
  method: generated
  name: Reddit Finops
  primary_unit: ''
  service_category: Social Media Data
  slug: reddit-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reddit.png
json_schemas:
- name: Account
  property_count: 11
  slug: reddit-account
- name: Reddit Comment
  property_count: 29
  slug: reddit-comment
- name: components_enums_report_field
  property_count: 0
  slug: reddit-components-enums-report-field
- name: components_enums_time_zones
  property_count: 0
  slug: reddit-components-enums-time-zones
- name: AppLastFiredAt
  property_count: 24
  slug: reddit-components-schema-app-last-fired-at-report
- name: Campaign
  property_count: 30
  slug: reddit-components-schema-campaign
- name: ConversionEvent
  property_count: 8
  slug: reddit-components-schema-pixel-conversion-event
- name: Product
  property_count: 48
  slug: reddit-components-schema-product
- name: KarmaBreakdown
  property_count: 3
  slug: reddit-karma-breakdown
- name: Listing
  property_count: 2
  slug: reddit-listing
- name: OEmbedResponse
  property_count: 14
  slug: reddit-oembed-response
- name: Reddit Post (Submission)
  property_count: 37
  slug: reddit-post
- name: SubredditRule
  property_count: 6
  slug: reddit-subreddit-rule
- name: Reddit Subreddit
  property_count: 30
  slug: reddit-subreddit
- name: WikiPage
  property_count: 2
  slug: reddit-wiki-page
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
mcp_servers:
- description: Reddit's Devvit developer platform ships an official MCP server, published on npm as @devvit/mcp ("MCP for Devvit things", latest 0.0.27, 2026-06-12), to assist with agent-driven development of Devvit
  name: Reddit Devvit MCP server
  slug: devvit
modified: '2026-11-05'
name: Reddit
nav: Providers
network: true
overview: 'Reddit publishes 39 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Flair API, Links & Comments API, and 36 more. Tagged areas include Reddit, Advertising, Community, Content, and Social Media.


  The Reddit catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Reddit''s developer surface includes CLI, changelog, authentication, API reference, documentation, getting-started guide, engineering blog, and 70 more developer resources.'
plans:
- name: Reddit Plans Pricing
  plan_count: 2
  slug: reddit-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 21
  name: Reddit Ads Api Rate Limits
  slug: reddit-ads-api-rate-limits
- limit_count: 4
  name: Reddit Rate Limits
  slug: reddit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Reddit — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: reddit-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
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
  scope_count: 23
  slug: reddit-scopes
  summary_line: 23 scopes · authorizationCode
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 41
    catalog_earned: 74.8
    catalog_earned_first_party: 20.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.7
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 67.5
    developer_ergonomics: 66.1
    discoverability: 68.3
    operational_transparency: 92.1
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/reddit/reddit-2026-08-17T081506.png
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
skill_count: 6
skills:
- name: reddit-ads-campaign-reporting
  slug: reddit-ads-campaign-reporting
- name: reddit-ads-launch-a-campaign
  slug: reddit-ads-launch-a-campaign
- name: reddit-browse-a-subreddit
  slug: reddit-browse-a-subreddit
- name: reddit-post-and-comment
  slug: reddit-post-and-comment
- name: reddit-search-reddit
  slug: reddit-search-reddit
- name: reddit-work-the-modqueue
  slug: reddit-work-the-modqueue
slug: reddit
tags:
- Reddit
- Advertising
- Community
- Content
- Social Media
- Social News
- Social
website: https://www.reddit.com
---
