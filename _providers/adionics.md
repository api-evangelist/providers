---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-10-03'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Adionics website at www.adionics.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: Adionics Website (WordPress REST)
  slug: adionics-com-website-wordpress-rest
- description: A live Model Context Protocol endpoint registered on the adionics.com WordPress install by the WordPress MCP Adapter, at https://www.adionics.com/wp-json/mcp/mcp-adapter-default-server. The route is s
  name: Adionics MCP Server
  slug: adionics-mcp-server
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/security/adionics-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/authentication/adionics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adionics-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/errors/adionics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adionics-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/conventions/adionics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adionics-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/data-model/adionics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adionics-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/conformance/adionics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adionics-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/lifecycle/adionics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adionics-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/rate-limits/adionics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adionics-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/plans/adionics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adionics-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/packages/adionics-packages.yml
  title: ''
  type: Packages
  url: packages/adionics-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/llms/adionics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adionics-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/mcp/adionics-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adionics-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/mcp/adionics-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adionics-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adionics/refs/heads/main/examples/adionics-examples.yml
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
overview: 'Adionics publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cleantech, Lithium, Direct Lithium Extraction, and Mining.


  Adionics'' developer surface includes engineering blog, authentication, code examples, and 24 more developer resources.'
plans:
- name: Adionics Plans Pricing
  plan_count: 0
  slug: adionics-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Adionics Rate Limits
  slug: adionics-rate-limits
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 60.0
    operational_transparency: 0.0
  previous_composite: 18.8
  provenance:
    conformance: derived
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
website: https://www.adionics.com/
---
