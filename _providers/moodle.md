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
  score: 0.6
  scored_at: '2026-11-06'
api_count: 12
apis:
- description: Exposes Moodle functionality as web services so external programs can integrate with a Moodle site for users, courses, enrollments, grading, and other operations. Supports REST, XML-RPC, and SOAP prot
  name: Moodle Web Services API
  slug: web-services
- description: Allows developers to expose parametrized functions to external systems, forming the basis of Moodle's web services and powering integrations consumed via REST, SOAP, and XML-RPC.
  name: Moodle External Functions API
  slug: external-functions
- description: Provides functions to determine what the current user is allowed to do, checking roles, capabilities, and permissions across system, course, and activity contexts.
  name: Moodle Access API
  slug: access
- description: An extension of the Access API that defines the set of actions a user is allowed to perform on certain system levels through assignable roles and capabilities.
  name: Moodle Roles API
  slug: roles
- description: Enables safe, consistent database read and write operations across Moodle, abstracting the underlying database driver and providing helpers for common query patterns.
  name: Moodle Data Manipulation API (DML)
  slug: dml
- description: Manages file storage across plugins, providing a unified interface for uploading, retrieving, and serving files associated with users, courses, and activities.
  name: Moodle File API
  slug: file
- description: Defines and processes user data submitted through web forms, including validation, rendering, and persistence.
  name: Moodle Form API
  slug: form
- description: Defines event handlers for inter-plugin communication and logging, enabling decoupled, observer-style integrations across Moodle.
  name: Moodle Events API
  slug: events
- description: Enables indirect communication between core and plugins through well-defined extension points, allowing plugins to react to and modify core behavior.
  name: Moodle Hooks API
  slug: hooks
- description: Describes stored personal data and supports discovery, export, and deletion of user data across plugins for GDPR and similar privacy compliance.
  name: Moodle Privacy API
  slug: privacy
- description: Executes background jobs on a schedule or as one-off operations, allowing plugins to defer long-running work to cron processing.
  name: Moodle Task API
  slug: task
- description: Manages payment processing in Moodle, providing pluggable payment gateways for paid enrollments and other monetized features.
  name: Moodle Payment API
  slug: payment
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/moodle/plans/moodle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moodle-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/moodle/rate-limits/moodle-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moodle-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/moodle/finops/moodle-finops.yml
  title: ''
  type: FinOps
  url: finops/moodle-finops.yml
- group: auth
  href: https://artifacts.apis.io/moodle/security/moodle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moodle-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moodle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moodle
- group: start
  title: ''
  type: Portal
  url: https://moodledev.io
- group: docs
  title: ''
  type: Documentation
  url: https://moodledev.io/docs/apis
- group: company
  title: ''
  type: Website
  url: https://moodle.org
- group: company
  title: ''
  type: Blog
  url: https://moodle.com/news/
created: '2025-01-08'
description: Moodle is the world's open source learning platform, used by educators and organizations to deliver online courses and learning experiences. The Moodle developer platform exposes a broad set of internal APIs for plugin and core development, plus a Web Services API that enables external systems to integrate with Moodle for users, courses, enrollments, grading, and more.
finops:
- has_sources: false
  method: generated
  name: Moodle Finops
  primary_unit: request
  service_category: API
  slug: moodle-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moodle.png
layout: provider
modified: '2026-04-28'
name: Moodle
nav: Providers
network: true
overview: 'Moodle is listed with 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Learning, EdTech, LMS, Moodle, and Open Source.


  Moodle''s developer surface includes developer portal, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Moodle Plans Pricing
  plan_count: 3
  slug: moodle-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Moodle Rate Limits
  slug: moodle-rate-limits
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 62.5
    operational_transparency: 10.5
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/moodle/moodle-2026-06-20T185749.png
security:
- kind: domain-security
  name: Moodle Domain Security
  slug: moodle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moodle
tags:
- E-Learning
- EdTech
- LMS
- Moodle
- Open Source
- Web Services
website: https://moodle.org
---
