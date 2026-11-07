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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.adonmo.com
  baseurl_source: declared
  description: The acumen API from Adonmo Private Limited — 2 operation(s) for acumen.
  name: Adonmo Private Limited Acumen API
  slug: adonmoprivatelimited-acumen-api
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/adonmoprivatelimited/overlays/adonmoprivatelimited-adonmo-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adonmoprivatelimited-adonmo-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://adonmo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.adonmo.com/apidocs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.adonmo.com/apidocs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.adonmo.com/apidocs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adonmo
- group: operate
  title: ''
  type: Support
  url: https://adonmo.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://acumencms.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://acumencms.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.acumencms.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adonmo.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adonmo.com/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/adonmoprivatelimited/llms/adonmoprivatelimited-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adonmoprivatelimited-llms.txt
- group: build
  href: https://artifacts.apis.io/adonmoprivatelimited/packages/adonmoprivatelimited-packages.yml
  title: ''
  type: Packages
  url: packages/adonmoprivatelimited-packages.yml
- group: design
  href: https://artifacts.apis.io/adonmoprivatelimited/conventions/adonmoprivatelimited-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adonmoprivatelimited-conventions.yml
- group: design
  href: https://artifacts.apis.io/adonmoprivatelimited/conformance/adonmoprivatelimited-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adonmoprivatelimited-conformance.yml
- group: design
  href: https://artifacts.apis.io/adonmoprivatelimited/lifecycle/adonmoprivatelimited-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adonmoprivatelimited-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/adonmoprivatelimited/security/adonmoprivatelimited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adonmoprivatelimited-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/adonmoprivatelimited/plans/adonmoprivatelimited-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adonmoprivatelimited-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/adonmoprivatelimited/rate-limits/adonmoprivatelimited-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adonmoprivatelimited-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/adonmoprivatelimited/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/adonmoprivatelimited/mcp/adonmoprivatelimited-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/adonmoprivatelimited-mcp.yml
- group: build
  href: https://artifacts.apis.io/adonmoprivatelimited/mcp/adonmoprivatelimited-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adonmoprivatelimited-tool-crosswalk.yml
created: '2026-09-07'
description: Adonmo Private Limited (AdOnMo) is a Hyderabad, India based ambient digital out-of-home (DOOH) advertising company, incorporated in 2016, that operates what it describes as India's largest ambient DOOH network — 66,000+ smart digital screens across 27+ Indian cities in residential lobbies, corporate offices, gyms, malls and transit environments, reaching a claimed 12M+ daily viewers. The company sells campaigns through its AdServe programmatic platform and a self-serve booking portal, and it operates the screens themselves with Acumen CMS, its digital-signage content management product. Adonmo publishes a small first-party OpenAPI 3.0.0 contract, "Adonmo API", from a Flasgger-backed Swagger UI on its production API host.
image: https://adonmo.com/icon-512.png
layout: provider
modified: '2026-09-07'
name: Adonmo
nav: Providers
network: true
overview: 'Adonmo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Private Limited Acumen API. Tagged areas include Advertising, Digital Out Of Home, Digital Signage, AdTech, and Content Management.


  The Adonmo catalog on APIs.io includes 1 Spectral governance ruleset.


  Adonmo''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Adonmoprivatelimited Plans Pricing
  plan_count: 1
  slug: adonmoprivatelimited-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Adonmoprivatelimited Rate Limits
  slug: adonmoprivatelimited-rate-limits
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Adonmo API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: adonmoprivatelimited-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 34.9
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 39.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/adonmoprivatelimited/adonmoprivatelimited-2026-10-11T092832.png
security:
- kind: authentication
  name: Adonmoprivatelimited Authentication
  slug: adonmoprivatelimited-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adonmoprivatelimited Domain Security
  slug: adonmoprivatelimited-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: adonmo-delete-spot
  slug: adonmoprivatelimited-delete-spot
- name: adonmo-list-spots
  slug: adonmoprivatelimited-list-spots
slug: adonmoprivatelimited
tags:
- Advertising
- Digital Out Of Home
- Digital Signage
- AdTech
- Content Management
- Marketing
- India
- Company
website: https://adonmo.com/
---
