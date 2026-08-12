---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The NeuBird production-operations API — projects, connections, investigation sessions, and root-cause analysis. Documented and driven through the official MCP server; authenticated with an Auth0-issue
  name: NeuBird API
  slug: neubird-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://neubird.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.neubird.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.neubird.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.neubird.ai/mcp/reference/tools/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.neubird.ai/mcp/getting-started/installation/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/neubird-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/neubird-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/neubird-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neubird-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/neubird-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neubird-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neubird-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.neubird.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/neubird-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neubird-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/neubird-sandbox.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neubirdai
- group: company
  title: ''
  type: Blog
  url: https://neubird.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://neubird.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.neubird.ai
- group: operate
  title: ''
  type: Support
  url: https://neubird.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neubird.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neubird.ai/legal
created: '2026-07-17'
description: NeuBird AI is "The Production Operations Agent" — an autonomous AI SRE platform that investigates, triages, and resolves production incidents. It connects to an organization's existing observability and operations stack (Datadog, Splunk, CloudWatch, PagerDuty, ServiceNow, Slack, Kubernetes, AWS, Azure, OpenShift and 30+ other tools) and delivers evidence-backed root-cause analysis in under three minutes without human investigation for L1/L2 incidents. NeuBird exposes its capabilities to developers and AI assistants through an official Model Context Protocol (MCP) server (@neubirdai/mcp-server-neubird, 33 tools), the NeuBird API at api.neubird.ai (Auth0-issued JWT bearer auth), a published community Agent Skills hub (FalconClaw SkillsHub, 17 skills), and the Neubird Falcon desktop workspace. Backed by Mayfield.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neubird.png
layout: provider
mcp_servers:
- description: ''
  name: neubird-mcp.yml
  slug: neubird-mcpyml
modified: '2026-07-20'
name: Neubird
nav: Providers
network: true
overview: 'Neubird publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI SRE, Incident Response, and Observability.


  Neubird''s developer surface includes documentation, API reference, quickstart, authentication, sandbox, engineering blog, pricing, and 17 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 38.0
  delta: -1.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 39.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neubird/refs/heads/main/screenshots/neubird-2026-08-07T184959.png
security:
- kind: authentication
  name: Neubird Authentication
  slug: neubird-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Neubird Domain Security
  slug: neubird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Neubird Trust Center
  slug: neubird-trust-center
  summary_line: SOC 2
slug: neubird
tags:
- Company
- Artificial Intelligence
- AI SRE
- Incident Response
- Observability
- DevOps
- AIOps
- Root Cause Analysis
- Model Context Protocol
- Agentic AI
website: https://neubird.ai
---
