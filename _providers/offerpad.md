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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 103
  human_in_the_loop: 0
  name: Offerpad Agentic Access
  operation_count: 227
  slug: offerpad-agentic-access
  summary_line: 227 operations · 103 acting
api_count: 1
apis:
- description: Offerpad's real transaction API, and it is closed. Discovered on 2026-07-26 as the API_URL constant compiled into the Offerpad Connect single-page-app bundle at https://connect.offerpad.com/bundle.js,
  name: Offerpad Helix API (private customer backend)
  slug: offerpad-helix-api
- description: 'The public WordPress REST API (wp-json) of the Offerpad website at www.offerpad.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: Offerpad Website (WordPress REST)
  slug: offerpad-com-website-wordpress-rest
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-offerpad-wp-json-discovery
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.offerpad.com/feed/
- group: agent
  href: https://artifacts.apis.io/offerpad/agentic-access/offerpad-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/offerpad-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/offerpad/security/offerpad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/offerpad-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/offerpad/authentication/offerpad-authentication.yml
  title: ''
  type: Authentication
  url: authentication/offerpad-authentication.yml
- group: auth
  href: https://artifacts.apis.io/offerpad/scopes/offerpad-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/offerpad-scopes.yml
- group: agent
  href: https://artifacts.apis.io/offerpad/well-known/offerpad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/offerpad-well-known.yml
- group: design
  href: https://artifacts.apis.io/offerpad/conventions/offerpad-conventions.yml
  title: ''
  type: Conventions
  url: conventions/offerpad-conventions.yml
- group: design
  href: https://artifacts.apis.io/offerpad/errors/offerpad-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/offerpad-problem-types.yml
- group: design
  href: https://artifacts.apis.io/offerpad/lifecycle/offerpad-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/offerpad-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/offerpad/conformance/offerpad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/offerpad-conformance.yml
- group: build
  href: https://artifacts.apis.io/offerpad/packages/offerpad-packages.yml
  title: ''
  type: Packages
  url: packages/offerpad-packages.yml
- group: agent
  href: https://artifacts.apis.io/offerpad/mcp/offerpad-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/offerpad-mcp.yml
- group: build
  href: https://artifacts.apis.io/offerpad/mcp/offerpad-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/offerpad-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/offerpad/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/offerpad/llms/offerpad-llms-api.txt
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
- group: design
  href: https://artifacts.apis.io/offerpad/data-model/offerpad-data-model.yml
  title: ''
  type: DataModel
  url: data-model/offerpad-data-model.yml
created: '2026-07-26'
description: 'Offerpad Solutions Inc. (NYSE: OPAD), headquartered in Chandler, Arizona, is a United States iBuyer and licensed residential real estate brokerage that buys homes directly from sellers for cash, renovates them, and resells them, while also offering traditional listing services, a free local move, and a Renovate service. It sits in the middle of the US residential value chain as a principal-position buyer and MLS-participating brokerage in seventeen states, consuming licensed MLS listing data rather than publishing it. Offerpad''s API posture is honestly minimal: there is no developer portal, no published API documentation, and no self-serve API access of any kind. The developer., developers., api. and docs. subdomains do not resolve, and /developers, /api, /docs, /openapi.json, /swagger.json and /api-docs all return 404. Offerpad is NOT listed in the RESO certification directory, holds no RESO Web API or Data Dictionary certification, and serves no OData service document, $metadata
  document, or Universal Property Identifier. Its partner surfaces — the Direct+ investor-buyer program, the Powered By Offerpad agent partner portal, the homebuilder program and the vendor network — are human web portals gated behind an intake form and a Mutual Non-Disclosure Agreement, with no programmatic interface described anywhere. The only publicly callable, self-describing API on the domain is the stock WordPress REST API of the marketing site. Offerpad does, however, run a real versioned transaction API privately: helix.offerpad.com serves the customer identity, cash-offer transaction, contract, document and form endpoints behind the Offerpad Connect portal and mobile apps, and it publishes a live RFC 8414 authorization-server metadata document delegating to Okta — so Offerpad''s identity layer is machine discoverable while none of its business capability is documented, schema-backed or obtainable by a third party.'
examples:
- key_count: 16
  name: Offerpad Wp V2 Types Response
  slug: offerpad-wp-v2-types-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-10-06'
name: Offerpad
nav: Providers
network: true
overview: 'Offerpad publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United States, iBuyer, PropTech, and Property Listings.


  The Offerpad catalog on APIs.io includes 1 Spectral governance ruleset.


  Offerpad''s developer surface includes authentication, developer portal, signup flow, engineering blog, support, and 37 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Offerpad API Rules
  rule_count: 64
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 8
  slug: offerpad-rules
scopes:
- name: Offerpad Scopes
  scope_count: 9
  slug: offerpad-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 35.1
    discoverability: 64.3
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/offerpad/offerpad-2026-08-17T124240.png
security:
- kind: authentication
  name: Offerpad Authentication
  slug: offerpad-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Offerpad Domain Security
  slug: offerpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Assess what Offerpad API access actually exists
  slug: offerpad-assess-api-access
- name: Read Offerpad site content
  slug: offerpad-read-site-content
- name: Search Offerpad content and enumerate its markets
  slug: offerpad-search-and-locations
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
