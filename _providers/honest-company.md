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
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 23.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'Agent-native commerce surface for the honest.com Shopify storefront. Exposes a live Universal Commerce Protocol (UCP) shopping MCP endpoint for catalog search, cart, and buyer-approved checkout, plus '
  name: Honest Storefront Agent Commerce (UCP)
  slug: honest-storefront-agent-commerce-ucp
- description: honest.com authenticates shoppers through the Shopify Customer Account API, an OAuth2 / OpenID Connect provider. Discovery is published at /.well-known/openid-configuration and /.well-known/oauth-auth
  name: Shopify Customer Account API (OAuth2 / OIDC)
  slug: shopify-customer-account-api-oauth2-oidc
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://honest.com
- group: start
  title: ''
  type: SignUp
  url: https://honest.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://support.honest.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://honest.com/blogs/archive
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://honest.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://honest.com/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/honest-company-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/honest-company-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/honest-company-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/honest-company-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/honest-company-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/honest-company-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honest-company-domain-security.yml
created: '2026-07-17'
description: 'The Honest Company is a consumer-products brand founded in 2011 and headquartered in Los Angeles, offering baby care, personal care, beauty, and household cleaning products built around its "Honest Standard" of ingredient transparency. Its direct-to-consumer storefront at honest.com runs on Shopify and exposes a modern agent-native commerce surface: a published /agents.md and /llms.txt, an /.well-known/ucp Universal Commerce Protocol merchant profile, a live UCP shopping MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout, and Shopify Customer Account API OAuth2/OIDC discovery documents. This profile was surfaced as a General Catalyst portfolio company and enriched by the API Evangelist pipeline from the store''s public agent and discovery surfaces.'
image: https://honest.com/cdn/shop/files/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Honest Company MCP Server
  slug: honest-company-mcp-server
modified: '2026-07-19'
name: Honest Company
nav: Providers
network: true
overview: 'Honest Company publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Goods, E-Commerce, Retail, and Baby Care.


  Honest Company''s developer surface includes signup flow, support, engineering blog, authentication, and 10 more developer resources.'
random_paper: 12
scopes:
- name: Honest Company Scopes
  scope_count: 4
  slug: honest-company-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 21.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honest-company/refs/heads/main/screenshots/honest-company-2026-08-07T170253.png
security:
- kind: authentication
  name: Honest Company Authentication
  slug: honest-company-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Honest Company Domain Security
  slug: honest-company-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: honest-company
tags:
- Company
- Consumer Goods
- E-Commerce
- Retail
- Baby Care
- Personal Care
- Beauty
- Shopify
- Agentic Commerce
- MCP
- UCP
website: https://honest.com
---
