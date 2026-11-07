---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 23.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: 2Pr Io Agentic Access
  operation_count: 6
  slug: 2pr-io-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
artifact_total: 17
common:
- group: auth
  href: https://artifacts.apis.io/2pr-io/security/2pr-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/2pr-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/2pr-io/security/2pr-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/2pr-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://2pr.io/
created: '2026-10-31'
description: 2pr is an AI-powered LinkedIn growth platform that helps users create, schedule, and publish LinkedIn posts automatically. It transforms ideas, voice notes, or links into tailored posts, generates carousel images, handles scheduling, cross‑posts to X (Twitter), and provides analytics and comment reply drafting. Targeted at founders, B2B salespeople, consultants, job seekers, and creators, 2pr offers plans from $17 to $49 per month with a free trial, leveraging a library of over two million viral LinkedIn posts to benchmark content performance.
json_schemas:
- name: InitializeRequest
  property_count: 4
  slug: 2pr-io-initialize-request
- name: JsonRpcResponse
  property_count: 4
  slug: 2pr-io-json-rpc-response
- name: PingRequest
  property_count: 3
  slug: 2pr-io-ping-request
- name: TokenRequest
  property_count: 7
  slug: 2pr-io-token-request
- name: ToolsCallRequest
  property_count: 4
  slug: 2pr-io-tools-call-request
- name: ToolsListRequest
  property_count: 3
  slug: 2pr-io-tools-list-request
jsonld:
- class_count: 54
  name: 2Pr Io Context
  property_count: 17
  slug: 2pr-io-context
layout: provider
modified: '2026-10-31'
name: 2pr
nav: Providers
network: true
overview: '2pr publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LinkedIn, Marketing, Automation, and Software-as-a-Service.


  The 2pr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: 2Pr Io Plans Pricing
  plan_count: 4
  slug: 2pr-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: 2Pr Io Rate Limits
  slug: 2pr-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: 2pr API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: 2pr-io-rules
scopes:
- name: 2Pr Io Scopes
  scope_count: 1
  slug: 2pr-io-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 52.5
    catalog_earned_first_party: 12.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 20.7
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  previous_composite: 21.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 2Pr Io Authentication
  slug: 2pr-io-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: 2Pr Io Domain Security
  slug: 2pr-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 2Pr Io Vulnerability Disclosure
  slug: 2pr-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: 2pr-io-mcp-tools
  slug: 2pr-io-mcp-tools
- name: 2pr-io-oauth-client-setup
  slug: 2pr-io-oauth-client-setup
slug: 2pr-io
tags:
- Artificial Intelligence
- LinkedIn
- Marketing
- Automation
- Software-as-a-Service
website: https://2pr.io/
---
