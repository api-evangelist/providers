---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Brandyze API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Brandyze API
  slug: brandyze-fr-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/brandyze-fr/plans/brandyze-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brandyze-fr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brandyze-fr/rules/brandyze-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/brandyze-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/brandyze-fr/vocabulary/brandyze-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brandyze-fr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brandyze-fr/conformance/brandyze-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brandyze-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brandyze-fr/llms/brandyze-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brandyze-fr-llms.txt
- group: auth
  href: https://artifacts.apis.io/brandyze-fr/well-known/brandyze-fr-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brandyze-fr-api-security.txt
- group: agent
  href: https://artifacts.apis.io/brandyze-fr/well-known/brandyze-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brandyze-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/brandyze-fr/hosts/brandyze-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandyze-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/brandyze-fr/vendors/brandyze-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandyze-fr-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://brandyze.fr/security
- group: commercial
  title: ''
  type: Pricing
  url: https://brandyze.fr/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://brandyze.fr/analyse/secteur/media
- group: start
  title: ''
  type: Login
  url: https://brandyze.fr/login
- group: docs
  title: ''
  type: Documentation
  url: https://brandyze.fr/guides
- group: auth
  href: https://artifacts.apis.io/brandyze-fr/security/brandyze-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandyze-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandyze.fr/
- group: company
  title: ''
  type: Blog
  url: https://brandyze.fr/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brandyze.fr/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brandyze.fr/privacy
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found on the provider's site.
  evidence:
  - status: 404
    url: https://brandyze.fr/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Brandyze provides AI-powered brand and creator analysis, evaluating strengths, weaknesses, virality, and competitors of any brand or creator. Users can input a URL and receive over 30 ready-to-publish content pieces, leveraging AI to generate insights and marketing assets.
image: https://brandyze.fr/og-default.png
layout: provider
modified: '2026-11-02'
name: Brandyze
nav: Providers
network: true
overview: 'Brandyze is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Content Generation, Brand Analysis, and Creator Tools.


  The Brandyze catalog on APIs.io includes 1 Spectral governance ruleset.


  Brandyze''s developer surface includes pricing, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Brandyze Fr Plans Pricing
  plan_count: 3
  slug: brandyze-fr-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Brandyze API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: brandyze-fr-rules
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 6.0
    discoverability: 58.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
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
- kind: domain-security
  name: Brandyze Fr Domain Security
  slug: brandyze-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brandyze-fr
tags:
- Artificial Intelligence
- Marketing
- Content Generation
- Brand Analysis
- Creator Tools
website: https://brandyze.fr/
---
