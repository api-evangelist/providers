---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Askedthrice Com Agentic Access
  operation_count: 5
  slug: askedthrice-com-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://askedthrice.com
  baseurl_source: declared
  description: Read-only artifacts meant to be served on someone else's site.
  name: Asked Thrice Embeds API
  slug: askedthrice-com-embeds-api
- baseURL: https://askedthrice.com
  baseurl_source: declared
  description: Start a paid scan, read its result, and buy scans.
  name: Asked Thrice Scans API
  slug: askedthrice-com-scans-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/askedthrice-com/agentic-access/askedthrice-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/askedthrice-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/askedthrice-com/rate-limits/askedthrice-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/askedthrice-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/askedthrice-com/plans/askedthrice-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askedthrice-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/askedthrice-com/rules/askedthrice-com-rules.yml
  title: ''
  type: Spectral
  url: rules/askedthrice-com-rules.yml
- group: design
  href: https://artifacts.apis.io/askedthrice-com/json-ld/askedthrice-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/askedthrice-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/askedthrice-com/vocabulary/askedthrice-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/askedthrice-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/askedthrice-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/askedthrice-com/data-model/askedthrice-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/askedthrice-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/askedthrice-com/errors/askedthrice-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/askedthrice-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/askedthrice-com/conformance/askedthrice-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/askedthrice-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/askedthrice-com/llms/askedthrice-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askedthrice-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/askedthrice-com/well-known/askedthrice-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askedthrice-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/askedthrice-com/hosts/askedthrice-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askedthrice-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/askedthrice-com/vendors/askedthrice-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askedthrice-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://askedthrice.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nahuelsoria
- group: auth
  href: https://artifacts.apis.io/askedthrice-com/security/askedthrice-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askedthrice-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askedthrice.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://askedthrice.com/developers
- group: company
  title: ''
  type: Blog
  url: https://askedthrice.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://askedthrice.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askedthrice.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askedthrice.com/privacy
created: '2026-11-02'
description: Asked Thrice provides an independent AI visibility audit tool that measures whether AI assistants such as OpenAI, Gemini, and Claude recommend a brand when customers inquire about its category. Founded in 2026 in Buenos Aires, Argentina, the service scans web content and LLM responses to reveal brand presence across generative search platforms, helping businesses understand and improve their AI-driven discoverability.
image: https://askedthrice.com/opengraph-image
json_schemas:
- name: CheckoutRequest
  property_count: 2
  slug: askedthrice-com-checkout-request
- name: ScanAllowance
  property_count: 5
  slug: askedthrice-com-scan-allowance
- name: ScanRequest
  property_count: 1
  slug: askedthrice-com-scan-request
- name: Scan
  property_count: 6
  slug: askedthrice-com-scan
- name: ScanStarted
  property_count: 1
  slug: askedthrice-com-scan-started
jsonld:
- class_count: 7
  name: Askedthrice Com Context
  property_count: 19
  slug: askedthrice-com-context
layout: provider
modified: '2026-11-02'
name: Asked Thrice
nav: Providers
network: true
overview: 'Asked Thrice publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Embeds API and Scans API. Tagged areas include Artificial Intelligence, Visibility, Audit, Generative AI, and Brand Analytics.


  The Asked Thrice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Asked Thrice''s developer surface includes engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Askedthrice Com Plans Pricing
  plan_count: 2
  slug: askedthrice-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Askedthrice Com Rate Limits
  slug: askedthrice-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 115
  extends:
  - spectral:oas
  name: Asked Thrice API Rules
  rule_count: 74
  severity_counts:
    error: 72
    hint: 0
    info: 1
    warn: 1
  slug: askedthrice-com-rules
scopes:
- name: Askedthrice Com Scopes
  scope_count: 0
  slug: askedthrice-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 66.3
    developer_ergonomics: 7.7
    discoverability: 66.1
    operational_transparency: 23.7
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Askedthrice Com Authentication
  slug: askedthrice-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Askedthrice Com Domain Security
  slug: askedthrice-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: askedthrice-com-main-skill
  slug: askedthrice-com-main-skill
- name: scan
  slug: askedthrice-com-scan
slug: askedthrice-com
tags:
- Artificial Intelligence
- Visibility
- Audit
- Generative AI
- Brand Analytics
website: https://askedthrice.com/
---
