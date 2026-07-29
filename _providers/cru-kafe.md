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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Shopify-native Universal Commerce Protocol surface served on crukafe.com: a hosted MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout, backed by Shopify Customer Account O'
  name: CRU Kafe Agent Commerce (UCP)
  slug: cru-kafe-agent-commerce-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cru-kafe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://crukafe.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cru-kafe-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cru-kafe-well-known.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crukafe.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crukafe.com/policies/terms-of-service
created: '2026-07-17'
description: 'CRU Kafe is a London-founded organic coffee brand selling Fairtrade, ethically sourced coffee - including award-winning Nespresso-compatible pods from 33p per pod, plus ground coffee and beans - direct to consumers through its Shopify storefront at crukafe.com. Backed by Seedcamp, the company was added to the API Evangelist network as a portfolio lead. CRU Kafe publishes no first-party developer API; its machine-readable surface is the Shopify / Universal Commerce Protocol (UCP) agent-commerce layer served on its own domain: a hosted UCP MCP endpoint for agent-driven catalog search and buyer-approved checkout, an llms.txt / agents.md for AI shopping assistants, and Shopify Customer Account OAuth 2.0 / OpenID Connect identity.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cru-kafe.png
layout: provider
mcp_servers:
- description: ''
  name: cru-kafe-mcp.yml
  slug: cru-kafe-mcpyml
modified: '2026-07-18'
name: CRU Kafe
nav: Providers
network: true
overview: CRU Kafe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, Ecommerce, Retail, and Consumer Goods.
random_paper: 71
scopes:
- name: Cru Kafe Scopes
  scope_count: 0
  slug: cru-kafe-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  delta: 0.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 13.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Cru Kafe Authentication
  slug: cru-kafe-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cru Kafe Domain Security
  slug: cru-kafe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cru-kafe
tags:
- Company
- Coffee
- Ecommerce
- Retail
- Consumer Goods
- Food and Beverage
- Shopify
- Agent Commerce
- UCP
website: http://crukafe.com
---
