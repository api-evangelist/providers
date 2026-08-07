---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 259
  human_in_the_loop: 15
  name: H2O Ai Agentic Access
  operation_count: 429
  slug: h2o-ai-agentic-access
  summary_line: 429 operations · 259 acting · 15 human-in-the-loop
api_count: 3
apis:
- description: The Enterprise h2oGPTe REST API is the machine-readable contract for H2O.ai's private generative-AI platform. It exposes 422 operations across 24 tags — Collections, Documents, Document Ingestion, Cha
  name: Enterprise h2oGPTe REST API
  slug: h2o-ai-enterprise-h2ogpte
- description: The H2O MLOps Scoring REST API is the runtime scoring contract for models deployed through H2O MLOps. It exposes seven operations on a deployed model endpoint — retrieve the model id, retrieve the mod
  name: H2O MLOps Scoring REST API
  slug: h2o-ai-mlops-scoring
- description: H2OGPTe MCP Server is H2O.ai's first-party Model Context Protocol server for Enterprise h2oGPTe. It runs locally over stdio and proxies traffic to the h2oGPTe REST API, generating one MCP tool per RES
  name: h2oGPTe MCP Server
  slug: h2o-ai-h2ogpte-mcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://h2o.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.h2o.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://h2ogpte.genai.h2o.ai/swagger-ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.h2o.ai/enterprise-h2ogpte/get-started
- group: operate
  title: ''
  type: Support
  url: https://support.h2o.ai/
- group: company
  title: ''
  type: Blog
  url: https://h2o.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/h2oai
- group: start
  title: ''
  type: SignUp
  url: https://genai.h2o.ai/appstore
- group: commercial
  title: ''
  type: TermsOfService
  url: https://h2o.ai/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://h2o.ai/legal/privacy/
- group: auth
  title: ''
  type: Security
  url: https://h2o.ai/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.h2o.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/h2o-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/h2o-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/h2o-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/h2o-ai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/h2o-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/h2o-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/h2o-ai-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/h2o-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/h2o-ai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/h2o-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/h2o-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/h2o-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://h2oai.statuspage.io/
- group: design
  title: ''
  type: Conventions
  url: conventions/h2o-ai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/h2o-ai-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/h2o-ai-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/h2o-ai-sandbox.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/h2o-ai-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: H2O.ai is an open-source artificial-intelligence and machine-learning company whose platform spans H2O-3 (a distributed, in-memory ML engine), H2O Driverless AI (automatic machine learning), H2O MLOps (model deployment, scoring and monitoring), H2O Wave (a Python/R framework for realtime AI apps), H2O LLM Studio, and Enterprise h2oGPTe (a private generative-AI, RAG and agent platform). Enterprise h2oGPTe publishes a 422-operation OpenAPI 3.0.1 contract covering collections, document ingestion, chat, agents, extractors, GraphRAG, guardrails, models, permissions and scheduled tasks, and H2O MLOps publishes an OpenAPI contract for its model-scoring endpoints. H2O.ai also ships a first-party MCP server that proxies the h2oGPTe REST API to agent clients, together with official Python, R, Java and JavaScript client libraries distributed via PyPI, CRAN, Maven Central and npm.
image: https://avatars.githubusercontent.com/u/1402695?v=4
layout: provider
mcp_servers:
- description: ''
  name: h2o-ai-mcp.yml
  slug: h2o-ai-mcpyml
modified: '2026-08-04'
name: H2O.ai
nav: Providers
network: true
overview: 'H2O.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network: Enterprise h2oGPTe REST API and H2O MLOps Scoring REST API. Tagged areas include Company, Artificial Intelligence, Machine Learning, MLOps, and Generative AI.


  H2O.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 60
score:
  band: developing
  composite: 53.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.3
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: H2O Ai Authentication
  slug: h2o-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: H2O Ai Domain Security
  slug: h2o-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: H2O Ai Vulnerability Disclosure
  slug: h2o-ai-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: H2O Ai Trust Center
  slug: h2o-ai-trust-center
  summary_line: SOC 2 Type 2, FedRAMP High, IRAP, HITECH
slug: h2o-ai
tags:
- Company
- Artificial Intelligence
- Machine Learning
- MLOps
- Generative AI
- Large Language Models
- Retrieval Augmented Generation
- Data Science
- Model Deployment
- AI Agents
- Enterprise AI
website: https://h2o.ai/
---
