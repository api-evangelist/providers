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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Apperio Agentic Access
  operation_count: 30
  slug: apperio-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 1
apis:
- description: A set of non resource based endpoints that power various components within Apperio. These endpoints primarily support discovery and data investigation.
  name: Apperio Analytics API
  slug: apperio-analytics-api
- description: The e-billing endpoints provide access to the e-billing invoices in Apperio. They allow you to retrieve information about the invoices and the approval workflow, and also to approve and reject invoice
  name: Apperio E-billing API
  slug: apperio-e-billing-api
- description: 'The filter endpoints provide resource discovery in Apperio. This has two basic mechanisms. Firstly there are the resource discovery endpoints. These are: * `/api/v1/filter/engagements/` * `/api/v1/fil'
  name: Apperio Filter API
  slug: apperio-filter-api
- description: A set of endpoints returning information about a specific matter.
  name: Apperio Matter information API
  slug: apperio-matter-information-api
- description: The users endpoints allow you to manage your API tokens. Tokens are used to authenticate requests to the Apperio API. You can list your existing tokens, delete tokens that are no longer needed, and ac
  name: Apperio Users API
  slug: apperio-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apperio API Documentation Analytics API
  slug: open-apperio-analytics-api
- collection_type: open
  name: Apperio API Documentation Analytics E-billing API
  slug: open-apperio-e-billing-api
- collection_type: open
  name: Apperio API Documentation Analytics Filter API
  slug: open-apperio-filter-api
- collection_type: open
  name: Apperio API Documentation Analytics Matter information API
  slug: open-apperio-matter-information-api
- collection_type: open
  name: Apperio API Documentation Analytics Users API
  slug: open-apperio-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/apperio-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apperio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apperio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.apperio.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.apperio.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/apperio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apperio-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apperio-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apperio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apperio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.apperio.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apperio-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apperio-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apperio-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apperio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.apperio.com/information-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/apperio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apperio-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apperio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apperio-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apperio-llms.txt
- group: start
  title: ''
  type: Login
  url: https://app.apperio.com/login/
- group: operate
  title: ''
  type: Support
  url: https://www.apperio.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.apperio.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apperio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apperio.com/privacy-notice
- group: company
  title: ''
  type: Website
  url: https://www.apperio.com
created: '2026-07-17'
description: Apperio is a legal spend management and matter management platform for in-house legal teams and the law firms they work with. It connects directly to law-firm time-and-billing systems to give continuous, real-time visibility into billed and unbilled ("work in progress") legal spend, benchmarking to negotiate rates, and AI-assisted e-billing review against Outside Counsel Guidelines. The Apperio REST API exposes the same secure data that powers the platform's analytics — legal-spend analytics, matter (engagement) and invoice discovery, matter tagging, and e-billing invoice approval workflows — across its two-sided business/law-firm model. Apperio is a Seedcamp portfolio company and is now part of Persuit.
image: https://developer.apperio.com/static/favicon-32x32.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the Apperio OpenAPI operations. Apperio publishes no official hosted/remote MCP server; this is a governance starting point mapping each REST operation to a pro
  name: Apperio MCP Server
  slug: apperio-mcp-server
modified: '2026-07-17'
name: Apperio
nav: Providers
network: true
overview: 'Apperio publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, E-billing API, Filter API, and 2 more. Tagged areas include Legal, Legal Spend Management, Legal Tech, E-Billing, and Matter Management.


  Apperio''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 21 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 2
  name: Apperio Rate Limits
  slug: apperio-rate-limits
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apperio/refs/heads/main/screenshots/apperio-2026-07-25T200728.png
security:
- kind: authentication
  name: Apperio Authentication
  slug: apperio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apperio Domain Security
  slug: apperio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Apperio Trust Center
  slug: apperio-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type 2, Cyber Essentials
slug: apperio
tags:
- Legal
- Legal Spend Management
- Legal Tech
- E-Billing
- Matter Management
- Legal Operations
- Analytics
- Company
website: https://www.apperio.com
---
