---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Two live Model Context Protocol endpoints served from the same WordPress installation and advertised through RFC 9728 OAuth 2.0 Protected Resource Metadata. Both are OAuth-gated - an anonymous tools/l
  name: Redefine Meat MCP Server
  slug: mcp
- description: The wc/store/v1 API from Redefine Meat — 30 operation(s) for wc/store/v1.
  name: Redefine Meat Wc/store/v1 API
  slug: redefine-meat-wc-store-v1-api
- description: The wp/v2 API from Redefine Meat — 117 operation(s) for wp/v2.
  name: Redefine Meat Wp/v2 API
  slug: redefine-meat-wp-v2-api
artifact_total: 8
asyncapis:
- description: ''
  name: Redefine Meat Webhooks
  slug: redefine-meat-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/redefine-meat-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redefine-meat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redefinemeat.com/
- group: other
  title: ''
  type: Company
  url: https://www.redefinemeat.com/company/
- group: other
  title: ''
  type: Products
  url: https://www.redefinemeat.com/products/
- group: operate
  title: ''
  type: Support
  url: https://www.redefinemeat.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.redefinemeat.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.redefinemeat.com/blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.redefinemeat.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.redefinemeat.com/news-media/
- group: company
  title: ''
  type: Careers
  url: https://www.redefinemeat.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redefinemeat.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redefinemeat.com/privacy-policy/
- group: other
  title: ''
  type: Imprint
  url: https://www.redefinemeat.com/imprint/
- group: other
  title: ''
  type: WhereToBuy
  url: https://www.redefinemeat.com/where-to-find/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/redefine-meat-stock
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redefine-meat-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redefine-meat-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/redefine-meat-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/redefine-meat-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/redefine-meat-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/redefine-meat-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/redefine-meat-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/redefine-meat-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redefine-meat-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'Redefine Meat is an Israeli food-technology company, founded in 2018, that manufactures plant-based whole-cut meat alternatives it markets as New-Meat, using proprietary industrial 3D printing together with plant-protein formulations it calls Alt-Muscle, Alt-Fat and Alt-Blood. Its range spans steaks, burgers, shawarma, beef mince, lamb kofta, pulled beef and bratwurst across consumer (B2C) and foodservice (B2B / PRO) lines, sold through restaurants, hotels, caterers and retail in the United Kingdom, Germany, the Netherlands, France and Israel. Redefine Meat operates no developer program, but its own website at www.redefinemeat.com runs on WordPress and WooCommerce and exposes a genuinely public, machine-readable API surface: a WordPress REST API discovery index advertising 845 routes across 30 namespaces, an anonymously readable WooCommerce Store API for products, categories and cart, and two OAuth-gated Model Context Protocol endpoints advertised through RFC 8414 and RFC 9728
  well-known metadata.'
image: https://www.redefinemeat.com/wp-content/uploads/2023/11/Europe_Retail_Support_1920x800.jpg
layout: provider
mcp_servers:
- description: ''
  name: redefine-meat-mcp.yml
  slug: redefine-meat-mcpyml
modified: '2026-08-05'
name: Redefine Meat
nav: Providers
network: true
overview: 'Redefine Meat publishes 2 APIs on the [APIs.io](https://apis.io/) network: Wc/store/v1 API and Wp/v2 API. Tagged areas include Food and Beverage, Alternative Protein, Plant-Based, Food Technology, and Manufacturing.


  The Redefine Meat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Redefine Meat''s developer surface includes support, FAQ, engineering blog, authentication, and 22 more developer resources.'
random_paper: 102
scopes:
- name: Redefine Meat Scopes
  scope_count: 1
  slug: redefine-meat-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.0
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 34.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Redefine Meat Authentication
  slug: redefine-meat-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Redefine Meat Domain Security
  slug: redefine-meat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: redefine-meat
tags:
- Food and Beverage
- Alternative Protein
- Plant-Based
- Food Technology
- Manufacturing
- E-Commerce
- WooCommerce
- WordPress
- Retail
- Model Context Protocol
website: https://www.redefinemeat.com/
---
