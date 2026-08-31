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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 24.0
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The callable surface a deployed Kana pipeline ("skill") exposes on the Kana application host. POST /skill/{pipelineid} starts a run and returns a runid; GET /run/{runid}/status reports progress and qu
  name: Kana Skill API
  slug: kana-skill-api
- description: Kana exposes each deployed agent/orchestrator as a remote MCP server at https://apps.kana.ai/mcp/{public access key}, fronted by the platform's OAuth 2.0 authorization server (PKCE S256, RFC 7591 dyna
  name: Kana MCP Server
  slug: kana-mcp-server
artifact_total: 8
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: company
  title: ''
  type: Website
  url: https://www.kana.ai
- group: company
  title: ''
  type: Blog
  url: https://www.kana.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.kana.ai/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kana.ai/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.kana.ai/legal
- group: design
  title: ''
  type: Conformance
  url: conformance/kana-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kana-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kana-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kana.ai/get-started
- group: start
  title: ''
  type: SignUp
  url: https://www.kana.ai/get-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.kana.ai/faq
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kana-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kana-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kana-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kana-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kana-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kana-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kana-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kana-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kana-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/kana-packages.yml
created: '2026-07-17'
description: 'Kana is an agentic AI growth and marketing platform that helps brands discover high-precision audiences, optimize acquisition efficiency, and stay visible across AI-driven discovery environments such as LLM answer engines, search copilots, and autonomous agents. Founded by martech veterans Tom Chavez and Vivek Vaidya (previously Rapt, acquired by Microsoft, and Krux, acquired by Salesforce) and incubated in the super{set} startup studio, Kana raised a $15M seed round led by Mayfield in February 2026. The platform orchestrates specialized AI agents that reason over customer data, plan multi-step workflows, and recommend next-best actions across a suite of purpose-built applications: Campaign Orchestrator, Marketing Intelligence, Personalization, Synthetic Data Generation, Media Proposal Generator, Category Intelligence, Audience Builder, OmniChannel Media Planner, and an Agentic Data Platform. Proprietary just-in-time data integration connects to existing CRM, CDP, marketing-automation,
  and data-warehouse systems without disruptive infrastructure changes, keeping a human-in-the-loop review step. Kana ships no public developer portal, but its application host apps.kana.ai does expose a real callable surface: an OAuth 2.0 authorization server whose RFC 8414 metadata is served anonymously and declares MCP protocol 2025-03-26 with mcp:read / mcp:write / kana:read / kana:write scopes, plus a per-deployment MCP endpoint and an api-key-authenticated Skill API for running pipelines and retrieving their outputs. Everything but the OAuth metadata sits behind a 401, so this profile captures Kana''s public identity, legal/compliance posture, authentication and scope model, and the shape of the gated API surface.'
image: https://cdn.prod.website-files.com/6938c88532164b75764d7ec5/693c0c5cc53ad3db97596f39_929e4e790efd0fbe50a55bee450f14e8_Frame%202087327472.jpg
layout: provider
mcp_servers:
- description: ''
  name: Kana MCP Server
  slug: kana-mcp-server
modified: '2026-08-13'
name: Kana
nav: Providers
network: true
overview: 'Kana publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Artificial Intelligence, Agentic AI, and Marketing Technology.


  Kana''s developer surface includes engineering blog, support, getting-started guide, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Kana Plans Pricing
  plan_count: 3
  slug: kana-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Kana Rate Limits
  slug: kana-rate-limits
scopes:
- name: Kana Scopes
  scope_count: 0
  slug: kana-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kana/refs/heads/main/screenshots/kana-2026-07-25T223445.png
security:
- kind: authentication
  name: Kana Authentication
  slug: kana-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kana Domain Security
  slug: kana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kana
tags:
- Company
- Marketing
- Artificial Intelligence
- Agentic AI
- Marketing Technology
- Audience Intelligence
- Customer Data Platform
- AI Search Optimization
- Growth
website: https://www.kana.ai
---
