---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Stacks Ai Agentic Access
  operation_count: 13
  slug: stacks-ai-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.stack-ai.com
  baseurl_source: declared
  description: The analytics API from Stacks Ai — 2 operation(s) for analytics.
  name: Stacks Ai Analytics API
  slug: stacks-ai-analytics-api
- baseURL: https://api.stack-ai.com
  baseurl_source: declared
  description: The Knowledge Base Resources API from Stacks Ai — 2 operation(s) for knowledge base resources.
  name: Stacks Ai Knowledge Base Resources API
  slug: stacks-ai-knowledge-base-resources-api
- baseURL: https://api.stack-ai.com
  baseurl_source: declared
  description: The Knowledge Base Sync API from Stacks Ai — 1 operation(s) for knowledge base sync.
  name: Stacks Ai Knowledge Base Sync API
  slug: stacks-ai-knowledge-base-sync-api
- baseURL: https://api.stack-ai.com
  baseurl_source: declared
  description: The Knowledge Bases API from Stacks Ai — 5 operation(s) for knowledge bases.
  name: Stacks Ai Knowledge Bases API
  slug: stacks-ai-knowledge-bases-api
- baseURL: https://api.stack-ai.com
  baseurl_source: declared
  description: The Run Flow API from Stacks Ai — 1 operation(s) for run flow.
  name: Stacks Ai Run Flow API
  slug: stacks-ai-run-flow-api
artifact_total: 21
collections:
- collection_type: open
  name: StackAI analytics API
  slug: open-stacks-ai-analytics-api
- collection_type: open
  name: StackAI analytics Knowledge Base Resources API
  slug: open-stacks-ai-knowledge-base-resources-api
- collection_type: open
  name: StackAI analytics Knowledge Base Sync API
  slug: open-stacks-ai-knowledge-base-sync-api
- collection_type: open
  name: StackAI analytics Knowledge Bases API
  slug: open-stacks-ai-knowledge-bases-api
- collection_type: open
  name: StackAI analytics Run Flow API
  slug: open-stacks-ai-run-flow-api
common:
- group: other
  href: https://artifacts.apis.io/stacks-ai/capabilities/stacks-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stacks-ai-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/stacks-ai/plans/stacks-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stacks-ai-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.stackai.com/
- group: agent
  href: https://artifacts.apis.io/stacks-ai/skills/stacks-ai-build-knowledge-base.md
  title: ''
  type: AgentSkill
  url: skills/stacks-ai-build-knowledge-base.md
- group: agent
  href: https://artifacts.apis.io/stacks-ai/mcp/stacks-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/stacks-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/stacks-ai/overlays/stacks-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stacks-ai-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/stacks-ai/security/stacks-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stacks-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/stacks-ai/security/stacks-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stacks-ai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/stacks-ai/agentic-access/stacks-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stacks-ai-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.stackai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stackai.com/interface-and-deployment/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackai.com/getting-started/start-here
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stackai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.stackai.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stackai.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stackai.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.stackai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stack-ai.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.stackai.com/
- group: agent
  href: https://artifacts.apis.io/stacks-ai/well-known/stacks-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stacks-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/stacks-ai/llms/stacks-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stacks-ai-llms.txt
created: '2026-07-17'
description: StackAI (Stack AI, Inc.) is an enterprise AI agent platform that lets teams build, deploy, and govern no-code agentic workflows at scale. Its visual Workflow Builder chains LLMs, knowledge bases, connections, and logic nodes into production agents that can be deployed as a REST API, chat assistant, form, or batch job. The public StackAI API runs deployed flows, manages Knowledge Bases and their file resources (upload, index, sync, cursor-paginated listing), and reads flow-run analytics. The platform targets regulated industries with SOC 2 Type II and ISO 27001 certifications, RBAC/SCIM governance, and multi-tenant, VPC, and on-premise deployment options. Backed by Lightspeed Venture Partners.
finops:
- has_sources: true
  method: derived
  name: Stacks Ai Finops
  primary_unit: subscription
  service_category: ''
  slug: stacks-ai-finops
  template: false
image: https://www.stackai.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Stacks Ai
nav: Providers
network: true
overview: 'Stacks Ai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Knowledge Base Resources API, Knowledge Base Sync API, and 2 more. Tagged areas include Company, Artificial Intelligence, Agents, LLM, and No-Code.


  The Stacks Ai catalog on APIs.io includes 1 Spectral governance ruleset.


  Stacks Ai''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Stacks Ai Plans Pricing
  plan_count: 2
  slug: stacks-ai-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Stacks Ai API Rules
  rule_count: 63
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 6
  slug: stacks-ai-rules
scopes:
- name: Stacks Ai Scopes
  scope_count: 0
  slug: stacks-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 49.2
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stacks-ai/stacks-ai-2026-08-17T082059.png
security:
- kind: authentication
  name: Stacks Ai Authentication
  slug: stacks-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Stacks Ai Domain Security
  slug: stacks-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stacks Ai Trust Center
  slug: stacks-ai-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 3
skills:
- name: Build and populate a StackAI knowledge base
  slug: stacks-ai-build-knowledge-base
- name: Monitor StackAI flow-run analytics
  slug: stacks-ai-monitor-flow-runs
- name: Run a deployed StackAI flow
  slug: stacks-ai-run-deployed-flow
slug: stacks-ai
tags:
- Company
- Artificial Intelligence
- Agents
- LLM
- No-Code
- Automation
- Workflows
- RAG
- Knowledge Base
- Enterprise
website: https://www.stackai.com/
---
