---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://protectai.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.paloaltonetworks.com/ai-security/prisma-airs — a different registrable domain (protectai.com -> paloaltonetworks.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Protectai Agentic Access
  operation_count: 8
  slug: protectai-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: Commercial AI model security product that scans first- and third-party models for serialization attacks, malicious code, and supply-chain threats before they reach production. The open-source ModelSca
  name: Guardian (Model Scanning)
  slug: guardian-model-scanning
- description: 'Commercial automated red-teaming product that rigorously tests LLM and GenAI applications for vulnerabilities, jailbreaks, and policy violations. Delivered as a sales-led platform; no public REST API '
  name: Recon (Red-Teaming)
  slug: recon-red-teaming
- description: Commercial runtime security product that monitors and controls AI applications in production with deep visibility and inline threat prevention. Delivered as a sales-led platform; no public REST API su
  name: Layer (Runtime)
  slug: layer-runtime
- baseURL: http://localhost:8000
  baseurl_source: declared
  description: The Output API from Protect AI — 2 operation(s) for output.
  name: Protect AI Output API
  slug: protectai-output-api
- baseURL: http://localhost:8000
  baseurl_source: declared
  description: The Prompt API from Protect AI — 2 operation(s) for prompt.
  name: Protect AI Prompt API
  slug: protectai-prompt-api
- baseURL: http://localhost:8000
  baseurl_source: declared
  description: The System API from Protect AI — 4 operation(s) for system.
  name: Protect AI System API
  slug: protectai-system-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LLM Guard Output API
  slug: open-protectai-output-api
- collection_type: open
  name: LLM Guard Output Prompt API
  slug: open-protectai-prompt-api
- collection_type: open
  name: LLM Guard Output System API
  slug: open-protectai-system-api
- collection_type: open
  name: LLM Guard API
  slug: open-protectai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/protectai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/protectai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/protectai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/protectai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/protect-ai
- group: company
  title: ''
  type: Website
  url: https://protectai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://llm-guard.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/protectai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/protectai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/protectai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://protectai.com/blog/rss.xml
created: '2026-06-20'
description: Protect AI is an AI/ML security platform (now part of Palo Alto Networks) whose products secure the AI lifecycle from model selection to runtime. Its developer surface centers on LLM Guard, an open-source Python toolkit of prompt and output scanners that ships a self-hostable REST API for real-time input/output sanitization. Commercial products - Guardian (model scanning), Recon (LLM red-teaming), and Layer (runtime protection) - are delivered through a portal under sales-led terms.
finops:
- name: Protectai Finops
  service_category: Security
  slug: protectai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/protectai.png
layout: provider
modified: '2026-06-20'
name: Protect AI
nav: Providers
network: true
overview: 'Protect AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Output API, Prompt API, and System API. Tagged areas include Artificial Intelligence, ML, Security, LLM, and Guardrails.


  Protect AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Protectai Plans Pricing
  plan_count: 3
  slug: protectai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Protectai Rate Limits
  slug: protectai-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.4
    developer_ergonomics: 22.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/protectai/refs/heads/main/screenshots/protectai-2026-06-20T192215.png
security:
- kind: authentication
  name: Protectai Authentication
  slug: protectai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Protectai Domain Security
  slug: protectai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: protectai
tags:
- Artificial Intelligence
- ML
- Security
- LLM
- Guardrails
website: https://protectai.com/
---
