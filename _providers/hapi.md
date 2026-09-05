---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'hapi is a rich, configuration-centric framework for building web applications and APIs in Node.js. It provides a powerful plugin system, built-in input validation with Joi, authentication strategies, '
  name: Hapi
  slug: hapi
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/hapijs/hapi/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/hapijs/hapi/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/hapijs/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/hapijs/.github/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hapi.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://hapi.dev/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://hapi.dev/tutorials/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hapijs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hapijs/hapi
- group: build
  title: ''
  type: Plugins
  url: https://hapi.dev/plugins/
- group: other
  title: ''
  type: Resources
  url: https://hapi.dev/resources/
created: '2026-03-26'
description: hapi is a rich, configuration-centric framework for building web applications and APIs in Node.js. It provides a powerful plugin system, built-in input validation with Joi, authentication strategies, caching, cookie handling, and a focus on security and reliability for enterprise-grade applications.
finops:
- name: Hapi Finops
  service_category: API
  slug: hapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hapi.png
json_schemas:
- name: hapi Route Definition
  property_count: 0
  slug: hapi-route-definition
- name: hapi Server Configuration
  property_count: 10
  slug: hapi-server-configuration
layout: provider
modified: '2026-03-26'
name: Hapi
nav: Providers
network: true
overview: 'Hapi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Frameworks, JavaScript, Node.js, and Validation.


  The Hapi catalog on APIs.io includes 1 Spectral governance ruleset.


  Hapi''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Hapi Plans Pricing
  plan_count: 3
  slug: hapi-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Hapi Rate Limits
  slug: hapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Hapi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hapi-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 13.3
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 17.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hapi/refs/heads/main/screenshots/hapi-2026-06-20T182508.png
security:
- kind: domain-security
  name: Hapi Domain Security
  slug: hapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hapi
tags:
- Authentication
- Frameworks
- JavaScript
- Node.js
- Validation
- Web Framework
website: https://hapi.dev/
---
