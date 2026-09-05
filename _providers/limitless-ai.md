---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Limitless Ai Agentic Access
  operation_count: 8
  slug: limitless-ai-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 2
apis:
- description: Wearable AI pendant that captures ambient audio, transcribes it, and stores it as Lifelogs in the user's Limitless account.
  name: Limitless Pendant
  slug: pendant
- description: Software assistant for meetings — transcripts, summaries, and Ask AI chat over personal memory. Available across desktop and mobile.
  name: Limitless Meeting Assistant
  slug: meeting-assistant
- description: Hosted Model Context Protocol endpoint that connects Claude and other MCP-compatible clients to the user's Limitless memory.
  name: Limitless MCP Server
  slug: mcp-server
- baseURL: https://www.limitless.ai
  baseurl_source: declared
  description: The Chats API from Limitless — 2 operation(s) for chats.
  name: Limitless Chats API
  slug: limitless-ai-chats-api
- baseURL: https://www.limitless.ai
  baseurl_source: declared
  description: The Download Audio API from Limitless — 1 operation(s) for download audio.
  name: Limitless Download Audio API
  slug: limitless-ai-download-audio-api
- baseURL: https://www.limitless.ai
  baseurl_source: declared
  description: The Lifelogs API from Limitless — 2 operation(s) for lifelogs.
  name: Limitless Lifelogs API
  slug: limitless-ai-lifelogs-api
- baseURL: https://www.limitless.ai
  baseurl_source: declared
  description: The Limitless Developer API API from Limitless — 1 operation(s) for limitless developer api.
  name: Limitless Limitless Developer API API
  slug: limitless-ai-limitless-developer-api-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Limitless Developer Chats API
  slug: open-limitless-ai-chats-api
- collection_type: open
  name: Limitless Developer Chats Download Audio API
  slug: open-limitless-ai-download-audio-api
- collection_type: open
  name: Limitless Developer Chats Lifelogs API
  slug: open-limitless-ai-lifelogs-api
- collection_type: open
  name: Limitless Developer Chats Limitless Developer API API
  slug: open-limitless-ai-limitless-developer-api-api
- collection_type: open
  name: Limitless Developer API
  slug: open-limitless-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/limitless-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/limitless-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/limitless-ai
- group: company
  title: ''
  type: Website
  url: https://www.limitless.ai/
- group: other
  title: ''
  type: Developers
  url: https://www.limitless.ai/developers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/limitless-ai-inc
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.limitless.ai/v1/openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/limitless-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/limitless-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/limitless-ai-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.limitless.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.limitless.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.limitless.ai/developers#endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://www.limitless.ai/developers#setup
- group: start
  title: ''
  type: SignUp
  url: https://app.limitless.ai
- group: start
  title: ''
  type: Login
  url: https://app.limitless.ai
- group: operate
  title: ''
  type: Support
  url: https://www.limitless.ai/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.limitless.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.limitless.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.limitless.ai/privacy-policy
- group: commercial
  title: ''
  type: Privacy
  url: https://www.limitless.ai/privacy
- group: company
  title: ''
  type: About
  url: https://www.limitless.ai/about
- group: company
  title: ''
  type: Careers
  url: https://www.limitless.ai/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/limitless-ai-inc
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/limitless-ai-inc/limitless-api-examples
- group: agent
  title: ''
  type: MCPServer
  url: mcp/limitless-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/limitless-ai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/limitless-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/limitless-ai-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/limitless-ai-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/limitless-ai-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/limitless-ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/limitless-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/limitless-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.limitless.ai/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/limitless-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/limitless-ai-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/limitless-ai-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/limitless-ai-developer-overlay.yaml
created: '2026-05-23'
description: Limitless is a personalized AI for meetings with a software assistant and the Limitless Pendant wearable that captures conversations as Lifelogs. The Limitless Developer API gives users programmatic access to their own Lifelogs, Ask AI chat history, and audio downloads, with an MCP endpoint that lets Claude and other MCP-compatible tools query Limitless memory directly. The OpenAPI spec is published and example code is hosted on GitHub.
finops:
- name: Limitless Ai Finops
  service_category: API
  slug: limitless-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/limitless-ai.png
layout: provider
mcp_servers:
- description: ''
  name: Limitless MCP Server
  slug: limitless-mcp-server
modified: '2026-08-08'
name: Limitless
nav: Providers
network: true
overview: 'Limitless publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chats API, Download Audio API, Lifelogs API, and 1 more. Tagged areas include Artificial Intelligence, Wearable, Pendant, Meeting Notes, and Lifelogs.


  Limitless'' developer surface includes GitHub presence, documentation, API reference, getting-started guide, signup flow, support, privacy policy, and 33 more developer resources.'
plans:
- name: Limitless Ai Plans Pricing
  plan_count: 1
  slug: limitless-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Limitless Ai Rate Limits
  slug: limitless-ai-rate-limits
scopes:
- name: Limitless Ai Scopes
  scope_count: 4
  slug: limitless-ai-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 49.1
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/limitless-ai/refs/heads/main/screenshots/limitless-ai-2026-07-25T225205.png
security:
- kind: authentication
  name: Limitless Ai Authentication
  slug: limitless-ai-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Limitless Ai Domain Security
  slug: limitless-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: limitless-ai
tags:
- Artificial Intelligence
- Wearable
- Pendant
- Meeting Notes
- Lifelogs
- Personal AI
- MCP
- OpenAPI
website: https://www.limitless.ai/
---
