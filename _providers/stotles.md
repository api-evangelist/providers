---
access_model:
  confidence: high
  label: Requires approval
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.stotles.com/pricing
  - https://www.stotles.com/integrations
  - https://api.stotles.com/v1/openapi.json
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Hosted, remote Model Context Protocol server exposing Stotles public sector market data to AI chat tools and agents. Streamable-HTTP transport at api.stotles.com/mcp, authenticated with the same x-api
  name: Stotles MCP Server
  slug: stotles-mcp-server
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Public sector buyers and their procurement activity.
  name: Stotles Buyers API
  slug: stotles-buyers-api
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Framework agreements and dynamic purchasing systems.
  name: Stotles Frameworks API
  slug: stotles-frameworks-api
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Public sector procurement notices.
  name: Stotles Notices API
  slug: stotles-notices-api
- baseURL: https://api.stotles.com/v1
  baseurl_source: declared
  description: Suppliers bidding for and winning public sector contracts.
  name: Stotles Suppliers API
  slug: stotles-suppliers-api
artifact_total: 16
common:
- group: other
  href: https://artifacts.apis.io/stotles/capabilities/stotles-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stotles-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/stotles/rate-limits/stotles-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stotles-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/stotles/overlays/stotles-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stotles-public-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/stotles/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.stotles.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.stotles.com/
- group: operate
  title: ''
  type: Support
  url: https://help.stotles.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.stotles.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://app.stotles.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://app.stotles.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.stotles.com/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stotles.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.stotles.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stotles.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stotles.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.eu.vanta.com/stotles.com/trust/xpcnkioxgcvk0i3qd7fm
- group: auth
  title: ''
  type: Compliance
  url: https://app.eu.vanta.com/stotles.com/trust/xpcnkioxgcvk0i3qd7fm
- group: design
  href: https://artifacts.apis.io/stotles/conformance/stotles-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stotles-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stotles/security/stotles-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stotles-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/stotles/llms/stotles-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stotles-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.stotles.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/stotles/security/stotles-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stotles-trust-center.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stotles
- group: build
  href: https://artifacts.apis.io/stotles/packages/stotles-packages.yml
  title: ''
  type: Packages
  url: packages/stotles-packages.yml
- group: commercial
  href: https://artifacts.apis.io/stotles/plans/stotles-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stotles-plans-pricing.yml
created: '2026-07-17'
description: 'Stotles is a B2G (business-to-government) public sector procurement and sales intelligence platform for the UK and Ireland. It aggregates procurement notices, contract awards, framework agreements, buyer spend history, and verified decision-maker contacts from public sources such as Find a Tender, Contracts Finder, Digital Marketplace, TED, and Public Contracts Scotland, then layers tender discovery, market intelligence, AI-assisted bid qualification (Bid Studio), account targeting (Sales Studio), and pipeline management on top so suppliers can find, qualify, and win government contracts. Delivered as a SaaS web application at app.stotles.com, and — since 2026 — as a programmable surface: the Stotles Public API is a documented OpenAPI 3.1.0 REST service at api.stotles.com/v1 covering notices, buyers, suppliers and framework agreements, alongside a hosted Model Context Protocol server at api.stotles.com/mcp that brings the same market data into AI chat tools and agents. Both
  authenticate with a static x-api-key header; keys are issued by a Customer Success Manager rather than self-serve, and MCP access is in beta behind a waitlist.'
finops:
- has_sources: true
  method: derived
  name: Stotles Finops
  primary_unit: subscription
  service_category: ''
  slug: stotles-finops
  template: false
image: https://cdn.prod.website-files.com/67caf809eabcc3eb572f7bc7/68149b136c8bcfe66f0b8b2f_SEO%20Image%20-%20Homepage.jpg
layout: provider
modified: '2026-08-14'
name: Stotles
nav: Providers
network: true
overview: 'Stotles publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buyers API, Frameworks API, Notices API, and 2 more. Tagged areas include Company, Procurement, Public Sector, Government, and Tenders.


  Stotles'' developer surface includes documentation, support, getting-started guide, signup flow, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Stotles Plans Pricing
  plan_count: 10
  slug: stotles-plans-pricing
- name: Stotles Price Estimates
  plan_count: 0
  slug: stotles-price-estimates
random_paper: 14
rate_limits:
- limit_count: 2
  name: Stotles Rate Limits
  slug: stotles-rate-limits
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 49.4
    discoverability: 71.7
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 58.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stotles/stotles-2026-08-17T082131.png
security:
- kind: authentication
  name: Stotles Authentication
  slug: stotles-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stotles Domain Security
  slug: stotles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stotles Trust Center
  slug: stotles-trust-center
  summary_line: SOC 2 Type II, GDPR
skill_count: 4
skills:
- name: Analyse a competitor's public sector wins
  slug: stotles-analyse-a-competitor
- name: Map a framework agreement and the call-offs made under it
  slug: stotles-map-a-framework
- name: Profile a public sector buyer and its procurement history
  slug: stotles-profile-a-buyer
- name: Track open tenders in your market
  slug: stotles-track-open-tenders
slug: stotles
tags:
- Company
- Procurement
- Public Sector
- Government
- Tenders
- Sales Intelligence
- B2G
- Market Intelligence
- OpenAPI
- MCP
- Agent-Native
- Contract Awards
- Framework Agreements
- CPV
- United Kingdom
- Ireland
- GovTech
website: https://www.stotles.com
---
