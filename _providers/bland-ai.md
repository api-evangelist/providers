---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
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
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bland AI Platform Calls API
  slug: open-bland-ai-calls-api
- collection_type: open
  name: Bland AI Platform API
  slug: open-bland-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bland-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bland-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bland-ai-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/bland-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bland-ai-rate-limits.yml
- group: commercial
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
- name: Bland Ai Finops
  service_category: AI
  slug: bland-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bland-ai.png
layout: provider
modified: '2026-05-08'
name: Bland AI
nav: Providers
network: true
overview: 'Bland AI publishes 1 API on the [APIs.io](https://apis.io/) network: Calls API. Tagged areas include Artificial Intelligence, Voice, Agents, Phone, and Real-Time.


  Bland AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Bland Ai Plans Pricing
  plan_count: 5
  slug: bland-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 9
  name: Bland Ai Rate Limits
  slug: bland-ai-rate-limits
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bland-ai/refs/heads/main/screenshots/bland-ai-2026-06-20T173346.png
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
website: https://www.bland.ai/
---
