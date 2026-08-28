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
    agentic_access: true
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
  score: 27.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 1
  name: Source Beauty Agentic Access
  operation_count: 5
  slug: source-beauty-agentic-access
  summary_line: 5 operations · 1 human-in-the-loop
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/source-beauty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sourcebeauty.com
- group: start
  title: ''
  type: SignUp
  url: https://sourcebeauty.com/account/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sourcebeauty.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sourcebeauty.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/source-beauty-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/source-beauty-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/source-beauty-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/source-beauty-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/source-beauty-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/source-beauty-agentic-access.yml
created: '2026-07-17'
description: Source Beauty is an online beauty and wellbeing marketplace serving Egypt, selling skincare, makeup, fragrance, hair care, body care, K-beauty and wellness/supplement products from hundreds of local Egyptian and international brands. The consumer-facing storefront (sourcebeauty.com) offers curated brand pages, bundles and gift sets, promotional offers, bilingual English/Arabic shopping, and free shipping on qualifying orders. Source Beauty is a 500 Global portfolio company. As of this enrichment pass the company operates a direct-to-consumer e-commerce website only and publishes no public developer program, API, SDKs, or technical documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/source-beauty.png
layout: provider
mcp_servers:
- description: ''
  name: Source Beauty UCP Shopping MCP
  slug: source-beauty-ucp-shopping-mcp
modified: '2026-07-21'
name: Source Beauty
nav: Providers
network: true
overview: 'Source Beauty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Cosmetics, E-Commerce, and Retail.


  Source Beauty''s developer surface includes signup flow, authentication, and 9 more developer resources.'
random_paper: 8
scopes:
- name: Source Beauty Scopes
  scope_count: 4
  slug: source-beauty-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 16.1
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  provenance:
    agentic_access: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Source Beauty Authentication
  slug: source-beauty-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Source Beauty Domain Security
  slug: source-beauty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: source-beauty
tags:
- Company
- Beauty
- Cosmetics
- E-Commerce
- Retail
- Marketplace
- Wellness
- Egypt
- Skincare
- Consumer
website: https://sourcebeauty.com
---
