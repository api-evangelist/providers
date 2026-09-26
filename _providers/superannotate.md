---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: REST API and Python SDK for managing annotation projects, datasets, folders, items, annotations, annotation classes, exports, custom metadata, subsets, images, and team operations on the SuperAnnotate
  name: SuperAnnotate API
  slug: superannotate-api
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/security/superannotate-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/superannotate-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/security/superannotate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/superannotate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.superannotate.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.superannotate.com/docs/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superannotateai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/superannotate/
- group: other
  title: ''
  type: X
  url: https://x.com/superannotate
- group: company
  title: ''
  type: Blog
  url: https://www.superannotate.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.superannotate.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superannotate.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/plans/superannotate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/superannotate-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/rate-limits/superannotate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/superannotate-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/finops/superannotate-finops.yml
  title: ''
  type: FinOps
  url: finops/superannotate-finops.yml
- group: company
  href: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/blogs/blogs.json
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/json-ld/superannotate-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/superannotate-context.jsonld
created: 2026-06-12
description: SuperAnnotate is an AI data annotation platform purpose-built for computer vision and NLP teams that need to build, fine-tune, and iterate machine learning models with high-quality training data. The platform provides a Python SDK and REST API for managing annotation projects, datasets, folders, items, annotation classes, exports, and team workflows programmatically. SuperAnnotate's Orchestrate module enables event-driven automation pipelines with configurable compute hours, while Agent Hub offers MCP server integration for AI agent workflows. The platform integrates natively with AWS, GCP, Azure, Databricks, and Snowflake, supporting enterprise-grade data governance and security requirements.
finops:
- name: Superannotate Finops
  service_category: ''
  slug: superannotate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superannotate.png
jsonld:
- class_count: 22
  name: Superannotate Context
  property_count: 26
  slug: superannotate-context
layout: provider
modified: 2026-06-12
name: SuperAnnotate
nav: Providers
network: true
overview: 'SuperAnnotate publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Annotation, Data Labeling, Computer Vision, and NLP.


  The SuperAnnotate catalog on APIs.io includes 1 JSON-LD context.


  SuperAnnotate''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Superannotate Plans Pricing
  plan_count: 3
  slug: superannotate-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Superannotate Rate Limits
  slug: superannotate-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 69.0
    catalog_earned_first_party: 0.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 54.7
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 13.1
    discoverability: 68.3
    operational_transparency: 37.4
  previous_composite: 29.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/superannotate/refs/heads/main/screenshots/superannotate-2026-06-20T194708.png
security:
- kind: domain-security
  name: Superannotate Domain Security
  slug: superannotate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Superannotate Trust Center
  slug: superannotate-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: superannotate
tags:
- Artificial Intelligence
- Annotation
- Data Labeling
- Computer Vision
- NLP
- Machine Learning
- Training Data
- Image Annotation
- Video Annotation
- Text Annotation
- Audio Annotation
- MLOps
website: https://www.superannotate.com
---
