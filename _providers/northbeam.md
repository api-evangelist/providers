---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.8
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: REST API for submitting order and purchase data to Northbeam as the revenue ground truth for multi-touch attribution and media mix modeling. Writes are natural-key upserts on a caller-supplied order_i
  name: Northbeam Orders API
  slug: orders-api
- description: REST API for uploading daily and hourly spend records from ad platforms Northbeam does not integrate with natively, so those channels can be attributed. Rows are upserted on the platform/campaign/adse
  name: Northbeam Spend API
  slug: spend-api
- description: Asynchronous REST API for exporting attribution performance metrics including revenue, transactions, CAC, AOV and creative analytics across attribution windows and models. Submit an export config, pol
  name: Northbeam Data Export API
  slug: data-export-api
- description: First-party remote Model Context Protocol server giving an agent read-only access to the caller's Northbeam dashboards — performance, attribution, spend and orders. Documented as a custom connector fo
  name: Northbeam MCP Server
  slug: mcp
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.northbeam.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.northbeam.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.northbeam.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.northbeam.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.northbeam.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.northbeam.io/submit-a-support-ticket
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.northbeam.io/docs/frequently-asked-questions
- group: company
  title: ''
  type: Blog
  url: https://www.northbeam.io/blog
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/north-beam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northbeam
- group: other
  title: ''
  type: X
  url: https://x.com/northbeam
- group: commercial
  title: ''
  type: Pricing
  url: https://www.northbeam.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.northbeam.io/demo
- group: start
  title: ''
  type: Login
  url: https://dashboard.northbeam.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.northbeam.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.northbeam.io/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.northbeam.io/data-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/northbeam-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northbeam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/northbeam-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/northbeam-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/northbeam-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/northbeam-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/northbeam-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/northbeam-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/northbeam-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/northbeam-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/northbeam-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/northbeam-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/northbeam-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/northbeam-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/northbeam-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/northbeam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/northbeam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/northbeam-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/northbeam-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/northbeam-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: 'Northbeam is a multi-touch marketing attribution platform for e-commerce brands. It joins first-party click and view data collected by its own browser pixel to order-level revenue and to ad spend across every channel, then reports channel, campaign, adset and ad level ROAS, CAC, AOV and creative performance under a choice of attribution models and windows. The developer surface is three REST APIs published as OpenAPI: an Orders API for pushing purchase data in as the revenue ground truth, a Spend API for uploading cost from channels Northbeam does not integrate with natively, and an asynchronous Data Export API for pulling attribution metrics back out to Northbeam documents, GCS or S3. Northbeam also runs a first-party remote MCP server at mcp.northbeam.io, OAuth-secured and read-only, which it documents as a custom connector for Claude and ChatGPT.'
finops:
- name: Northbeam Finops
  service_category: ''
  slug: northbeam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/northbeam.png
jsonld:
- class_count: 11
  name: Northbeam Context
  property_count: 38
  slug: northbeam-context
layout: provider
mcp_servers:
- description: ''
  name: northbeam-mcp.yml
  slug: northbeam-mcpyml
modified: '2026-08-13'
name: Northbeam
nav: Providers
network: true
overview: 'Northbeam publishes 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Spend API, and Data Export API. Tagged areas include Marketing Attribution, Multi-Touch Attribution, E-Commerce, ROAS, and Media Mix Modeling.


  The Northbeam catalog on APIs.io includes 1 JSON-LD context.


  Northbeam''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Northbeam Plans Pricing
  plan_count: 4
  slug: northbeam-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 8
  name: Northbeam Rate Limits
  slug: northbeam-rate-limits
score:
  band: strong
  composite: 65.3
  delta: -1.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 58.7
    developer_ergonomics: 55.4
    discoverability: 92.6
    governance: 45.5
    operational_transparency: 36.8
  previous_composite: 67.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/northbeam/refs/heads/main/screenshots/northbeam-2026-06-20T190413.png
security:
- kind: authentication
  name: Northbeam Authentication
  slug: northbeam-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Northbeam Domain Security
  slug: northbeam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Northbeam Trust Center
  slug: northbeam-trust-center
  summary_line: SOC 2 Type 2
slug: northbeam
tags:
- Marketing Attribution
- Multi-Touch Attribution
- E-Commerce
- ROAS
- Media Mix Modeling
- Creative Analytics
- Performance Marketing
- Advertising
- Marketing Analytics
- Agents
website: https://www.northbeam.io
---
