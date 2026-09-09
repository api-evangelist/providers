---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.7
  scored_at: '2026-09-08'
api_count: 7
apis:
- baseURL: https://www.adionics.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Adionics news and press archive — company milestones, partnership announcements, pilot-plant results and conference appearances — via the WordPress core REST
  name: Adionics Posts API
  slug: adionics-posts-api
- baseURL: https://www.adionics.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static pages of adionics.com — Our Technology, Our Offer, Markets, Applications, Expertise, Adionics' History, Management Team, Careers, Contact and the lega
  name: Adionics Pages API
  slug: adionics-pages-api
- baseURL: https://www.adionics.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the adionics.com media library — pilot and plant photography, process diagrams, downloadable brochures and press assets, each with its generated size variants an
  name: Adionics Media API
  slug: adionics-media-api
- baseURL: https://www.adionics.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the classification terms behind adionics.com — the four post categories used across the English and Spanish news trees, the registered (and currently unused) pos
  name: Adionics Taxonomy API
  slug: adionics-taxonomy-api
- baseURL: https://www.adionics.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated cross-content search over adionics.com — posts and pages together — returning lightweight id / title / url / type / subtype records. Verified live at 267 searchable objects on '
  name: Adionics Search API
  slug: adionics-search-api
- baseURL: https://www.adionics.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated discovery metadata for adionics.com — the self-describing REST route index (370 routes across 23 namespaces at capture), the registered content types and publication statuses, '
  name: Adionics Discovery API
  slug: adionics-discovery-api
- description: A live Model Context Protocol endpoint registered on the adionics.com WordPress install by the WordPress MCP Adapter, at https://www.adionics.com/wp-json/mcp/mcp-adapter-default-server. The route is s
  name: Adionics MCP Server
  slug: adionics-mcp-server
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adionics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adionics.com/
- group: company
  title: ''
  type: About
  url: https://www.adionics.com/in-few-words/
- group: company
  title: ''
  type: Blog
  url: https://www.adionics.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.adionics.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.adionics.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.adionics.com/in-few-words/careers/
- group: other
  title: ''
  type: Products
  url: https://www.adionics.com/our-offer/
- group: other
  title: ''
  type: Technology
  url: https://www.adionics.com/our-technology/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adionics.com/credits-terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adionics.com/politique-de-confidentialite/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adionics/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Adionics
- group: auth
  title: ''
  type: Authentication
  url: authentication/adionics-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adionics-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adionics-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adionics-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adionics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adionics-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adionics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adionics-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/adionics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adionics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adionics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/adionics-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/adionics-examples.yml
created: '2026-09-07'
description: Adionics is a French cleantech company founded in 2012 in Paris by Guillaume de Souza, out of research into liquid-liquid salt extraction started in 2007. It develops and licenses a patented Direct Lithium Extraction (DLE) process built on Flionex, a proprietary, thermally regenerated and highly selective liquid salt absorbent that captures lithium salts from brine at ambient temperature and releases them at higher temperature in a closed loop, with no traditional reagents and more than 90% less water than evaporation ponds. The company sells a staged engagement to mining operators — a proprietary modeling study, a lab-scale bench test, an on-site pilot plant, and basic engineering plus commissioning support for a commercial plant — targeting lithium-rich salars, geothermal brines, oil-and-gas produced water, industrial effluents and battery recycling streams. It has run 1,500 hours of continuous lithium extraction in the Salar de Atacama, opened a pilot test centre in Salta
  Province, Argentina, and raised roughly $40M across four rounds. Adionics is a process-technology and engineering company, not a software vendor, and publishes no developer portal, no product API, no SDKs and no OpenAPI. The only machine-readable interface it exposes is the WordPress REST content API behind www.adionics.com, which is anonymously readable, read-only for the public, and captured here for discovery.
image: https://www.adionics.com/wp-content/uploads/2022/05/clean-lithium-adionics-1024x393.jpg
layout: provider
mcp_servers:
- description: ''
  name: Adionics MCP Server
  slug: adionics-mcp-server
modified: '2026-09-07'
name: Adionics
nav: Providers
network: true
overview: 'Adionics publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 3 more. Tagged areas include Company, Cleantech, Lithium, Direct Lithium Extraction, and Mining.


  Adionics'' developer surface includes engineering blog, authentication, code examples, and 24 more developer resources.'
plans:
- name: Adionics Plans Pricing
  plan_count: 0
  slug: adionics-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Adionics Rate Limits
  slug: adionics-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 51.8
    developer_ergonomics: 16.1
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Adionics Authentication
  slug: adionics-authentication
  summary_line: none/http · 1 scheme
- kind: domain-security
  name: Adionics Domain Security
  slug: adionics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: adionics
tags:
- Company
- Cleantech
- Lithium
- Direct Lithium Extraction
- Mining
- Battery Materials
- Water Treatment
- Desalination
- Geothermal
- Industrial Process Technology
- Sustainability
- Content
website: https://www.adionics.com/
---
