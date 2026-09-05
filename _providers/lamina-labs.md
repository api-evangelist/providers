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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Lamina Labs Agentic Access
  operation_count: 2
  slug: lamina-labs-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: 'The Simi API submits and retrieves whiteboard-style explainer video generation jobs. Submission is asynchronous: a job is created and returns immediately with job metadata, then the job is polled unti'
  name: Simi Video Generation API
  slug: simi
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lamina-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.laminalabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://app.laminalabs.ai/simi
- group: start
  title: ''
  type: SignUp
  url: https://app.laminalabs.ai/simi
- group: operate
  title: ''
  type: Support
  url: https://lamina-labs.cal.com/lamina
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lamina-labs-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lamina-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lamina-labs-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lamina-labs-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lamina-labs-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lamina-labs-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lamina-labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lamina-labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lamina-labs-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lamina-labs-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/lamina-labs-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lamina-labs-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lamina-labs-llms.txt
created: '2026-07-17'
description: Lamina Labs is a San Francisco company (Y Combinator Spring 2026) building near-real-time video infrastructure for large language models. Its flagship product, Simi, turns prompts, documents, and AI-generated answers into whiteboard-style teaching videos in seconds, handling script writing, illustration, animation, and narration automatically, for durations from one minute to an hour and in over 80 languages. The company targets training, onboarding, product walkthroughs, sales, marketing, and educational use cases, with the stated goal of making video the default interface for AI communication. Lamina exposes Simi to agents through a public remote MCP server at https://api.laminalabs.ai/mcp, secured by an OAuth 2.1-style authorization server with PKCE, dynamic client registration, and job-scoped access tokens.
image: https://www.laminalabs.ai/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Lamina Labs MCP Server
  slug: lamina-labs-mcp-server
modified: '2026-07-19'
name: Lamina Labs
nav: Providers
network: true
overview: 'Lamina Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, Video Generation, and Machine-Learning.


  Lamina Labs'' developer surface includes documentation, signup flow, support, authentication, and 15 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Lamina Labs Rate Limits
  slug: lamina-labs-rate-limits
scopes:
- name: Lamina Labs Scopes
  scope_count: 2
  slug: lamina-labs-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 19.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lamina-labs/refs/heads/main/screenshots/lamina-labs-2026-08-07T171605.png
security:
- kind: authentication
  name: Lamina Labs Authentication
  slug: lamina-labs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lamina Labs Domain Security
  slug: lamina-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lamina-labs
tags:
- Company
- Artificial Intelligence
- Video
- Video Generation
- Machine-Learning
- Education
- Media
- MCP
- Content Generation
website: https://www.laminalabs.ai/
---
