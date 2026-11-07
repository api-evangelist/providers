---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: 'The core Mercor platform that matches expert humans to AI lab and enterprise demand for RLHF, SFT, evals, agent training, and frontier research projects. Domains covered include software engineering, '
  name: Mercor Talent Marketplace
  slug: mercor-platform
- description: Mercor's managed data-pipeline product for designing and operating large, expert-driven labeling and evaluation pipelines for AI training data.
  name: Mercor Data Pipelines
  slug: mercor-data-pipelines
- description: Mercor's public AI productivity benchmark and research surface. APEX measures how well AI models perform real expert-grade work.
  name: APEX Benchmarks (AI Productivity Index)
  slug: apex-benchmarks
- description: Public leaderboard for AI agent performance run by Mercor's research team.
  name: APEX-Agents Leaderboard
  slug: apex-agents-leaderboard
- description: Public leaderboard for AI software-engineering performance run by Mercor's research team.
  name: APEX-SWE Leaderboard
  slug: apex-swe-leaderboard
- description: Public benchmark / task-submission framework published by Mercor (terminal-bench-3 on GitHub) for evaluating AI agents on terminal-based engineering tasks.
  name: Terminal-Bench
  slug: terminal-bench
artifact_total: 24
common:
- group: design
  href: https://artifacts.apis.io/mercor/conformance/mercor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mercor-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mercor/llms/mercor-www-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mercor-www-llms.txt
- group: agent
  href: https://artifacts.apis.io/mercor/llms/mercor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mercor-llms.txt
- group: other
  href: https://artifacts.apis.io/mercor/a2a/mercor-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mercor-a2a.yml
- group: agent
  href: https://artifacts.apis.io/mercor/well-known/mercor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mercor-well-known.yml
- group: other
  href: https://artifacts.apis.io/mercor/hosts/mercor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mercor-hosts.yml
- group: other
  href: https://artifacts.apis.io/mercor/vendors/mercor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mercor-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/mercor/finops/mercor-finops.yml
  title: ''
  type: FinOps
  url: finops/mercor-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.mercor.com/
- group: auth
  href: https://artifacts.apis.io/mercor/security/mercor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mercor-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.mercor.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.mercor.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://talent.docs.mercor.com
- group: company
  title: ''
  type: Blog
  url: https://www.mercor.com/blog/
- group: company
  title: ''
  type: Careers
  url: https://www.mercor.com/careers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mercor-io
- group: start
  title: ''
  type: Signup
  url: https://www.mercor.com/experts/
- group: operate
  title: ''
  type: Support
  url: https://talent.docs.mercor.com/
- group: other
  title: ''
  type: X
  url: https://x.com/mercor
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mercor-Intelligence
- group: start
  title: ''
  type: GettingStarted
  url: https://talent.docs.mercor.com/working/getting-started
- group: start
  title: ''
  type: Login
  url: https://work.mercor.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mercor.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mercor.com/privacy-notice/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mercor.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.mercor.com/newsroom/
- group: operate
  title: ''
  type: Contact
  url: https://www.mercor.com/partner/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercor-ai/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@mercor-ai
- group: agent
  title: ''
  type: LlmsText
  url: https://talent.docs.mercor.com/llms.txt
coverage:
  checked: '2026-10-27'
  detail: Mercor's Mintlify docs host docs.mercor.com 307-redirects every path, including /openapi.json and /api-reference, to /login, and its /mcp answers 401, while the public www.mercor.com/docs/api/ is a soft-404 page.
  evidence:
  - status: 307
    url: https://docs.mercor.com/openapi.json
  - status: 307
    url: https://docs.mercor.com/api-reference
  - status: 401
    url: https://docs.mercor.com/mcp
  - status: 200
    url: https://www.mercor.com/docs/api/
  reason: customer-only-docs
  state: gated
created: '2026-05-23'
description: 'Mercor is an AI-powered talent and human-intelligence marketplace that organizes expert humans to power frontier AI work (its site: "organizing human intelligence to power the AI economy"). The platform routes specialized professionals (software engineers, finance and investment-banking experts, clinicians, attorneys, generalist consultants) to AI labs and enterprises for RLHF data, SFT data, agent training, evals, frontier research, and managed data pipelines. Mercor also publishes APEX, a public research and benchmarking suite (AI Productivity Index, APEX-Agents, APEX-SWE and partner leaderboards). Mercor maintains guides at mercor.com/docs, an expert-facing help center at talent.docs.mercor.com, and a trust center at trust.mercor.com. No public API reference is published: mercor.com/docs/api/ returns a not-found page (checked 2026-10-27).'
features:
- description: Routes expert humans across software engineering, finance, healthcare, legal, and consulting into AI lab and enterprise projects.
  name: AI Talent Marketplace
- description: Provides preference, reward, and demonstration data for foundation-model training.
  name: RLHF and SFT Data
- description: Specialist data for training and evaluating AI agents.
  name: Agent Training Data
- description: End-to-end design and operation of expert-driven labeling and evaluation pipelines.
  name: Managed Data Pipelines
- description: Public benchmarks (AI Productivity Index, APEX-Agents, APEX-SWE) measuring real-world AI performance.
  name: APEX Research Suite
- description: Open-source benchmark and task-submission framework for AI agents on terminal engineering tasks.
  name: Terminal-Bench
finops:
- has_sources: false
  method: generated
  name: Mercor Finops
  primary_unit: ''
  service_category: API
  slug: mercor-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercor.png
integrations:
- description: Expert workflows and team coordination run over Slack channels.
  name: Slack
- description: Engineering experts integrate with customer GitHub repositories for code-related work.
  name: GitHub
- description: Mercor designs custom ingest and delivery pipelines per customer engagement.
  name: Custom Data Pipelines
layout: provider
mcp_servers:
- description: Remote MCP server at docs.mercor.com over HTTP requiring OAuth.
  name: Mercor docs MCP server
  slug: mercor
modified: '2026-10-27'
name: Mercor
nav: Providers
network: true
overview: 'Mercor is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Talent Marketplace, Human Intelligence, RLHF, SFT, and AI Evals.


  Mercor''s developer surface includes developer portal, documentation, engineering blog, signup flow, support, getting-started guide, YouTube channel, and 23 more developer resources.'
plans:
- name: Mercor Plans Pricing
  plan_count: 0
  slug: mercor-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Mercor Rate Limits
  slug: mercor-rate-limits
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 72.5
    operational_transparency: 2.6
  previous_composite: 28.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mercor/mercor-2026-06-20T185214.png
security:
- kind: domain-security
  name: Mercor Domain Security
  slug: mercor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mercor
tags:
- Talent Marketplace
- Human Intelligence
- RLHF
- SFT
- AI Evals
- Data Pipeline
- APEX Benchmarks
use_cases:
- description: Source preference and reward data from domain experts for RLHF.
  name: Frontier Model RLHF
- description: Capture demonstrations of expert workflows for supervised fine-tuning.
  name: Expert SFT Data
- description: Benchmark agent performance against expert-graded tasks via APEX and Terminal-Bench.
  name: AI Agent Evaluation
- description: Stand up managed labeling and evaluation pipelines for enterprise AI programs.
  name: Enterprise Data Engineering
website: https://www.mercor.com/
---
