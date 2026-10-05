---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Loadoptimizer Ai Agentic Access
  operation_count: 3
  slug: loadoptimizer-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.loadoptimizer.ai/v2
  baseurl_source: declared
  description: The Health API from LoadOptimizer.ai — 1 operation(s) for health.
  name: LoadOptimizer.ai Health API
  slug: loadoptimizer-ai-health-api
- baseURL: https://api.loadoptimizer.ai/v2
  baseurl_source: declared
  description: The Jobs API from LoadOptimizer.ai — 2 operation(s) for jobs.
  name: LoadOptimizer.ai Jobs API
  slug: loadoptimizer-ai-jobs-api
artifact_total: 8
asyncapis:
- description: ''
  name: Loadoptimizer Ai Webhooks
  slug: loadoptimizer-ai-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/capabilities/loadoptimizer-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/loadoptimizer-ai-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/agentic-access/loadoptimizer-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loadoptimizer-ai-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/plans/loadoptimizer-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loadoptimizer-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/rules/loadoptimizer-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/loadoptimizer-ai-rules.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/asyncapi/loadoptimizer-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/loadoptimizer-ai-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/conventions/loadoptimizer-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/loadoptimizer-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/conventions/loadoptimizer-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/loadoptimizer-ai-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/authentication/loadoptimizer-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loadoptimizer-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/conformance/loadoptimizer-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loadoptimizer-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/llms/loadoptimizer-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loadoptimizer-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/well-known/loadoptimizer-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loadoptimizer-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/hosts/loadoptimizer-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loadoptimizer-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.loadoptimizer.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loadoptimizer.ai/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.loadoptimizer.ai/auth/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.loadoptimizer.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.loadoptimizer.ai/docs/quickstart.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/loadoptimizer-ai/refs/heads/main/security/loadoptimizer-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loadoptimizer-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loadoptimizer.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.loadoptimizer.ai/docs/
created: '2026-10-02'
description: LoadOptimizer.ai provides an AI‑powered 3‑D load‑planning service for containers, trucks and pallets. Its API lets developers submit a job describing items, dimensions and constraints, then poll for a detailed load plan that optimizes space utilization, reduces trips and cuts costs. The platform supports REST/JSON with OpenAPI 3.1, offers idempotent job handling, and includes authentication via API keys. It targets logistics, shipping and warehousing companies seeking automated load optimization.
layout: provider
modified: '2026-10-02'
name: LoadOptimizer.ai
nav: Providers
network: true
overview: 'LoadOptimizer.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network: Health API and Jobs API. Tagged areas include Logistics, Artificial Intelligence, Load Planning, Optimization, and Shipping.


  The LoadOptimizer.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LoadOptimizer.ai''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Loadoptimizer Ai Plans Pricing
  plan_count: 5
  slug: loadoptimizer-ai-plans-pricing
random_paper: 8
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: LoadOptimizer.ai API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: loadoptimizer-ai-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 44.9
    developer_ergonomics: 37.5
    discoverability: 69.6
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Loadoptimizer Ai Authentication
  slug: loadoptimizer-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Loadoptimizer Ai Domain Security
  slug: loadoptimizer-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: loadoptimizer-ai
tags:
- Logistics
- Artificial Intelligence
- Load Planning
- Optimization
- Shipping
website: https://www.loadoptimizer.ai/
---
