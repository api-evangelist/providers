---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Voiceflow Agentic Access
  operation_count: 8
  slug: voiceflow-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- description: REST + SSE API for running Voiceflow agent turns, managing conversation state, updating variables, and emitting session events. Endpoints include Interact v4 (non-stream and SSE stream), Get/Update Co
  name: Voiceflow Conversations API
  slug: conversations
- baseURL: https://general-runtime.voiceflow.com
  baseurl_source: declared
  description: Run a turn against a Voiceflow agent.
  name: Voiceflow Interact API
  slug: voiceflow-interact-api
- baseURL: https://general-runtime.voiceflow.com
  baseurl_source: declared
  description: Start a session and emit session events.
  name: Voiceflow Session API
  slug: voiceflow-session-api
- baseURL: https://general-runtime.voiceflow.com
  baseurl_source: declared
  description: Read, replace, or delete the conversation state for a user.
  name: Voiceflow State API
  slug: voiceflow-state-api
- baseURL: https://general-runtime.voiceflow.com
  baseurl_source: declared
  description: Patch session variables.
  name: Voiceflow Variables API
  slug: voiceflow-variables-api
artifact_total: 20
collections:
- collection_type: open
  name: Voiceflow Conversations Interact API
  slug: open-voiceflow-interact-api
- collection_type: open
  name: Voiceflow Conversations Interact Session API
  slug: open-voiceflow-session-api
- collection_type: open
  name: Voiceflow Conversations Interact State API
  slug: open-voiceflow-state-api
- collection_type: open
  name: Voiceflow Conversations Interact Variables API
  slug: open-voiceflow-variables-api
- collection_type: open
  name: Voiceflow Conversations API
  slug: open-voiceflow
common:
- group: agent
  href: https://artifacts.apis.io/voiceflow/agentic-access/voiceflow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/voiceflow-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/voiceflow/security/voiceflow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/voiceflow-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/voiceflow/security/voiceflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/voiceflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/voiceflow/security/voiceflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voiceflow-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/voiceflow/authentication/voiceflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voiceflow-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voiceflow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voiceflowhq
- group: company
  title: ''
  type: Website
  url: https://www.voiceflow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.voiceflow.com/
- group: commercial
  href: https://artifacts.apis.io/voiceflow/plans/voiceflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/voiceflow-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/voiceflow/rate-limits/voiceflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/voiceflow-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/voiceflow/finops/voiceflow-finops.yml
  title: ''
  type: FinOps
  url: finops/voiceflow-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.voiceflow.com/blog
created: '2026-05-08'
description: Voiceflow is a conversational AI design and orchestration platform for building chat and voice agents with no-code flows, knowledge bases, and tool integrations. The Voiceflow Conversations API (formerly Dialog Manager API) enables programmatic interaction with Voiceflow agents — running turns, managing session state, and modifying conversation variables. Authentication via API key.
finops:
- has_sources: true
  method: generated
  name: Voiceflow Finops
  primary_unit: ''
  service_category: AI
  slug: voiceflow-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voiceflow.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.voiceflow.com over HTTP.
  name: Voiceflow MCP Server
  slug: voiceflow
modified: '2026-05-08'
name: Voiceflow
nav: Providers
network: true
overview: 'Voiceflow publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Interact API, Session API, State API, and 2 more. Tagged areas include Artificial Intelligence, Conversational AI, Chat, Voice, and Agent Builder.


  The Voiceflow catalog on APIs.io includes 1 Spectral governance ruleset.


  Voiceflow''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Voiceflow Plans Pricing
  plan_count: 3
  slug: voiceflow-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Voiceflow Rate Limits
  slug: voiceflow-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Voiceflow API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: voiceflow-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 46.8
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/voiceflow/voiceflow-2026-06-20T201125.png
security:
- kind: authentication
  name: Voiceflow Authentication
  slug: voiceflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Voiceflow Domain Security
  slug: voiceflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Voiceflow Vulnerability Disclosure
  slug: voiceflow-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Voiceflow Trust Center
  slug: voiceflow-trust-center
  summary_line: SOC 2, ISO 27001
slug: voiceflow
tags:
- Artificial Intelligence
- Conversational AI
- Chat
- Voice
- Agent Builder
- Dialog Manager
website: https://www.voiceflow.com/
---
