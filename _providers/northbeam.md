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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-01'
api_count: 8
apis:
- description: First-party remote Model Context Protocol server giving an agent read-only access to the caller's Northbeam dashboards — performance, attribution, spend and orders. Documented as a custom connector fo
  name: Northbeam MCP Server
  slug: mcp
- description: The Attribution Models API from Northbeam — 1 operation(s) for attribution models.
  name: Northbeam Attribution Models API
  slug: northbeam-attribution-models-api
- description: The Breakdowns API from Northbeam — 1 operation(s) for breakdowns.
  name: Northbeam Breakdowns API
  slug: northbeam-breakdowns-api
- description: The Data Export API from Northbeam — 2 operation(s) for data export.
  name: Northbeam Data Export API
  slug: northbeam-data-export-api
- description: The Metrics API from Northbeam — 1 operation(s) for metrics.
  name: Northbeam Metrics API
  slug: northbeam-metrics-api
- description: The Orders API from Northbeam — 2 operation(s) for orders.
  name: Northbeam Orders API
  slug: northbeam-orders-api
- description: The Spend API from Northbeam — 1 operation(s) for spend.
  name: Northbeam Spend API
  slug: northbeam-spend-api
- description: The Spend Hourly API from Northbeam — 1 operation(s) for spend hourly.
  name: Northbeam Spend Hourly API
  slug: northbeam-spend-hourly-api
artifact_total: 16
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/northbeam-orders-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/northbeam-orders-v1-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/northbeam-sync-orders.md
- group: other
  title: ''
  type: Overlay
  url: overlays/northbeam-spend-v1-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/northbeam-sync-ad-spend.md
- group: other
  title: ''
  type: Overlay
  url: overlays/northbeam-data-export-v1-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/northbeam-export-attribution-data.md
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
- description: Northbeam ships a first-party remote MCP server that gives an agent read-only access to the caller's Northbeam dashboards — performance, attribution, spend and orders. Northbeam documents it as a cust
  name: Northbeam MCP
  slug: northbeam-mcp
modified: '2026-08-13'
name: Northbeam
nav: Providers
network: true
overview: 'Northbeam publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attribution Models API, Breakdowns API, Data Export API, and 4 more. Tagged areas include Marketing Attribution, Multi-Touch Attribution, E-Commerce, ROAS, and Media Mix Modeling.


  The Northbeam catalog on APIs.io includes 1 JSON-LD context.


  Northbeam''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
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
  composite: 62.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 32.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 33.3
    contract_quality: 58.6
    developer_ergonomics: 55.4
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 36.8
  previous_composite: 62.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
