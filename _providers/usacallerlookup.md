---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the USACallerLookup website at www.usacallerlookup.com: the route index of the site''s content management system, catalogued as one site surface rather than a'
  name: USACallerLookup Website (WordPress REST)
  slug: usacallerlookup-com-website-wordpress-rest
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.usacallerlookup.com/
- group: docs
  href: https://artifacts.apis.io/usacallerlookup/openapi/_original/usacallerlookup-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/usacallerlookup-openapi.json
- group: agent
  href: https://artifacts.apis.io/usacallerlookup/llms/usacallerlookup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usacallerlookup-llms.txt
- group: build
  href: https://artifacts.apis.io/usacallerlookup/packages/usacallerlookup-packages.yml
  title: ''
  type: Packages
  url: packages/usacallerlookup-packages.yml
- group: build
  href: https://artifacts.apis.io/usacallerlookup/packages/usacallerlookup-packages.yml
  title: ''
  type: SDKs
  url: packages/usacallerlookup-packages.yml
- group: auth
  href: https://artifacts.apis.io/usacallerlookup/authentication/usacallerlookup-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usacallerlookup-authentication.yml
- group: operate
  href: https://artifacts.apis.io/usacallerlookup/rate-limits/usacallerlookup-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/usacallerlookup-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/usacallerlookup/plans/usacallerlookup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usacallerlookup-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/usacallerlookup/errors/usacallerlookup-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usacallerlookup-problem-types.yml
- group: design
  href: https://artifacts.apis.io/usacallerlookup/conventions/usacallerlookup-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usacallerlookup-conventions.yml
- group: design
  href: https://artifacts.apis.io/usacallerlookup/data-model/usacallerlookup-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usacallerlookup-data-model.yml
- group: design
  href: https://artifacts.apis.io/usacallerlookup/conformance/usacallerlookup-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usacallerlookup-conformance.yml
- group: design
  href: https://artifacts.apis.io/usacallerlookup/lifecycle/usacallerlookup-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usacallerlookup-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/usacallerlookup/security/usacallerlookup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usacallerlookup-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/usacallerlookup/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/usacallerlookup/overlays/usacallerlookup-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/usacallerlookup-openapi-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://www.usacallerlookup.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.usacallerlookup.com/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usacallerlookup.com/terms-conditions/
- group: company
  title: ''
  type: Blog
  url: https://www.usacallerlookup.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.usacallerlookup.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.usacallerlookup.com/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usacallerlookup
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.usacallerlookup.com/llms.txt
created: '2026-09-14'
description: A free, read-only JSON REST API over US phone-numbering data and FTC robocall complaint records. No API key or signup required; access is throttled at 60 requests/minute per IP. Data is sourced from FTC Do Not Call complaints and the NANPA registry and dedicated to the public domain under CC0.
image: https://www.usacallerlookup.com/favicon.ico
layout: provider
modified: '2026-09-16'
name: USACallerLookup
nav: Providers
network: true
overview: 'USACallerLookup publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Phone Lookup, Caller ID, robocall, FTC, and Telecommunications.


  USACallerLookup''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 19 more developer resources.'
plans:
- name: Usacallerlookup Plans Pricing
  plan_count: 0
  slug: usacallerlookup-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Usacallerlookup Rate Limits
  slug: usacallerlookup-rate-limits
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 44.6
    discoverability: 64.3
    operational_transparency: 23.7
  previous_composite: 20.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/usacallerlookup/usacallerlookup-2026-10-11T131536.png
security:
- kind: authentication
  name: Usacallerlookup Authentication
  slug: usacallerlookup-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Usacallerlookup Domain Security
  slug: usacallerlookup-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: usacallerlookup-area-code-intel
  slug: usacallerlookup-area-code-intel
- name: usacallerlookup-reverse-lookup
  slug: usacallerlookup-reverse-lookup
slug: usacallerlookup
tags:
- Phone Lookup
- Caller ID
- robocall
- FTC
- Telecommunications
- Open Data
- Fraud Prevention
website: https://www.usacallerlookup.com/
---
