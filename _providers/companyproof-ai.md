---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CompanyProof REST API provides company verification, profile, and intelligence endpoints.
  name: CompanyProof REST API
  slug: companyproof-rest-api
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/companyproof-ai/rate-limits/companyproof-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/companyproof-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/companyproof-ai/plans/companyproof-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/companyproof-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/companyproof-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/companyproof-ai/conventions/companyproof-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/companyproof-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/companyproof-ai/conventions/companyproof-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/companyproof-ai-conventions.yml
- group: start
  href: https://artifacts.apis.io/companyproof-ai/sandbox/companyproof-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/companyproof-ai-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://companyproof.ai/security
- group: auth
  href: https://artifacts.apis.io/companyproof-ai/authentication/companyproof-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/companyproof-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/companyproof-ai/conformance/companyproof-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/companyproof-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/companyproof-ai/llms/companyproof-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/companyproof-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/companyproof-ai/mcp/companyproof-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/companyproof-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/companyproof-ai/well-known/companyproof-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/companyproof-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/companyproof-ai/well-known/companyproof-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/companyproof-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/companyproof-ai/hosts/companyproof-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/companyproof-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/companyproof-ai/vendors/companyproof-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/companyproof-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://companyproof.ai/security
- group: start
  title: ''
  type: Login
  url: https://companyproof.ai/login
- group: auth
  href: https://artifacts.apis.io/companyproof-ai/security/companyproof-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/companyproof-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/companyproof-ai/security/companyproof-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/companyproof-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/companyproof-ai/security/companyproof-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/companyproof-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://companyproof.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://companyproof.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://companyproof.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://companyproof.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://companyproof.ai/docs/choose-api
- group: operate
  title: ''
  type: Support
  url: https://companyproof.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://companyproof.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://companyproof.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://companyproof.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://companyproof.ai/privacy
created: '2026-10-30'
description: CompanyProof AI provides a verification API that grounds AI model outputs with factual company data. It offers claim verification, company profiles, ownership, financials, and compliance information across global registries. The platform integrates with AI assistants, compliance tools, and data pipelines, delivering evidence‑backed answers and continuous monitoring of company facts. Users can retrieve structured data via REST endpoints, supporting use cases in procurement, due diligence, and AI safety.
image: https://companyproof.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at companyproof.ai.
  name: companyproof-ai MCP Server
  slug: companyproof-ai-mcp-yml
modified: '2026-10-30'
name: companyproof-ai
nav: Providers
network: true
overview: 'companyproof-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Verification, Compliance, Data, and CompanyProof.


  companyproof-ai''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
plans:
- name: Companyproof Ai Plans Pricing
  plan_count: 3
  slug: companyproof-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Companyproof Ai Rate Limits
  slug: companyproof-ai-rate-limits
scopes:
- name: Companyproof Ai Scopes
  scope_count: 0
  slug: companyproof-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 48.1
    discoverability: 65.0
    operational_transparency: 36.8
  previous_composite: 49.1
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/companyproof-ai/companyproof-ai-2026-11-03T124958.png
security:
- kind: authentication
  name: Companyproof Ai Authentication
  slug: companyproof-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Companyproof Ai Domain Security
  slug: companyproof-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Companyproof Ai Vulnerability Disclosure
  slug: companyproof-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Companyproof Ai Trust Center
  slug: companyproof-ai-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: companyproof-ai-agent-quickstart
  slug: companyproof-ai-agent-quickstart
slug: companyproof-ai
tags:
- Artificial Intelligence
- Verification
- Compliance
- Data
- CompanyProof
website: https://companyproof.ai/
---
