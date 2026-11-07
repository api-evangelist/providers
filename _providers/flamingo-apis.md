---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Flamingo Apis Agentic Access
  operation_count: 3
  slug: flamingo-apis-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 4
apis:
- description: Export Access tables to CSV or JSON.
  name: Access File Extractor
  slug: access-file-extractor
- description: Optimize HTML5 ad ZIP size while preserving code and paths.
  name: CreativePack
  slug: creativepack
- description: Personalize a layered sewing-pattern PDF with an API.
  name: PatternCopy PDF
  slug: patterncopy-pdf
- description: Import ONIX book metadata into WooCommerce with a preview first.
  name: ShelfRelay ONIX
  slug: shelfrelay-onix
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/flamingo-apis/agentic-access/flamingo-apis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flamingo-apis-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/flamingo-apis/rate-limits/flamingo-apis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flamingo-apis-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/flamingo-apis/plans/flamingo-apis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flamingo-apis-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flamingo-apis/rules/flamingo-apis-rules.yml
  title: ''
  type: Spectral
  url: rules/flamingo-apis-rules.yml
- group: agent
  href: https://artifacts.apis.io/flamingo-apis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/flamingo-apis/components/flamingo-apis-components.yml
  title: ''
  type: Components
  url: components/flamingo-apis-components.yml
- group: design
  href: https://artifacts.apis.io/flamingo-apis/conventions/flamingo-apis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flamingo-apis-conventions.yml
- group: auth
  href: https://artifacts.apis.io/flamingo-apis/authentication/flamingo-apis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flamingo-apis-authentication.yml
- group: design
  href: https://artifacts.apis.io/flamingo-apis/conformance/flamingo-apis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flamingo-apis-conformance.yml
- group: other
  href: https://artifacts.apis.io/flamingo-apis/hosts/flamingo-apis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flamingo-apis-hosts.yml
- group: other
  href: https://artifacts.apis.io/flamingo-apis/vendors/flamingo-apis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flamingo-apis-vendors.yml
- group: auth
  href: https://artifacts.apis.io/flamingo-apis/security/flamingo-apis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flamingo-apis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flamingo-api-guides.flatemu1.chatgpt.site
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/IsraelDiego/api/access-file-extractor/pricing
- group: start
  title: ''
  type: SignUp
  url: https://rapidapi.com/auth/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flamingo-api-guides.flatemu1.chatgpt.site/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/israeldi
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://flamingo-api-guides.flatemu1.chatgpt.site
  - status: 200
    url: https://github.com/israeldi/flamingo-api-examples
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Flamingo APIs provides a suite of file‑processing APIs that enable developers to export Microsoft Access tables to CSV or JSON, optimize HTML5 advertising ZIP packages, personalize layered PDF documents, and integrate ONIX book metadata into WooCommerce stores. The company offers Python example scripts, WooCommerce connectors, and detailed integration guides hosted at https://flamingo-api-guides.flatemu1.chatgpt.site. All APIs are available through RapidAPI with free plans and paid tiers, and the service emphasizes privacy, with processing details outlined on its privacy page.
image: https://flamingo-api-guides.flatemu1.chatgpt.site/favicon.svg
layout: provider
modified: '2026-11-02'
name: Flamingo APIs
nav: Providers
network: true
overview: 'Flamingo APIs is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include File Processing, Python, RapidAPI, WooCommerce, and Data Export.


  The Flamingo APIs catalog on APIs.io includes 1 Spectral governance ruleset.


  Flamingo APIs'' developer surface includes authentication, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Flamingo Apis Plans Pricing
  plan_count: 3
  slug: flamingo-apis-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Flamingo Apis Rate Limits
  slug: flamingo-apis-rate-limits
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: Flamingo APIs API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: flamingo-apis-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 71.4
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Flamingo Apis Authentication
  slug: flamingo-apis-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Flamingo Apis Domain Security
  slug: flamingo-apis-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: creativepack-optimize
  slug: creativepack-optimize
- name: shelfrelay-normalize
  slug: shelfrelay-normalize
- name: shelfrelay-usage
  slug: shelfrelay-usage
slug: flamingo-apis
tags:
- File Processing
- Python
- RapidAPI
- WooCommerce
- Data Export
website: https://flamingo-api-guides.flatemu1.chatgpt.site
---
