---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Vestaron Agentic Access
  operation_count: 89
  slug: vestaron-agentic-access
  summary_line: 89 operations · 54 acting
api_count: 10
apis:
- description: 'A remote Model Context Protocol server published on the vestaron.com host and advertised anonymously through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. The '
  name: Vestaron MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: The Comments API from Vestaron — 2 operation(s) for comments.
  name: Vestaron Comments API
  slug: vestaron-comments-api
- description: The Discovery API from Vestaron — 5 operation(s) for discovery.
  name: Vestaron Discovery API
  slug: vestaron-discovery-api
- description: The Media API from Vestaron — 4 operation(s) for media.
  name: Vestaron Media API
  slug: vestaron-media-api
- description: The Pages API from Vestaron — 6 operation(s) for pages.
  name: Vestaron Pages API
  slug: vestaron-pages-api
- description: The Posts API from Vestaron — 6 operation(s) for posts.
  name: Vestaron Posts API
  slug: vestaron-posts-api
- description: The Search API from Vestaron — 1 operation(s) for search.
  name: Vestaron Search API
  slug: vestaron-search-api
- description: The Settings API from Vestaron — 1 operation(s) for settings.
  name: Vestaron Settings API
  slug: vestaron-settings-api
- description: The Taxonomy API from Vestaron — 6 operation(s) for taxonomy.
  name: Vestaron Taxonomy API
  slug: vestaron-taxonomy-api
- description: The Users API from Vestaron — 6 operation(s) for users.
  name: Vestaron Users API
  slug: vestaron-users-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://vestaron.com/
- group: company
  title: ''
  type: About
  url: https://vestaron.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://vestaron.com/overview/
- group: other
  title: ''
  type: Technology
  url: https://vestaron.com/science/
- group: company
  title: ''
  type: News
  url: https://vestaron.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://vestaron.com/feed/
- group: other
  title: ''
  type: Resources
  url: https://vestaron.com/resources/
- group: other
  title: ''
  type: Downloads
  url: https://vestaron.com/downloads/
- group: other
  title: ''
  type: Sustainability
  url: https://vestaron.com/socialresponsibility/
- group: operate
  title: ''
  type: Support
  url: https://vestaron.com/contact/
- group: operate
  title: ''
  type: Contact
  url: https://vestaron.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vestaron.com/legal/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vestaron.com/legal/privacy-statement/
- group: commercial
  title: ''
  type: Legal
  url: https://vestaron.com/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vestaron-corporation
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@vestaroncropprotection
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/vestaron_stock/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/vestaron-content-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vestaron-content-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vestaron-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/vestaron-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vestaron-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vestaron-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vestaron-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vestaron-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vestaron-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vestaron-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/vestaron-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vestaron-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vestaron-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vestaron-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vestaron-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vestaron-llms.txt
created: '2026-08-05'
description: Vestaron is an agricultural biotechnology company founded in 2005 and headquartered in Kalamazoo, Michigan, that develops peptide-based bioinsecticides derived from the venom of spiders and other venomous species. Its peptides deliver insecticidal modes of action that had never before been used for insect control — SPEAR, the first commercialised active ingredient, introduced IRAC Group 32, the first new neuromuscular mode of action since the diamides — and are effective on lepidopteran and sucking pests while remaining gentle on pollinators and beneficial insects. The commercial portfolio is SPEAR LEP, SPEAR RC, SPEAR T, BASIN FLEX, LEPROTEC and LEPROTEC WG, manufactured in partnership with ADM. The company has won the Crop Science Award and an EPA Green Chemistry Challenge award, and in 2024 became the first agriculture and food company inducted into the Global CleanTech 100 Hall of Fame. Vestaron publishes no developer program, no product API and no API documentation. The
  only machine-readable surfaces on vestaron.com are the WordPress REST content API (wp/v2), which is anonymously readable and serves the corporate newsroom, product and company pages and media library, and an OAuth-gated Model Context Protocol endpoint advertised through RFC 8414 and RFC 9728 metadata.
image: https://vestaron.com/wp-content/uploads/Logo_sep_23.png
layout: provider
mcp_servers:
- description: ''
  name: vestaron-mcp.yml
  slug: vestaron-mcpyml
modified: '2026-08-05'
name: Vestaron
nav: Providers
network: true
overview: 'Vestaron publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, Media API, and 6 more. Tagged areas include Company, Agriculture, AgTech, Biotechnology, and Crop Protection.


  Vestaron''s developer surface includes product news, support, legal docs, YouTube channel, authentication, code examples, and 28 more developer resources.'
random_paper: 70
scopes:
- name: Vestaron Scopes
  scope_count: 1
  slug: vestaron-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 27.9
  delta: -0.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 14.6
    developer_ergonomics: 25.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Vestaron Authentication
  slug: vestaron-authentication
  summary_line: none/http/oauth2 · 3 schemes
- kind: domain-security
  name: Vestaron Domain Security
  slug: vestaron-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vestaron
tags:
- Company
- Agriculture
- AgTech
- Biotechnology
- Crop Protection
- Bioinsecticides
- Peptides
- Biologicals
- Sustainability
- Pollinator Safety
- Life Sciences
- Content
website: https://vestaron.com/
---
