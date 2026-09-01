---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'The WooCommerce Store API served from the Reed Semiconductor corporate site. Anonymous, read-only over the product catalog: 99 power-management parts (multiphase controllers, smart power stages, eFuse'
  name: Reed Semiconductor Store API
  slug: reed-semiconductor-store-api
- description: The WordPress REST API (wp/v2) served from the Reed Semiconductor corporate site. Anonymous read access to newsroom posts, pages, media, categories and taxonomies — the machine-readable form of the Re
  name: Reed Semiconductor Content API
  slug: reed-semiconductor-content-api
- description: A Model Context Protocol server mounted at the Reed Semiconductor apex domain by the Novamira WordPress plugin (v1.11.4). It advertises itself through RFC 9728 protected-resource metadata and RFC 8414
  name: Reed Semiconductor MCP Server
  slug: reed-semiconductor-mcp
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reed-semiconductor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reedsemi.com/
- group: company
  title: ''
  type: Blog
  url: https://www.reedsemi.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.reedsemi.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.reedsemi.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.reedsemi.com/my-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reedsemi.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reedsemi.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reed-semiconductor-corp
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reed-semiconductor-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reed-semiconductor-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reed-semiconductor-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/reed-semiconductor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/reed-semiconductor-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reed-semiconductor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reed-semiconductor-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reed-semiconductor-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reed-semiconductor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reed-semiconductor-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/reed-semiconductor-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/reed-semiconductor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reed-semiconductor-rate-limits.yml
created: '2026-08-26'
description: 'Reed Semiconductor Corp. is a fabless power-management semiconductor company founded in 2019 and headquartered in Rhode Island, USA, with offices in Taipei, Shenzhen and Bengaluru. The name stands for Robust, Efficient, Eco-friendly and Dense power solutions. It designs multiphase DC-DC controllers, smart power stages, half-bridge power stages, point-of-load converters, power modules, intermediate bus converters, eFuses and power multiplexers for data center and AI/HPC accelerators, 48V and 12V distribution, communication and datacom equipment, automotive ADAS and infotainment, industrial systems and personal electronics. Reed does not operate a developer program, but its WordPress/WooCommerce corporate site exposes real machine-readable surfaces: an anonymous WooCommerce Store API serving the 99-part parametric product catalog across 81 application and technology categories, the WordPress content API, and an OAuth 2.1 protected Model Context Protocol server published through
  RFC 8414 and RFC 9728 metadata at the apex domain.'
image: https://cdn.reedsemi.com/2024/09/reedsemi-og-logo.png
layout: provider
mcp_servers:
- description: 'Reed Semiconductor''s corporate WordPress site mounts a Model Context Protocol server at the apex domain. It is real, reachable and OAuth-gated: an anonymous JSON-RPC tools/list returns HTTP 401 with a'
  name: Reed Semiconductor MCP Server
  slug: reed-semiconductor-mcp-server
modified: '2026-08-26'
name: Reed Semiconductor
nav: Providers
network: true
overview: 'Reed Semiconductor publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Power Management, Electronic Components, and Data-Center.


  Reed Semiconductor''s developer surface includes engineering blog, support, signup flow, authentication, and 18 more developer resources.'
plans:
- name: Reed Semiconductor Plans Pricing
  plan_count: 0
  slug: reed-semiconductor-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Reed Semiconductor Rate Limits
  slug: reed-semiconductor-rate-limits
scopes:
- name: Reed Semiconductor Scopes
  scope_count: 0
  slug: reed-semiconductor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 52.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Reed Semiconductor Authentication
  slug: reed-semiconductor-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Reed Semiconductor Domain Security
  slug: reed-semiconductor-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: reed-semiconductor
tags:
- Company
- Semiconductors
- Power Management
- Electronic Components
- Data-Center
- Artificial Intelligence
- Automotive
- Hardware
- Manufacturing
- Product Catalog
website: https://www.reedsemi.com/
---
