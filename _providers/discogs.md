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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Discogs Agentic Access
  operation_count: 50
  slug: discogs-agentic-access
  summary_line: 50 operations · 16 acting
api_count: 8
apis:
- description: 'Access Discogs database: artists, releases, masters, labels, and search.'
  name: Discogs Database API
  slug: discogs-database-api
- description: Image asset retrieval (proxied via OAuth).
  name: Discogs Image API
  slug: discogs-image-api
- description: Bulk inventory export and CSV upload management.
  name: Discogs Inventory Management API
  slug: discogs-inventory-management-api
- description: Marketplace listings, orders, fees, price suggestions, and release stats.
  name: Discogs Marketplace API
  slug: discogs-marketplace-api
- description: Manage a user's record collection.
  name: Discogs User Collection API
  slug: discogs-user-collection-api
- description: Authenticated user identity, profile, submissions, and contributions.
  name: Discogs User Identity API
  slug: discogs-user-identity-api
- description: Browse and manage user-created lists of releases, artists, and labels.
  name: Discogs User Lists API
  slug: discogs-user-lists-api
- description: Manage a user's wantlist.
  name: Discogs User Wantlist API
  slug: discogs-user-wantlist-api
artifact_total: 177
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/discogs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/discogs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/discogs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/discogs-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.discogs.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.discogs.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.discogs.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.discogs.com/hc/articles/360009334593-API-Terms-of-Use
- group: auth
  title: ''
  type: Authentication
  url: https://www.discogs.com/developers#page:authentication
- group: operate
  title: ''
  type: Support
  url: https://support.discogs.com
- group: operate
  title: ''
  type: Forums
  url: https://www.discogs.com/forum/topic/1082
- group: operate
  title: ''
  type: Status
  url: https://status.discogs.com
- group: company
  title: ''
  type: Blog
  url: https://blog.discogs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/discogs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/discogs-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/discogs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: other
  title: Monthly XML Data Dumps
  type: BulkData
  url: https://discogs-data-dumps.s3.us-west-2.amazonaws.com/index.html
- group: build
  title: MCP Server (cswkim)
  type: Tools
  url: https://github.com/cswkim/discogs-mcp-server
- group: build
  title: MCP Server (rianvdm OAuth)
  type: Tools
  url: https://github.com/rianvdm/discogs-mcp
- group: build
  title: MCP Server (pipeworx-io)
  type: Tools
  url: https://github.com/pipeworx-io/mcp-discogs
- group: build
  title: MCP Server (andylobban Self-hostable)
  type: Tools
  url: https://github.com/andylobban/discogs-mcp-server
- group: build
  title: MCP Server (leosakharoff)
  type: Tools
  url: https://github.com/leosakharoff/discogs-mcp
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/discogs-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/discogs-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/discogs-context.jsonld
created: '2026-05-28'
description: Discogs is a community-built music database and marketplace for physical music releases (vinyl, CD, cassette, and more). The Discogs API gives developers programmatic read/write access to artists, releases, masters, labels, search, user collections and wantlists, marketplace listings, orders, and inventory management — using Discogs Auth tokens, key+secret credentials, or full OAuth 1.0a on behalf of other users.
examples:
- key_count: 12
  name: Discogs Artist Example
  slug: discogs-artist-example
- key_count: 11
  name: Discogs Artist Release Example
  slug: discogs-artist-release-example
- key_count: 7
  name: Discogs Artist Summary Example
  slug: discogs-artist-summary-example
- key_count: 4
  name: Discogs Collection Folder Example
  slug: discogs-collection-folder-example
- key_count: 6
  name: Discogs Collection Release Example
  slug: discogs-collection-release-example
- key_count: 7
  name: Discogs Community Example
  slug: discogs-community-example
- key_count: 2
  name: Discogs Contribution Example
  slug: discogs-contribution-example
- key_count: 2
  name: Discogs Fee Example
  slug: discogs-fee-example
- key_count: 3
  name: Discogs Identifier Example
  slug: discogs-identifier-example
- key_count: 4
  name: Discogs Identity Example
  slug: discogs-identity-example
- key_count: 6
  name: Discogs Image Example
  slug: discogs-image-example
- key_count: 8
  name: Discogs Inventory Export Example
  slug: discogs-inventory-export-example
- key_count: 2
  name: Discogs Inventory Exports Response Example
  slug: discogs-inventory-exports-response-example
- key_count: 7
  name: Discogs Inventory Upload Example
  slug: discogs-inventory-upload-example
- key_count: 2
  name: Discogs Inventory Uploads Response Example
  slug: discogs-inventory-uploads-response-example
- key_count: 12
  name: Discogs Label Example
  slug: discogs-label-example
- key_count: 9
  name: Discogs Label Release Example
  slug: discogs-label-release-example
- key_count: 5
  name: Discogs Label Summary Example
  slug: discogs-label-summary-example
- key_count: 11
  name: Discogs List Example
  slug: discogs-list-example
- key_count: 7
  name: Discogs List Item Example
  slug: discogs-list-item-example
- key_count: 18
  name: Discogs Listing Example
  slug: discogs-listing-example
- key_count: 11
  name: Discogs Listing New Example
  slug: discogs-listing-new-example
- key_count: 9
  name: Discogs Listing Release Example
  slug: discogs-listing-release-example
- key_count: 0
  name: Discogs Listing Update Example
  slug: discogs-listing-update-example
- key_count: 2
  name: Discogs Lists Response Example
  slug: discogs-lists-response-example
- key_count: 0
  name: Discogs Master Example
  slug: discogs-master-example
- key_count: 17
  name: Discogs Order Example
  slug: discogs-order-example
- key_count: 7
  name: Discogs Order Message Example
  slug: discogs-order-message-example
- key_count: 2
  name: Discogs Order Messages Response Example
  slug: discogs-order-messages-response-example
- key_count: 2
  name: Discogs Orders Response Example
  slug: discogs-orders-response-example
- key_count: 5
  name: Discogs Pagination Example
  slug: discogs-pagination-example
- key_count: 2
  name: Discogs Price Example
  slug: discogs-price-example
- key_count: 2
  name: Discogs Price Suggestion Example
  slug: discogs-price-suggestion-example
- key_count: 0
  name: Discogs Price Suggestions Response Example
  slug: discogs-price-suggestions-response-example
- key_count: 30
  name: Discogs Profile Example
  slug: discogs-profile-example
- key_count: 5
  name: Discogs Profile Update Example
  slug: discogs-profile-update-example
- key_count: 31
  name: Discogs Release Example
  slug: discogs-release-example
- key_count: 4
  name: Discogs Release Format Example
  slug: discogs-release-format-example
- key_count: 2
  name: Discogs Release Rating Example
  slug: discogs-release-rating-example
- key_count: 3
  name: Discogs Release Stats Example
  slug: discogs-release-stats-example
- key_count: 11
  name: Discogs Release Summary Example
  slug: discogs-release-summary-example
- key_count: 12
  name: Discogs Release Version Example
  slug: discogs-release-version-example
- key_count: 15
  name: Discogs Search Result Release Example
  slug: discogs-search-result-release-example
- key_count: 2
  name: Discogs Submission Example
  slug: discogs-submission-example
- key_count: 5
  name: Discogs Track Example
  slug: discogs-track-example
- key_count: 3
  name: Discogs User Release Rating Example
  slug: discogs-user-release-rating-example
- key_count: 3
  name: Discogs User Summary Example
  slug: discogs-user-summary-example
- key_count: 5
  name: Discogs Video Example
  slug: discogs-video-example
- key_count: 5
  name: Discogs Want Example
  slug: discogs-want-example
graphqls:
- description: This document describes a conceptual GraphQL schema for the Discogs API. Discogs is a community-built music database and marketplace for physical music releases (vinyl, CD, cassette, and more). The Di
  name: Discogs GraphQL Schema
  slug: discogs-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/discogs.png
json_schemas:
- name: ArtistRelease
  property_count: 11
  slug: discogs-artist-release
- name: Artist
  property_count: 12
  slug: discogs-artist
- name: ArtistSummary
  property_count: 7
  slug: discogs-artist-summary
- name: CollectionFolder
  property_count: 4
  slug: discogs-collection-folder
- name: CollectionRelease
  property_count: 6
  slug: discogs-collection-release
- name: Community
  property_count: 7
  slug: discogs-community
- name: Contribution
  property_count: 2
  slug: discogs-contribution
- name: Currency
  property_count: 0
  slug: discogs-currency
- name: Fee
  property_count: 2
  slug: discogs-fee
- name: Identifier
  property_count: 3
  slug: discogs-identifier
- name: Identity
  property_count: 4
  slug: discogs-identity
- name: Image
  property_count: 6
  slug: discogs-image
- name: InventoryExport
  property_count: 8
  slug: discogs-inventory-export
- name: InventoryExportsResponse
  property_count: 2
  slug: discogs-inventory-exports-response
- name: InventoryUpload
  property_count: 7
  slug: discogs-inventory-upload
- name: InventoryUploadsResponse
  property_count: 2
  slug: discogs-inventory-uploads-response
- name: LabelRelease
  property_count: 9
  slug: discogs-label-release
- name: Label
  property_count: 12
  slug: discogs-label
- name: LabelSummary
  property_count: 5
  slug: discogs-label-summary
- name: ListItem
  property_count: 7
  slug: discogs-list-item
- name: List
  property_count: 11
  slug: discogs-list
- name: ListingNew
  property_count: 11
  slug: discogs-listing-new
- name: ListingRelease
  property_count: 9
  slug: discogs-listing-release
- name: Listing
  property_count: 18
  slug: discogs-listing
- name: ListingUpdate
  property_count: 0
  slug: discogs-listing-update
- name: ListsResponse
  property_count: 2
  slug: discogs-lists-response
- name: Master
  property_count: 0
  slug: discogs-master
- name: MediaCondition
  property_count: 0
  slug: discogs-media-condition
- name: OrderMessage
  property_count: 7
  slug: discogs-order-message
- name: OrderMessagesResponse
  property_count: 2
  slug: discogs-order-messages-response
- name: Order
  property_count: 17
  slug: discogs-order
- name: OrdersResponse
  property_count: 2
  slug: discogs-orders-response
- name: Pagination
  property_count: 5
  slug: discogs-pagination
- name: Price
  property_count: 2
  slug: discogs-price
- name: PriceSuggestion
  property_count: 2
  slug: discogs-price-suggestion
- name: PriceSuggestionsResponse
  property_count: 0
  slug: discogs-price-suggestions-response
- name: Profile
  property_count: 30
  slug: discogs-profile
- name: ProfileUpdate
  property_count: 5
  slug: discogs-profile-update
- name: ReleaseFormat
  property_count: 4
  slug: discogs-release-format
- name: ReleaseRating
  property_count: 2
  slug: discogs-release-rating
- name: Release
  property_count: 31
  slug: discogs-release
- name: ReleaseStats
  property_count: 3
  slug: discogs-release-stats
- name: ReleaseSummary
  property_count: 11
  slug: discogs-release-summary
- name: ReleaseVersion
  property_count: 12
  slug: discogs-release-version
- name: SearchResultArtist
  property_count: 0
  slug: discogs-search-result-artist
- name: SearchResultLabel
  property_count: 0
  slug: discogs-search-result-label
- name: SearchResultMaster
  property_count: 0
  slug: discogs-search-result-master
- name: SearchResultRelease
  property_count: 15
  slug: discogs-search-result-release
- name: SleeveCondition
  property_count: 0
  slug: discogs-sleeve-condition
- name: Submission
  property_count: 2
  slug: discogs-submission
- name: Track
  property_count: 5
  slug: discogs-track
- name: UserReleaseRating
  property_count: 3
  slug: discogs-user-release-rating
- name: UserSummary
  property_count: 3
  slug: discogs-user-summary
- name: Video
  property_count: 5
  slug: discogs-video
- name: Want
  property_count: 5
  slug: discogs-want
json_structures:
- name: Discogs Artist Release Structure
  property_count: 11
  slug: discogs-artist-release-structure
- name: Discogs Artist Structure
  property_count: 12
  slug: discogs-artist-structure
- name: Discogs Artist Summary Structure
  property_count: 7
  slug: discogs-artist-summary-structure
- name: Discogs Collection Folder Structure
  property_count: 4
  slug: discogs-collection-folder-structure
- name: Discogs Collection Release Structure
  property_count: 6
  slug: discogs-collection-release-structure
- name: Discogs Community Structure
  property_count: 7
  slug: discogs-community-structure
- name: Discogs Contribution Structure
  property_count: 2
  slug: discogs-contribution-structure
- name: Discogs Currency Structure
  property_count: 0
  slug: discogs-currency-structure
- name: Discogs Fee Structure
  property_count: 2
  slug: discogs-fee-structure
- name: Discogs Identifier Structure
  property_count: 3
  slug: discogs-identifier-structure
- name: Discogs Identity Structure
  property_count: 4
  slug: discogs-identity-structure
- name: Discogs Image Structure
  property_count: 6
  slug: discogs-image-structure
- name: Discogs Inventory Export Structure
  property_count: 8
  slug: discogs-inventory-export-structure
- name: Discogs Inventory Exports Response Structure
  property_count: 2
  slug: discogs-inventory-exports-response-structure
- name: Discogs Inventory Upload Structure
  property_count: 7
  slug: discogs-inventory-upload-structure
- name: Discogs Inventory Uploads Response Structure
  property_count: 2
  slug: discogs-inventory-uploads-response-structure
- name: Discogs Label Release Structure
  property_count: 9
  slug: discogs-label-release-structure
- name: Discogs Label Structure
  property_count: 12
  slug: discogs-label-structure
- name: Discogs Label Summary Structure
  property_count: 5
  slug: discogs-label-summary-structure
- name: Discogs List Item Structure
  property_count: 7
  slug: discogs-list-item-structure
- name: Discogs List Structure
  property_count: 11
  slug: discogs-list-structure
- name: Discogs Listing New Structure
  property_count: 11
  slug: discogs-listing-new-structure
- name: Discogs Listing Release Structure
  property_count: 9
  slug: discogs-listing-release-structure
- name: Discogs Listing Structure
  property_count: 18
  slug: discogs-listing-structure
- name: Discogs Listing Update Structure
  property_count: 0
  slug: discogs-listing-update-structure
- name: Discogs Lists Response Structure
  property_count: 2
  slug: discogs-lists-response-structure
- name: Discogs Master Structure
  property_count: 0
  slug: discogs-master-structure
- name: Discogs Media Condition Structure
  property_count: 0
  slug: discogs-media-condition-structure
- name: Discogs Order Message Structure
  property_count: 7
  slug: discogs-order-message-structure
- name: Discogs Order Messages Response Structure
  property_count: 2
  slug: discogs-order-messages-response-structure
- name: Discogs Order Structure
  property_count: 17
  slug: discogs-order-structure
- name: Discogs Orders Response Structure
  property_count: 2
  slug: discogs-orders-response-structure
- name: Discogs Pagination Structure
  property_count: 5
  slug: discogs-pagination-structure
- name: Discogs Price Structure
  property_count: 2
  slug: discogs-price-structure
- name: Discogs Price Suggestion Structure
  property_count: 2
  slug: discogs-price-suggestion-structure
- name: Discogs Price Suggestions Response Structure
  property_count: 0
  slug: discogs-price-suggestions-response-structure
- name: Discogs Profile Structure
  property_count: 30
  slug: discogs-profile-structure
- name: Discogs Profile Update Structure
  property_count: 5
  slug: discogs-profile-update-structure
- name: Discogs Release Format Structure
  property_count: 4
  slug: discogs-release-format-structure
- name: Discogs Release Rating Structure
  property_count: 2
  slug: discogs-release-rating-structure
- name: Discogs Release Stats Structure
  property_count: 3
  slug: discogs-release-stats-structure
- name: Discogs Release Structure
  property_count: 31
  slug: discogs-release-structure
- name: Discogs Release Summary Structure
  property_count: 11
  slug: discogs-release-summary-structure
- name: Discogs Release Version Structure
  property_count: 12
  slug: discogs-release-version-structure
- name: Discogs Search Result Artist Structure
  property_count: 0
  slug: discogs-search-result-artist-structure
- name: Discogs Search Result Label Structure
  property_count: 0
  slug: discogs-search-result-label-structure
- name: Discogs Search Result Master Structure
  property_count: 0
  slug: discogs-search-result-master-structure
- name: Discogs Search Result Release Structure
  property_count: 15
  slug: discogs-search-result-release-structure
- name: Discogs Sleeve Condition Structure
  property_count: 0
  slug: discogs-sleeve-condition-structure
- name: Discogs Submission Structure
  property_count: 2
  slug: discogs-submission-structure
- name: Discogs Track Structure
  property_count: 5
  slug: discogs-track-structure
- name: Discogs User Release Rating Structure
  property_count: 3
  slug: discogs-user-release-rating-structure
- name: Discogs User Summary Structure
  property_count: 3
  slug: discogs-user-summary-structure
- name: Discogs Video Structure
  property_count: 5
  slug: discogs-video-structure
- name: Discogs Want Structure
  property_count: 5
  slug: discogs-want-structure
jsonld:
- class_count: 49
  name: Discogs Context
  property_count: 159
  slug: discogs-context
layout: provider
modified: '2026-05-29'
name: Discogs
nav: Providers
network: true
overview: 'Discogs publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Database API, Image API, Inventory Management API, and 5 more. Tagged areas include Music, Marketplace, Catalog, Community, and Vinyl.


  The Discogs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Discogs'' developer surface includes authentication, documentation, API reference, support, status page, engineering blog, tooling, and 19 more developer resources.'
plans:
- name: Discogs Plans Pricing
  plan_count: 2
  slug: discogs-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Discogs Rate Limits
  slug: discogs-rate-limits
rules:
- name: Discogs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: discogs-jsonschema-spectral-rules
- name: Discogs API Rules
  rule_count: 35
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 19
  slug: discogs-rules
scopes:
- name: Discogs Scopes
  scope_count: 2
  slug: discogs-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.1
  delta: -5.9
  facets:
    commercial_clarity: 31.6
    contract_quality: 64.4
    developer_ergonomics: 32.6
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/discogs/refs/heads/main/screenshots/discogs-2026-07-25T212056.png
security:
- kind: authentication
  name: Discogs Authentication
  slug: discogs-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Discogs Domain Security
  slug: discogs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: discogs
tags:
- Music
- Marketplace
- Catalog
- Community
- Vinyl
- Public APIs
website: https://www.discogs.com
---
