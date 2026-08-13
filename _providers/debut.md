---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The agent-facing commerce API for Debut's direct-to-consumer skincare brand DEINDE. It is a Shopify-hosted Universal Commerce Protocol (UCP) service exposed over MCP at https://www.deinde.com/api/ucp/
  name: DEINDE Commerce (UCP MCP)
  slug: deinde-commerce-ucp-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.debutbiotech.com/
- group: other
  title: ''
  type: Product
  url: https://www.debutbiotech.com/platform
- group: company
  title: ''
  type: About
  url: https://www.debutbiotech.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.debutbiotech.com/news
- group: company
  title: ''
  type: News
  url: https://www.debutbiotech.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.debutbiotech.com/contact-us
- group: operate
  title: ''
  type: Contact
  url: https://www.debutbiotech.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.debutbiotech.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.debutbiotech.com/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/debut-biotechnology
- group: other
  title: ''
  type: Store
  url: https://www.deinde.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.deinde.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/debut-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/debut-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/debut-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/debut-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/debut-scopes.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/debut-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/debut-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/debut-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/debut-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/debut-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/debut-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/debut-lifecycle.yml
created: '2026-08-12'
description: 'Debut (Debut Biotechnology, Inc.) is a San Diego, California biotechnology company founded in 2019 by Dr. Joshua Britton that combines AI-driven molecular discovery, skin genomics and cell-free biomanufacturing to create novel cosmetic active ingredients and finished skincare formulations. Its BeautyORB platform screens billions of candidate molecules in silico against a skin-health genomic dataset, and the company is vertically integrated from discovery through fermentation, scale-up and formulation, selling ingredients and brand-ready products to beauty manufacturers as well as running its own direct-to-consumer skincare brand, DEINDE. Debut has raised roughly $89M across Series A, Series B (led by BOLD, the L''Oreal venture fund) and later rounds, employs more than 80 people, and was named to the TIME100 Most Innovative Companies 2025. Debut sells molecules and formulations rather than software: debutbiotech.com publishes no developer program, no public API and no machine-readable
  API contract. Its only agent-reachable API surface is the Shopify-hosted Universal Commerce Protocol (UCP) MCP endpoint on its DEINDE storefront at www.deinde.com, which is live, unauthenticated for catalog and cart operations, and returns full JSON Schema tool definitions.'
image: https://cdn.prod.website-files.com/697a5ef4d9ca0a3187500d0b/697a5ef4d9ca0a3187500d47_Debut-Favicon.png
layout: provider
mcp_servers:
- description: ''
  name: debut-mcp.yml
  slug: debut-mcpyml
modified: '2026-08-12'
name: Debut
nav: Providers
network: true
overview: 'Debut publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Beauty, Cosmetics, and Skincare.


  Debut''s developer surface includes engineering blog, product news, support, documentation, authentication, and 21 more developer resources.'
plans:
- name: Debut Plans Pricing
  plan_count: 0
  slug: debut-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Debut Rate Limits
  slug: debut-rate-limits
scopes:
- name: Debut Scopes
  scope_count: 0
  slug: debut-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Debut Authentication
  slug: debut-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Debut Domain Security
  slug: debut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: debut
tags:
- Company
- Biotechnology
- Beauty
- Cosmetics
- Skincare
- Ingredients
- Synthetic Biology
- Artificial Intelligence
- Manufacturing
- Ecommerce
- Agentic Commerce
website: https://www.debutbiotech.com/
---
