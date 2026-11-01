---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Universal Commerce Protocol (UCP) shopping service for Lovisa's Shopify-hosted online store, advertised in https://www.lovisa.com/llms.txt and the store's /.well-known/ucp profile. An MCP (JSON-RPC) e
  name: Lovisa UCP Shopping MCP
  slug: lovisa-ucp-shopping-mcp
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/lovisa/rate-limits/lovisa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lovisa-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/lovisa/conventions/lovisa-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lovisa-conventions.yml
- group: design
  href: https://artifacts.apis.io/lovisa/conventions/lovisa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lovisa-conventions.yml
- group: auth
  href: https://artifacts.apis.io/lovisa/authentication/lovisa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lovisa-authentication.yml
- group: design
  href: https://artifacts.apis.io/lovisa/lifecycle/lovisa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lovisa-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lovisa/conformance/lovisa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lovisa-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lovisa/llms/lovisa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lovisa-llms.txt
- group: agent
  href: https://artifacts.apis.io/lovisa/mcp/lovisa-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lovisa-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lovisa/well-known/lovisa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lovisa-well-known.yml
- group: other
  href: https://artifacts.apis.io/lovisa/hosts/lovisa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lovisa-hosts.yml
- group: build
  href: https://artifacts.apis.io/lovisa/integrations/lovisa-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/lovisa-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/lovisa/vendors/lovisa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lovisa-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://ambassador.lovisa.com/create-account
- group: auth
  href: https://artifacts.apis.io/lovisa/security/lovisa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lovisa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lovisa.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lovisa.com/blogs/stylechannel
- group: operate
  title: ''
  type: Support
  url: https://www.lovisa.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lovisa.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lovisa.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lovisa.com/pages/security-privacy
- group: company
  title: ''
  type: AboutUs
  url: https://www.lovisa.com/pages/about
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.lovisa.com/pages/investor-centre
- group: company
  title: ''
  type: Careers
  url: https://careers.lovisa.com/
created: '2026-10-21'
description: 'Lovisa (Lovisa Holdings, ASX code: LOV) is an Australian fast-fashion jewellery retailer established in April 2010, selling affordable, on-trend earrings, necklaces, wristwear, rings and piercing services through more than 900 stores in over 45 countries and its Shopify-based online store at lovisa.com. Its site publishes an investor centre, a style blog, careers and ambassador programs; no public developer API, API documentation or developer portal was found on its own domains. Surfaced via the API Evangelist harvest backlog (source: australia-apidays-2026).'
image: https://cdn.shopify.com/s/files/1/0257/8130/5424/files/Lovisa_Logo_80_BLACK_1000x1000px.png
json_schemas:
- name: Lovisa Ucp Mcp Tools List
  property_count: 0
  slug: lovisa-ucp-mcp-tools-list
layout: provider
mcp_servers:
- description: Remote MCP (JSON-RPC over HTTP) Universal Commerce Protocol shopping service for Lovisa's Shopify-hosted US online store. Advertised in the store's own llms.txt and /.well-known/ucp profile. It is Sho
  name: Lovisa UCP Shopping MCP
  slug: lovisa-ucp-shopping-mcp
modified: '2026-10-21'
name: Lovisa
nav: Providers
network: true
overview: 'Lovisa is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Jewelry, Fashion, and E-Commerce.


  Lovisa''s developer surface includes authentication, signup flow, engineering blog, support, and 19 more developer resources.'
plans:
- name: Lovisa Plans Pricing
  plan_count: 0
  slug: lovisa-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Lovisa Rate Limits
  slug: lovisa-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.4
    catalog_earned_first_party: 8.0
    catalog_gap: 64.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 7.2
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 27.2
  provenance:
    conformance: first-party
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lovisa Authentication
  slug: lovisa-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Lovisa Domain Security
  slug: lovisa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lovisa
tags:
- Company
- Retail
- Jewelry
- Fashion
- E-Commerce
- Australia
- ASX Listed
website: https://www.lovisa.com/
---
