---
access_model:
  confidence: high
  label: No published developer API
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probe
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 103
  human_in_the_loop: 0
  name: Offerpad Agentic Access
  operation_count: 227
  slug: offerpad-agentic-access
  summary_line: 227 operations · 103 acting
api_count: 2
apis:
- description: The stock WordPress REST API served by Offerpad's WP Engine-hosted marketing site at https://www.offerpad.com/wp-json/. Confirmed live and anonymously readable on 2026-07-26 (HTTP 200, application/jso
  name: Offerpad WordPress REST API
  slug: offerpad-wordpress-rest-api
- description: Offerpad's real transaction API, and it is closed. Discovered on 2026-07-26 as the API_URL constant compiled into the Offerpad Connect single-page-app bundle at https://connect.offerpad.com/bundle.js,
  name: Offerpad Helix API (private customer backend)
  slug: offerpad-helix-api
artifact_total: 10
collections:
- collection_type: open
  name: Offerpad WordPress REST API (wp/v2)
  slug: open-offerpad-wordpress-wp-v2
- collection_type: open
  name: API Collection
  slug: open-offerpad-wp-json-discovery
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/offerpad-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offerpad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/offerpad-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/offerpad-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/offerpad-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/offerpad-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/offerpad-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/offerpad-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/offerpad-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/offerpad-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/offerpad-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/offerpad-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/offerpad-llms-api.txt
- group: company
  title: ''
  type: Website
  url: https://www.offerpad.com
- group: company
  title: ''
  type: About
  url: https://www.offerpad.com/about/
- group: other
  title: ''
  type: Product
  url: https://www.offerpad.com/sell/
- group: other
  title: ''
  type: Product
  url: https://www.offerpad.com/renovate/
- group: company
  title: ''
  type: Partners
  url: https://www.offerpad.com/agents/
- group: company
  title: ''
  type: Partners
  url: https://www.offerpad.com/pbo/
- group: start
  title: ''
  type: Onboarding
  url: https://www.offerpad.com/dplusonboarding/
- group: company
  title: ''
  type: Partners
  url: https://www.offerpad.com/hba/
- group: company
  title: ''
  type: Partners
  url: https://www.offerpad.com/vendors/
- group: start
  title: ''
  type: Portal
  url: https://connect.offerpad.com/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://connect.offerpad.com/auth/register
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.offerpad.com/llms.txt
- group: other
  title: ''
  type: Sitemap
  url: https://www.offerpad.com/sitemap_index.xml
- group: company
  title: ''
  type: Blog
  url: https://www.offerpad.com/articles/
- group: company
  title: ''
  type: PressRoom
  url: https://www.offerpad.com/press/
- group: operate
  title: ''
  type: Support
  url: https://www.offerpad.com/faq/
- group: operate
  title: ''
  type: Contact
  url: https://www.offerpad.com/contact/
- group: other
  title: ''
  type: Licensing
  url: https://www.offerpad.com/licenses/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.offerpad.com/
- group: company
  title: ''
  type: Careers
  url: https://www.offerpad.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.offerpad.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.offerpad.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Offerpad
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/offerpad
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/offerpad
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/offerpad
created: '2026-07-26'
description: 'Offerpad Solutions Inc. (NYSE: OPAD), headquartered in Chandler, Arizona, is a United States iBuyer and licensed residential real estate brokerage that buys homes directly from sellers for cash, renovates them, and resells them, while also offering traditional listing services, a free local move, and a Renovate service. It sits in the middle of the US residential value chain as a principal-position buyer and MLS-participating brokerage in seventeen states, consuming licensed MLS listing data rather than publishing it. Offerpad''s API posture is honestly minimal: there is no developer portal, no published API documentation, and no self-serve API access of any kind. The developer., developers., api. and docs. subdomains do not resolve, and /developers, /api, /docs, /openapi.json, /swagger.json and /api-docs all return 404. Offerpad is NOT listed in the RESO certification directory, holds no RESO Web API or Data Dictionary certification, and serves no OData service document, $metadata
  document, or Universal Property Identifier. Its partner surfaces — the Direct+ investor-buyer program, the Powered By Offerpad agent partner portal, the homebuilder program and the vendor network — are human web portals gated behind an intake form and a Mutual Non-Disclosure Agreement, with no programmatic interface described anywhere. The only publicly callable, self-describing API on the domain is the stock WordPress REST API of the marketing site. Offerpad does, however, run a real versioned transaction API privately: helix.offerpad.com serves the customer identity, cash-offer transaction, contract, document and form endpoints behind the Offerpad Connect portal and mobile apps, and it publishes a live RFC 8414 authorization-server metadata document delegating to Okta — so Offerpad''s identity layer is machine discoverable while none of its business capability is documented, schema-backed or obtainable by a third party.'
examples:
- key_count: 16
  name: Offerpad Wp V2 Types Response
  slug: offerpad-wp-v2-types-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the public content API
  slug: candidate-mcp-tool-surface-derived-from-the-public-content-api
modified: '2026-07-26'
name: Offerpad
nav: Providers
network: true
overview: 'Offerpad publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Real Estate, United States, iBuyer, PropTech, and Property Listings.


  Offerpad''s developer surface includes authentication, developer portal, signup flow, engineering blog, support, and 35 more developer resources.'
random_paper: 94
scopes:
- name: Offerpad Scopes
  scope_count: 9
  slug: offerpad-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.2
    developer_ergonomics: 29.9
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/offerpad/refs/heads/main/screenshots/offerpad-2026-08-07T190021.png
security:
- kind: authentication
  name: Offerpad Authentication
  slug: offerpad-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Offerpad Domain Security
  slug: offerpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: offerpad
tags:
- Real Estate
- United States
- iBuyer
- PropTech
- Property Listings
- Brokerage
- MLS
- Cash Offer
- Renovation
- Home Buying
website: https://www.offerpad.com
---
