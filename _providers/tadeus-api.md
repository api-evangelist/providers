---
access_model:
  confidence: high
  label: Public
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://tadeus.net/#pricing
  - https://app.tadeus.net/signup
  - https://app.tadeus.net/api/integration/v1/swagger/?format=openapi
  trial: true
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The attempts API from Tadeus API — 2 operation(s) for attempts.
  name: Tadeus API Attempts API
  slug: tadeus-api-attempts-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The billing API from Tadeus API — 6 operation(s) for billing.
  name: Tadeus API Billing API
  slug: tadeus-api-billing-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The campaigns API from Tadeus API — 5 operation(s) for campaigns.
  name: Tadeus API Campaigns API
  slug: tadeus-api-campaigns-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The insights API from Tadeus API — 6 operation(s) for insights.
  name: Tadeus API Insights API
  slug: tadeus-api-insights-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The organisation API from Tadeus API — 2 operation(s) for organisation.
  name: Tadeus API Organisation API
  slug: tadeus-api-organisation-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The results API from Tadeus API — 4 operation(s) for results.
  name: Tadeus API Results API
  slug: tadeus-api-results-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The sessions API from Tadeus API — 2 operation(s) for sessions.
  name: Tadeus API Sessions API
  slug: tadeus-api-sessions-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The templates API from Tadeus API — 2 operation(s) for templates.
  name: Tadeus API Templates API
  slug: tadeus-api-templates-api
- baseURL: https://app.tadeus.net/api/integration/v1
  baseurl_source: declared
  description: The transcripts API from Tadeus API — 2 operation(s) for transcripts.
  name: Tadeus API Transcripts API
  slug: tadeus-api-transcripts-api
artifact_total: 17
collections:
- collection_type: open
  name: Integration API
  slug: open-tadeus-api-integration
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tadeus-api-integration-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://tadeus.net/
- group: docs
  title: ''
  type: Documentation
  url: https://app.tadeus.net/api/integration/v1/swagger/
- group: docs
  title: ''
  type: APIReference
  url: https://app.tadeus.net/api/integration/v1/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://tadeus.net/api-examples
- group: operate
  title: ''
  type: Support
  url: https://tadeus.net/contact
- group: company
  title: ''
  type: Blog
  url: https://tadeus.net/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://tadeus.net/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://tadeus.net/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.tadeus.net/signup
- group: start
  title: ''
  type: Login
  url: https://app.tadeus.net/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tadeus.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tadeus.net/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tadeus-ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tadeus-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tadeus-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tadeus-api-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tadeus-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tadeus-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tadeus-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tadeus-api-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tadeus-api-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tadeus-api-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tadeus-api-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/tadeus-api-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tadeus-api-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tadeus-api-domain-security.yml
created: '2026-07-06'
description: 'Tadeus is an AI voice agent platform for workforce platforms: one agent holds real, adaptive voice conversations with every employee at scale, in their own language, and returns structured, timestamped records to the HCM, payroll, scheduling and compliance systems people already use. It works from the transcript rather than the audio and reports comprehension and engagement signals about responses rather than inferring emotion, which is the position its published EU AI Act documentation rests on. The public Integration API is a 47-operation REST surface for creating interview templates and campaigns, inviting participants individually or in bulk, creating anonymous sessions, and retrieving transcripts, structured results with per-response quality signals, and cross-session AI insights. Tadeus went generally available on 14 July 2026 and also ships a hosted, first-party MCP server so agents can commission interviews and query results as tool calls.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tadeus-api.png
layout: provider
mcp_servers:
- description: Tadeus publishes a first-party, hosted, remote MCP server that lets any MCP-compatible agent (Claude and others) commission real voice interview campaigns with people, monitor them, search the resulti
  name: Tadeus MCP
  slug: tadeus-mcp
modified: '2026-08-11'
name: Tadeus API
nav: Providers
network: true
overview: 'Tadeus API publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Attempts API, Billing API, Campaigns API, and 6 more. Tagged areas include Voice AI, Research, Interviews, Workforce, and HR Tech.


  Tadeus API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Tadeus Api Plans Pricing
  plan_count: 3
  slug: tadeus-api-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Tadeus Api Rate Limits
  slug: tadeus-api-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 80.3
    commercial_clarity: 80.3
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 49.4
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tadeus-api/refs/heads/main/screenshots/tadeus-api-2026-08-17T082242.png
security:
- kind: authentication
  name: Tadeus Api Authentication
  slug: tadeus-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Tadeus Api Domain Security
  slug: tadeus-api-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tadeus Api Vulnerability Disclosure
  slug: tadeus-api-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Tadeus Api Trust Center
  slug: tadeus-api-trust-center
  summary_line: count, audited, claimed, note
slug: tadeus-api
tags:
- Voice AI
- Research
- Interviews
- Workforce
- HR Tech
- Conversational AI
- Employee Experience
- AI Agents
- MCP
- EU AI Act
- Compliance
- Employee Engagement
website: https://tadeus.net/
---
