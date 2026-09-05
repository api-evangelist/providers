---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for AIMon LLM monitoring and evaluation — manage users, models, applications, evaluations and evaluation runs, retrieve evaluation and production metrics, and manage datasets, records, and da
  name: AIMon API
  slug: aimon-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aimon-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.aimon.ai/trust
- group: company
  title: ''
  type: Website
  url: https://www.aimon.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aimon.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aimon.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aimon.ai/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/aimonlabs/aimon-typescript-sdk/blob/main/api.md
- group: company
  title: ''
  type: Blog
  url: https://www.aimon.ai/blog/all
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aimonlabs
- group: start
  title: ''
  type: SignUp
  url: https://app.aimon.ai/?screen=signup
- group: start
  title: ''
  type: Login
  url: https://app.aimon.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aimon.ai/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimon.ai/docs/privacy-policy.pdf
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/Cp6YZ9qTdm
- group: build
  title: ''
  type: Packages
  url: packages/aimon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aimon-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aimon-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aimon-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aimon-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aimon-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aimon-domain-security.yml
created: '2026-07-17'
description: AIMon (AIMon Labs) is an enterprise AI monitoring, evaluation, and governance platform that helps teams ship trustworthy LLM, RAG, and agentic AI applications. Its API and SDKs detect hallucinations and quality issues (instruction adherence, context quality, conciseness, completeness, toxicity) across offline evaluation, continuous production monitoring, and inline/real-time detection. Developers create applications and models, run evaluations and evaluation runs, retrieve evaluation and production metrics, and manage datasets, dataset records, and dataset collections through a REST API (base https://sdkbe-production.aimon.ai) with Bearer API-key authentication, plus official Python and TypeScript SDKs and a LlamaIndex integration. Surfaced as a portfolio company of Bessemer Venture Partners; sector ai-ml.
image: https://www.aimon.ai/favicon.ico
layout: provider
modified: '2026-07-17'
name: AIMon
nav: Providers
network: true
overview: 'AIMon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, LLM Observability, AI Monitoring, and Evaluation.


  AIMon''s developer surface includes documentation, getting-started guide, API reference, engineering blog, signup flow, pricing, support, and 14 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 28.5
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aimon/refs/heads/main/screenshots/aimon-2026-07-25T195355.png
security:
- kind: authentication
  name: Aimon Authentication
  slug: aimon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aimon Domain Security
  slug: aimon-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Aimon Trust Center
  slug: aimon-trust-center
  summary_line: SOC 2, HIPAA
slug: aimon
tags:
- Company
- Ai Ml
- LLM Observability
- AI Monitoring
- Evaluation
- Hallucination Detection
- LLM Guardrails
- RAG
- AI Governance
- Trustworthy AI
website: https://www.aimon.ai/
---
