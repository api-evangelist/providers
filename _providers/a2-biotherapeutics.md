---
agent_readiness:
  band: agent-ready
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
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The live WordPress REST API served by the A2 Biotherapeutics corporate website. Route discovery is anonymous and advertises 298 routes across 16 namespaces; published content under wp/v2 (posts, pages
  name: A2 Biotherapeutics WordPress REST API
  slug: a2-biotherapeutics-wordpress-rest-api
artifact_total: 5
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
  url: openapi/a2-biotherapeutics-wp-rest-openapi.yml
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
overview: 'A2 Biotherapeutics publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Immuno-Oncology.


  A2 Biotherapeutics'' developer surface includes engineering blog, authentication, and 25 more developer resources.'
random_paper: 108
scopes:
- name: A2 Biotherapeutics Scopes
  scope_count: 1
  slug: a2-biotherapeutics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.7
    developer_ergonomics: 23.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 39.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
