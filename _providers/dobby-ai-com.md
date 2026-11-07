---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Programmatic access to Dobby AI platform agents, tasks, approvals, and knowledge base.
  name: Dobby Platform API
  slug: dobby-platform-api
- baseURL: http://dobby-ai.com
  baseurl_source: declared
  description: The Dobby Platform API provides programmatic access to your AI agents, tasks, approvals, and knowledge base (RAG).
  name: Dobby Platform API API
  slug: dobby-platform-api-api
artifact_total: 15
asyncapis:
- description: ''
  name: Dobby Ai Com Webhooks
  slug: dobby-ai-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/dobby-ai-com/rate-limits/dobby-ai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dobby-ai-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/dobby-ai-com/rules/dobby-ai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dobby-ai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dobby-ai-com/json-ld/dobby-ai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dobby-ai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dobby-ai-com/vocabulary/dobby-ai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dobby-ai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dobby-ai-com/asyncapi/dobby-ai-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dobby-ai-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dobby-ai-com/data-model/dobby-ai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dobby-ai-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dobby-ai-com/changelog/dobby-ai-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dobby-ai-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dobby-ai.com/trust
- group: auth
  href: https://artifacts.apis.io/dobby-ai-com/security/dobby-ai-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dobby-ai-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/dobby-ai-com/errors/dobby-ai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dobby-ai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dobby-ai-com/conformance/dobby-ai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dobby-ai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dobby-ai-com/llms/dobby-ai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dobby-ai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dobby-ai-com/a2a/dobby-ai-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dobby-ai-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/dobby-ai-com/well-known/dobby-ai-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dobby-ai-com-status-security.txt
- group: auth
  href: https://artifacts.apis.io/dobby-ai-com/well-known/dobby-ai-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dobby-ai-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dobby-ai-com/well-known/dobby-ai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dobby-ai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dobby-ai-com/hosts/dobby-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dobby-ai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dobby-ai-com/vendors/dobby-ai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dobby-ai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dobby-ai.com/terms
- group: operate
  title: ''
  type: Support
  url: https://dobby-ai.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dobby-ai.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dobby-ai.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dobby-ai.com/pricing
- group: start
  title: ''
  type: Login
  url: https://dobby-ai.com/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://dobby-ai.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://dobby-ai.com/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://dobby-ai.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://dobby-ai.com/docs/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://dobby-ai.com/api/docs
- group: auth
  href: https://artifacts.apis.io/dobby-ai-com/security/dobby-ai-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dobby-ai-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dobby-ai-com/security/dobby-ai-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dobby-ai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dobby-ai-com/security/dobby-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dobby-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dobby-ai.com/
created: '2026-11-05'
description: Dobby AI provides a Data Policy Platform for AI, offering a control plane with multiple compliance modules. It helps organizations automate evidence collection for AI regulations, featuring a flagship Fintech AI Evidence module and integrations with Stripe and analytics tools.
image: https://dobby-ai.com/opengraph-image
json_schemas:
- name: Agent
  property_count: 8
  slug: dobby-ai-com-agent
- name: ApiKey
  property_count: 9
  slug: dobby-ai-com-api-key
- name: Approval
  property_count: 9
  slug: dobby-ai-com-approval
- name: ControlVerdict
  property_count: 4
  slug: dobby-ai-com-control-verdict
- name: Integration
  property_count: 8
  slug: dobby-ai-com-integration
- name: Policy
  property_count: 12
  slug: dobby-ai-com-policy
jsonld:
- class_count: 9
  name: Dobby Ai Com Context
  property_count: 46
  slug: dobby-ai-com-context
layout: provider
modified: '2026-11-05'
name: Dobby AI
nav: Providers
network: true
overview: 'Dobby AI publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dobby Platform API API, and 1 more. Tagged areas include Artificial Intelligence, Compliance, DataPolicy, Fintech, and Platform.


  The Dobby AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Dobby AI''s developer surface includes changelog, support, pricing, documentation, engineering blog, getting-started guide, API reference, and 26 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 3
  name: Dobby Ai Com Rate Limits
  slug: dobby-ai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Dobby AI API Rules
  rule_count: 63
  severity_counts:
    error: 58
    hint: 0
    info: 4
    warn: 1
  slug: dobby-ai-com-rules
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 81.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dobby Ai Com Domain Security
  slug: dobby-ai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dobby Ai Com Vulnerability Disclosure
  slug: dobby-ai-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dobby Ai Com Trust Center
  slug: dobby-ai-com-trust-center
  summary_line: SOC 2, GDPR
slug: dobby-ai-com
tags:
- Artificial Intelligence
- Compliance
- DataPolicy
- Fintech
- Platform
website: https://dobby-ai.com/
---
