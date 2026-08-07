---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 7
apis:
- description: 'The core Mercor platform that matches expert humans to AI lab and enterprise demand for RLHF, SFT, evals, agent training, and frontier research projects. Domains covered include software engineering, '
  name: Mercor Talent Marketplace
  slug: mercor-platform
- description: Mercor's managed data-pipeline product for designing and operating large, expert-driven labeling and evaluation pipelines for AI training data.
  name: Mercor Data Pipelines
  slug: mercor-data-pipelines
- description: Mercor's developer-facing API documentation surface. Endpoint shapes and authentication details are not currently published openly; access is via Mercor's enterprise sales process.
  name: Mercor API
  slug: mercor-api
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
- group: auth
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
  url: https://www.mercor.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://talent.docs.mercor.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.mercor.com/docs/api/
- group: company
  title: ''
  type: Blog
  url: https://www.mercor.com/blog
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
  url: https://talent.docs.mercor.com/working/getting-started
- group: other
  title: ''
  type: X
  url: https://x.com/Mercor_ai
- group: agent
  title: ''
  type: LlmsText
  url: https://talent.docs.mercor.com/llms.txt
created: '2026-05-23'
description: Mercor is an AI-powered talent and human-intelligence marketplace that organizes expert humans to power frontier AI work. The platform routes specialized professionals (software engineers, finance and investment-banking experts, clinicians, attorneys, generalist consultants) to AI labs and enterprises for RLHF data, SFT data, agent training, evals, frontier research, and managed data pipelines. Mercor also ships APEX, a public research and benchmarking suite — APEX Benchmarks (AI Productivity Index), APEX-Agents Leaderboard, and APEX-SWE Leaderboard. Mercor maintains documentation hubs at mercor.com/docs and talent.docs.mercor.com (the expert-facing help center), and exposes a developer-facing documentation surface at mercor.com/docs/api. Public API endpoint details are not advertised on the open web at this time; this profile documents the product and documentation surfaces rather than endpoint shapes.
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
- name: Mercor Finops
  service_category: API
  slug: mercor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercor.png
integrations:
- description: Expert workflows and team coordination run over Slack channels.
  name: Slack
- description: Engineering experts integrate with customer GitHub repositories for code-related work.
  name: GitHub
- description: Mercor designs custom ingest and delivery pipelines per customer engagement.
  name: Custom Data Pipelines
layout: provider
modified: '2026-05-23'
name: Mercor
nav: Providers
network: true
overview: 'Mercor publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Talent Marketplace, Human Intelligence, RLHF, SFT, and AI Evals.


  Mercor''s developer surface includes developer portal, documentation, API reference, engineering blog, signup flow, support, and 6 more developer resources.'
plans:
- name: Mercor Plans Pricing
  plan_count: 1
  slug: mercor-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 2
  name: Mercor Rate Limits
  slug: mercor-rate-limits
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mercor/refs/heads/main/screenshots/mercor-2026-06-20T185214.png
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
- Data Pipelines
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
website: https://www.mercor.com
---
