---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.6
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Model Context Protocol servers exposed by the WordPress MCP adapter. Both servers require OAuth 2.1 bearer auth (observed HTTP 401 anonymously).
  name: A2 Biotherapeutics MCP API
  slug: a2-biotherapeutics-mcp-api
- description: oEmbed discovery and proxy endpoints.
  name: A2 Biotherapeutics Oembed/1.0 API
  slug: a2-biotherapeutics-oembed-1-0-api
- description: REST API index / namespace discovery.
  name: A2 Biotherapeutics Root API
  slug: a2-biotherapeutics-root-api
- description: WordPress Abilities API — registry of named abilities an agent may discover and run. Read access is capability-gated (observed HTTP 401 anonymously).
  name: A2 Biotherapeutics Wp Abilities/v1 API
  slug: a2-biotherapeutics-wp-abilities-v1-api
- description: WordPress core content API (posts, pages, media, taxonomies, users, settings).
  name: A2 Biotherapeutics Wp/v2 API
  slug: a2-biotherapeutics-wp-v2-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: A2 Biotherapeutics WordPress REST MCP API
  slug: open-a2-biotherapeutics-mcp-api
- collection_type: open
  name: A2 Biotherapeutics WordPress REST Oembed/1.0 API
  slug: open-a2-biotherapeutics-oembed-1-0-api
- collection_type: open
  name: A2 Biotherapeutics WordPress REST Root API
  slug: open-a2-biotherapeutics-root-api
- collection_type: open
  name: A2 Biotherapeutics WordPress REST Wp Abilities/v1 API
  slug: open-a2-biotherapeutics-wp-abilities-v1-api
- collection_type: open
  name: API Collection
  slug: open-a2-biotherapeutics-wp-rest-discovery-original
- collection_type: open
  name: A2 Biotherapeutics WordPress REST Wp/v2 API
  slug: open-a2-biotherapeutics-wp-v2-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.a2bio.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.a2bio.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://www.a2bio.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.a2bio.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.a2bio.com/careers/
- group: company
  title: ''
  type: Investors
  url: https://www.a2bio.com/about-us/investors/
- group: operate
  title: ''
  type: Contact
  url: https://www.a2bio.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.a2bio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.a2bio.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.a2bio.com/california-compliance/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/a2-biotherapeutics_stock/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/a2-biotherapeutics-wp-rest-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/a2-biotherapeutics-wp-rest-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/a2-biotherapeutics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/a2-biotherapeutics-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/a2-biotherapeutics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/a2-biotherapeutics-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/a2-biotherapeutics-robots.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/a2-biotherapeutics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/a2-biotherapeutics-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/a2-biotherapeutics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/a2-biotherapeutics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/a2-biotherapeutics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/a2-biotherapeutics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/a2-biotherapeutics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/a2-biotherapeutics-domain-security.yml
created: '2026-08-02'
description: A2 Biotherapeutics (A2 Bio) is a clinical-stage biotechnology company headquartered in Agoura Hills, California, founded in 2018 by Alexander Kamb, Michael Gallo and Paul Kang. It develops logic-gated cell therapies for solid tumors on its proprietary Tmod platform, a two-receptor activator/blocker design that lets an engineered T cell attack tumor cells which have lost an HLA allele while sparing normal cells that retain it. A2 Bio operates no developer API programme and publishes no product, clinical or research API. It is catalogued here because its corporate website runs a live WordPress REST API with 298 discoverable routes, and because that same install exposes two Model Context Protocol servers guarded by an OAuth 2.1 authorization server the host advertises through RFC 8414 and RFC 9728 metadata.
image: https://www.a2bio.com/wp-content/uploads/A2-Bio-Email-Logo-200-x-200.jpg
layout: provider
mcp_servers:
- description: ''
  name: a2-biotherapeutics-mcp.yml
  slug: a2-biotherapeutics-mcpyml
modified: '2026-08-02'
name: A2 Biotherapeutics
nav: Providers
network: true
overview: 'A2 Biotherapeutics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including MCP API, Oembed/1.0 API, Root API, and 2 more. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Immuno-Oncology.


  A2 Biotherapeutics'' developer surface includes engineering blog, authentication, and 25 more developer resources.'
random_paper: 18
scopes:
- name: A2 Biotherapeutics Scopes
  scope_count: 1
  slug: a2-biotherapeutics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 39.5
  delta: 1.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 16.7
    contract_quality: 57.4
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 38.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/a2-biotherapeutics/refs/heads/main/screenshots/a2-biotherapeutics-2026-08-07T160729.png
security:
- kind: authentication
  name: A2 Biotherapeutics Authentication
  slug: a2-biotherapeutics-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: A2 Biotherapeutics Domain Security
  slug: a2-biotherapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: a2-biotherapeutics
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Immuno-Oncology
- Oncology
- Pharmaceuticals
- Clinical Trials
- Healthcare
- Model Context Protocol
- WordPress
website: https://www.a2bio.com/
---
