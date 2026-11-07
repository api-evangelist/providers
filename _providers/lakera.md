---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lakera Agentic Access
  operation_count: 7
  slug: lakera-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
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
- baseURL: https://platform.lakera.ai/api
  baseurl_source: spec
  description: Policy validation (self-hosted)
  name: Lakera Policies API
  slug: lakera-policies-api
- baseURL: https://platform.lakera.ai/api
  baseurl_source: spec
  description: The analytics API from Lakera — 1 operation(s) for analytics.
  name: Lakera Analytics API
  slug: lakera-analytics-api
- baseURL: https://platform.lakera.ai/api
  baseurl_source: spec
  description: The logs API from Lakera — 1 operation(s) for logs.
  name: Lakera Logs API
  slug: lakera-logs-api
- baseURL: https://platform.lakera.ai/api
  baseurl_source: spec
  description: The projects API from Lakera — 2 operation(s) for projects.
  name: Lakera Projects API
  slug: lakera-projects-api
artifact_total: 39
collections:
- collection_type: open
  name: Lakera Guard API
  slug: open-lakera-guard-api
- collection_type: open
  name: Lakera Guard Health API
  slug: open-lakera-health-api
- collection_type: open
  name: Lakera Guard Policies API
  slug: open-lakera-policies-api
- collection_type: open
  name: Lakera Guard API
  slug: open-lakera
common:
- group: commercial
  href: https://artifacts.apis.io/lakera/plans/lakera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lakera-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lakera/rate-limits/lakera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lakera-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lakera/finops/lakera-finops.yml
  title: ''
  type: FinOps
  url: finops/lakera-finops.yml
- group: agent
  href: https://artifacts.apis.io/lakera/agentic-access/lakera-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lakera-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lakera/security/lakera-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lakera-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lakera/security/lakera-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lakera-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lakera/security/lakera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lakera-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lakera/authentication/lakera-authentication.yml
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
- has_sources: false
  method: generated
  name: Lakera Finops
  primary_unit: ''
  service_category: API
  slug: lakera-finops
  template: true
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
overview: 'Lakera publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Policies API, Analytics API, Logs API, and 4 more. Tagged areas include AI Security, LLM Security, Prompt Injection, Guardrails, and Red Teaming.


  The Lakera catalog on APIs.io includes 1 Spectral governance ruleset.


  Lakera''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Lakera Plans Pricing
  plan_count: 1
  slug: lakera-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Lakera Rate Limits
  slug: lakera-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Lakera API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: lakera-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 30.3
    contract_governance: 13.6
    contract_quality: 57.2
    developer_ergonomics: 42.9
    discoverability: 64.3
    operational_transparency: 18.4
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 8
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lakera/lakera-2026-06-20T184245.png
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
  summary_line: no policy recorded
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
- Generative AI
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
