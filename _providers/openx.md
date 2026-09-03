---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.openx.com/pricing/
  - https://docs.openx.com/marketers/openxbuild/oxb-rtb-api-get-started/
  - https://docs.openx.com/publishers/reporting-api/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: JSON REST API (v4) for the OpenX ad server. Sixteen CRUD objects (account, ad, adunit, adunitgroup, comment, creative, deal, floorrule, lineitem, optimization, order, package, paymenthistory, site, si
  name: OpenX Platform API
  slug: openx-platform-api
- description: Asynchronous reporting API for authorized OpenX publishers. POST generateReport with dimensions, metrics, filters, reportType (HOURLY|DAILY) and an ISO-8601 date range returns a report id; POST pullRe
  name: OpenX Reporting API
  slug: openx-reporting-api
- description: GraphQL API (BETA) for the OpenXSelect curation platform — query providers, segments, audiences, deals and packages, and mutate audiences (create/update/archive/activate), deals, routed retargeting se
  name: OpenXSelect API
  slug: openxselect-api
- description: 'Live remote Model Context Protocol server at https://api.openx.com/mcp. Discovered by probe, not by documentation — OpenX does not mention MCP anywhere in its published docs, but the endpoint answers '
  name: OpenX MCP Server
  slug: openx-mcp-server
- description: An inverted API — OpenX is the caller. A partner implements an enrichment service that OpenX hosts as a container inside its own Kubernetes namespace and calls in the auction path, either as HTTP POST
  name: OpenXBuild Real-Time Bidstream API
  slug: openxbuild-real-time-bidstream-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.openx.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.openx.com/developers/about-topics-api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openx.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openx.com/developers/api-ref/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openx.com/developers/api-get-started-auth/
- group: operate
  title: ''
  type: Support
  url: https://docs.openx.com/resources/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.openx.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.openx.com/resources/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openx-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/openx-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openx-error-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openx-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openx-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openx-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openx-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/openx-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/openx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openx-packages.yml
- group: design
  title: ''
  type: Components
  url: components/openx-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/openx-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openx-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openx-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openx-llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/openx-graphql.md
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openx-domain-security.yml
- group: other
  title: ''
  type: OpenXExchange
  url: https://www.openx.com/openxexchange/
- group: other
  title: ''
  type: OpenXSelect
  url: https://www.openx.com/openxselect/
- group: other
  title: ''
  type: OpenXBuild
  url: https://www.openx.com/openxbuild/
- group: other
  title: ''
  type: OpenXControl
  url: https://www.openx.com/openxcontrol/
- group: other
  title: ''
  type: Publishers
  url: https://www.openx.com/publishers/
- group: other
  title: ''
  type: Advertisers
  url: https://www.openx.com/advertisers/
- group: company
  title: ''
  type: Partners
  url: https://www.openx.com/partners/
- group: other
  title: ''
  type: KnowledgeHub
  url: https://www.openx.com/knowledge-hub/
- group: other
  title: ''
  type: Leadership
  url: https://www.openx.com/leadership/
- group: company
  title: ''
  type: Newsroom
  url: https://www.openx.com/news-press/
- group: company
  title: ''
  type: Blog
  url: https://blog.openx.com/
- group: company
  title: ''
  type: Careers
  url: https://www.openx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.openx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openx.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openx.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: Legal
  url: https://www.openx.com/legal/
- group: other
  title: ''
  type: Regulations
  url: https://docs.openx.com/resources/regulations/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openx
- group: build
  title: ''
  type: SDK — Python (OX3)
  url: https://github.com/openx/OX3-Python-API-Client
- group: build
  title: ''
  type: SDK — PHP (OX3)
  url: https://github.com/openx/OX3-PHP-API-Client
- group: build
  title: ''
  type: SDK — Java (OX3)
  url: https://github.com/openx/OX3-Java-API-Client
- group: build
  title: ''
  type: SDK — Perl (OX3)
  url: https://github.com/openx/OX3-Perl-API-Client
- group: build
  title: ''
  type: SDK — Ruby (OX3)
  url: https://github.com/openx/OX3-Ruby-API-Client
- group: build
  title: ''
  type: Tool — Reporting API Client (Python)
  url: https://github.com/openx/reporting-api-client
- group: build
  title: ''
  type: Tool — Enrichment Service Template
  url: https://github.com/openx/openx-enrichment-service-template
- group: docs
  title: ''
  type: Tool — OpenRTB 2.x Specification
  url: https://github.com/openx/openrtb2.x
- group: build
  title: ''
  type: Tool — Prebid.js
  url: https://github.com/openx/Prebid.js
- group: build
  title: ''
  type: Tool — Prebid Server
  url: https://github.com/openx/prebid-server
- group: build
  title: ''
  type: Tool — SSRTBPriceCrypter
  url: https://github.com/openx/SSRTBPriceCrypter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openx
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OpenX
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@OpenX
created: '2026-05-25'
description: 'OpenX is an independent supply-side platform (SSP) and programmatic ad exchange headquartered in Pasadena, California, founded in 2008. OpenX connects publishers and app developers to advertiser demand through a real-time marketplace that runs OpenRTB-based auctions across display, video, CTV, native, and mobile inventory. Its product suite is organized around the OpenX Exchange (the core marketplace), OpenXSelect (curation, deal creation, and supply-path targeting), OpenXBuild (real-time bidstream enrichment, auction insights, and identity resolution), and OpenXControl (publisher yield management and demand routing). OpenX runs five developer surfaces on api.openx.com: a REST Platform API (v4) for accounts, inventory, orders, deals, and targeting; a Reporting API for asynchronous CSV report generation across 41 dimensions and 9 metrics; an OpenXSelect GraphQL API for audiences, segments, deals, and bidder objects; an OpenXBuild Real-Time Bidstream API that a partner implements
  as a containerized enrichment service (HTTP POST /openrtb25 plus an IAB Agentic RTB Framework gRPC RTBExtensionPoint); and an undocumented but live remote MCP server. Authentication is OAuth 2.0 authorization-code with PKCE fronted by Google Cloud Identity Platform, published through real OIDC and RFC 9728 discovery documents, with a separate 90-day x-apikey credential for the GraphQL API. OpenX publishes no OpenAPI, no Postman collection, no status page, no pricing, and no security.txt, and its documentation site currently renders as a broken single-page-app shell whose underlying content survives only as a JSON search index. The company is a major contributor to the Prebid.org header-bidding ecosystem and maintains a large GitHub organization, though its first-party API client libraries were last released to a package registry in 2021 and still target a legacy OAuth 1.0 login host that now returns HTTP 502. The business model is transaction-fee based, and API access requires an active
  OpenX account and BD/account-management onboarding rather than self-service signup.'
graphqls:
- description: 'generated: ''2026-08-13'''
  name: OpenXSelect API (GraphQL)
  slug: openx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openx.png
layout: provider
mcp_servers:
- description: ''
  name: OpenX MCP Server
  slug: openx-mcp-server
modified: '2026-08-13'
name: OpenX
nav: Providers
network: true
overview: 'OpenX publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Programmatic Advertising, Ad Exchange, Supply Side Platform, and SSP.


  OpenX''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 53 more developer resources.'
plans:
- name: Openx Plans Pricing
  plan_count: 0
  slug: openx-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Openx Rate Limits
  slug: openx-rate-limits
scopes:
- name: Openx Scopes
  scope_count: 5
  slug: openx-scopes
  summary_line: 5 scopes · authorizationCode/refreshToken
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 69.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openx/refs/heads/main/screenshots/openx-2026-06-20T191054.png
security:
- kind: authentication
  name: Openx Authentication
  slug: openx-authentication
  summary_line: oauth2/openIdConnect/apiKey/http · 4 schemes
- kind: domain-security
  name: Openx Domain Security
  slug: openx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openx
tags:
- Advertising
- Programmatic Advertising
- Ad Exchange
- Supply Side Platform
- SSP
- Real-Time Bidding
- OpenRTB
- Header Bidding
- Prebid
- AdTech
- CTV
- Video Advertising
- Display Advertising
- Curation
- Identity
- GraphQL
- gRPC
- MCP
- Reporting
- Audience Targeting
website: https://www.openx.com
---
