---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 92
  human_in_the_loop: 7
  name: Aura Historia Com Agentic Access
  operation_count: 153
  slug: aura-historia-com-agentic-access
  summary_line: 153 operations · 92 acting · 7 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: The Administration API from Aura Historia — 1 operation(s) for administration.
  name: Aura Historia Administration API
  slug: aura-historia-com-administration-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Public Auction discovery, catalogue reads, and administrator Auction management.
  name: Aura Historia Auctions API
  slug: aura-historia-com-auctions-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Stripe checkout, billing-portal, and subscription-management session creation for authenticated users.
  name: Aura Historia Billing API
  slug: aura-historia-com-billing-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: ListingSource retrieval, authenticated creation and update, and caller-administered listing sources.
  name: Aura Historia Listing Sources API
  slug: aura-historia-com-listingsources-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Newsletter subscription upsert workflows for website or product-surface sign-up flows.
  name: Aura Historia Newsletter API
  slug: aura-historia-com-newsletter-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: In-app notification retrieval, bulk updates, single-notification updates, and notification cleanup workflows.
  name: Aura Historia Notifications API
  slug: aura-historia-com-notifications-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: OAuth 2.0 authorization, token, revocation, introspection, and OAuth client metadata management.
  name: Aura Historia OAuth API
  slug: aura-historia-com-oauth-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Public process liveness and service readiness probes.
  name: Aura Historia Operations API
  slug: aura-historia-com-operations-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Public aggregate catalogue statistics.
  name: Aura Historia Overview API
  slug: aura-historia-com-overview-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: The Parties API from Aura Historia — 1 operation(s) for parties.
  name: Aura Historia Parties API
  slug: aura-historia-com-parties-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Partnership application submission, review tracking, administration, and decision workflows.
  name: Aura Historia Partnership Applications API
  slug: aura-historia-com-partnershipapplications-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Partnership administration, safe summary reads, and membership/ListingSource count workflows.
  name: Aura Historia Partnerships API
  slug: aura-historia-com-partnerships-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: The Party API from Aura Historia — 7 operation(s) for party.
  name: Aura Historia Party API
  slug: aura-historia-com-party-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Product retrieval, product history, similar-product discovery, product search, and partner catalog ingestion workflows.
  name: Aura Historia Product Listings API
  slug: aura-historia-com-productlistings-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Saved search creation, maintenance, persisted matches, and match-feedback workflows.
  name: Aura Historia Search Filters API
  slug: aura-historia-com-search-filters-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Authenticated user profile management, admin user management, access-token lifecycle management, and partnership listing.
  name: Aura Historia User Account API
  slug: aura-historia-com-user-account-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: The Users API from Aura Historia — 3 operation(s) for users.
  name: Aura Historia Users API
  slug: aura-historia-com-users-api
- baseURL: https://api.stage.aura-historia.com
  baseurl_source: declared
  description: Watchlist membership, notification preferences, and watchlist-specific product state for authenticated users.
  name: Aura Historia Watchlist API
  slug: aura-historia-com-watchlist-api
artifact_total: 37
common:
- group: agent
  href: https://artifacts.apis.io/aura-historia-com/agentic-access/aura-historia-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aura-historia-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aura-historia-com/rules/aura-historia-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aura-historia-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aura-historia-com/json-ld/aura-historia-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aura-historia-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aura-historia-com/vocabulary/aura-historia-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aura-historia-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aura-historia-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aura-historia-com/data-model/aura-historia-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aura-historia-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aura-historia-com/authentication/aura-historia-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aura-historia-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/aura-historia-com/errors/aura-historia-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aura-historia-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aura-historia-com/conformance/aura-historia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aura-historia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aura-historia-com/llms/aura-historia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aura-historia-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aura-historia-com/mcp/aura-historia-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aura-historia-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aura-historia-com/mcp/aura-historia-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aura-historia-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aura-historia-com/well-known/aura-historia-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aura-historia-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aura-historia-com/hosts/aura-historia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aura-historia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aura-historia-com/vendors/aura-historia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aura-historia-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.aura-historia.com/
- group: auth
  href: https://artifacts.apis.io/aura-historia-com/security/aura-historia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aura-historia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aura-historia.com
- group: commercial
  title: ''
  type: Pricing
  url: https://aura-historia.com/en#pricing
- group: start
  title: ''
  type: SignUp
  url: https://aura-historia.com/en/login?redirect=%2Fen%2F&mode=sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aura-historia.com/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aura-historia.com/en/terms-and-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aura-historia
created: '2026-10-29'
description: Aura Historia is a global platform for antiques, art, and distinctive objects. It indexes dealers, auction houses, and specialist sellers worldwide, providing a single searchable view for collectors, decorators, and trade professionals. The service aggregates scattered inventory, offers watchlists, alerts, and multilingual search, and connects users directly to original listings, ensuring clarity and accessibility across markets.
image: https://aura-historia.com/logo-banner.png
json_schemas:
- name: AsyncProductListingBatchReport
  property_count: 3
  slug: aura-historia-com-async-product-listing-batch-report
- name: CreateProductListingData
  property_count: 10
  slug: aura-historia-com-create-product-listing-data
- name: OAuthClientConsentMetadataData
  property_count: 8
  slug: aura-historia-com-oauth-client-consent-metadata-data
- name: OAuthClientMetadataResponseData
  property_count: 10
  slug: aura-historia-com-oauth-client-metadata-response-data
- name: OAuthTokenResponseData
  property_count: 5
  slug: aura-historia-com-oauth-token-response-data
- name: ReplaceShippingProfileData
  property_count: 4
  slug: aura-historia-com-replace-shipping-profile-data
- name: ShippingDefaultData
  property_count: 4
  slug: aura-historia-com-shipping-default-data
- name: ShippingProfileData
  property_count: 6
  slug: aura-historia-com-shipping-profile-data
- name: UpdateProductListingData
  property_count: 10
  slug: aura-historia-com-update-product-listing-data
- name: UpsertProductListingData
  property_count: 10
  slug: aura-historia-com-upsert-product-listing-data
- name: WoocommerceProductWebhookUpsertData
  property_count: 11
  slug: aura-historia-com-woocommerce-product-webhook-upsert-data
jsonld:
- class_count: 120
  name: Aura Historia Com Context
  property_count: 174
  slug: aura-historia-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.aura-historia.com.
  name: Aura Historia MCP Server
  slug: aura-historia-com-mcp-yml
modified: '2026-10-29'
name: Aura Historia
nav: Providers
network: true
overview: 'Aura Historia publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Administration API, Auctions API, Billing API, and 15 more. Tagged areas include Company, Antiques, Marketplace, Search, and SaaS.


  The Aura Historia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aura Historia''s developer surface includes authentication, API reference, pricing, signup flow, and 19 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Aura Historia API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: aura-historia-com-rules
scopes:
- name: Aura Historia Com Scopes
  scope_count: 0
  slug: aura-historia-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 66.1
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aura Historia Com Authentication
  slug: aura-historia-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aura Historia Com Domain Security
  slug: aura-historia-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: discover-party-locations
  slug: aura-historia-com-discover-party-locations
slug: aura-historia-com
tags:
- Company
- Antiques
- Marketplace
- Search
- SaaS
website: https://aura-historia.com
---
