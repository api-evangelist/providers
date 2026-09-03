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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lendis Agentic Access
  operation_count: 28
  slug: lendis-agentic-access
  summary_line: 28 operations
api_count: 10
apis:
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Customer case studies
  name: Lendis case-study API
  slug: lendis-case-study-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Route, type and taxonomy discovery plus site-wide search
  name: Lendis discovery API
  slug: lendis-discovery-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Kataloge (downloadable product catalogs)
  name: Lendis kataloge API
  slug: lendis-kataloge-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Medien (media library items)
  name: Lendis media API
  slug: lendis-media-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Seiten (site pages)
  name: Lendis pages API
  slug: lendis-pages-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Beitraege (blog posts from the Lendis Magazin)
  name: Lendis posts API
  slug: lendis-posts-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Ratgeber (buyer's guides)
  name: Lendis ratgeber API
  slug: lendis-ratgeber-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: 'Taxonomy terms: categories, tags, wiki letters, Ratgeber categories'
  name: Lendis taxonomies API
  slug: lendis-taxonomies-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Customer testimonials
  name: Lendis testimonial API
  slug: lendis-testimonial-api
- baseURL: https://www.lendis.io/wp-json
  baseurl_source: declared
  description: Wiki glossary entries
  name: Lendis wiki API
  slug: lendis-wiki-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study API
  slug: open-lendis-case-study-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study discovery API
  slug: open-lendis-discovery-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study kataloge API
  slug: open-lendis-kataloge-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study media API
  slug: open-lendis-media-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study pages API
  slug: open-lendis-pages-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study posts API
  slug: open-lendis-posts-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study ratgeber API
  slug: open-lendis-ratgeber-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study taxonomies API
  slug: open-lendis-taxonomies-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study testimonial API
  slug: open-lendis-testimonial-api
- collection_type: open
  name: Lendis Content API (WordPress REST) case-study wiki API
  slug: open-lendis-wiki-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lendis-harvest-catalog.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lendis-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lendis-content-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lendis-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.lendis.io
- group: company
  title: ''
  type: Blog
  url: https://www.lendis.io/magazin/
- group: operate
  title: ''
  type: Support
  url: https://www.lendis.io/kontakt/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lendis.io/faq/
- group: start
  title: ''
  type: Login
  url: https://app.lendis.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lendis.io/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lendis.io/datenschutz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lendis-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lendis/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@lendis_io
- group: company
  title: ''
  type: Careers
  url: https://www.lendis.io/karriere/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lendis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lendis-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/lendis-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lendis-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendis-domain-security.yml
created: '2026-07-17'
description: Lendis GmbH is a Berlin-based B2B technology company, founded in 2018, that rents IT hardware to German small and mid-sized businesses under a Device-as-a-Service (DaaS) model. Lendis bundles hardware procurement, configuration and staging, delivery logistics, financing, IT support, lifecycle management and device offboarding into a single monthly rental rate, and manages the whole estate through LendisOS, a web platform covering a self-service shop, order tracking, asset inventory and contract management. The company targets organisations of roughly 50 to 500 employees that want to avoid tying up capital in laptops, smartphones, monitors and accessories. Lendis publishes no public developer program; its commercial platform runs on a private AWS API Gateway at api.lendis.io. Its marketing site does expose a public read-only WordPress REST content API, and Lendis publishes a machine-readable llms.txt for AI agents.
image: https://res.cloudinary.com/lendis-gmbh/images/f_svg,q_auto/fl_sanitize/v1774942862/www.lendis.io/lendis-logo-it/lendis-logo-it.svg
layout: provider
mcp_servers:
- description: ''
  name: Lendis MCP Server
  slug: lendis-mcp-server
modified: '2026-07-19'
name: Lendis
nav: Providers
network: true
overview: 'Lendis publishes 10 APIs on the [APIs.io](https://apis.io/) network, including case-study API, discovery API, kataloge API, and 7 more. Tagged areas include Company, Ai Enterprise Software, Device As A Service, IT Hardware, and Leasing.


  Lendis'' developer surface includes engineering blog, support, YouTube channel, and 17 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 13.7
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 22.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lendis/refs/heads/main/screenshots/lendis-2026-07-25T224902.png
security:
- kind: authentication
  name: Lendis Authentication
  slug: lendis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lendis Domain Security
  slug: lendis-domain-security
  summary_line: TLSv1.3
slug: lendis
tags:
- Company
- Ai Enterprise Software
- Device As A Service
- IT Hardware
- Leasing
- Asset Management
- Workplace Technology
- Procurement
- Germany
- Software-as-a-Service
website: https://www.lendis.io
---
