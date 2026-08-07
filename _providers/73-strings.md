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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: 73 Strings Agentic Access
  operation_count: 23
  slug: 73-strings-agentic-access
  summary_line: 23 operations · 23 acting
api_count: 6
apis:
- description: RESTful service returning company and entity insights from the 73 Strings platform — entity lists, entity securities, business units, attribute identifiers and version lists — for portfolio management
  name: 73 Strings Asset Info API
  slug: 73-strings-asset-info-api
- description: RESTful service returning capitalization-table data for a portfolio company held in the 73 Strings platform, including security-level ownership detail scoped to an organization.
  name: 73 Strings Captable API
  slug: 73-strings-captable-api
- description: RESTful service listing the documents attached to a portfolio company in the 73 Strings platform and returning download details for an individual document by document and company id.
  name: 73 Strings Documents API
  slug: 73-strings-documents-api
- description: RESTful service reading and writing entity, business-unit and security-level financial data in the 73 Strings platform, including a v2 streaming variant for entity financial data and an endpoint retur
  name: 73 Strings Financial Data API
  slug: 73-strings-financial-data-api
- description: RESTful service returning qualitative and general company detail from the 73 Strings platform — general entity details, custom attribute data and qualitative analysis data.
  name: 73 Strings Qualitative Data API
  slug: 73-strings-qualitative-data-api
- description: RESTful service letting external enterprise customers ingest and retrieve transaction-ledger records in the 73 Strings platform. Supports bulk create/update of transaction ledger records with partial-
  name: 73 Strings Transaction API
  slug: 73-strings-transaction-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/73-strings-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/73-strings-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/73-strings-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.73strings.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-accord-eut-73strings.developer.azure-api.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api-accord-eut-73strings.developer.azure-api.net/apis
- group: docs
  title: ''
  type: APIReference
  url: https://api-accord-eut-73strings.developer.azure-api.net/apis
- group: start
  title: ''
  type: SignUp
  url: https://api-accord-eut-73strings.developer.azure-api.net/signup
- group: start
  title: ''
  type: Login
  url: https://api-accord-eut-73strings.developer.azure-api.net/signin
- group: operate
  title: ''
  type: Support
  url: mailto:support@73strings.com
- group: company
  title: ''
  type: Blog
  url: https://www.73strings.com/insights/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/73Strings
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.73strings.com/terms-and-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.73strings.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.73strings.com/resources/about/
- group: design
  title: ''
  type: Conventions
  url: conventions/73-strings-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/73-strings-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/73-strings-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/73-strings-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/73-strings-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/73-strings-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/73-strings-plans.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/73-strings-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/73-strings-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/73-strings-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/73-strings-asset-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/73-strings-captable-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/73-strings-documents-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/73-strings-financial-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/73-strings-qualitative-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/73-strings-transaction-api-overlay.yaml
created: '2026-08-05'
description: 73 Strings is an AI-powered financial technology company serving alternative asset managers in private equity, private credit, venture capital, infrastructure and multi-strategy funds. Its platform digitises the valuation and portfolio-monitoring lifecycle for illiquid assets through three products — 73 Value (audit-ready equity and credit valuations), 73 Monitor (portfolio monitoring and analytics) and 73 Extract (AI extraction of unstructured private-market documents into structured data). 73 Strings exposes a REST API surface through Microsoft Azure API Management developer portals, covering asset information, cap tables, documents, financial data, qualitative data and transaction-ledger ingestion, all authenticated with a subscription key and scoped by organization and user identifiers. The company is headquartered in Paris with offices in London, New York, San Francisco, Singapore, Riyadh, Abu Dhabi, Bengaluru and Hyderabad, and is backed by Blackstone, Goldman Sachs, Hamilton
  Lane, Golub Capital and Broadhaven.
image: https://backend.73strings.com/wp-content/uploads/73-Intelligence_image-1.png
layout: provider
mcp_servers:
- description: ''
  name: 73-strings-mcp.yml
  slug: 73-strings-mcpyml
modified: '2026-08-05'
name: 73 Strings
nav: Providers
network: true
overview: '73 Strings publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Asset Info API, Captable API, Documents API, and 3 more. Tagged areas include private-markets, valuation, portfolio-monitoring, private-equity, and private-credit.


  73 Strings'' developer surface includes authentication, documentation, API reference, signup flow, support, engineering blog, and 26 more developer resources.'
plans:
- name: 73 Strings Plans
  plan_count: 4
  slug: 73-strings-plans
random_paper: 25
rate_limits:
- limit_count: 5
  name: 73 Strings Rate Limits
  slug: 73-strings-rate-limits
score:
  band: developing
  composite: 55.3
  facets:
    commercial_clarity: 73.7
    contract_quality: 64.3
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: 73 Strings Authentication
  slug: 73-strings-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 73 Strings Domain Security
  slug: 73-strings-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 73-strings
tags:
- private-markets
- valuation
- portfolio-monitoring
- private-equity
- private-credit
- venture-capital
- alternative-assets
- financial-data
- data-extraction
- fintech
- asset-management
- azure-api-management
website: https://www.73strings.com/
---
