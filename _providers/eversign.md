---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RESTful JSON API for creating and sending documents for electronic signature, managing templates, uploading files, tracking audit trails, bulk sending via CSV, and receiving webhook event notification
  name: Eversign API
  slug: eversign-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/eversign/eversign-php-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/eversign/eversign-php-sdk/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/eversign/eversign-php-sdk/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/eversign/eversign-php-sdk/blob/master/LICENSE
- group: auth
  href: https://artifacts.apis.io/eversign/security/eversign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eversign-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eversign.com
- group: docs
  title: ''
  type: Documentation
  url: https://eversign.com/api/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/eversign
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xodosign
- group: company
  title: ''
  type: Blog
  url: https://eversign.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://eversign.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://eversign.com/status-page
- group: other
  title: ''
  type: X
  url: https://twitter.com/geteversign
- group: commercial
  href: https://artifacts.apis.io/eversign/plans/eversign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eversign-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/eversign/rate-limits/eversign-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eversign-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/eversign/finops/eversign-finops.yml
  title: ''
  type: FinOps
  url: finops/eversign-finops.yml
created: '2026-06-13'
description: E-signature and document management platform with a REST API for creating, sending, and managing electronic signature requests, templates, audit trails, bulk sending, embedded signing, and webhook notifications. Now branded as Xodo Sign, formerly eversign.
finops:
- has_sources: false
  method: generated
  name: Eversign Finops
  primary_unit: ''
  service_category: ''
  slug: eversign-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eversign.png
jsonld:
- class_count: 0
  name: Eversign Context
  property_count: 20
  slug: eversign-context
layout: provider
modified: '2026-06-13'
name: Eversign
nav: Providers
network: true
overview: 'Eversign is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Signature, Document Management, PDF, Audit Trail, and Webhook.


  The Eversign catalog on APIs.io includes 1 JSON-LD context.


  Eversign''s developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Eversign Plans Pricing
  plan_count: 6
  slug: eversign-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Eversign Rate Limits
  slug: eversign-rate-limits
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 10.4
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 40.0
  previous_composite: 25.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/eversign/eversign-2026-06-20T180911.png
security:
- kind: domain-security
  name: Eversign Domain Security
  slug: eversign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eversign
tags:
- E-Signature
- Document Management
- PDF
- Audit Trail
- Webhook
- Bulk Sending
website: https://eversign.com
---
