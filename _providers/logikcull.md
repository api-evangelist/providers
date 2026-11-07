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
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for programmatic access to Logikcull's eDiscovery platform, enabling document upload, project management, tagging, redactions, and production set generation for legal review workflows.
  name: Logikcull API
  slug: logikcull-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.logikcull.com/
- group: auth
  href: https://artifacts.apis.io/logikcull/security/logikcull-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/logikcull-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/logikcull/security/logikcull-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/logikcull-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/logikcull/security/logikcull-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logikcull-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/logikcull/plans/logikcull-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logikcull-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/logikcull/rate-limits/logikcull-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/logikcull-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/logikcull/finops/logikcull-finops.yml
  title: ''
  type: FinOps
  url: finops/logikcull-finops.yml
- group: operate
  title: ''
  type: Status
  url: https://status.logikcull.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logikcull.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.logikcull.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.revealdata.com/logikcull
- group: operate
  title: ''
  type: Contact
  url: https://www.logikcull.com/company/contact-us
created: '2026-06-13'
description: Cloud eDiscovery platform with a REST API for uploading case documents, managing review projects, applying tags and redactions, and generating production sets. Logikcull enables legal teams to process, review, and produce data in a self-service model with integrations for Slack, Microsoft 365, Google Workspace, Box, and Dropbox.
finops:
- has_sources: false
  method: generated
  name: Logikcull Finops
  primary_unit: ''
  service_category: ''
  slug: logikcull-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logikcull.png
jsonld:
- class_count: 28
  name: Logikcull Context
  property_count: 4
  slug: logikcull-context
layout: provider
modified: '2026-06-13'
name: Logikcull
nav: Providers
network: true
overview: 'Logikcull is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include eDiscovery, Legal, Document Management, Legal Hold, and Redaction.


  The Logikcull catalog on APIs.io includes 1 JSON-LD context.


  Logikcull''s developer surface includes status page, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Logikcull Plans Pricing
  plan_count: 2
  slug: logikcull-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Logikcull Rate Limits
  slug: logikcull-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 34.7
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 26.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/logikcull/logikcull-2026-06-20T184702.png
security:
- kind: domain-security
  name: Logikcull Domain Security
  slug: logikcull-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Logikcull Vulnerability Disclosure
  slug: logikcull-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Logikcull Trust Center
  slug: logikcull-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: logikcull
tags:
- eDiscovery
- Legal
- Document Management
- Legal Hold
- Redaction
- Production Sets
- Cloud
website: https://www.logikcull.com/
---
