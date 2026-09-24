---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-09-24'
api_count: 2
apis:
- baseURL: https://api.genderapi.io
  baseurl_source: declared
  description: REST + JSON API that infers gender from first/full names, email addresses, and social usernames, with bulk/multi-country requests, phone validation, and credit/quota endpoints. Supports Bearer token a
  name: GenderAPI.io
  slug: genderapiio
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/security/ozan-soft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ozan-soft-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/authentication/ozan-soft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ozan-soft-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://www.genderapi.io/docs-authentication
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/llms/ozan-soft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ozan-soft-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.genderapi.io/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/skills/ozan-soft-integrate-genderapi.md
  title: ''
  type: AgentSkill
  url: skills/ozan-soft-integrate-genderapi.md
- group: agent
  title: ''
  type: AgentSkill
  url: https://www.genderapi.io/skill.md
- group: other
  title: ''
  type: APIsJson
  url: https://www.genderapi.io/apis.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/well-known/ozan-soft-apis-json.json
  title: ''
  type: APIsJson
  url: well-known/ozan-soft-apis-json.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/packages/ozan-soft-packages.yml
  title: ''
  type: Packages
  url: packages/ozan-soft-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/packages/ozan-soft-packages.yml
  title: ''
  type: SDKs
  url: packages/ozan-soft-packages.yml
- group: build
  title: ''
  type: JavaScript SDK
  url: https://github.com/GenderAPI/genderapi-js
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/GenderAPI/genderapi-python
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/GenderAPI/genderapi-php
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/GenderAPI/genderapi-ruby
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/GenderAPI/genderapi-java
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/overlays/ozan-soft-openapi-overlay.yaml
  title: ''
  type: OpenAPIOverlay
  url: overlays/ozan-soft-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/conformance/ozan-soft-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ozan-soft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.genderapi.io/gdpr-compliance
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/errors/ozan-soft-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ozan-soft-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/lifecycle/ozan-soft-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ozan-soft-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/lifecycle/ozan-soft-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ozan-soft-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/conventions/ozan-soft-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ozan-soft-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/data-model/ozan-soft-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ozan-soft-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/plans/ozan-soft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ozan-soft-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ozan-soft/refs/heads/main/rate-limits/ozan-soft-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ozan-soft-rate-limits.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.genderapi.io/gdpr-compliance
- group: other
  title: ''
  type: Subprocessors
  url: https://www.genderapi.io/subprocessors
- group: company
  title: ''
  type: Website
  url: https://www.genderapi.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.genderapi.io/api-documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.genderapi.io/price
- group: start
  title: ''
  type: SignUp
  url: https://app.genderapi.io/user/register
- group: start
  title: ''
  type: Login
  url: https://app.genderapi.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.genderapi.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genderapi.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.genderapi.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.genderapi.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GenderAPI
created: '2026-09-19'
description: Independent software company based in Ankara, Türkiye, whose flagship developer product is GenderAPI.io — a REST API for gender detection and name/email/username analysis, phone validation, and demographic data enrichment.
layout: provider
modified: '2026-09-20'
name: Ozan Soft
nav: Providers
network: true
overview: 'Ozan Soft publishes 1 API on the [APIs.io](https://apis.io/) network: GenderAPI.io. Tagged areas include Data Enrichment, Gender Detection, Name Analysis, Demographics, and Identity.


  Ozan Soft''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 33 more developer resources.'
plans:
- name: Ozan Soft Plans Pricing
  plan_count: 13
  slug: ozan-soft-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Ozan Soft Rate Limits
  slug: ozan-soft-rate-limits
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 73.8
    discoverability: 66.7
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Ozan Soft Authentication
  slug: ozan-soft-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ozan Soft Domain Security
  slug: ozan-soft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ozan-soft
tags:
- Data Enrichment
- Gender Detection
- Name Analysis
- Demographics
- Identity
- Marketing Data
- Developer API
- Phone Validation
website: https://www.genderapi.io/
---
