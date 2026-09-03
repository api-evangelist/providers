---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API that exposes the Jigso platform in code - query all organizational data with simple REST calls, embed insights into dashboards, chatbots, and internal applications, and trigger scheduled or e
  name: Jigso API
  slug: jigso-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/jigso-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jigso-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jigso.io
- group: company
  title: ''
  type: Blog
  url: https://www.jigso.io/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@jigso.io
- group: start
  title: ''
  type: Login
  url: https://app.jigso.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jigso.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jigso.io/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.jigso.io/security-portal
- group: design
  title: ''
  type: Conformance
  url: conformance/jigso-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jigso-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/jigso-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jigso-lifecycle.yml
coverage:
  checked: '2026-08-13'
  detail: 'Jigso markets both a REST API and an enterprise MCP platform as top-level products, but neither has a developer portal, a reference, or a published endpoint - both pages end at "Book a Demo", docs.jigso.io and developer.jigso.io do not resolve, and the live API host api.jigso.io answers every path, including "/", with {"error": {"type": "Unauthorized", "message": "Authorization header required"}}.'
  evidence:
  - status: 200
    url: https://www.jigso.io/jigso-api
  - status: 401
    url: https://api.jigso.io/openapi.json
  - status: 200
    url: https://www.jigso.io/mcp-for-enterprise
  - status: 404
    url: https://www.jigso.io/pricing
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Jigso is a proactive AI operating system for enterprises that synthesizes data from across a company's business applications - CRM, support, communication, and data warehouses - into a unified, always-on intelligence layer. Rather than reactive search, Jigso continuously monitors connected systems to surface deal risks, churn signals, and action items, and grounds every answer in verifiable business data to avoid hallucination. It exposes this capability through a REST API for embedding insights into workflows, dashboards, and internal tools, and through an enterprise MCP (Model Context Protocol) platform that lets AI assistants such as ChatGPT and Claude securely query internal systems with permission-aware access. Jigso integrates with Salesforce, HubSpot, Slack, Gmail, Google Drive, Jira, Zendesk, Snowflake, BigQuery, and more, and is SOC 2 Type II certified and GDPR compliant. Jigso is backed by General Catalyst.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jigso.png
layout: provider
modified: '2026-07-19'
name: Jigso
nav: Providers
network: true
overview: 'Jigso publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Business Intelligence, and Revenue Operations.


  Jigso''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Jigso Plans Pricing
  plan_count: 0
  slug: jigso-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Jigso Rate Limits
  slug: jigso-rate-limits
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jigso/refs/heads/main/screenshots/jigso-2026-07-25T223148.png
security:
- kind: domain-security
  name: Jigso Domain Security
  slug: jigso-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Jigso Trust Center
  slug: jigso-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: jigso
tags:
- Company
- Artificial Intelligence
- Enterprise
- Business Intelligence
- Revenue Operations
- MCP
- Agents
- Data Integration
- Customer Success
- Sales
website: https://www.jigso.io
---
