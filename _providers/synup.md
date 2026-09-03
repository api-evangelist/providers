---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: First-party remote Model Context Protocol server enumerating 126 tools in its published tool table across six surfaces (Locations, Listings, Reviews, Rankings, Posts & Social, Account & Insights). Ten
  name: Synup MCP Server
  slug: synup-mcp
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Automations API from Synup — 1 operation(s) for automations.
  name: Synup Automations API
  slug: synup-automations-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Connected Accounts API from Synup — 20 operation(s) for connected accounts.
  name: Synup Connected Accounts API
  slug: synup-connected-accounts-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Grid Rank API from Synup — 3 operation(s) for grid rank.
  name: Synup Grid Rank API
  slug: synup-grid-rank-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Listings API from Synup — 7 operation(s) for listings.
  name: Synup Listings API
  slug: synup-listings-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Local Post Ideas API from Synup — 41 operation(s) for local post ideas.
  name: Synup Local Post Ideas API
  slug: synup-local-post-ideas-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Locations API from Synup — 25 operation(s) for locations.
  name: Synup Locations API
  slug: synup-locations-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Menus API from Synup — 5 operation(s) for menus.
  name: Synup Menus API
  slug: synup-menus-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Organizing locations API from Synup — 14 operation(s) for organizing locations.
  name: Synup Organizing locations API
  slug: synup-organizing-locations-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Posts API from Synup — 6 operation(s) for posts.
  name: Synup Posts API
  slug: synup-posts-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Profile Analytics API from Synup — 3 operation(s) for profile analytics.
  name: Synup Profile Analytics API
  slug: synup-profile-analytics-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Rankings API from Synup — 6 operation(s) for rankings.
  name: Synup Rankings API
  slug: synup-rankings-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Review Campaigns API from Synup — 4 operation(s) for review campaigns.
  name: Synup Review Campaigns API
  slug: synup-review-campaigns-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Reviews API from Synup — 9 operation(s) for reviews.
  name: Synup Reviews API
  slug: synup-reviews-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Reviews/Review Sources API from Synup — 3 operation(s) for reviews/review sources.
  name: Synup Reviews/Review Sources API
  slug: synup-reviews-review-sources-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Social API from Synup — 3 operation(s) for social.
  name: Synup Social API
  slug: synup-social-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Social Post Ideas API from Synup — 47 operation(s) for social post ideas.
  name: Synup Social Post Ideas API
  slug: synup-social-post-ideas-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The User Management API from Synup — 11 operation(s) for user management.
  name: Synup User Management API
  slug: synup-user-management-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Webhooks API from Synup — 0 operation(s) for webhooks.
  name: Synup Webhooks API
  slug: synup-webhooks-api
- baseURL: https://api.synup.com/api/v4
  baseurl_source: declared
  description: The Webhooks/Webhooks API from Synup — 0 operation(s) for webhooks/webhooks.
  name: Synup Webhooks/Webhooks API
  slug: synup-webhooks-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Synup Webhooks
  slug: synup-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/synup-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.synup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.synup.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.synup.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.synup.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.synup.com/synup-local-seo-api-getting-started-doc-824500
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/synup-api-openapi.yml
- group: design
  title: ''
  type: Webhooks
  url: openapi/synup-webhooks-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/synup-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/synup-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synup-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/synup-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synup-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/synup-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/synup-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synup-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/synup-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synup-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synup-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.synup.com/en/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/synup-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/synup-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/synup-packages.yml
- group: design
  title: ''
  type: Components
  url: components/synup-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/synup-api-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/synup-examples.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/synup-schemas.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/synup-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/synup-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synup-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/synup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/synup-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synup
- group: other
  title: ''
  type: X
  url: https://x.com/synupinc
- group: company
  title: ''
  type: Blog
  url: https://www.synup.com/en/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synup.com/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.synup.com/
- group: start
  title: ''
  type: Login
  url: https://local.synup.com/users/find_workspace
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synup.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synup.com/en/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.synup.com/
created: '2026-06-13'
description: Synup is a local marketing platform for agencies and multi-location brands, providing a REST API (v4) for managing business locations, syndicating listing data to 80+ directories including Google, Apple, Bing and Facebook, aggregating and responding to reviews across every connected platform, running SMS and email review campaigns, tracking local search rankings with grid-rank heatmaps, publishing local and social posts, and pulling unified profile analytics. The platform serves marketing agencies with white-label tooling covering listings sync, reputation management, social media, local SEO and reporting, and ships a first-party remote MCP server so AI agents can drive the same surface as the dashboard.
finops:
- name: Synup Finops
  service_category: ''
  slug: synup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synup.png
json_schemas:
- name: Synup API v4 component schemas
  property_count: 0
  slug: synup-schemas
jsonld:
- class_count: 33
  name: Synup Context
  property_count: 2
  slug: synup-context
layout: provider
mcp_servers:
- description: 'Synup ships a first-party remote MCP server that exposes the same surface area as the Synup dashboard as agent tools: locations, listings, reviews, rankings, local and social posts, flows, account and'
  name: Synup MCP Server
  slug: synup-mcp-server
modified: '2026-08-13'
name: Synup
nav: Providers
network: true
overview: 'Synup publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Automations API, Connected Accounts API, Grid Rank API, and 16 more. Tagged areas include Local Marketing, Listings Management, Reputation Management, Local SEO, and Reviews.


  The Synup catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Synup''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, code examples, engineering blog, and 37 more developer resources.'
plans:
- name: Synup Plans Pricing
  plan_count: 3
  slug: synup-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Synup Rate Limits
  slug: synup-rate-limits
scopes:
- name: Synup Scopes
  scope_count: 2
  slug: synup-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 28
    catalog_gap: 44.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 19.7
    contract_quality: 72.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 26.3
  previous_composite: 60.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synup/refs/heads/main/screenshots/synup-2026-06-20T194835.png
security:
- kind: authentication
  name: Synup Authentication
  slug: synup-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Synup Domain Security
  slug: synup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synup
tags:
- Local Marketing
- Listings Management
- Reputation Management
- Local SEO
- Reviews
- Social-Media
- Analytics
- Business Listings
- Review Management
- Agency Software
website: https://www.synup.com/
---
