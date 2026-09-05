---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Allbirds's agent-facing commerce API, implemented via the Shopify Universal Commerce Protocol (UCP) over MCP. Agents can search the catalog, manage a cart, read store policies/FAQs, and drive a buyer-
  name: Allbirds Storefront Commerce (UCP / MCP)
  slug: allbirds-storefront-commerce-ucp-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.allbirds.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allbirds-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allbirds-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allbirds-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allbirds-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allbirds-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allbirds-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allbirds-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allbirds.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allbirds.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.allbirds.com/pages/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.allbirds.com/blogs/news
created: '2026-07-17'
description: 'Allbirds is a sustainability-focused footwear and apparel brand known for its wool and tree-fiber shoes, selling direct-to-consumer through its Shopify-powered online store at allbirds.com. It was surfaced as a portfolio company of Addition and added to the API Evangelist network. While Allbirds publishes no traditional developer program, its storefront exposes a real agent-commerce surface: a live Shopify Universal Commerce Protocol (UCP) MCP server for catalog search, cart, and checkout; OpenID Connect / OAuth 2.0 Customer Accounts authentication; and an /llms.txt agent-instructions document. This profile captures that agent-native commerce and authentication surface.'
image: https://www.allbirds.com/cdn/shop/files/Allbirds_Logo.png
layout: provider
mcp_servers:
- description: ''
  name: Allbirds MCP Server
  slug: allbirds-mcp-server
modified: '2026-07-17'
name: Allbirds
nav: Providers
network: true
overview: 'Allbirds publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Footwear.


  Allbirds'' developer surface includes authentication, support, engineering blog, and 9 more developer resources.'
random_paper: 5
scopes:
- name: Allbirds Scopes
  scope_count: 4
  slug: allbirds-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allbirds/refs/heads/main/screenshots/allbirds-2026-08-07T161217.png
security:
- kind: authentication
  name: Allbirds Authentication
  slug: allbirds-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Allbirds Domain Security
  slug: allbirds-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allbirds
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Footwear
- Apparel
- Sustainability
- Direct to Consumer
- Agent Commerce
- Shopify
website: https://www.allbirds.com
---
