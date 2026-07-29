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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Protectai Agentic Access
  operation_count: 8
  slug: protectai-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 6
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
- description: The Output API from Protect AI — 2 operation(s) for output.
  name: Protect AI Output API
  slug: protectai-output-api
- description: The Prompt API from Protect AI — 2 operation(s) for prompt.
  name: Protect AI Prompt API
  slug: protectai-prompt-api
- description: The System API from Protect AI — 4 operation(s) for system.
  name: Protect AI System API
  slug: protectai-system-api
artifact_total: 13
collections:
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
overview: 'Protect AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Output API, Prompt API, and System API. Tagged areas include AI, ML, Security, LLM, and Guardrails.


  Protect AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Protectai Plans Pricing
  plan_count: 3
  slug: protectai-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 2
  name: Protectai Rate Limits
  slug: protectai-rate-limits
score:
  band: thin
  composite: 35.2
  delta: -3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- AI
- ML
- Security
- LLM
- Guardrails
website: https://protectai.com/
---
