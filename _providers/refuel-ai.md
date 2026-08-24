---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.refuel.ai/get-started
  - plans/refuel-ai-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Refuel Ai Agentic Access
  operation_count: 109
  slug: refuel-ai-agentic-access
  summary_line: 109 operations · 64 acting
api_count: 3
apis:
- description: Autolabel is the open-source Python library (pip install refuel-autolabel) to label, clean, and enrich text datasets with any LLM (OpenAI, Anthropic, Google, HuggingFace, vLLM, Refuel-hosted). It is a
  name: Refuel Autolabel (Open Source)
  slug: refuel-autolabel-oss
- description: 'The full Refuel Cloud REST API — 108 operations across 77 paths, harvested verbatim from https://cloud-api.refuel.ai/openapi.json on 2026-08-14. Covers projects, datasets and items, tasks, task runs, '
  name: Refuel Cloud API
  slug: refuel-cloud-api
- description: The documented realtime application label surface — the endpoint Refuel's own catalog page publishes as `POST https://cloud-api.refuel.ai/applications/{applicationName}/label`, with the concrete reque
  name: Refuel Applications API
  slug: refuel-ai-applications-api
artifact_total: 16
asyncapis:
- description: ''
  name: Refuel Ai Events
  slug: refuel-ai-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Refuel Cloud Applications API
  slug: open-refuel-ai-applications-api
- collection_type: open
  name: Refuel Cloud API
  slug: open-refuel-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/refuel-ai-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/refuel-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/refuel-ai-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/refuel-ai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/refuel-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/refuel-ai-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/refuel-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/refuel-ai-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/refuel-ai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/refuel-ai-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/refuel-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/refuel-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/refuel-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.refuel.ai/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/refuel-ai-sandbox.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/refuel-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/refuel-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.refuel.ai/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refuel-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/refuel-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/refuel-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/refuel-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/refuelai
- group: company
  title: ''
  type: Website
  url: https://www.refuel.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.refuel.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.refuel.ai
- group: docs
  title: ''
  type: APIReference
  url: https://cloud-api.refuel.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.refuel.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/uEdr8nrMGm
- group: company
  title: ''
  type: Blog
  url: https://www.refuel.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.refuel.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://app.refuel.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.refuel.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.refuel.ai/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/refuel-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/refuel-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/refuel-ai-finops.yml
created: '2026-06-21'
description: Refuel is an AI data-labeling and data-enrichment platform that uses large language models to label, clean, structure and enrich enterprise datasets. Refuel Cloud exposes a REST API at cloud-api.refuel.ai covering projects, datasets, tasks and task runs, taxonomies, seedsets and evalsets, confidence calibration, Refuel LLM-2 finetuning, and deployed applications whose realtime label endpoint transforms new rows on demand. The open-source autolabel library lets teams run the same LLM labeling workflows in their own environment against OpenAI, Anthropic, Google, HuggingFace, vLLM or Refuel-hosted models. Refuel.ai was acquired by Together AI in May 2025; the platform continues to operate and its API is still live.
finops:
- name: Refuel Ai Finops
  service_category: AI and Machine Learning
  slug: refuel-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refuel-ai.png
layout: provider
mcp_servers:
- description: 'Refuel serves a live, anonymous, remote MCP endpoint at https://docs.refuel.ai/mcp. It is a DOCUMENTATION server, not a Refuel Cloud API server: the three tools search and read the docs corpus and fil'
  name: Refuel.ai
  slug: refuelai
modified: '2026-08-14'
name: Refuel
nav: Providers
network: true
overview: 'Refuel publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cloud API and Applications API. Tagged areas include Artificial Intelligence, LLM, Data Labeling, Data Enrichment, and Autolabel.


  The Refuel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Refuel''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 31 more developer resources.'
plans:
- name: Refuel Ai Plans Pricing
  plan_count: 3
  slug: refuel-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Refuel Ai Rate Limits
  slug: refuel-ai-rate-limits
score:
  band: strong
  composite: 65.1
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 30.3
    contract_quality: 68.2
    developer_ergonomics: 69.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 34.2
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refuel-ai/refs/heads/main/screenshots/refuel-ai-2026-08-17T080415.png
security:
- kind: authentication
  name: Refuel Ai Authentication
  slug: refuel-ai-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Refuel Ai Domain Security
  slug: refuel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Refuel Ai Vulnerability Disclosure
  slug: refuel-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Refuel Ai Trust Center
  slug: refuel-ai-trust-center
  summary_line: SOC 2, GDPR
slug: refuel-ai
tags:
- Artificial Intelligence
- LLM
- Data Labeling
- Data Enrichment
- Autolabel
- Machine-Learning
- Data Quality
- Training Data
- Fine-Tuning
- Data Transformation
- Entity Resolution
- Content Moderation
website: https://www.refuel.ai
---
