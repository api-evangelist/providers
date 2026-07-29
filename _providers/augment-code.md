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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: 'Cosmos is Augment''s unified agents platform for agentic software development at organizational scale. It bundles specialized agents — Work Dispatcher (triage), PR Author (first commit through merge), '
  name: Augment Cosmos
  slug: cosmos
- description: Auggie is Augment's command-line interface that brings the Augment agent, Context Engine, and tool integrations to the terminal for local development.
  name: Auggie CLI
  slug: auggie-cli
- description: IDE plugin that surfaces Augment's Context Engine and agent capabilities inside Visual Studio Code for completion, chat, and inline edits.
  name: Augment for Visual Studio Code
  slug: vscode-plugin
- description: IDE plugin for IntelliJ IDEA, PyCharm, GoLand, and other JetBrains IDEs.
  name: Augment for JetBrains
  slug: jetbrains-plugin
- description: Proprietary indexing and retrieval engine that gives Augment's agents codebase-aware context — intelligent file selection, organization knowledge, and shared memory across agents — and underpins every
  name: Augment Context Engine
  slug: context-engine
artifact_total: 26
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/augment-code-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/augment-code-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.augmentcode.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.augmentcode.com
- group: company
  title: ''
  type: Blog
  url: https://www.augmentcode.com/blog
- group: start
  title: ''
  type: Signup
  url: https://www.augmentcode.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.augmentcode.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://docs.augmentcode.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.augmentcode.com/llms.txt
created: '2026-05-23'
description: Augment Code is a context-aware AI platform for software engineering teams. The flagship is Cosmos, a "unified agents platform" for agentic software development at organizational scale, packaged as a set of specialized agents — Work Dispatcher (triages tickets), PR Author (drives tasks from first commit through merge), Pair Review and Deep Code Review (inline review feedback), and Tester (verification of changes end-to-end). The product also ships the Auggie CLI for local use and IDE plugins for Visual Studio Code and JetBrains. Augment is built around a proprietary Context Engine for codebase understanding and a unified agents runtime with scheduling, sandboxed execution, and human-in-the-loop escalation. Deployment options span local, managed cloud, customer cloud (AWS, GCP), and on-premises. As of this writing Augment does not advertise a public REST API — it is a product-led, partner-driven surface — so this profile documents the product surfaces and developer resources
  rather than endpoint shapes.
features:
- description: Codebase-aware indexing and retrieval that powers every agent and IDE integration.
  name: Context Engine
- description: Cosmos runs Work Dispatcher, PR Author, Pair Review, Deep Code Review, and Tester agents under one scheduling and sandboxing layer.
  name: Unified Agents Platform
- description: Agents escalate to humans when confidence drops or policy requires review.
  name: Human-in-the-Loop
- description: Shared knowledge and memory across agents and engineers in the same org.
  name: Organizational Memory
- description: Bring Augment's agent and Context Engine to a local terminal.
  name: Auggie CLI
- description: First-party VS Code and JetBrains plugins.
  name: IDE Plugins
- description: Run on local laptops and dev VMs, in managed Augment cloud, in customer-owned AWS or GCP, or fully on-premises.
  name: Flexible Deployment
finops:
- name: Augment Code Finops
  service_category: API
  slug: augment-code-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/augment-code.png
integrations:
- description: PR Author opens and updates pull requests; Pair Review and Deep Code Review post inline review feedback.
  name: GitHub
- description: Agent notifications and human-in-the-loop interactions in Slack channels.
  name: Slack
- description: Work Dispatcher reads tickets and routes work to specialized agents.
  name: Jira
- description: Cosmos integrates with CI for build, test, and verification signal.
  name: CI Systems
- description: Customer-cloud deployment supported on AWS and GCP, plus on-premises.
  name: AWS and GCP
layout: provider
modified: '2026-05-23'
name: Augment Code
nav: Providers
network: true
overview: 'Augment Code publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Coding Agent, Context Engine, IDE Plugin, Cosmos, and Auggie CLI.


  Augment Code''s developer surface includes developer portal, documentation, engineering blog, signup flow, pricing, support, and 3 more developer resources.'
plans:
- name: Augment Code Plans Pricing
  plan_count: 1
  slug: augment-code-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 2
  name: Augment Code Rate Limits
  slug: augment-code-rate-limits
score:
  band: emerging
  composite: 23.5
  delta: -2.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/augment-code/refs/heads/main/screenshots/augment-code-2026-06-20T172557.png
security:
- kind: domain-security
  name: Augment Code Domain Security
  slug: augment-code-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Augment Code Trust Center
  slug: augment-code-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: augment-code
tags:
- AI Coding Agent
- Context Engine
- IDE Plugin
- Cosmos
- Auggie CLI
- Software Engineering
use_cases:
- description: Work Dispatcher triages tickets and dispatches work to PR Author, which drives commits through merge.
  name: Ticket-to-PR Automation
- description: Pair Review and Deep Code Review give inline PR feedback at organization scale.
  name: Automated Code Review
- description: The Tester agent exercises changes end-to-end before they ship.
  name: Test Generation and Verification
- description: IDE plugins and Auggie CLI let individual engineers code with the Context Engine in the loop.
  name: Codebase-Aware Development
website: https://www.augmentcode.com
---
