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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: RESTful JSON API to manage the TrojAI platform programmatically (users, groups, roles/permissions, datasets, models, firewall policies/configs, firewall events, red team jobs and results, and secrets)
  name: TrojAI Platform API
  slug: trojai-platform-api
artifact_total: 4
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/a10-networks/
- group: company
  title: ''
  type: Website
  url: https://troj.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.troj.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.troj.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.troj.ai/reference/eng-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.troj.ai/trojai/getting-started/for-data-scientists
- group: company
  title: ''
  type: Blog
  url: https://troj.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://troj.ai/company/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://troj.ai/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://troj.ai/legal/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://troj.ai/legal/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trojai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/trojai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/trojai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trojai-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trojai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trojai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trojai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trojai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trojai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trojai-vulnerability-disclosure.yml
created: '2026-07-17'
description: TrojAI is an enterprise AI security platform (acquired by A10 Networks) that lets organizations deploy AI models and agents safely. Its two products — TrojAI Detect (generative-AI red teaming, model robustness stress-testing, and integrity/risk audits for tabular and NLP models) and TrojAI Defend (a runtime firewall / proxy that inspects prompts and tool calls for prompt injection, jailbreaks, data leakage, toxic content, and rogue MCP/tool abuse) — are managed through a self-hosted RESTful platform API (/api/v2, authenticated with the x-trojai-api-key header), a Firewall Proxy API, a Python SDK (trojai-sdk), and a Keycloak-backed web application. It deploys as Cloud or Enterprise (Helm/Kubernetes).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trojai.png
layout: provider
modified: '2026-07-21'
name: TrojAI
nav: Providers
network: true
overview: 'TrojAI publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Company, AI Security, Machine-Learning, LLM Security, and Red Teaming.


  TrojAI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 14 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 36.9
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trojai/refs/heads/main/screenshots/trojai-2026-09-02T164312.png
security:
- kind: authentication
  name: Trojai Authentication
  slug: trojai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Trojai Domain Security
  slug: trojai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trojai Vulnerability Disclosure
  slug: trojai-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: trojai
tags:
- Company
- AI Security
- Machine-Learning
- LLM Security
- Red Teaming
- AI Firewall
- Prompt Injection
- Model Risk
- MLOps
- Agentic AI
website: https://troj.ai/
---
