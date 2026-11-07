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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Bland Ai Agentic Access
  operation_count: 4
  slug: bland-ai-agentic-access
  summary_line: 4 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST API for sending and managing AI phone calls, pathways (conversation flows), voices and voice clones, personas, tools, knowledge bases, transfer lists, and analytics. Auth is bearer token; base UR
  name: Bland AI Platform API
  slug: platform
- baseURL: https://api.bland.ai
  baseurl_source: declared
  description: Send, list, retrieve, and stop AI phone calls.
  name: Bland AI Calls API
  slug: bland-ai-calls-api
artifact_total: 13
collections:
- collection_type: open
  name: Bland AI Platform Calls API
  slug: open-bland-ai-calls-api
- collection_type: open
  name: Bland AI Platform API
  slug: open-bland-ai
common:
- group: other
  href: https://artifacts.apis.io/bland-ai/capabilities/bland-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bland-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bland-ai/agentic-access/bland-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bland-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bland-ai/security/bland-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bland-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bland-ai/security/bland-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bland-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bland-ai/authentication/bland-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bland-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bland-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bland-ai
- group: company
  title: ''
  type: Website
  url: https://www.bland.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bland.ai/
- group: commercial
  href: https://artifacts.apis.io/bland-ai/plans/bland-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bland-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bland-ai/rate-limits/bland-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bland-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bland-ai/finops/bland-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/bland-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bland.ai/blog
created: '2026-05-08'
description: Bland AI is an enterprise-grade conversational voice AI platform for inbound and outbound phone agents. The Bland REST API covers calls, pathways (conversation graphs), voices and voice cloning, personas, tools, knowledge bases, dynamic data, transfer lists, and webhooks.
finops:
- has_sources: true
  method: generated
  name: Bland Ai Finops
  primary_unit: ''
  service_category: AI
  slug: bland-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bland-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.bland.ai over HTTP.
  name: Bland AI MCP Server
  slug: bland-ai
modified: '2026-05-08'
name: Bland AI
nav: Providers
network: true
overview: 'Bland AI publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calls API, and 1 more. Tagged areas include Artificial Intelligence, Voice, Agents, Phone, and Real-Time.


  The Bland AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Bland AI''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Bland Ai Plans Pricing
  plan_count: 5
  slug: bland-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 9
  name: Bland Ai Rate Limits
  slug: bland-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Bland AI API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: bland-ai-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 44.1
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bland-ai/bland-ai-2026-06-20T173346.png
security:
- kind: authentication
  name: Bland Ai Authentication
  slug: bland-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bland Ai Domain Security
  slug: bland-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bland Ai Vulnerability Disclosure
  slug: bland-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bland-ai
tags:
- Artificial Intelligence
- Voice
- Agents
- Phone
- Real-Time
- Conversational AI
- Voice AI
- Voice Agents
website: https://www.bland.ai/
---
