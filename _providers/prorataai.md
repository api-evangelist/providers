---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The publisher ingest API for the Gist Content Network. Publisher partners push articles to ProRata in real time (POST /ingest/article) or in bulk for archived content (POST /ingest/multiple_articles),
  name: Gist Content API (Ingest)
  slug: prorataai-gist-content-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Chat API from ProRata.ai — 5 operation(s) for chat.
  name: ProRata.ai Chat API
  slug: prorataai-chat-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Health API from ProRata.ai — 1 operation(s) for health.
  name: ProRata.ai Health API
  slug: prorataai-health-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Publishers API from ProRata.ai — 2 operation(s) for publishers.
  name: ProRata.ai Publishers API
  slug: prorataai-publishers-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Questions API from ProRata.ai — 2 operation(s) for questions.
  name: ProRata.ai Questions API
  slug: prorataai-questions-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Root API from ProRata.ai — 1 operation(s) for root.
  name: ProRata.ai Root API
  slug: prorataai-root-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Summaries API from ProRata.ai — 2 operation(s) for summaries.
  name: ProRata.ai Summaries API
  slug: prorataai-summaries-api
- baseURL: https://api.gist.ai
  baseurl_source: declared
  description: The Threads API from ProRata.ai — 2 operation(s) for threads.
  name: ProRata.ai Threads API
  slug: prorataai-threads-api
artifact_total: 13
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/prorataai-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prorataai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prorata.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.gist.ai/docs/about-gist-services
- group: docs
  title: ''
  type: Documentation
  url: https://platform.gist.ai/docs/about-gist-services
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.gist.ai/docs/quick-start-using-widgets
- group: operate
  title: ''
  type: Support
  url: https://gist.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://gist.ai/get-the-gist
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prorata-ai
- group: start
  title: ''
  type: SignUp
  url: https://console.gist.ai/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gist.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gist.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prorataai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/prorataai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/prorataai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/prorataai-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prorataai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/prorataai-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prorataai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prorataai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prorataai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prorataai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/prorataai-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prorataai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prorataai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prorataai-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/prorataai-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: ProRata.ai is an AI attribution, search and advertising company founded in 2024 by Idealab founder Bill Gross. It operates the Gist family of products — Gist Answers (an embeddable, publisher-hosted AI answer widget), Gist Content Network (a licensed publisher content corpus with revenue share), Gist Ads (advertising placed inside AI answer surfaces) and Gist GEO (generative-engine-optimization visibility tracking). Its developer surface is the Gist Developer Hub at platform.gist.ai, which publishes a public OpenAPI 3.0 contract — the "Prorata API Service" — covering chat, streaming completions, citations and attributions, threads, recommended and related questions, document summarization, publisher lookup and service health, served from https://api.gist.ai behind a Bearer API key issued at the Publisher Group level.
image: https://prorata.ai/wp-content/uploads/2026/01/prorata-OGshare-OS-1.webp
layout: provider
mcp_servers:
- description: ProRata serves a remote MCP endpoint on its own developer-hub host, platform.gist.ai. A GET returns the plain-text guard "This URL can only be accessed with a MCP client." and a JSON-RPC POST is answe
  name: Gist Developer Hub MCP
  slug: gist-developer-hub-mcp
modified: '2026-08-26'
name: ProRata.ai
nav: Providers
network: true
overview: 'ProRata.ai publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Health API, Publishers API, and 4 more. Tagged areas include Artificial Intelligence, Search, Content, Publishing, and Advertising.


  ProRata.ai''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, sandbox, and 21 more developer resources.'
plans:
- name: Prorataai Plans Pricing
  plan_count: 0
  slug: prorataai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Prorataai Rate Limits
  slug: prorataai-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 47.9
    developer_ergonomics: 50.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 39.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prorataai/refs/heads/main/screenshots/prorataai-2026-09-02T152208.png
security:
- kind: authentication
  name: Prorataai Authentication
  slug: prorataai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prorataai Domain Security
  slug: prorataai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prorataai
tags:
- Artificial Intelligence
- Search
- Content
- Publishing
- Advertising
- Attribution
- Answer Engines
- Generative AI
- Media
- Content Licensing
website: https://prorata.ai/
---
