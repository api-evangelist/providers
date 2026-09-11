---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-10'
api_count: 1
apis:
- baseURL: https://api.adonmo.com
  baseurl_source: declared
  description: Adonmo's common API for its portals and services, published as an OpenAPI 3.0.0 document behind a Flasgger Swagger UI at https://api.adonmo.com/apidocs/. The publicly served contract exposes two opera
  name: Adonmo API
  slug: adonmoprivatelimited-adonmo-api
artifact_total: 5
common:
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
  title: ''
  type: LLMsTxt
  url: llms/adonmoprivatelimited-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/adonmoprivatelimited-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adonmoprivatelimited-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adonmoprivatelimited-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adonmoprivatelimited-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adonmoprivatelimited-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adonmoprivatelimited-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adonmoprivatelimited-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/adonmoprivatelimited-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/adonmoprivatelimited-tool-crosswalk.yml
created: '2026-09-07'
description: Adonmo Private Limited (AdOnMo) is a Hyderabad, India based ambient digital out-of-home (DOOH) advertising company, incorporated in 2016, that operates what it describes as India's largest ambient DOOH network — 66,000+ smart digital screens across 27+ Indian cities in residential lobbies, corporate offices, gyms, malls and transit environments, reaching a claimed 12M+ daily viewers. The company sells campaigns through its AdServe programmatic platform and a self-serve booking portal, and it operates the screens themselves with Acumen CMS, its digital-signage content management product. Adonmo publishes a small first-party OpenAPI 3.0.0 contract, "Adonmo API", from a Flasgger-backed Swagger UI on its production API host.
image: https://adonmo.com/icon-512.png
layout: provider
modified: '2026-09-07'
name: Adonmo Private Limited
nav: Providers
network: true
overview: 'Adonmo Private Limited publishes 1 API on the [APIs.io](https://apis.io/) network: Adonmo API. Tagged areas include Advertising, Digital Out-of-Home, DOOH, Digital Signage, and AdTech.


  Adonmo Private Limited''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Adonmoprivatelimited Plans Pricing
  plan_count: 1
  slug: adonmoprivatelimited-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Adonmoprivatelimited Rate Limits
  slug: adonmoprivatelimited-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 38.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 38.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Adonmoprivatelimited Authentication
  slug: adonmoprivatelimited-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adonmoprivatelimited Domain Security
  slug: adonmoprivatelimited-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adonmoprivatelimited
tags:
- Advertising
- Digital Out-of-Home
- DOOH
- Digital Signage
- AdTech
- Content Management
- Marketing
- India
- Company
website: https://adonmo.com/
---
