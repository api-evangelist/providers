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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Group14 Technologies Agentic Access
  operation_count: 1
  slug: group14-technologies-agentic-access
  summary_line: 1 operation
api_count: 11
apis:
- description: A WordPress MCP Adapter endpoint registered on group14.technology at /wp-json/mcp/mcp-adapter-default-server. The route is real — the namespace `mcp` is declared in the site REST index and the endpoin
  name: Group14 Technologies MCP Server (gated)
  slug: group14-technologies-mcp-server
- description: Self-describing route, type and taxonomy metadata.
  name: Group14 Technologies Discovery API
  slug: group14-technologies-discovery-api
- description: Open roles published on group14.technology/careers.
  name: Group14 Technologies Job Openings API
  slug: group14-technologies-job-openings-api
- description: Group14 manufacturing sites and offices as structured records.
  name: Group14 Technologies Locations API
  slug: group14-technologies-locations-api
- description: WordPress media attachments — photography, press assets and their generated size variants.
  name: Group14 Technologies Media API
  slug: group14-technologies-media-api
- description: Static marketing, corporate and policy pages of group14.technology.
  name: Group14 Technologies Pages API
  slug: group14-technologies-pages-api
- description: The WordPress post archive (Group14 publishes editorial content mainly as resources, not posts).
  name: Group14 Technologies Posts API
  slug: group14-technologies-posts-api
- description: Press releases, news, blog posts and whitepapers published by Group14 Technologies.
  name: Group14 Technologies Resources API
  slug: group14-technologies-resources-api
- description: Cross-content search over every public content type.
  name: Group14 Technologies Search API
  slug: group14-technologies-search-api
- description: The job-department and job-location vocabularies used to classify roles.
  name: Group14 Technologies Taxonomy API
  slug: group14-technologies-taxonomy-api
- description: The site-specific video custom post type.
  name: Group14 Technologies Video API
  slug: group14-technologies-video-api
artifact_total: 17
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/group14-technologies-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/group14-technologies-resources-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/group14-technologies-content-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/group14-technologies-careers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/group14-technologies-locations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/group14-technologies-media-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/group14-technologies-search-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/group14-technologies-discovery-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://group14.technology/
- group: company
  title: ''
  type: About
  url: https://group14.technology/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://group14.technology/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://group14.technology/careers/
- group: company
  title: ''
  type: Blog
  url: https://group14.technology/resource-category/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://group14.technology/feed/
- group: company
  title: ''
  type: Press
  url: https://group14.technology/resource-category/press-releases/
- group: company
  title: ''
  type: News
  url: https://group14.technology/resource-category/news/
- group: other
  title: ''
  type: Whitepapers
  url: https://group14.technology/resource-category/whitepapers/
- group: other
  title: ''
  type: Products
  url: https://group14.technology/our-technology/
- group: other
  title: ''
  type: Manufacturing
  url: https://group14.technology/manufacturing/
- group: other
  title: ''
  type: Patents
  url: https://group14.technology/patents/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://group14.technology/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://group14.technology/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/group14-technologies
- group: other
  title: ''
  type: JobBoard
  url: https://job-boards.greenhouse.io/group14
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/group14-technologies_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/group14-technologies-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/group14-technologies-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/group14-technologies-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/group14-technologies-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/group14-technologies-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/group14-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/group14-technologies-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/group14-technologies-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/group14-technologies-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/group14-technologies-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/group14-technologies-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/group14-technologies-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/group14-technologies-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/group14-technologies-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/group14-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/group14-technologies-domain-security.yml
created: '2026-08-22'
description: 'Group14 Technologies is a battery materials manufacturer headquartered in Woodinville, Washington, founded in 2015 by Rick Luebbe, Dr. Rick Costantino and Aaron Feaver as a spinout of EnerG2. It produces SCC55, a silicon-carbon composite anode material that replaces graphite in lithium-ion cells to raise energy density, shorten charge times and extend cycle life for electric mobility, grid-scale storage and consumer electronics. Manufacturing runs through its BAM (battery active materials) factory network — BAM-1 and the silane factory in Washington State, BAM-2 in Moses Lake, and BAM-3 operated by the SK materials Group14 joint venture in Sangju, South Korea — and the company reports more than 170 issued patents worldwide. Group14 is a materials manufacturer rather than a software vendor: it publishes no developer program, no API documentation, no SDKs and no pricing for machine access. The only machine-readable interfaces it exposes are the anonymously readable WordPress
  REST content API behind group14.technology, captured here for discovery purposes and read-only without credentials, and a WordPress MCP Adapter endpoint on the same host that is registered but authentication-gated.'
image: https://group14.technology/wp-content/uploads/2025/10/cropped-group14_favicon.jpg
layout: provider
mcp_servers:
- description: Group14 Technologies does not advertise, document or market an MCP server. What exists is a WordPress MCP Adapter endpoint registered on the corporate website. The `mcp` namespace is declared in the s
  name: Group14 Technologies MCP Server
  slug: group14-technologies-mcp-server
modified: '2026-08-22'
name: Group14 Technologies
nav: Providers
network: true
overview: 'Group14 Technologies publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Job Openings API, Locations API, and 7 more. Tagged areas include Company, Materials Science, Battery Materials, Silicon Anode, and Lithium-Ion.


  Group14 Technologies'' developer surface includes engineering blog, product news, authentication, code examples, and 38 more developer resources.'
plans:
- name: Group14 Technologies Plans Pricing
  plan_count: 0
  slug: group14-technologies-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Group14 Technologies Rate Limits
  slug: group14-technologies-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 56.0
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Group14 Technologies Authentication
  slug: group14-technologies-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Group14 Technologies Domain Security
  slug: group14-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: group14-technologies
tags:
- Company
- Materials Science
- Battery Materials
- Silicon Anode
- Lithium-Ion
- Energy Storage
- Electric Vehicles
- Advanced Manufacturing
- Clean Energy
- Content
website: https://group14.technology/
---
