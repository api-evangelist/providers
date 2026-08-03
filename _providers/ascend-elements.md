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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 354
  human_in_the_loop: 0
  name: Ascend Elements Agentic Access
  operation_count: 601
  slug: ascend-elements-agentic-access
  summary_line: 601 operations · 354 acting
api_count: 1
apis:
- description: The WordPress REST API surface published by Ascend Elements at ascendelements.com/wp-json — 362 routes across 20 namespaces. The anonymously readable core is the wp/v2 content surface (posts, pages, m
  name: Ascend Elements WordPress REST API
  slug: ascend-elements-wordpress-rest-api
artifact_total: 5
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ascend-elements-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ascend-elements-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ascendelements.com/
- group: company
  title: ''
  type: About
  url: https://ascendelements.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://ascendelements.com/products/
- group: other
  title: ''
  type: Services
  url: https://ascendelements.com/services/
- group: company
  title: ''
  type: Blog
  url: https://ascendelements.com/category/news/
- group: company
  title: ''
  type: Press
  url: https://ascendelements.com/category/coverage/
- group: company
  title: ''
  type: Careers
  url: https://ascendelements.com/careers/
- group: other
  title: ''
  type: Policies
  url: https://ascendelements.com/corporate-policies/
- group: commercial
  title: ''
  type: Privacy
  url: https://ascendelements.com/opt-out-preferences/
- group: operate
  title: ''
  type: ContactUs
  url: mailto:info@ascendelements.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/battery-resourcers
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ascendelements
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/@AscendElements
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ascend-elements_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ascend-elements-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ascend-elements-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ascend-elements-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ascend-elements-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ascend-elements-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ascend-elements-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ascend-elements-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ascend-elements-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ascend-elements-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ascend-elements-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ascend-elements-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Ascend Elements is a Westborough, Massachusetts battery materials company that manufactures engineered lithium-ion battery materials from valuable elements reclaimed from spent lithium-ion batteries and gigafactory manufacturing scrap. Founded in 2015 as Battery Resourcers out of MIT-affiliated research by Eric Gratz and Professor Yan Wang, it recovers up to 98% of the critical battery metals in end-of-life cells and uses its patented Hydro-to-Cathode direct cathode precursor (pCAM) synthesis process to produce cathode precursor and battery-grade lithium carbonate, reducing the carbon footprint of new EV battery cathode material by up to 90%. Its Base 1 facility in Covington, Georgia is North America's largest electric-vehicle battery recycling plant, and Apex 1 in Hopkinsville, Kentucky is its commercial pCAM plant. Ascend Elements publishes no public developer API for its materials, recycling or logistics business; the only machine-readable surface observed on its own hosts
  is the WordPress REST API at ascendelements.com/wp-json, which serves the corporate website's content, media-coverage, jobs and supplier sourcing-event collections.
image: https://ascendelements.com/wp-content/uploads/2022/01/cropped-AE_favicon.png
layout: provider
mcp_servers:
- description: ''
  name: ascend-elements-mcp.yml
  slug: ascend-elements-mcpyml
modified: '2026-08-02'
name: Ascend Elements
nav: Providers
network: true
overview: 'Ascend Elements publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Company, Battery Materials, Battery Recycling, Lithium-Ion, and Critical Minerals.


  Ascend Elements'' developer surface includes engineering blog, privacy policy, YouTube channel, authentication, and 24 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 19.6
  facets:
    commercial_clarity: 10.5
    contract_quality: 16.3
    developer_ergonomics: 16.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Ascend Elements Authentication
  slug: ascend-elements-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ascend Elements Domain Security
  slug: ascend-elements-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ascend-elements
tags:
- Company
- Battery Materials
- Battery Recycling
- Lithium-Ion
- Critical Minerals
- Cathode Precursor
- Electric Vehicles
- Circular Economy
- Advanced Manufacturing
- Sustainability
- Supply Chain
- Content Management
website: https://ascendelements.com/
---
