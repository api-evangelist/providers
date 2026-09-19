---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-09-18'
api_count: 4
apis:
- description: 'OpenDirect is IAB Tech Lab''s standard REST API for programmatic direct (guaranteed) media buying: organizations, accounts, products, orders, lines, creatives, assignments, change requests and messages'
  name: OpenDirect API
  slug: opendirect-api
- description: The canonical wire protocol between IAB Tech Lab's buyer and seller agents, published from the iab-agentic-primitives repository as an OpenAPI 3.1 document (catalog, quote-to-book deal flow, negotiati
  name: IAB Agentic Advertising API
  slug: agentic-advertising-api
- description: 'IAB Tech Lab''s reference seller agent for publishers: an OpenAPI 3.1 REST surface (87 operations — products and avails, tiered pricing, quotes, deal booking, negotiation, change requests, orders, pack'
  name: Seller Agent API
  slug: seller-agent-api
- description: 'IAB Tech Lab''s reference buyer agent for DSPs, agencies and advertisers: an OpenAPI 3.1 REST surface (14 operations — orders and audit trails, booking jobs and approvals, product search, events, repor'
  name: Buyer Agent API
  slug: buyer-agent-api
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
artifact_total: 31
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/security/iab-tech-lab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iab-tech-lab-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/scopes/iab-tech-lab-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/iab-tech-lab-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/authentication/iab-tech-lab-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/packages/iab-tech-lab-packages.yml
  title: ''
  type: Packages
  url: packages/iab-tech-lab-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/packages/iab-tech-lab-packages.yml
  title: ''
  type: SDKs
  url: packages/iab-tech-lab-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/mcp/iab-tech-lab-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/iab-tech-lab-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/mcp/iab-tech-lab-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/iab-tech-lab-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/llms/iab-tech-lab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iab-tech-lab-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/conformance/iab-tech-lab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iab-tech-lab-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/errors/iab-tech-lab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iab-tech-lab-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/lifecycle/iab-tech-lab-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iab-tech-lab-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/conventions/iab-tech-lab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/iab-tech-lab-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/conventions/iab-tech-lab-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/iab-tech-lab-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/changelog/iab-tech-lab-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iab-tech-lab-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/cli/iab-tech-lab-cli.yml
  title: ''
  type: CLI
  url: cli/iab-tech-lab-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/data-model/iab-tech-lab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iab-tech-lab-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/plans/iab-tech-lab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iab-tech-lab-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/rate-limits/iab-tech-lab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iab-tech-lab-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/iab-tech-lab/refs/heads/main/grpc/iab-tech-lab-openrtb-v2.proto
  title: ''
  type: Protobuf
  url: grpc/iab-tech-lab-openrtb-v2.proto
created: '2026-09-17'
description: 'IAB Technology Laboratory (IAB Tech Lab) is the non-profit consortium that writes the technical standards the digital advertising supply chain runs on — OpenRTB (real-time bidding), AdCOM, OpenDirect (programmatic direct), VAST and VMAP (video ad serving), the Transparency and Consent Framework and Global Privacy Platform (consent signals), ads.txt, app-ads.txt and sellers.json (supply-chain transparency), the Open Measurement SDK and the content/audience/ad-product taxonomies. Its machine-readable contracts are published in the open on GitHub: an OpenRTB 2.x Protocol Buffers definition, the AdCOM protobuf, an OpenDirect Swagger specification, VAST XSDs, and an agentic-advertising stack (buyer-agent, seller-agent, Deals API, Agentic RTB Framework gRPC) that ships OpenAPI 3.1 contracts, JSON Schema primitives, MCP servers and A2A agent cards as reference implementations. The Tech Lab Tools Portal and its Core API sit behind a member login.'
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
  slug: iab-tech-lab-mcp-server
modified: '2026-09-17'
name: IAB Tech Lab
nav: Providers
network: true
overview: 'IAB Tech Lab publishes 4 APIs on the [APIs.io](https://apis.io/) network, including OpenDirect API, IAB Agentic Advertising API, Seller Agent API, and 1 more. Tagged areas include Company, Advertising, AdTech, Standards, and Programmatic.


  IAB Tech Lab''s developer surface includes authentication, documentation, engineering blog, support, pricing, developer portal, changelog, and 28 more developer resources.'
plans:
- name: Iab Tech Lab Plans Pricing
  plan_count: 2
  slug: iab-tech-lab-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Iab Tech Lab Rate Limits
  slug: iab-tech-lab-rate-limits
scopes:
- name: Iab Tech Lab Scopes
  scope_count: 1
  slug: iab-tech-lab-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 53.0
    catalog_earned_first_party: 8.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 61.3
    discoverability: 64.8
    operational_transparency: 21.1
  previous_composite: 51.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Iab Tech Lab Authentication
  slug: iab-tech-lab-authentication
  summary_line: apiKey/http-bearer/oauth2 · 5 schemes
- kind: domain-security
  name: Iab Tech Lab Domain Security
  slug: iab-tech-lab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
