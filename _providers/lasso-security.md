---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lasso Security Agentic Access
  operation_count: 2
  slug: lasso-security-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: The Classify API from Lasso Security — 2 operation(s) for classify.
  name: Lasso Security Classify API
  slug: lasso-security-classify-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lasso Security / Threat Detection Classify API
  slug: open-lasso-security-classify-api
- collection_type: open
  name: Lasso Security / Threat Detection Classify Masking API
  slug: open-lasso-security-masking-api
- collection_type: open
  name: Lasso Security Classify / Threat Detection API
  slug: open-lasso-security
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lasso-security-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lasso-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lasso-security-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lasso-security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lasso-security
- group: company
  title: ''
  type: Website
  url: https://www.lasso.security/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lasso.security/platform/lasso-for-applications
- group: commercial
  title: ''
  type: Plans
  url: plans/lasso-security-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lasso-security-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lasso-security-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lasso.security/blog
created: '2026-06-20'
description: Lasso Security is a GenAI security platform that protects every LLM and AI agent touchpoint. Its Deputy gateway inspects LLM and MCP traffic in real time, and the Classify / Threat Detection API scores prompts and completions for prompt injection, jailbreaks, PII, and harmful content, returning structured BLOCK / WARN / AUTO_MASKING findings.
finops:
- name: Lasso Security Finops
  service_category: Security
  slug: lasso-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lasso-security.png
layout: provider
modified: '2026-06-20'
name: Lasso Security
nav: Providers
network: true
overview: 'Lasso Security publishes 1 API on the [APIs.io](https://apis.io/) network: Classify API. Tagged areas include Artificial Intelligence, LLM, GenAI Security, Prompt Injection, and Guardrails.


  Lasso Security''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Lasso Security Plans Pricing
  plan_count: 3
  slug: lasso-security-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Lasso Security Rate Limits
  slug: lasso-security-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lasso-security/refs/heads/main/screenshots/lasso-security-2026-06-20T184320.png
security:
- kind: authentication
  name: Lasso Security Authentication
  slug: lasso-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lasso Security Domain Security
  slug: lasso-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lasso-security
tags:
- Artificial Intelligence
- LLM
- GenAI Security
- Prompt Injection
- Guardrails
- MCP
website: https://www.lasso.security/
---
