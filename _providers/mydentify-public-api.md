---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Mydentify Public Api Agentic Access
  operation_count: 14
  slug: mydentify-public-api-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- description: The Directories API from Mydentify Public API — 2 operation(s) for directories.
  name: Mydentify Public API Directories API
  slug: mydentify-public-api-directories-api
- description: The Directories.json API from Mydentify Public API — 1 operation(s) for directories.json.
  name: Mydentify Public API Directories.json API
  slug: mydentify-public-api-directories-json-api
- description: The Imports API from Mydentify Public API — 8 operation(s) for imports.
  name: Mydentify Public API Imports API
  slug: mydentify-public-api-imports-api
- description: The Leaderboards API from Mydentify Public API — 1 operation(s) for leaderboards.
  name: Mydentify Public API Leaderboards API
  slug: mydentify-public-api-leaderboards-api
- description: The Leaderboards.json API from Mydentify Public API — 1 operation(s) for leaderboards.json.
  name: Mydentify Public API Leaderboards.json API
  slug: mydentify-public-api-leaderboards-json-api
- description: The Product Categories.json API from Mydentify Public API — 1 operation(s) for product categories.json.
  name: Mydentify Public API Product Categories.json API
  slug: mydentify-public-api-product-categories-json-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mydentify Public Directories API
  slug: open-mydentify-public-api-directories-api
- collection_type: open
  name: Mydentify Public Directories.json API
  slug: open-mydentify-public-api-directories-json-api
- collection_type: open
  name: Mydentify Public Imports API
  slug: open-mydentify-public-api-imports-api
- collection_type: open
  name: Mydentify Public Leaderboards API
  slug: open-mydentify-public-api-leaderboards-api
- collection_type: open
  name: Mydentify Public Leaderboards.json API
  slug: open-mydentify-public-api-leaderboards-json-api
- collection_type: open
  name: Mydentify Public Product Categories.json API
  slug: open-mydentify-public-api-product-categories-json-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mydentify-public-api-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mydentify-public-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mydentify-public-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mydentify-public-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mydentify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mydentify.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://mydentify.com/submit.md
- group: start
  title: ''
  type: GettingStarted
  url: https://mydentify.com/submit.md
- group: operate
  title: ''
  type: StatusPage
  url: https://mydentify.com/api/health
- group: commercial
  title: ''
  type: Pricing
  url: https://mydentify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mydentify.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mydentify.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mydentify.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@mydentify.com
- group: company
  title: ''
  type: Blog
  url: https://mydentify.com/articles
- group: company
  title: ''
  type: BlogFeeds
  url: https://mydentify.com/articles/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mitdralla
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mydentify-public-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/mydentify-public-api-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: https://mydentify.com/robots.txt
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: well-known/mydentify-public-api-ai.txt
- group: other
  title: ''
  type: APIsJson
  url: https://mydentify.com/apis.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mydentify-public-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mydentify-public-api-conformance.yml
created: '2026-07-27'
description: 'Public, keyless REST API for Mydentify — a permanent product directory with weekly community-signaled product leaderboards. The OpenAPI 3.1 contract covers intent-based product discovery, the curated startup/SaaS/AI directory catalog with Directory Score and link-type metadata, a portable product-category taxonomy mapped to G2/Capterra/Product Hunt, and a diagnostic-first product submission workflow: a non-destructive dry run, an idempotency-keyed durable import with a resumable SSE event stream, an AI-readiness rubric report, duplicate resolution, editorial manual review and backlink-verified publication. Mydentify also ships an unusually complete agent-native discovery surface — an APIs.json index, an RFC 9727 API Catalog, site-wide and per-resource llms.txt, an ai.txt usage policy, robots.txt Content Signals, and three published agentskills.io skills.'
examples:
- key_count: 17
  name: Mydentify Public Api Directories Response
  slug: mydentify-public-api-directories-response
- key_count: 5
  name: Mydentify Public Api Health Response
  slug: mydentify-public-api-health-response
- key_count: 7
  name: Mydentify Public Api Imports Dry Run Response
  slug: mydentify-public-api-imports-dry-run-response
- key_count: 3
  name: Mydentify Public Api Product Categories Response
  slug: mydentify-public-api-product-categories-response
image: https://mydentify.com/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Mydentify Public API MCP Server
  slug: mydentify-public-api-mcp-server
modified: '2026-08-09'
name: Mydentify Public API
nav: Providers
network: true
overview: 'Mydentify Public API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Directories API, Directories.json API, Imports API, and 3 more. Tagged areas include product discovery, startup directories, leaderboards, research, and Software-as-a-Service.


  Mydentify Public API''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, engineering blog, and 19 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 45.2
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Mydentify Public Api Authentication
  slug: mydentify-public-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mydentify Public Api Domain Security
  slug: mydentify-public-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mydentify-public-api
tags:
- product discovery
- startup directories
- leaderboards
- research
- Software-as-a-Service
- Developer Tools
- agent-native
- llms-txt
- agent skills
- Directories
website: https://mydentify.com
---
