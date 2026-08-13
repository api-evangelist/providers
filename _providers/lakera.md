---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Lakera Agentic Access
  operation_count: 7
  slug: lakera-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 6
apis:
- description: 'Lakera Guard is a low-latency screening API that inspects text content sent to or from LLMs and flags threats including prompt injection, jailbreaks, PII, profanity, and policy violations. The /guard '
  name: Lakera Guard
  slug: lakera-guard
- description: Lakera Red is an automated red teaming product that probes GenAI applications for jailbreaks, prompt injection, data leakage, and other adversarial failures, then produces a risk-based remediation rep
  name: Lakera Red
  slug: lakera-red
- description: Gandalf is Lakera's free interactive game that teaches prompt injection by challenging players to extract a secret from an LLM across progressively harder defenses. It has become a primary research an
  name: Gandalf
  slug: gandalf
- description: Screen prompts and model responses for threats
  name: Lakera Guard API
  slug: lakera-guard-api
- description: Kubernetes-style health and lifecycle probes (self-hosted)
  name: Lakera Health API
  slug: lakera-health-api
- description: Policy validation (self-hosted)
  name: Lakera Policies API
  slug: lakera-policies-api
artifact_total: 34
collections:
- collection_type: open
  name: Lakera Guard API
  slug: open-lakera
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lakera-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lakera-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lakera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lakera-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lakera-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lakera.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakera.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lakera.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lakera.ai/docs/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.lakera.ai/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.lakera.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lakera.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://platform.lakera.ai/login
- group: start
  title: ''
  type: Signup
  url: https://platform.lakera.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lakeraai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lakeraai/
- group: other
  title: ''
  type: Events
  url: https://www.lakera.ai/events
- group: other
  title: ''
  type: Game
  url: https://gandalf.lakera.ai/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lakera.ai/llms.txt
created: '2026-05-23'
description: Lakera is an AI security company building runtime defenses for generative AI applications. Its flagship Lakera Guard API screens prompts and responses for prompt injection, jailbreaks, PII leakage, unsafe content, and policy violations, while Lakera Red provides automated red teaming and risk assessment for GenAI systems. Lakera follows an API-first architecture with a managed SaaS platform, regional endpoints, self-hosted deployments for regulated environments, and a free Gandalf training game that has driven much of the prompt injection research community.
features:
- description: Detects direct and indirect prompt injection attempts targeting LLM-powered applications and agents.
  name: Prompt Injection Detection
- description: Identifies attempts to bypass system prompts, safety policies, and model guardrails.
  name: Jailbreak Detection
- description: Screens prompts and responses for personally identifiable information leakage.
  name: PII Detection
- description: Flags unsafe, toxic, or policy-violating content in user inputs and model outputs.
  name: Content Moderation
- description: Configurable detection policies scoped to projects, models, and use cases.
  name: Custom Policies
- description: Hosted endpoints in US, EU, and APAC regions for data residency and latency.
  name: Regional Endpoints
- description: On-premises and VPC deployments for regulated industries that cannot send data to a SaaS.
  name: Self-Hosted Deployment
- description: Model Context Protocol server for embedding Lakera Guard into AI clients like Claude Code and Cursor.
  name: MCP Server
finops:
- name: Lakera Finops
  service_category: API
  slug: lakera-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lakera.png
integrations:
- description: Wrap OpenAI calls with Guard screening for input and output safety.
  name: OpenAI
- description: Screen prompts and responses from Anthropic Claude models.
  name: Anthropic
- description: Drop-in callbacks and chains for integrating Guard into LangChain applications.
  name: LangChain
- description: Screen queries and retrieved context in LlamaIndex RAG pipelines.
  name: LlamaIndex
- description: MCP server for surfacing Lakera Guard inside Claude Code, Cursor, and other MCP clients.
  name: Model Context Protocol
- description: Self-hosted Helm-based deployments with health, readiness, and liveness probes.
  name: Kubernetes
layout: provider
modified: '2026-05-23'
name: Lakera
nav: Providers
network: true
overview: 'Lakera publishes 3 APIs on the [APIs.io](https://apis.io/) network: Guard API, Health API, and Policies API. Tagged areas include AI Security, LLM Security, Prompt Injection, Guardrails, and Red Teaming.


  Lakera''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Lakera Plans Pricing
  plan_count: 1
  slug: lakera-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 2
  name: Lakera Rate Limits
  slug: lakera-rate-limits
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.7
    developer_ergonomics: 39.1
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lakera/refs/heads/main/screenshots/lakera-2026-06-20T184245.png
security:
- kind: authentication
  name: Lakera Authentication
  slug: lakera-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lakera Domain Security
  slug: lakera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lakera Vulnerability Disclosure
  slug: lakera-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lakera Trust Center
  slug: lakera-trust-center
  summary_line: GDPR
slug: lakera
tags:
- AI Security
- LLM Security
- Prompt Injection
- Guardrails
- Red Teaming
- GenAI
- API
use_cases:
- description: Screen inputs and outputs of chatbots, copilots, and RAG applications for prompt injection and unsafe content.
  name: LLM Application Guardrails
- description: Inspect tool inputs, retrieved context, and agent reasoning steps for indirect prompt injection.
  name: AI Agent Protection
- description: Govern employee use of public LLMs and prevent sensitive data exfiltration.
  name: Workforce AI Security
- description: Run automated adversarial assessments against pre-production GenAI applications.
  name: GenAI Red Teaming
- description: Self-host Guard in financial services, healthcare, and government environments with strict data residency.
  name: Regulated Industry Deployments
website: https://www.lakera.ai/
---
