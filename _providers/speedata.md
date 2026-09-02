---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.speedata.io/
- group: company
  title: ''
  type: Blog
  url: https://www.speedata.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.speedata.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Speedata-io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/speedata-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/speedata-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/speedata-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/speedata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/speedata-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/speedata-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/speedata-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speedata-domain-security.yml
coverage:
  checked: '2026-08-28'
  detail: Speedata is a fabless semiconductor company whose only programmatic surface is a Spark plugin JAR (speedata-dash-0.8.1-spark_2.12.jar, com.speedata.spark.DashPlugin) handed to Early Access customers — there is no api.speedata.io, no docs. or developer. host (both NXDOMAIN), no /pricing or /docs route in the full Wix pages sitemap, and the only live machine endpoint on the domain is the platform-authored Wix Site MCP server that every Wix tenant gets by default.
  evidence:
  - status: 0
    url: https://api.speedata.io/
  - status: 0
    url: https://docs.speedata.io/
  - status: 200
    url: https://www.speedata.io/pages-sitemap.xml
  - status: 404
    url: https://workloadanalyzer.speedata.io/openapi.json
  - status: 200
    url: https://www.speedata.io/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: Speedata is a Tel Aviv-based semiconductor company that builds the APU (Analytics Processing Unit), a processor purpose-built for accelerating Apache Spark SQL, batch ETL and AI data-preparation workloads rather than graphics or model training. The APU ships as the C200 PCIe Gen5 accelerator card powered by the company's Callisto ASIC, paired with a software layer called Dash that plugs into the Spark Catalyst optimizer and offloads compute-intensive stages to the card with no application code changes. Founded in 2019 by researchers in multi-threaded coarse-grained reconfigurable architecture, the company raised a $44M Series B in June 2025 (total funding ~$114M) from Walden Catalyst Ventures, 83North and Koch Disruptive. Speedata publishes no public web API, developer portal or machine-readable API contract; its programmatic surface is a Spark plugin JAR distributed under an early-access program, plus a free browser/CLI Workload Analyzer for estimating acceleration on a customer's
  own Spark workloads.
image: https://static.wixstatic.com/media/443c60_bb2144681e7648e5b1e6d9ddb3b51102~mv2.jpeg/v1/fill/w_2500,h_1381,al_c/443c60_bb2144681e7648e5b1e6d9ddb3b51102~mv2.jpeg
layout: provider
mcp_servers:
- description: A live, anonymous Model Context Protocol endpoint served on Speedata's own host (www.speedata.io). It is the Wix Site MCP server, exposed automatically because speedata.io is built on Wix — the tool s
  name: Speedata Site MCP Server
  slug: speedata-site-mcp-server
modified: '2026-08-28'
name: Speedata
nav: Providers
network: true
overview: 'Speedata is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware Acceleration, Analytics, and Big Data.


  Speedata''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Speedata Plans Pricing
  plan_count: 0
  slug: speedata-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Speedata Rate Limits
  slug: speedata-rate-limits
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 10.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Speedata Domain Security
  slug: speedata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: speedata
tags:
- Company
- Semiconductors
- Hardware Acceleration
- Analytics
- Big Data
- Apache Spark
- Data Engineering
- Artificial Intelligence
- Data Infrastructure
- Israel
website: https://www.speedata.io/
---
