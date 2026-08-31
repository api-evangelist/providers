---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Accelsius Agentic Access
  operation_count: 23
  slug: accelsius-agentic-access
  summary_line: 23 operations
api_count: 1
apis:
- description: The public WordPress REST collection behind https://accelsius.com/resources/ - the Accelsius resource library, holding 154 published items at time of capture across eight content classes carried as ca
  name: Accelsius Resources Content API
  slug: content
- description: The `news` WordPress custom post type Accelsius registered for curated third-party press coverage, surfaced at https://accelsius.com/in-the-news/ and served from accelsius.com/wp-json/wp/v2/news. Eigh
  name: Accelsius News API
  slug: news
- description: Public read access to the 30 static marketing, product, company and legal pages of accelsius.com via the WordPress REST API - the NeuCool IR150 and MR250 product pages, the Thermal Simulation Rack and
  name: Accelsius Pages API
  slug: pages
- description: Public read access to the 903-item accelsius.com media library - NeuCool product renders and photography, thermal diagrams, partner and customer logos, and the PDF white papers, studies and infographi
  name: Accelsius Media API
  slug: media
- description: Site-wide search across every searchable object on accelsius.com - resource-library posts, static pages and news items, 192 objects at time of capture. Returns a lightweight uniform record (id, title,
  name: Accelsius Search API
  slug: search
- description: The WordPress REST route-discovery documents served at accelsius.com/wp-json/ and accelsius.com/wp-json/wp/v2 - the only machine-readable API description documents Accelsius serves. They enumerate 387
  name: Accelsius API Discovery
  slug: discovery
- description: Content-class terms in the category taxonomy.
  name: Accelsius Categories API
  slug: accelsius-categories-api
- description: HappyFiles folders organising the media library.
  name: Accelsius Media Folders API
  slug: accelsius-media-folders-api
- description: Post types, taxonomies and publication statuses registered on the site.
  name: Accelsius Registry API
  slug: accelsius-registry-api
- description: Topic terms in the post_tag taxonomy.
  name: Accelsius Tags API
  slug: accelsius-tags-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Accelsius Taxonomy Categories API
  slug: open-accelsius-categories-api
- collection_type: open
  name: Accelsius Resources Content API
  slug: open-accelsius-content-api
- collection_type: open
  name: Accelsius Discovery API
  slug: open-accelsius-discovery-api
- collection_type: open
  name: Accelsius Media API
  slug: open-accelsius-media-api
- collection_type: open
  name: Accelsius Taxonomy Media Folders API
  slug: open-accelsius-media-folders-api
- collection_type: open
  name: Accelsius News API
  slug: open-accelsius-news-api
- collection_type: open
  name: Accelsius Pages API
  slug: open-accelsius-pages-api
- collection_type: open
  name: Accelsius Taxonomy Registry API
  slug: open-accelsius-registry-api
- collection_type: open
  name: Accelsius Search API
  slug: open-accelsius-search-api
- collection_type: open
  name: Accelsius Taxonomy Tags API
  slug: open-accelsius-tags-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/accelsius-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accelsius-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accelsius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accelsius.com/
- group: company
  title: ''
  type: About
  url: https://accelsius.com/company/
- group: operate
  title: ''
  type: Contact
  url: https://accelsius.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://accelsius.com/customer-support/
- group: operate
  title: ''
  type: FAQ
  url: https://accelsius.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://accelsius.com/resources/
- group: company
  title: ''
  type: BlogFeeds
  url: https://accelsius.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://accelsius.com/in-the-news/
- group: other
  title: ''
  type: WhitePapers
  url: https://accelsius.com/papers-studies/
- group: company
  title: ''
  type: Partners
  url: https://accelsius.com/our-partners/
- group: company
  title: ''
  type: Careers
  url: https://accelsius.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accelsius
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accelsius.com/privacy-policy/
- group: other
  title: ''
  type: Sitemap
  url: https://accelsius.com/sitemap_index.xml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accelsius-agentic-access.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accelsius-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accelsius-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accelsius-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accelsius-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accelsius-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accelsius-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accelsius-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/accelsius-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/accelsius-examples.yml
- group: other
  title: ''
  type: Robots
  url: well-known/accelsius-robots.txt
created: '2026-08-06'
description: 'Accelsius LLC is an Austin, Texas thermal-management company founded in 2022 by Innventure to commercialize two-phase, direct-to-chip liquid cooling for AI, HPC and mission-critical data centers. Its NeuCool platform circulates a non-conductive dielectric refrigerant through cold plates mounted directly on CPUs and GPUs, removing heat by evaporation rather than by bringing water into the IT rack, and supports 4,500W+ per socket and rack densities up to 250kW. The product line includes the IR150 in-rack CDU, the MR250 medium-rack CDU, the NeuCool Thermal Simulation Rack and Liquid Simulation System used for evaluation and deployment planning, and multi-GPU cold plate assemblies, backed by professional services spanning system architecture, integration, deployment and maintenance. Accelsius is a hardware manufacturer, not a software or data company: it publishes no developer program, product API, SDK or machine-readable product specification. The only machine-readable interface
  on its public surface is the WordPress core REST API behind accelsius.com, which serves the company''s own blog, news, white-paper, case-study, podcast and video content anonymously and read-only.'
image: https://accelsius.com/wp-content/uploads/Accelsius_Logo_Footer-1.svg
layout: provider
mcp_servers:
- description: ''
  name: Accelsius MCP Server
  slug: accelsius-mcp-server
modified: '2026-08-06'
name: Accelsius
nav: Providers
network: true
overview: 'Accelsius publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Resources Content API, News API, Pages API, and 7 more. Tagged areas include Company, Data Centers, Liquid Cooling, Thermal Management, and Direct-to-Chip Cooling.


  Accelsius'' developer surface includes authentication, support, FAQ, engineering blog, code examples, and 24 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 58.2
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accelsius/refs/heads/main/screenshots/accelsius-2026-08-07T160754.png
security:
- kind: authentication
  name: Accelsius Authentication
  slug: accelsius-authentication
  summary_line: none/http/cookie · 3 schemes
- kind: domain-security
  name: Accelsius Domain Security
  slug: accelsius-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accelsius
tags:
- Company
- Data Centers
- Liquid Cooling
- Thermal Management
- Direct-to-Chip Cooling
- Two-Phase Cooling
- Artificial Intelligence Infrastructure
- High Performance Computing
- Hardware
- Manufacturing
- Content
- WordPress
website: https://accelsius.com/
---
