---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: OpenRTB is the real-time bidding protocol between ad exchanges and bidders. IAB Tech Lab publishes the 2.x specification (current release 2.6-202606) with a Protocol Buffers definition (package com.ia
  name: OpenRTB 2.x Protocol
  slug: openrtb
- description: Advertising Common Object Model (AdCOM) 1.0 is the shared object layer beneath OpenRTB 3.0, OpenDirect and the Ad Management API — media (ads, assets), placement, context (site, app, user, device, geo
  name: AdCOM Protobuf
  slug: adcom
- description: The Agentic Real-Time Framework (ARTF) 1.0 defines gRPC extension points an exchange calls during an auction so that agents can mutate the bidstream. The RTBExtensionPoint service (package com.iabtech
  name: Agentic RTB Framework gRPC
  slug: agentic-rtb-framework
- description: Video Ad Serving Template (VAST) is the XML contract between video players and ad servers; VMAP (Video Multiple Ad Playlist) schedules ad breaks around content. IAB Tech Lab publishes XML Schema defin
  name: VAST and VMAP Schemas
  slug: vast
- description: 'IAB Tech Lab''s hosted, subscription API for aggregated supply-chain data: crawled and validated ads.txt, app-ads.txt and sellers.json files, plus the Transparency Center''s compliance and identifier re'
  name: Supply Chain API
  slug: supply-chain-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The A2a API from IAB Tech Lab — 1 operation(s) for a2a.
  name: IAB Tech Lab A2a API
  slug: iab-tech-lab-a2a-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Accounts API from IAB Tech Lab — 2 operation(s) for accounts.
  name: IAB Tech Lab Accounts API
  slug: iab-tech-lab-accounts-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: A2A agent discovery and trust management
  name: IAB Tech Lab Agent Registry API
  slug: iab-tech-lab-agent-registry-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Human-in-the-loop approval workflow
  name: IAB Tech Lab Approvals API
  slug: iab-tech-lab-approvals-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Assignments API from IAB Tech Lab — 3 operation(s) for assignments.
  name: IAB Tech Lab Assignments API
  slug: iab-tech-lab-assignments-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Audience API from IAB Tech Lab — 1 operation(s) for audience.
  name: IAB Tech Lab Audience API
  slug: iab-tech-lab-audience-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Order audit logs and operational reports
  name: IAB Tech Lab Audit API
  slug: iab-tech-lab-audit-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: API key lifecycle management
  name: IAB Tech Lab Authentication API
  slug: iab-tech-lab-authentication-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Campaign booking workflow lifecycle
  name: IAB Tech Lab Bookings API
  slug: iab-tech-lab-bookings-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Batch deal create/update/cancel
  name: IAB Tech Lab Bulk Operations API
  slug: iab-tech-lab-bulk-operations-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Buyer Orders API from IAB Tech Lab — 2 operation(s) for buyer orders.
  name: IAB Tech Lab Buyer Orders API
  slug: iab-tech-lab-buyer-orders-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Change Requests API from IAB Tech Lab — 8 operation(s) for change requests.
  name: IAB Tech Lab Change Requests API
  slug: iab-tech-lab-change-requests-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Change Requests Lines API from IAB Tech Lab — 2 operation(s) for change requests lines.
  name: IAB Tech Lab Change Requests Lines API
  slug: iab-tech-lab-change-requests-lines-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Health check and API root
  name: IAB Tech Lab Core API
  slug: iab-tech-lab-core-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Creatives API from IAB Tech Lab — 2 operation(s) for creatives.
  name: IAB Tech Lab Creatives API
  slug: iab-tech-lab-creatives-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Curators API from IAB Tech Lab — 3 operation(s) for curators.
  name: IAB Tech Lab Curators API
  slug: iab-tech-lab-curators-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Quote-to-deal booking (IAB Deals API v1.0)
  name: IAB Tech Lab Deal Booking API
  slug: iab-tech-lab-deal-booking-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Deal delivery and performance metrics
  name: IAB Tech Lab Deal Performance API
  slug: iab-tech-lab-deal-performance-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Deals API from IAB Tech Lab — 3 operation(s) for deals.
  name: IAB Tech Lab Deals API
  slug: iab-tech-lab-deals-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Natural language inventory discovery
  name: IAB Tech Lab Discovery API
  slug: iab-tech-lab-discovery-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Event bus query endpoints
  name: IAB Tech Lab Events API
  slug: iab-tech-lab-events-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Service health and readiness
  name: IAB Tech Lab Health API
  slug: iab-tech-lab-health-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Lines API from IAB Tech Lab — 6 operation(s) for lines.
  name: IAB Tech Lab Lines API
  slug: iab-tech-lab-lines-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Public media kit and package catalog
  name: IAB Tech Lab Media Kit API
  slug: iab-tech-lab-media-kit-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Multi-round price negotiation
  name: IAB Tech Lab Negotiation API
  slug: iab-tech-lab-negotiation-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Negotiations API from IAB Tech Lab — 2 operation(s) for negotiations.
  name: IAB Tech Lab Negotiations API
  slug: iab-tech-lab-negotiations-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Orders API from IAB Tech Lab — 7 operation(s) for orders.
  name: IAB Tech Lab Orders API
  slug: iab-tech-lab-orders-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Organizations API from IAB Tech Lab — 2 operation(s) for organizations.
  name: IAB Tech Lab Organizations API
  slug: iab-tech-lab-organizations-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Package management (authenticated/admin)
  name: IAB Tech Lab Packages API
  slug: iab-tech-lab-packages-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Tiered pricing with buyer context
  name: IAB Tech Lab Pricing API
  slug: iab-tech-lab-pricing-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Products API from IAB Tech Lab — 6 operation(s) for products.
  name: IAB Tech Lab Products API
  slug: iab-tech-lab-products-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Proposal submission and evaluation
  name: IAB Tech Lab Proposals API
  slug: iab-tech-lab-proposals-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Quotes API from IAB Tech Lab — 2 operation(s) for quotes.
  name: IAB Tech Lab Quotes API
  slug: iab-tech-lab-quotes-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Registry API from IAB Tech Lab — 1 operation(s) for registry.
  name: IAB Tech Lab Registry API
  slug: iab-tech-lab-registry-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The Reporting API from IAB Tech Lab — 7 operation(s) for reporting.
  name: IAB Tech Lab Reporting API
  slug: iab-tech-lab-reporting-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Multi-turn buyer conversation sessions
  name: IAB Tech Lab Sessions API
  slug: iab-tech-lab-sessions-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: Supply chain transparency (sellers.json-like self-description)
  name: IAB Tech Lab Supply Chain API
  slug: iab-tech-lab-supply-chain-api
- baseURL: https://api.iabtechlab.com
  baseurl_source: declared
  description: The .well Known API from IAB Tech Lab — 1 operation(s) for .well known.
  name: IAB Tech Lab .well Known API
  slug: iab-tech-lab-well-known-api
artifact_total: 71
common:
- group: other
  href: https://artifacts.apis.io/iab-tech-lab/capabilities/iab-tech-lab-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/iab-tech-lab-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/iab-tech-lab/overlays/iab-tech-lab-opendirect-1-5-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iab-tech-lab-opendirect-1-5-1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/iab-tech-lab/skills/iab-tech-lab-opendirect-book-line.md
  title: ''
  type: AgentSkill
  url: skills/iab-tech-lab-opendirect-book-line.md
- group: other
  href: https://artifacts.apis.io/iab-tech-lab/overlays/iab-tech-lab-agentic-advertising-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iab-tech-lab-agentic-advertising-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/iab-tech-lab/overlays/iab-tech-lab-seller-agent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iab-tech-lab-seller-agent-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/iab-tech-lab/skills/iab-tech-lab-quote-to-book-deal.md
  title: ''
  type: AgentSkill
  url: skills/iab-tech-lab-quote-to-book-deal.md
- group: agent
  href: https://artifacts.apis.io/iab-tech-lab/skills/iab-tech-lab-negotiate-deal.md
  title: ''
  type: AgentSkill
  url: skills/iab-tech-lab-negotiate-deal.md
- group: other
  href: https://artifacts.apis.io/iab-tech-lab/overlays/iab-tech-lab-buyer-agent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iab-tech-lab-buyer-agent-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/iab-tech-lab/security/iab-tech-lab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iab-tech-lab-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/iab-tech-lab/scopes/iab-tech-lab-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/iab-tech-lab-scopes.yml
- group: auth
  href: https://artifacts.apis.io/iab-tech-lab/authentication/iab-tech-lab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iab-tech-lab-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://iabtechlab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://iabtechlab.com/standards/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IABTechLab
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InteractiveAdvertisingBureau
- group: company
  title: ''
  type: Blog
  url: https://iabtechlab.com/category/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://iabtechlab.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://iabtechlab.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iabtechlab.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iabtechlab.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://iabtechlab.com/membership/
- group: start
  title: ''
  type: Login
  url: https://tools.iabtechlab.com/
- group: start
  title: ''
  type: Portal
  url: https://tools.iabtechlab.com/
- group: other
  title: ''
  type: Software
  url: https://iabtechlab.com/software/
- group: other
  title: ''
  type: Events
  url: https://iabtechlab.com/events/
- group: operate
  title: ''
  type: PressReleases
  url: https://iabtechlab.com/press-releases/
- group: build
  href: https://artifacts.apis.io/iab-tech-lab/packages/iab-tech-lab-packages.yml
  title: ''
  type: Packages
  url: packages/iab-tech-lab-packages.yml
- group: build
  href: https://artifacts.apis.io/iab-tech-lab/packages/iab-tech-lab-packages.yml
  title: ''
  type: SDKs
  url: packages/iab-tech-lab-packages.yml
- group: agent
  href: https://artifacts.apis.io/iab-tech-lab/mcp/iab-tech-lab-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/iab-tech-lab-mcp.yml
- group: build
  href: https://artifacts.apis.io/iab-tech-lab/mcp/iab-tech-lab-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/iab-tech-lab-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/iab-tech-lab/llms/iab-tech-lab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iab-tech-lab-llms.txt
- group: design
  href: https://artifacts.apis.io/iab-tech-lab/conformance/iab-tech-lab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iab-tech-lab-conformance.yml
- group: design
  href: https://artifacts.apis.io/iab-tech-lab/errors/iab-tech-lab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iab-tech-lab-problem-types.yml
- group: design
  href: https://artifacts.apis.io/iab-tech-lab/lifecycle/iab-tech-lab-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iab-tech-lab-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/iab-tech-lab/conventions/iab-tech-lab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/iab-tech-lab-conventions.yml
- group: design
  href: https://artifacts.apis.io/iab-tech-lab/conventions/iab-tech-lab-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/iab-tech-lab-conventions.yml
- group: operate
  href: https://artifacts.apis.io/iab-tech-lab/changelog/iab-tech-lab-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iab-tech-lab-changelog.yml
- group: build
  href: https://artifacts.apis.io/iab-tech-lab/cli/iab-tech-lab-cli.yml
  title: ''
  type: CLI
  url: cli/iab-tech-lab-cli.yml
- group: design
  href: https://artifacts.apis.io/iab-tech-lab/data-model/iab-tech-lab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iab-tech-lab-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/iab-tech-lab/plans/iab-tech-lab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iab-tech-lab-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/iab-tech-lab/rate-limits/iab-tech-lab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iab-tech-lab-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/iab-tech-lab/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/iab-tech-lab/grpc/iab-tech-lab-openrtb-v2.proto
  title: ''
  type: Protobuf
  url: grpc/iab-tech-lab-openrtb-v2.proto
created: '2026-09-17'
description: 'IAB Technology Laboratory (IAB Tech Lab) is the non-profit consortium that writes the technical standards the digital advertising supply chain runs on — OpenRTB (real-time bidding), AdCOM, OpenDirect (programmatic direct), VAST and VMAP (video ad serving), the Transparency and Consent Framework and Global Privacy Platform (consent signals), ads.txt, app-ads.txt and sellers.json (supply-chain transparency), the Open Measurement SDK and the content/audience/ad-product taxonomies. Its machine-readable contracts are published in the open on GitHub: an OpenRTB 2.x Protocol Buffers definition, the AdCOM protobuf, an OpenDirect Swagger specification, VAST XSDs, and an agentic-advertising stack (buyer-agent, seller-agent, Deals API, Agentic RTB Framework gRPC) that ships OpenAPI 3.1 contracts, JSON Schema primitives, MCP servers and A2A agent cards as reference implementations. The Tech Lab Tools Portal and its Core API sit behind a member login.'
finops:
- has_sources: true
  method: derived
  name: Iab Tech Lab Finops
  primary_unit: subscription
  service_category: ''
  slug: iab-tech-lab-finops
  template: false
image: https://iabtechlab.com/wp-content/uploads/2017/08/IABTL_Logo_512.png
json_schemas:
- name: Account
  property_count: 7
  slug: iab-tech-lab-agentic-primitive-account
- name: Agent
  property_count: 17
  slug: iab-tech-lab-agentic-primitive-agent
- name: Assignment
  property_count: 9
  slug: iab-tech-lab-agentic-primitive-assignment
- name: ChangeRequest
  property_count: 20
  slug: iab-tech-lab-agentic-primitive-changerequest
- name: ConsentContext
  property_count: 8
  slug: iab-tech-lab-agentic-primitive-consentcontext
- name: Creative
  property_count: 14
  slug: iab-tech-lab-agentic-primitive-creative
- name: CreativeApproval
  property_count: 7
  slug: iab-tech-lab-agentic-primitive-creativeapproval
- name: Deal
  property_count: 18
  slug: iab-tech-lab-agentic-primitive-deal
- name: DecisionRecord
  property_count: 13
  slug: iab-tech-lab-agentic-primitive-decisionrecord
- name: Line
  property_count: 13
  slug: iab-tech-lab-agentic-primitive-line
- name: MediaKit
  property_count: 9
  slug: iab-tech-lab-agentic-primitive-mediakit
- name: Negotiation
  property_count: 10
  slug: iab-tech-lab-agentic-primitive-negotiation
- name: Order
  property_count: 14
  slug: iab-tech-lab-agentic-primitive-order
- name: Organization
  property_count: 7
  slug: iab-tech-lab-agentic-primitive-organization
- name: Product
  property_count: 16
  slug: iab-tech-lab-agentic-primitive-product
- name: Proposal
  property_count: 11
  slug: iab-tech-lab-agentic-primitive-proposal
layout: provider
mcp_servers:
- description: IAB Tech Lab publishes three MCP servers, all as open-source reference implementations that an operator runs on their own host — none is hosted by IAB Tech Lab, so no agent can reach them without a hu
  name: IAB Tech Lab MCP Server
  slug: iab-tech-lab-mcp-yml
modified: '2026-09-17'
name: IAB Tech Lab
nav: Providers
network: true
overview: 'IAB Tech Lab publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Accounts API, Agent Registry API, and 40 more. Tagged areas include Company, Advertising, AdTech, Standards, and Programmatic.


  The IAB Tech Lab catalog on APIs.io includes 1 Spectral governance ruleset.


  IAB Tech Lab''s developer surface includes authentication, documentation, engineering blog, support, pricing, developer portal, changelog, and 36 more developer resources.'
plans:
- name: Iab Tech Lab Plans Pricing
  plan_count: 3
  slug: iab-tech-lab-plans-pricing
- name: Iab Tech Lab Price Estimates
  plan_count: 0
  slug: iab-tech-lab-price-estimates
random_paper: 9
rate_limits:
- limit_count: 0
  name: Iab Tech Lab Rate Limits
  slug: iab-tech-lab-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: IAB Tech Lab API Rules
  rule_count: 57
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 12
  slug: iab-tech-lab-rules
scopes:
- name: Iab Tech Lab Scopes
  scope_count: 1
  slug: iab-tech-lab-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 63.5
    catalog_earned_first_party: 12.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 48.8
    developer_ergonomics: 61.3
    discoverability: 62.5
    operational_transparency: 18.4
  previous_composite: 56.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/iab-tech-lab/iab-tech-lab-2026-10-11T105600.png
security:
- kind: authentication
  name: Iab Tech Lab Authentication
  slug: iab-tech-lab-authentication
  summary_line: apiKey/http-bearer/oauth2 · 5 schemes
- kind: domain-security
  name: Iab Tech Lab Domain Security
  slug: iab-tech-lab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: iab-tech-lab-negotiate-deal
  slug: iab-tech-lab-negotiate-deal
- name: iab-tech-lab-opendirect-book-line
  slug: iab-tech-lab-opendirect-book-line
- name: iab-tech-lab-quote-to-book-deal
  slug: iab-tech-lab-quote-to-book-deal
slug: iab-tech-lab
tags:
- Company
- Advertising
- AdTech
- Standards
- Programmatic
- Real-Time Bidding
- Consent
- Privacy
- Video Ads
- Agentic Advertising
- Non-Profit
website: https://iabtechlab.com/
---
