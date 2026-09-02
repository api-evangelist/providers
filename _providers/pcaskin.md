---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
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
  score: 9.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Universal Commerce Protocol agent-commerce surface for the PCA SKIN Shopify store — a hosted MCP endpoint (search_catalog, create_cart, create_checkout, update_checkout, complete_checkout) plus read-o
  name: PCA SKIN Agent Commerce (UCP)
  slug: pca-skin-agent-commerce-ucp
artifact_total: 3
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pcaskin-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pcaskin-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pcaskin-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/pcaskin-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pcaskin-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pcaskin.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pcaskin.com/policies/terms-of-service
- group: company
  title: ''
  type: Website
  url: https://pcaskin.com
created: '2026-07-17'
description: 'PCA SKIN is a professional skincare brand specializing in dermatologically tested chemical peels and result-oriented corrective products, positioned as a leading professional chemical-peel brand among estheticians and skincare professionals. The brand''s direct-to-consumer store at pcaskin.com is built on Shopify and exposes a modern agent-commerce surface: it implements the Universal Commerce Protocol (UCP) with a hosted MCP endpoint plus read-only storefront JSON, so AI shopping agents can discover the catalog, build carts, and drive buyer-approved checkout. Surfaced as a portfolio company of Norwest Venture Partners and enriched by the API Evangelist pipeline from the store''s published agent surface (/llms.txt, /.well-known/ucp).'
image: https://pcaskin.com/cdn/shop/files/PCA_SKIN_logo.png
layout: provider
mcp_servers:
- description: ''
  name: PCA SKIN (Universal Commerce Protocol)
  slug: pca-skin-universal-commerce-protocol
modified: '2026-07-20'
name: PCA SKIN
nav: Providers
network: true
overview: PCA SKIN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Skincare, Beauty, Cosmetics, and E-Commerce.
random_paper: 10
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pcaskin/refs/heads/main/screenshots/pcaskin-2026-08-07T191713.png
security:
- kind: domain-security
  name: Pcaskin Domain Security
  slug: pcaskin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pcaskin
tags:
- Company
- Skincare
- Beauty
- Cosmetics
- E-Commerce
- Retail
- Agent Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://pcaskin.com
---
