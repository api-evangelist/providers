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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Ninetailed Agentic Access
  operation_count: 6
  slug: ninetailed-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 2
apis:
- description: Batch event ingestion endpoints for profile enrichment.
  name: Ninetailed Events API
  slug: ninetailed-events-api
- description: Operations for creating, reading, updating, and deleting visitor profiles.
  name: Ninetailed Profiles API
  slug: ninetailed-profiles-api
artifact_total: 17
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
random_paper: 13
rate_limits:
- limit_count: 4
  name: Ninetailed Rate Limits
  slug: ninetailed-rate-limits
rules:
- name: Ninetailed API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ninetailed-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.8
  delta: -4.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 65.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
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
