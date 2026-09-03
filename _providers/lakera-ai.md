---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Lakera Ai Agentic Access
  operation_count: 12
  slug: lakera-ai-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 2
apis:
- baseURL: https://api.lakera.ai/v2
  baseurl_source: spec
  description: Screen LLM inputs and outputs for threats.
  name: Lakera Guard API
  slug: lakera-ai-guard-api
- baseURL: https://api.lakera.ai/v2
  baseurl_source: spec
  description: Create and manage Lakera Guard policies.
  name: Lakera Policies API
  slug: lakera-ai-policies-api
- baseURL: https://api.lakera.ai/v2
  baseurl_source: spec
  description: Create and manage projects bound to policies.
  name: Lakera Projects API
  slug: lakera-ai-projects-api
- baseURL: https://api.lakera.ai/v2
  baseurl_source: spec
  description: Retrieve detector confidence levels without runtime enforcement.
  name: Lakera Results API
  slug: lakera-ai-results-api
artifact_total: 52
collections:
- collection_type: postman
  name: Lakera Guard API
  slug: postman-lakera-ai-guard-api
- collection_type: postman
  name: Lakera Guard Policies API
  slug: postman-lakera-ai-policies-api
- collection_type: postman
  name: Lakera Guard Projects API
  slug: postman-lakera-ai-projects-api
- collection_type: postman
  name: Lakera Guard Results API
  slug: postman-lakera-ai-results-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lakera Guard API
  slug: open-lakera-ai-guard-api
- collection_type: open
  name: Lakera Guard Policies API
  slug: open-lakera-ai-policies-api
- collection_type: open
  name: Lakera Guard Projects API
  slug: open-lakera-ai-projects-api
- collection_type: open
  name: Lakera Guard Results API
  slug: open-lakera-ai-results-api
- collection_type: open
  name: Lakera Guard API
  slug: open-lakera-guard-api
- collection_type: open
  name: Lakera Platform API
  slug: open-lakera-platform-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lakera/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lakera-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lakera-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lakera-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lakera-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lakera-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lakeraai
- group: start
  title: ''
  type: Portal
  url: https://www.lakera.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakera.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakera.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lakera.ai/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakera.ai/guard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakera.ai/docs/integration
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakera.ai/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.lakera.ai/_mcp/server
- group: start
  title: ''
  type: Portal
  url: https://platform.lakera.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.lakera.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.lakera.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.lakera.ai/blog
- group: company
  title: ''
  type: Press
  url: https://www.lakera.ai/news
- group: other
  title: ''
  type: CaseStudy
  url: https://www.lakera.ai/customers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lakera.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lakera.ai/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lakera.ai
- group: start
  title: ''
  type: Sandbox
  url: https://gandalf.lakera.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lakeraai
- group: build
  title: ''
  type: Tools
  url: https://github.com/lakeraai/pint-benchmark
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/lakeraai/guard-demo-client
- group: build
  title: ''
  type: Tools
  url: https://github.com/lakeraai/chrome-extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/lakeraai/canica
- group: build
  title: ''
  type: Tools
  url: https://github.com/lakeraai/dsec-gandalf
- group: build
  title: ''
  type: Tools
  url: https://github.com/lakeraai/intent-augmentation
- group: commercial
  title: ''
  type: Plans
  url: plans/lakera-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lakera-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lakera-ai-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/lakera-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lakera-ai-vocabulary.yml
created: '2026-05-25T00:00:00.000Z'
description: Lakera is an AI-native security platform that protects GenAI applications, agents, and workforces from prompt injection, data leakage, PII exposure, content violations, and malicious links. Lakera Guard exposes a single-endpoint runtime screening API (/v2/guard) that accepts OpenAI-style chat messages and returns a flagged decision in sub-50ms; a companion /v2/guard/results endpoint returns L1–L5 detector confidence levels for offline analysis. The Lakera Platform API lets Enterprise customers manage policies (detector sensitivity and action) and projects (per-application bindings) programmatically. Founded in Zurich and acquired by Check Point Software in 2025, Lakera also operates Gandalf, the 1M+ player prompt injection challenge that feeds its detector training pipeline, and publishes the open-source PINT benchmark for prompt injection detection evaluation.
examples:
- key_count: 2
  name: Lakera Guard Results Example
  slug: lakera-guard-results-example
- key_count: 2
  name: Lakera Guard Screen Content Example
  slug: lakera-guard-screen-content-example
features:
- Lakera Guard — runtime AI security screening for LLM applications with sub-50ms p95 latency
- Single-endpoint /v2/guard API following the OpenAI chat completions message format
- Detectors for prompt attacks, data leakage, PII, content moderation, and unknown links
- 100+ language coverage and multimodal / model-agnostic protection
- L1–L5 confidence levels aligned with OWASP paranoia level conventions
- Per-detector breakdown and character-level payload match locations for masking
- /v2/guard/results endpoint for offline threshold tuning and quality monitoring
- Policies and Projects as first-class concepts — central policy control without code changes
- SaaS deployment with daily detector model updates and real-time analytics
- Self-hosted deployment with bi-weekly model updates and Kubernetes probes
- Regional endpoints — Global, US East, US West, EU West, Asia Pacific
- Lakera Red — AI red-teaming with direct and indirect attack simulations and risk-based findings
- Workforce AI Security — monitors employee AI usage across applications and browsers
- AI Agent Security — runtime protection for autonomous agents and tool use
- Gandalf — 1M+ player prompt injection challenge feeding detector training signal
- PINT Benchmark — open prompt injection detection benchmark on GitHub
- LiteLLM, AI gateway, and RAG pipeline integration patterns
- MCP server at docs.lakera.ai/_mcp/server for AI client tools
- Browser extension (Chrome) for ChatGPT data leak protection
- Part of Check Point Software Technologies as of 2025
finops:
- name: Lakera Ai Finops
  service_category: ''
  slug: lakera-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lakera-ai.png
json_schemas:
- name: Lakera Guard Request
  property_count: 6
  slug: lakera-guard-request
- name: Lakera Guard Response
  property_count: 5
  slug: lakera-guard-response
json_structures:
- name: Lakera Guard Request Structure
  property_count: 0
  slug: lakera-guard-request-structure
jsonld:
- class_count: 34
  name: Lakera Ai Context
  property_count: 0
  slug: lakera-ai-context
layout: provider
mcp_servers:
- description: ''
  name: Lakera Docs MCP Server
  slug: lakera-docs-mcp-server
modified: '2026-05-25'
name: Lakera
nav: Providers
network: true
overview: 'Lakera publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Guard API, Policies API, Projects API, and 1 more. Tagged areas include AI Security, Artificial Intelligence, Generative AI, LLM Security, and Prompt Injection.


  The Lakera catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Lakera''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, support, engineering blog, and 30 more developer resources.'
plans:
- name: Lakera Ai Plans Pricing
  plan_count: 4
  slug: lakera-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Lakera Ai Rate Limits
  slug: lakera-ai-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lakera API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lakera-ai-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Lakera API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: lakera-rules
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 28.8
    contract_quality: 73.8
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lakera-ai/refs/heads/main/screenshots/lakera-ai-2026-06-20T184246.png
security:
- kind: authentication
  name: Lakera Ai Authentication
  slug: lakera-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lakera Ai Domain Security
  slug: lakera-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lakera Ai Vulnerability Disclosure
  slug: lakera-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lakera Ai Trust Center
  slug: lakera-ai-trust-center
  summary_line: GDPR
slug: lakera-ai
tags:
- AI Security
- Artificial Intelligence
- Generative AI
- LLM Security
- Prompt Injection
- AI Guardrails
- AI Red Teaming
- Data Loss Prevention
- Content Moderation
- Check Point
website: https://www.lakera.ai
---
