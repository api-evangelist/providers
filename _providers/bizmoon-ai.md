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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Bizmoon Ai Agentic Access
  operation_count: 24
  slug: bizmoon-ai-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 1
apis:
- baseURL: https://bizmoon.ai
  baseurl_source: declared
  description: The Read API from Bizmoon — 14 operation(s) for read.
  name: Bizmoon Read API
  slug: bizmoon-ai-read-api
- baseURL: https://bizmoon.ai
  baseurl_source: declared
  description: The Write API from Bizmoon — 8 operation(s) for write.
  name: Bizmoon Write API
  slug: bizmoon-ai-write-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bizmoon-ai/agentic-access/bizmoon-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bizmoon-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bizmoon-ai/plans/bizmoon-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bizmoon-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bizmoon-ai/rules/bizmoon-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bizmoon-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bizmoon-ai/vocabulary/bizmoon-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bizmoon-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bizmoon-ai/errors/bizmoon-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bizmoon-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bizmoon-ai/conformance/bizmoon-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bizmoon-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bizmoon-ai/llms/bizmoon-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bizmoon-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bizmoon-ai/well-known/bizmoon-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bizmoon-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bizmoon-ai/hosts/bizmoon-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bizmoon-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bizmoon-ai/vendors/bizmoon-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bizmoon-ai-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://bizmoon.ai/mcp/playground
- group: start
  title: ''
  type: Login
  url: https://bizmoon.ai/login
- group: docs
  title: ''
  type: APIReference
  url: https://bizmoon.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/bizmoon-ai/authentication/bizmoon-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bizmoon-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bizmoon-ai/security/bizmoon-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bizmoon-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bizmoon.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://bizmoon.ai/mcp/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://bizmoon.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://bizmoon.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bizmoon.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bizmoon.ai/terms
created: '2026-11-02'
description: Bizmoon is an AI‑powered platform that helps small businesses navigate regulations, discover eligible government grants, and stay on top of compliance deadlines. It aggregates regulatory data, offers a conversational assistant, and provides APIs for integration with other tools, aiming to simplify compliance and funding discovery for entrepreneurs and enterprises alike.
image: https://bizmoon.ai/opengraph-image
layout: provider
modified: '2026-11-02'
name: Bizmoon
nav: Providers
network: true
overview: 'Bizmoon publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Read API and Write API. Tagged areas include Company, Artificial Intelligence, Compliance, Grants, and Small Business.


  The Bizmoon catalog on APIs.io includes 1 Spectral governance ruleset.


  Bizmoon''s developer surface includes sandbox, API reference, authentication, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Bizmoon Ai Plans Pricing
  plan_count: 6
  slug: bizmoon-ai-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Bizmoon API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: bizmoon-ai-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 49.0
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bizmoon Ai Authentication
  slug: bizmoon-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bizmoon Ai Domain Security
  slug: bizmoon-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bizmoon-ai
tags:
- Company
- Artificial Intelligence
- Compliance
- Grants
- Small Business
website: https://bizmoon.ai/
---
