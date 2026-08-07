---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Jentic Agentic Access
  operation_count: 4
  slug: jentic-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 8
apis:
- description: The Jentic Remote MCP Server is the hosted Model Context Protocol endpoint that exposes the Jentic catalog to MCP-capable clients (Claude Desktop, ChatGPT, Cursor, Windsurf, VS Code). It speaks the sa
  name: Jentic Remote MCP Server
  slug: jentic-mcp
- description: Open-source Python engine that executes Arazzo workflow specifications alongside OpenAPI operation definitions. Powers the Jentic platform's workflow execution and is also installable standalone as ar
  name: Arazzo Engine
  slug: arazzo-engine
- description: 'Open-source composable reasoning agent framework that plans, acts, and recovers from failures, preconfigured with Jentic tools and a ReWOO reasoning loop. Primary entry point is the ReWOOAgent Python '
  name: Jentic Standard Agent
  slug: standard-agent
- description: 'Free, open-source, self-hosted API execution layer that sits between an agent and the outside world. The agent says what it wants to do and Jentic Mini handles the how: finding the right API, injectin'
  name: Jentic Mini
  slug: jentic-mini
- description: Technical specification for evaluating how interpretable, operable, and trustworthy an API is for AI systems and autonomous agents. Defines the signals, dimensions, scoring model, and normalization ru
  name: Jentic API AI-Readiness Framework (JAIRF)
  slug: jairf
- description: Registration and API key management for accessing the Jentic platform.
  name: Jentic Authentication API
  slug: jentic-authentication-api
- description: Load execution details and execute API operations or Arazzo workflows with managed authentication and credential injection.
  name: Jentic Execution API
  slug: jentic-execution-api
- description: Semantic search over the Jentic API and workflow catalog using natural language queries.
  name: Jentic Search API
  slug: jentic-search-api
artifact_total: 33
collections:
- collection_type: postman
  name: Jentic Authentication API
  slug: postman-jentic-authentication-api
- collection_type: postman
  name: Jentic Authentication Execution API
  slug: postman-jentic-execution-api
- collection_type: postman
  name: Jentic Authentication Search API
  slug: postman-jentic-search-api
- collection_type: open
  name: Jentic API
  slug: open-jentic
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jentic/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jentic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jentic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jentic-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://jentic.com/
- group: company
  title: ''
  type: Blog
  url: https://jentic.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jentic.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://jentic.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.jentic.com/sign-up
- group: start
  title: ''
  type: Console
  url: https://app.jentic.com/
- group: operate
  title: ''
  type: Contact
  url: https://jentic.com/contact
- group: company
  title: ''
  type: About
  url: https://jentic.com/company
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jentic
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jentic.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jentic.com/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jentic
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@JenticAI
- group: operate
  title: ''
  type: Support
  url: https://docs.jentic.com/community/support/
- group: operate
  title: ''
  type: FAQ
  url: https://docs.jentic.com/community/faq/
- group: auth
  title: ''
  type: Security
  url: https://docs.jentic.com/community/security/
- group: other
  title: ''
  type: Contributing
  url: https://docs.jentic.com/community/contributing/
- group: company
  title: ''
  type: Press
  url: https://jentic.com/blog/press
- group: company
  title: ''
  type: BlogFeed
  url: https://jentic.com/blog/feed.xml
- group: build
  title: ''
  type: PythonPackage
  url: https://pypi.org/project/jentic/
- group: build
  title: ''
  type: PythonPackage
  url: https://pypi.org/project/arazzo-runner/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/jentic-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jentic-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jentic-operation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jentic-agent-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jentic-workflow-schema.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/jentic/jentic-skills
created: '2026-01-02'
description: Jentic is an AI infrastructure company building the agentic knowledge layer for APIs. Founded in late 2024 and backed by $4.5M in pre-seed funding, Jentic enables enterprises to confidently manage, scale, and govern AI agent initiatives in a unified platform built on open standards. The platform provides secure execution, managed authentication, unified permissions, and observability for AI agents accessing 1,500+ public APIs and 2,000+ agent-ready workflows. Jentic's bet is that AI agents need a standards-based control plane built on OpenAPI plus Arazzo workflows plus MCP, rather than ad-hoc tool wiring inside every agent framework. The platform ships the Jentic Public APIs catalog, the Arazzo Engine (workflow runner), the Standard Agent (a composable ReWOO-style reasoning agent), the Jentic Mini self-hosted execution layer, a hosted Remote MCP server at api.jentic.com/mcp, and the Jentic API AI-Readiness Framework (JAIRF) for scoring API readiness for agents.
examples:
- key_count: 5
  name: Jentic Execute Example
  slug: jentic-execute-example
- key_count: 5
  name: Jentic Load Example
  slug: jentic-load-example
- key_count: 5
  name: Jentic Register Example
  slug: jentic-register-example
- key_count: 5
  name: Jentic Search Example
  slug: jentic-search-example
- key_count: 6
  name: Jentic Workflow Execute Example
  slug: jentic-workflow-execute-example
finops:
- name: Jentic Finops
  service_category: AI Agent Platform
  slug: jentic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jentic.png
json_schemas:
- name: Jentic Agent
  property_count: 9
  slug: jentic-agent
- name: Jentic Operation
  property_count: 10
  slug: jentic-operation
- name: Jentic Workflow
  property_count: 10
  slug: jentic-workflow
json_structures:
- name: Jentic Operation Structure
  property_count: 0
  slug: jentic-operation-structure
jsonld:
- class_count: 0
  name: Jentic Context
  property_count: 6
  slug: jentic-context
layout: provider
modified: '2026-05-19'
name: Jentic
nav: Providers
network: true
overview: 'Jentic publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Execution API, and Search API. Tagged areas include AI Agents, Arazzo, OpenAPI, MCP, and Workflows.


  The Jentic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Jentic''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, developer console, YouTube channel, and 24 more developer resources.'
plans:
- name: Jentic Plans Pricing
  plan_count: 2
  slug: jentic-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 4
  name: Jentic Rate Limits
  slug: jentic-rate-limits
rules:
- name: Jentic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: jentic-jsonschema-spectral-rules
- name: Jentic API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 5
  slug: jentic-rules
score:
  band: strong
  composite: 60.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 79.8
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jentic/refs/heads/main/screenshots/jentic-2026-06-20T183721.png
security:
- kind: authentication
  name: Jentic Authentication
  slug: jentic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jentic Domain Security
  slug: jentic-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 3
skills:
- name: jentic-v1
  slug: jentic-v1
- name: jentic-workflows
  slug: jentic-workflows
- name: jentic
  slug: jentic
slug: jentic
tags:
- AI Agents
- Arazzo
- OpenAPI
- MCP
- Workflows
- Integrations
- Agent Runtime
- Standard Agent
- Just In Time Tooling
- Credential Vault
- Agent Governance
- Observability
- API AI Readiness
website: https://jentic.com/
---
