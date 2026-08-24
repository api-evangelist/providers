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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-08-24'
api_count: 11
apis:
- description: The akismet/v1 API from CaaMTech — 7 operation(s) for akismet/v1.
  name: CaaMTech Akismet/v1 API
  slug: caamtech-akismet-v1-api
- description: The mcp API from CaaMTech — 2 operation(s) for mcp.
  name: CaaMTech MCP API
  slug: caamtech-mcp-api
- description: The objectcache/v1 API from CaaMTech — 5 operation(s) for objectcache/v1.
  name: CaaMTech Objectcache/v1 API
  slug: caamtech-objectcache-v1-api
- description: The oembed/1.0 API from CaaMTech — 3 operation(s) for oembed/1.0.
  name: CaaMTech Oembed/1.0 API
  slug: caamtech-oembed-1-0-api
- description: The regenerate-thumbnails/v1 API from CaaMTech — 4 operation(s) for regenerate-thumbnails/v1.
  name: CaaMTech Regenerate Thumbnails/v1 API
  slug: caamtech-regenerate-thumbnails-v1-api
- description: The root API from CaaMTech — 2 operation(s) for root.
  name: CaaMTech Root API
  slug: caamtech-root-api
- description: The wp-abilities/v1 API from CaaMTech — 6 operation(s) for wp-abilities/v1.
  name: CaaMTech Wp Abilities/v1 API
  slug: caamtech-wp-abilities-v1-api
- description: The wp-block-editor/v1 API from CaaMTech — 4 operation(s) for wp-block-editor/v1.
  name: CaaMTech Wp Block Editor/v1 API
  slug: caamtech-wp-block-editor-v1-api
- description: The wp-site-health/v1 API from CaaMTech — 8 operation(s) for wp-site-health/v1.
  name: CaaMTech Wp Site Health/v1 API
  slug: caamtech-wp-site-health-v1-api
- description: The wp/v2 API from CaaMTech — 106 operation(s) for wp/v2.
  name: CaaMTech Wp/v2 API
  slug: caamtech-wp-v2-api
- description: The wpforms/v1 API from CaaMTech — 8 operation(s) for wpforms/v1.
  name: CaaMTech Wpforms/v1 API
  slug: caamtech-wpforms-v1-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CaaMTech WordPress REST Akismet/v1 API
  slug: open-caamtech-akismet-v1-api
- collection_type: open
  name: CaaMTech WordPress REST MCP API
  slug: open-caamtech-mcp-api
- collection_type: open
  name: CaaMTech WordPress REST Objectcache/v1 API
  slug: open-caamtech-objectcache-v1-api
- collection_type: open
  name: CaaMTech WordPress REST Oembed/1.0 API
  slug: open-caamtech-oembed-1-0-api
- collection_type: open
  name: CaaMTech WordPress REST Regenerate Thumbnails/v1 API
  slug: open-caamtech-regenerate-thumbnails-v1-api
- collection_type: open
  name: CaaMTech WordPress REST Root API
  slug: open-caamtech-root-api
- collection_type: open
  name: API Collection
  slug: open-caamtech-wordpress-rest-routes-original
- collection_type: open
  name: CaaMTech WordPress REST Wp Abilities/v1 API
  slug: open-caamtech-wp-abilities-v1-api
- collection_type: open
  name: CaaMTech WordPress REST Wp Block Editor/v1 API
  slug: open-caamtech-wp-block-editor-v1-api
- collection_type: open
  name: CaaMTech WordPress REST Wp Site Health/v1 API
  slug: open-caamtech-wp-site-health-v1-api
- collection_type: open
  name: CaaMTech WordPress REST Wp/v2 API
  slug: open-caamtech-wp-v2-api
- collection_type: open
  name: CaaMTech WordPress REST Wpforms/v1 API
  slug: open-caamtech-wpforms-v1-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/caamtech-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/caamtech-wordpress-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://caam.tech/
- group: company
  title: ''
  type: Blog
  url: https://caam.tech/updates/
- group: company
  title: ''
  type: BlogRSS
  url: https://caam.tech/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caamtech
- group: auth
  title: ''
  type: Authentication
  url: authentication/caamtech-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caamtech-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caamtech-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caamtech-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caamtech-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/caamtech-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caamtech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caamtech-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: CaaMTech is a pharmaceutical drug discovery company in Issaquah, Washington, founded by Dr. Andrew Chadeayne, engineering next-generation psychedelic-inspired small-molecule therapeutics for mental health conditions. It synthesizes and characterizes novel tryptamines, screens natural and synthetic compounds for safety and efficacy, publishes fundamental crystallographic and pharmacological research, and builds a patent portfolio around the results. CaaMTech operates no developer program and publishes no product API; the only machine-readable surface on caam.tech is the standard WordPress REST API that serves the company site, which does make its research updates, pages and media programmatically readable without credentials, alongside an authenticated WordPress MCP adapter endpoint.
image: https://caam.tech/wp-content/uploads/2019/12/cropped-caamtech-logo-on-green-2400-square.png
layout: provider
mcp_servers:
- description: ''
  name: CaaMTech MCP Server
  slug: caamtech-mcp-server
modified: '2026-08-08'
name: CaaMTech
nav: Providers
network: true
overview: 'CaaMTech publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Akismet/v1 API, MCP API, Objectcache/v1 API, and 8 more. Tagged areas include Company, Pharmaceuticals, Life Sciences, Drug Discovery, and Biotechnology.


  CaaMTech''s developer surface includes engineering blog, authentication, and 13 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 16.3
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Caamtech Authentication
  slug: caamtech-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Caamtech Domain Security
  slug: caamtech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caamtech
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Biotechnology
- Chemistry
- Mental Health
- Research
- Psychedelics
- WordPress
website: https://caam.tech/
---
