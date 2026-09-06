---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Ninetailed Agentic Access
  operation_count: 6
  slug: ninetailed-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://experience.ninetailed.co/v2
  baseurl_source: declared
  description: Batch event ingestion endpoints for profile enrichment.
  name: Ninetailed Events API
  slug: ninetailed-events-api
- baseURL: https://experience.ninetailed.co/v2
  baseurl_source: declared
  description: Operations for creating, reading, updating, and deleting visitor profiles.
  name: Ninetailed Profiles API
  slug: ninetailed-profiles-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ninetailed Experience Events API
  slug: open-ninetailed-events-api
- collection_type: open
  name: Ninetailed Experience Events Profiles API
  slug: open-ninetailed-profiles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ninetailed-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ninetailed-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ninetailed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ninetailed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.contentful.com/products/personalization/
- group: docs
  title: ''
  type: Documentation
  url: https://www.contentful.com/developers/docs/ninetailed/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ninetailed-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ninetailed
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@Ninetailed
- group: commercial
  title: ''
  type: Pricing
  url: https://www.contentful.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://ninetailedstatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/ninetailedhq
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.contentful.com/developers/docs/ninetailed/ninetailed-changelog/
- group: commercial
  title: ''
  type: Plans
  url: plans/ninetailed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ninetailed-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ninetailed-finops.yml
created: '2026-06-13'
description: Ninetailed (now Contentful Personalization) is an API-first personalization and experimentation platform for content-rich applications. It provides a REST-based Experience API for managing visitor profiles, defining audience segments, running A/B tests, and delivering personalized experiences at the edge. SDKs are available for JavaScript, React, Next.js, Node.js, and React Native.
examples:
- key_count: 4
  name: Batch Events Sync
  slug: batch-events-sync
- key_count: 4
  name: Create Profile
  slug: create-profile
- key_count: 4
  name: Update Profile Identify
  slug: update-profile-identify
finops:
- name: Ninetailed Finops
  service_category: ''
  slug: ninetailed-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ninetailed.png
json_schemas:
- name: NinetailedEvent
  property_count: 7
  slug: ninetailed-event
- name: NinetailedExperience
  property_count: 4
  slug: ninetailed-experience
- name: NinetailedProfile
  property_count: 9
  slug: ninetailed-profile
jsonld:
- class_count: 10
  name: Ninetailed Context
  property_count: 39
  slug: ninetailed-context
layout: provider
modified: '2026-06-13'
name: Ninetailed
nav: Providers
network: true
overview: 'Ninetailed publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and Profiles API. Tagged areas include Personalization, Experimentation, A/B Testing, Audience Segmentation, and Feature Flags.


  The Ninetailed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ninetailed''s developer surface includes documentation, engineering blog, pricing, changelog, and 12 more developer resources.'
plans:
- name: Ninetailed Plans Pricing
  plan_count: 3
  slug: ninetailed-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Ninetailed Rate Limits
  slug: ninetailed-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ninetailed API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ninetailed-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 78.3
    catalog_earned_first_party: 0.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 9.8
    contract_quality: 65.3
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ninetailed/refs/heads/main/screenshots/ninetailed-2026-06-20T190329.png
security:
- kind: domain-security
  name: Ninetailed Domain Security
  slug: ninetailed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ninetailed Vulnerability Disclosure
  slug: ninetailed-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ninetailed Trust Center
  slug: ninetailed-trust-center
  summary_line: SOC 2, ISO 27001
slug: ninetailed
tags:
- Personalization
- Experimentation
- A/B Testing
- Audience Segmentation
- Feature Flags
- Headless CMS
- Edge Computing
- Content Management
website: https://www.contentful.com/products/personalization/
---
