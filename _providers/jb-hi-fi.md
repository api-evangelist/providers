---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Universal Commerce Protocol (UCP) shopping service for the JB Hi-Fi online store, advertised in the store's agents.md and its /.well-known/ucp profile, exposed as a remote MCP endpoint whose tools/lis
  name: JB Hi-Fi UCP Shopping MCP Server
  slug: jb-hi-fi-ucp-shopping-mcp
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/jb-hi-fi/rate-limits/jb-hi-fi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jb-hi-fi-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/jb-hi-fi/conventions/jb-hi-fi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/jb-hi-fi-conventions.yml
- group: design
  href: https://artifacts.apis.io/jb-hi-fi/conventions/jb-hi-fi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jb-hi-fi-conventions.yml
- group: auth
  href: https://artifacts.apis.io/jb-hi-fi/authentication/jb-hi-fi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jb-hi-fi-authentication.yml
- group: design
  href: https://artifacts.apis.io/jb-hi-fi/lifecycle/jb-hi-fi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jb-hi-fi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jb-hi-fi/conformance/jb-hi-fi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jb-hi-fi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jb-hi-fi/llms/jb-hi-fi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jb-hi-fi-llms.txt
- group: agent
  href: https://artifacts.apis.io/jb-hi-fi/mcp/jb-hi-fi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jb-hi-fi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/jb-hi-fi/well-known/jb-hi-fi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jb-hi-fi-well-known.yml
- group: other
  href: https://artifacts.apis.io/jb-hi-fi/hosts/jb-hi-fi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jb-hi-fi-hosts.yml
- group: build
  href: https://artifacts.apis.io/jb-hi-fi/integrations/jb-hi-fi-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/jb-hi-fi-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/jb-hi-fi/vendors/jb-hi-fi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jb-hi-fi-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.instagram.com/
- group: auth
  href: https://artifacts.apis.io/jb-hi-fi/security/jb-hi-fi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jb-hi-fi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jbhifi.com.au/
- group: company
  title: ''
  type: AboutUs
  url: https://www.jbhifi.com.au/pages/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.jbhifi.com.au/pages/help-and-support
- group: company
  title: ''
  type: Blog
  url: https://www.jbhifi.com.au/blogs/news-and-reviews
- group: company
  title: ''
  type: Newsroom
  url: https://www.jbhifi.com.au/blogs/music/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jbhifi.com.au/pages/help-and-support/terms-of-use
- group: commercial
  title: ''
  type: TermsOfSale
  url: https://www.jbhifi.com.au/pages/help-and-support/terms-of-sale
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jbhifi.com.au/pages/help-and-support/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.jbhifi.com.au/pages/jobs
- group: company
  title: ''
  type: Investors
  url: https://investors.jbhifi.com.au/
- group: other
  title: ''
  type: Sustainability
  url: https://www.jbhifi.com.au/pages/sustainability
- group: other
  title: ''
  type: AgentInstructions
  url: https://www.jbhifi.com.au/agents.md
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/jbhifi/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/JBHiFiOfficial
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@jbhifi
created: '2026-10-21'
description: JB Hi-Fi Limited is an ASX-listed Australian retailer of consumer electronics and home entertainment, founded in 1974 by John Barbuto with a single store in East Keilor, Victoria, and floated on the Australian Stock Exchange in October 2003. It describes itself as Australia's largest home entertainment retailer, selling computers, tablets, TVs, cameras, hi-fi, games, music and movies through its stores and its online store at jbhifi.com.au, alongside JB Hi-Fi HOME stores, JB Hi-Fi Business, a BYOD education portal and the JB Hi-Fi Marketplace. Its online store publishes an agents.md guide advertising Universal Commerce Protocol (UCP) discovery and an MCP endpoint for agentic shopping.
image: https://cdn.shopify.com/s/files/1/0024/9803/5810/files/logo.png?height=628&pad_color=fff&v=1613146384&width=1200
json_schemas:
- name: Jb Hi Fi Ucp Mcp Tools List
  property_count: 0
  slug: jb-hi-fi-ucp-mcp-tools-list
layout: provider
mcp_servers:
- description: Remote MCP endpoint for JB Hi-Fi's Shopify-hosted online store implementing the Universal Commerce Protocol (UCP) shopping service (dev.ucp.shopping). Advertised in https://www.jbhifi.com.au/agents.md
  name: JB Hi-Fi UCP Shopping MCP Server
  slug: jb-hi-fi-ucp-shopping-mcp-server
modified: '2026-10-21'
name: JB Hi-Fi
nav: Providers
network: true
overview: 'JB Hi-Fi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Consumer Electronics, E-Commerce, and Home Entertainment.


  JB Hi-Fi''s developer surface includes authentication, documentation, support, engineering blog, YouTube channel, and 24 more developer resources.'
plans:
- name: Jb Hi Fi Plans Pricing
  plan_count: 0
  slug: jb-hi-fi-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Jb Hi Fi Rate Limits
  slug: jb-hi-fi-rate-limits
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.4
    catalog_earned_first_party: 8.0
    catalog_gap: 64.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 7.2
    developer_ergonomics: 20.2
    discoverability: 75.8
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jb-hi-fi/jb-hi-fi-2026-11-03T134139.png
security:
- kind: authentication
  name: Jb Hi Fi Authentication
  slug: jb-hi-fi-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Jb Hi Fi Domain Security
  slug: jb-hi-fi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jb-hi-fi
tags:
- Company
- Retail
- Consumer Electronics
- E-Commerce
- Home Entertainment
- Australia
- Agentic Commerce
website: https://www.jbhifi.com.au/
---
