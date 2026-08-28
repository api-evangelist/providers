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
    agent_skills: derived
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
  score: 21.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Agent-driven commerce surface for the AMUSED Co store implemented with the Universal Commerce Protocol (UCP) over MCP: catalog search/lookup, cart, checkout, fulfillment, discount and order capabiliti'
  name: AMUSED Co Commerce (UCP / MCP)
  slug: amused-co-commerce-ucp-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://amusedco.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amusedco.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amusedco.com/policies/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thamarah-al-jill-co-llc-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thamarah-al-jill-co-llc-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thamarah-al-jill-co-llc-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thamarah-al-jill-co-llc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thamarah-al-jill-co-llc-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thamarah-al-jill-co-llc-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thamarah-al-jill-co-llc-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thamarah-al-jill-co-llc-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thamarah-al-jill-co-llc-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Thamarah Al-Jill Co LLC operates AMUSED Co (amusedco.com), a Saudi Arabia-based online marketplace for authenticated, curated pre-loved luxury — designer handbags and women''s clothing from houses such as Louis Vuitton, Hermes and Chanel at up to 70% off retail. Under a "Resell, Rebuy, Relove" model, buyers shop verified second-hand pieces (backed by a one-year authentication money-back guarantee) and sellers list their own unused items; payment options include credit card, Mada and Tamara. The store is a 500 Global portfolio company. It is built on Shopify and is fully agent-native: it publishes an /llms.txt agent guide and implements the Universal Commerce Protocol (UCP) over an MCP endpoint, with Shopify Customer Accounts OpenID Connect for buyer authentication.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thamarah-al-jill-co-llc.png
layout: provider
mcp_servers:
- description: ''
  name: Thamarah Al-Jill Co LLC MCP Server
  slug: thamarah-al-jill-co-llc-mcp-server
modified: '2026-07-21'
name: Thamarah Al-Jill Co LLC
nav: Providers
network: true
overview: 'Thamarah Al-Jill Co LLC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Luxury, and Resale.


  Thamarah Al-Jill Co LLC''s developer surface includes authentication and 12 more developer resources.'
random_paper: 12
scopes:
- name: Thamarah Al Jill Co Llc Scopes
  scope_count: 4
  slug: thamarah-al-jill-co-llc-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Thamarah Al Jill Co Llc Authentication
  slug: thamarah-al-jill-co-llc-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Thamarah Al Jill Co Llc Domain Security
  slug: thamarah-al-jill-co-llc-domain-security
  summary_line: HSTS · DMARC
slug: thamarah-al-jill-co-llc
tags:
- Company
- E-Commerce
- Marketplace
- Luxury
- Resale
- Fashion
- Agent Commerce
- Shopify
- Saudi Arabia
website: https://amusedco.com
---
