---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-11'
api_count: 18
apis:
- description: AI-optimized keyword and natural-language search results for products and other index sections, returned by search query with filtering, faceting, sorting, pagination and variations mapping.
  name: Constructor Search API
  slug: constructor-search-api
- description: AI-optimized autocomplete and autosuggest results for products and search suggestions retrieved by query prefix, with multi-section responses.
  name: Constructor Autocomplete API
  slug: constructor-autocomplete-api
- description: AI-optimized category browse results by facet name/value, item ID, collection ID or group ID, plus endpoints for browse groups, countable facets, facet options and collections.
  name: Constructor Browse API
  slug: constructor-browse-api
- description: AI-optimized recommendation results retrieved by pod identifier for onsite recommendation placements.
  name: Constructor Recommendations API
  slug: constructor-recommendations-api
- description: AI-optimized search results retrieved by uploaded image, with optional multi-item detection (segmentation) support.
  name: Constructor Image Search API
  slug: constructor-image-search-api
- description: Conversational product-discovery API returning intent-based suggestions over a Server-Sent Events stream, plus AI-generated item questions and answers.
  name: Constructor AI Shopping Agent API
  slug: constructor-ai-shopping-agent-api
- description: Authenticated catalog surface for creating, replacing, updating and deleting items, variations, item groups and full catalog files, plus item field statistics and asynchronous task tracking.
  name: Constructor Catalog Management API
  slug: constructor-catalog-management-api
- description: Batched catalog ingestion service for high-volume item and variation update and delete operations.
  name: Constructor Catalog Batching API
  slug: constructor-catalog-batching-api
- description: Authenticated configuration surface for facets, facet options, searchabilities, one-way synonyms, synonym groups, sort options, redirect rules, collections, quizzes and metadata overrides.
  name: Constructor Configuration API
  slug: constructor-configuration-api
- description: Merchandising-rule surface for refined queries, refined filters, refined collections, refined tags, campaigns and facet-rule campaigns across search, browse and collections.
  name: Constructor Searchandising API
  slug: constructor-searchandising-api
- description: Guided-selling quiz surface returning the next question given prior answers, quiz results and results-page configuration.
  name: Constructor Quizzes API
  slug: constructor-quizzes-api
- description: Recommendation and collection results for offsite channels (email, SMS, push, social, paid media), including redirecting item image and item URL endpoints addressable by pod/collection and position.
  name: Constructor Offsite Discovery Recommendations API
  slug: constructor-offsite-discovery-recommendations-api
- description: Retail media surface for updating advertiser engagement suspension status and retrieving per-advertiser ad spend accrued within an index.
  name: Constructor Retail Media API
  slug: constructor-retail-media-api
- description: Display-ads surface returning ads for each requested placement, with banner and multi-banner placement responses ordered by auction rank.
  name: Constructor Retail Media Display Ads API
  slug: constructor-retail-media-display-ads-api
- description: Retrieval of item and variation product-detail records for a given index.
  name: Constructor Product Details API
  slug: constructor-product-details-api
- description: Offline behavioral-action ingestion for submitting user events (such as purchases and conversions) that feed Constructor's KPI-optimized ranking.
  name: Constructor Behavioral Actions API
  slug: constructor-behavioral-actions-api
- description: Creation of user preference records that personalize discovery results for an identified shopper.
  name: Constructor User Profile API
  slug: constructor-user-profile-api
- description: Remote, anonymously reachable Model Context Protocol server published by Constructor that exposes documentation search/fetch and OpenAPI endpoint discovery tools to AI coding tools such as Claude, Cur
  name: Constructor Documentation MCP Server
  slug: constructor-documentation-mcp-server
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://constructor.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.constructor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.constructor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.constructor.com/reference/main-readme
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.constructor.com/docs/integrating-with-constructor-retrieving-results-getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.constructor.com/docs/integrating-with-constructor-customer-support-guide
- group: company
  title: ''
  type: Blog
  url: https://constructor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Constructor-io
- group: start
  title: ''
  type: SignUp
  url: https://info.constructor.com/ecommerce-search-discovery-demo
- group: start
  title: ''
  type: Login
  url: https://app.constructor.io/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://constructor.com/terms-of-service-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://constructor.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://constructor.com/security-and-compliance
- group: operate
  title: ''
  type: StatusPage
  url: https://constructor.status.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://releases.constructor.io/
- group: build
  title: ''
  type: SDKs
  url: packages/constructorio-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/constructorio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/constructorio-cli.yml
- group: design
  title: ''
  type: Components
  url: components/constructorio-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/constructorio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/constructorio-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/constructorio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/constructorio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/constructorio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.constructor.com/reference/configuration-facets-and-searchabilities-v2-migration-guide
- group: design
  title: ''
  type: Conformance
  url: conformance/constructorio-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/constructorio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/constructorio-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/constructorio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/constructorio-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/constructorio-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/constructorio-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Constructor (Constructor.io) is an AI-powered ecommerce search and product discovery platform for online retailers. Its APIs cover autocomplete/autosuggest, keyword and natural-language search, image search, category browse, recommendations, quizzes, collections, offsite/email discovery, retail media (sponsored listings and display ads), an AI Shopping Agent and Product Insights Agent, plus a full catalog-management and configuration surface for items, variations, item groups, facets, searchabilities, synonyms, sort options, redirects and searchandising rules. Results are optimized against ecommerce KPIs (conversion, revenue per visit) using natural-language processing, behavioral re-ranking and per-user personalization, and are delivered through a REST API served from the ac.cnstrc.com family of hosts with first-party client libraries for JavaScript, Node.js, Python, Java, .NET, Ruby, Swift and Kotlin.
image: https://constructor.com/hubfs/constructor-featured-image-2026.png
layout: provider
mcp_servers:
- description: ''
  name: constructorio-mcp.yml
  slug: constructorio-mcpyml
modified: '2026-08-01'
name: Constructor.io
nav: Providers
network: true
overview: 'Constructor.io publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Constructor Search API, Constructor Autocomplete API, Constructor Browse API, and 14 more. Tagged areas include Company, Search, Ecommerce, Product Discovery, and Recommendations.


  Constructor.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 26 more developer resources.'
random_paper: 46
scopes:
- name: Constructorio Scopes
  scope_count: 37
  slug: constructorio-scopes
  summary_line: 37 scopes
score:
  band: developing
  composite: 55.0
  delta: -1.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.7
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 56.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/constructorio/refs/heads/main/screenshots/constructorio-2026-08-07T163752.png
security:
- kind: authentication
  name: Constructorio Authentication
  slug: constructorio-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Constructorio Domain Security
  slug: constructorio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Constructorio Trust Center
  slug: constructorio-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, CCPA, MACH Certified
slug: constructorio
tags:
- Company
- Search
- Ecommerce
- Product Discovery
- Recommendations
- Personalization
- Retail
- Retail Media
- Artificial Intelligence
- Merchandising
- Catalog Management
- Agentic Commerce
website: https://constructor.com/
---
