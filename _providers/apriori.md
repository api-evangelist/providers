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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: Agent Controller
  name: aPriori Agent API
  slug: apriori-agent-api
- description: Workflows Controller
  name: aPriori Workflow API
  slug: apriori-workflow-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: aP Connect REST Agent API
  slug: open-apriori-agent-api
- collection_type: open
  name: aP Connect Agent REST Workflow API
  slug: open-apriori-workflow-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/apriori-ap-connect-agent-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.apriori.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apriori.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apriori.com/en/Connect/apc/rarg/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apriori.com/en/Connect/apc/ig/Agent-Installation-Overview/
- group: operate
  title: ''
  type: Support
  url: https://support.apriori.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.apriori.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.apriori.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apriori.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://cloud.apriori.net/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apriori.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apriori.com/legal-notice/
- group: auth
  title: ''
  type: Compliance
  url: security/apriori-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apriori-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apriori-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apriori-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apriori-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apriori-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apriori-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apriori-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apriori-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apriori-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apriori-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/apriori-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apriori-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apriori-well-known.yml
created: '2026-08-06'
description: aPriori Technologies is a manufacturing insights software company founded in 2003 that simulates how a product will actually be made. Its platform ingests CAD geometry and returns should-cost estimates, design-for-manufacturability (DFM) guidance, routing and cycle-time analysis, and manufacturing carbon figures, so design, cost, sourcing and sustainability teams can act on production economics before tooling is cut. The product family covers aP Pro, aP Design, aP Generate, aP Analytics, aP Workspace and aiSource, delivered as aPriori Cloud or on-premise. Its public integration surface is aP Connect — a PLM/file-system connector plus a customer-installed Agent that carries a documented REST API for listing workflows, invoking REST-driven costing jobs, polling job state and retrieving per-part costing results, used to wire aPriori into Windchill, Teamcenter and file-system pipelines.
image: https://www.apriori.com/wp-content/uploads/2021/08/manufacturing-simulation-software-expert-partnership.jpg
layout: provider
mcp_servers:
- description: ''
  name: apriori-mcp.yml
  slug: apriori-mcpyml
modified: '2026-08-06'
name: aPriori
nav: Providers
network: true
overview: 'aPriori publishes 2 APIs on the [APIs.io](https://apis.io/) network: Agent API and Workflow API. Tagged areas include Company, manufacturing, product-cost-management, design-for-manufacturability, and should-cost.


  aPriori''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 20 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 43.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 48.7
    developer_ergonomics: 47.3
    discoverability: 66.7
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 43.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apriori/refs/heads/main/screenshots/apriori-2026-08-07T161510.png
security:
- kind: authentication
  name: Apriori Authentication
  slug: apriori-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Apriori Domain Security
  slug: apriori-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apriori Trust Center
  slug: apriori-trust-center
  summary_line: ISO/IEC 27001, SOC 2, GDPR
slug: apriori
tags:
- Company
- manufacturing
- product-cost-management
- design-for-manufacturability
- should-cost
- plm-integration
- cost-engineering
- digital-manufacturing
- sustainability
- workflow-automation
- cad
website: https://www.apriori.com/
---
