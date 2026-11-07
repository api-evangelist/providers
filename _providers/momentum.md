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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Momentum Agentic Access
  operation_count: 5
  slug: momentum-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 5
apis:
- baseURL: https://api.momentum.io
  baseurl_source: spec
  description: API for Momentum AI-powered revenue orchestration platform
  name: Momentum API
  slug: momentum-api
- baseURL: https://api.momentum.io
  baseurl_source: declared
  description: The Meeting API from Momentum — 1 operation(s) for meeting.
  name: Momentum Meeting API
  slug: momentum-meeting-api
- baseURL: https://api.momentum.io
  baseurl_source: declared
  description: The Momentum API API from Momentum — 1 operation(s) for momentum api.
  name: Momentum Momentum API
  slug: momentum-momentum-api-api
- baseURL: https://api.momentum.io
  baseurl_source: declared
  description: The Signals API from Momentum — 2 operation(s) for signals.
  name: Momentum Signals API
  slug: momentum-signals-api
- baseURL: https://api.momentum.io
  baseurl_source: declared
  description: The User Provided Meeting API from Momentum — 1 operation(s) for user provided meeting.
  name: Momentum User Provided Meeting API
  slug: momentum-user-provided-meeting-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/momentum/agentic-access/momentum-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/momentum-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/momentum/finops/momentum-finops.yml
  title: ''
  type: FinOps
  url: finops/momentum-finops.yml
- group: auth
  href: https://artifacts.apis.io/momentum/authentication/momentum-authentication.yml
  title: ''
  type: Authentication
  url: authentication/momentum-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/momentum/plans/momentum-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/momentum-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/momentum/rules/momentum-rules.yml
  title: ''
  type: Spectral
  url: rules/momentum-rules.yml
- group: design
  href: https://artifacts.apis.io/momentum/json-ld/momentum-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/momentum-context.jsonld
- group: design
  href: https://artifacts.apis.io/momentum/vocabulary/momentum-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/momentum-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/momentum/data-model/momentum-data-model.yml
  title: ''
  type: DataModel
  url: data-model/momentum-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.momentum.io/security
- group: design
  href: https://artifacts.apis.io/momentum/conformance/momentum-conformance.yml
  title: ''
  type: Conformance
  url: conformance/momentum-conformance.yml
- group: agent
  href: https://artifacts.apis.io/momentum/llms/momentum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/momentum-llms.txt
- group: other
  href: https://artifacts.apis.io/momentum/a2a/momentum-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/momentum-a2a.yml
- group: agent
  href: https://artifacts.apis.io/momentum/well-known/momentum-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/momentum-well-known.yml
- group: other
  href: https://artifacts.apis.io/momentum/hosts/momentum-hosts.yml
  title: ''
  type: Hosts
  url: hosts/momentum-hosts.yml
- group: other
  href: https://artifacts.apis.io/momentum/vendors/momentum-vendors.yml
  title: ''
  type: Vendors
  url: vendors/momentum-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.momentum.io/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.momentum.io/
- group: start
  title: ''
  type: SignUp
  url: https://www.momentum.io/prompts/create-account-management-plan
- group: auth
  title: ''
  type: Security
  url: https://www.momentum.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.momentum.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.momentum.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.momentum.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.momentum.io/getting-started-with-momentum-ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.momentum.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.momentum.io/api-reference/meetings/retrieve-a-list-of-meetings
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/momentum
- group: auth
  href: https://artifacts.apis.io/momentum/security/momentum-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/momentum-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/momentum/security/momentum-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/momentum-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/momentum/security/momentum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/momentum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.momentum.io/
coverage:
  detail: Documentation provides API reference but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.momentum.io/api-reference/meetings/retrieve-a-list-of-meetings
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Momentum is an AI‑powered revenue orchestration platform that helps sales and revenue teams automate deal execution, customer retention, coaching, and executive insights. Now part of Salesforce, Momentum integrates with CRM and productivity tools to surface actionable intelligence, streamline workflows, and accelerate revenue growth across the enterprise.
finops:
- has_sources: true
  method: derived
  name: Momentum Finops
  primary_unit: seat
  service_category: ''
  slug: momentum-finops
  template: false
image: https://cdn.prod.website-files.com/678526103b0c749e78e38221/69a87cc95292436ce509e051_Websitethumb.png
json_schemas:
- name: GetV1SignalsPromptsResponse
  property_count: 1
  slug: momentum-get-v1-signals-prompts-response
- name: GetV1V1IdResponse
  property_count: 1
  slug: momentum-get-v1-v1-id-response
- name: GetV2SignalsResponse
  property_count: 1
  slug: momentum-get-v2-signals-response
- name: PostV1MeetingRemapResponse
  property_count: 2
  slug: momentum-post-v1-meeting-remap-response
jsonld:
- class_count: 4
  name: Momentum Context
  property_count: 4
  slug: momentum-context
layout: provider
modified: '2026-10-12'
name: Momentum
nav: Providers
network: true
overview: 'Momentum is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Meeting API, Momentum API, and 3 more. Tagged areas include Company, Artificial Intelligence, Revenue, Automation, and Salesforce.


  The Momentum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Momentum''s developer surface includes authentication, signup flow, pricing, engineering blog, getting-started guide, documentation, API reference, and 23 more developer resources.'
plans:
- name: Momentum Plans Pricing
  plan_count: 2
  slug: momentum-plans-pricing
- name: Momentum Price Estimates
  plan_count: 0
  slug: momentum-price-estimates
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Momentum API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: momentum-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 27.4
    discoverability: 69.6
    operational_transparency: 15.8
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/momentum/momentum-2026-11-03T135817.png
security:
- kind: authentication
  name: Momentum Authentication
  slug: momentum-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Momentum Domain Security
  slug: momentum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Momentum Vulnerability Disclosure
  slug: momentum-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Momentum Trust Center
  slug: momentum-trust-center
  summary_line: SOC 2, GDPR
slug: momentum
tags:
- Company
- Artificial Intelligence
- Revenue
- Automation
- Salesforce
website: https://www.momentum.io/
---
