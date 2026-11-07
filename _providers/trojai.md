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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RESTful JSON API to manage the TrojAI platform programmatically (users, groups, roles/permissions, datasets, models, firewall policies/configs, firewall events, red team jobs and results, and secrets)
  name: TrojAI Platform API
  slug: trojai-platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://troj.ai/feed/
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
  href: https://artifacts.apis.io/trojai/llms/trojai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trojai-llms.txt
- group: auth
  href: https://artifacts.apis.io/trojai/authentication/trojai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trojai-authentication.yml
- group: build
  href: https://artifacts.apis.io/trojai/packages/trojai-packages.yml
  title: ''
  type: Packages
  url: packages/trojai-packages.yml
- group: build
  href: https://artifacts.apis.io/trojai/packages/trojai-packages.yml
  title: ''
  type: SDKs
  url: packages/trojai-packages.yml
- group: operate
  href: https://artifacts.apis.io/trojai/changelog/trojai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trojai-changelog.yml
- group: design
  href: https://artifacts.apis.io/trojai/lifecycle/trojai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trojai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/trojai/conventions/trojai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trojai-conventions.yml
- group: design
  href: https://artifacts.apis.io/trojai/conformance/trojai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trojai-conformance.yml
- group: auth
  href: https://artifacts.apis.io/trojai/security/trojai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trojai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/trojai/security/trojai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trojai-vulnerability-disclosure.yml
created: '2026-07-17'
description: TrojAI is an enterprise AI security platform (acquired by A10 Networks) that lets organizations deploy AI models and agents safely. Its two products — TrojAI Detect (generative-AI red teaming, model robustness stress-testing, and integrity/risk audits for tabular and NLP models) and TrojAI Defend (a runtime firewall / proxy that inspects prompts and tool calls for prompt injection, jailbreaks, data leakage, toxic content, and rogue MCP/tool abuse) — are managed through a self-hosted RESTful platform API (/api/v2, authenticated with the x-trojai-api-key header), a Firewall Proxy API, a Python SDK (trojai-sdk), and a Keycloak-backed web application. It deploys as Cloud or Enterprise (Helm/Kubernetes).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trojai.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.troj.ai over HTTP; 4 tools listed.
  name: TrojAI MCP Server
  slug: trojai
- description: Remote MCP server at troj.ai over HTTP.
  name: TrojAI MCP Server
  slug: trojai-2
modified: '2026-10-06'
name: TrojAI
nav: Providers
network: true
overview: 'TrojAI is listed with 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Company, AI Security, Machine Learning, LLM Security, and Red Teaming.


  TrojAI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 15 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 38.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trojai/trojai-2026-09-02T164312.png
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
- Machine Learning
- LLM Security
- Red Teaming
- AI Firewall
- Prompt Injection
- Model Risk
- MLOps
- AI Agents
website: https://troj.ai/
---
