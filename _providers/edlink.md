---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Edlink Agentic Access
  operation_count: 22
  slug: edlink-agentic-access
  summary_line: 22 operations · 1 acting
api_count: 12
apis:
- description: Source connection agents.
  name: Edlink Agents API
  slug: edlink-agents-api
- description: Classes and their enrollments.
  name: Edlink Classes API
  slug: edlink-classes-api
- description: Course catalog.
  name: Edlink Courses API
  slug: edlink-courses-api
- description: Districts shared with the integration.
  name: Edlink Districts API
  slug: edlink-districts-api
- description: Relationships between people and classes.
  name: Edlink Enrollments API
  slug: edlink-enrollments-api
- description: Change events for incremental sync.
  name: Edlink Events API
  slug: edlink-events-api
- description: Institution-level roster and school data.
  name: Edlink Graph API
  slug: edlink-graph-api
- description: Source and integration metadata.
  name: Edlink Integrations API
  slug: edlink-integrations-api
- description: Students, teachers, and other people.
  name: Edlink People API
  slug: edlink-people-api
- description: Schools within a district.
  name: Edlink Schools API
  slug: edlink-schools-api
- description: Sections that subdivide classes.
  name: Edlink Sections API
  slug: edlink-sections-api
- description: OAuth 2.0 and OpenID Connect single sign-on.
  name: Edlink SSO API
  slug: edlink-sso-api
artifact_total: 19
collections:
- collection_type: open
  name: Edlink API
  slug: open-edlink
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edlink-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edlink-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edlink-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://ed.link/community/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edlink
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edlink-inc
- group: company
  title: ''
  type: Website
  url: https://ed.link/
- group: docs
  title: ''
  type: Documentation
  url: https://ed.link/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/edlink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edlink-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/edlink-finops.yml
created: '2026-06-21'
description: Edlink is an education-integration platform offering a unified API for rostering and school data across SIS and LMS systems. The Edlink Graph API exposes normalized districts, schools, classes, sections, courses, people, and enrollments from hundreds of source systems behind a single Bearer-authenticated REST interface, plus SSO, source integrations, and change events.
finops:
- name: Edlink Finops
  service_category: Education Integration
  slug: edlink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edlink.png
layout: provider
modified: '2026-06-21'
name: Edlink
nav: Providers
network: true
overview: 'Edlink publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Classes API, Courses API, and 9 more. Tagged areas include Education, EdTech, Rostering, SIS, and LMS.


  Edlink''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Edlink Plans Pricing
  plan_count: 3
  slug: edlink-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 4
  name: Edlink Rate Limits
  slug: edlink-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edlink/refs/heads/main/screenshots/edlink-2026-07-25T212853.png
security:
- kind: authentication
  name: Edlink Authentication
  slug: edlink-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Edlink Domain Security
  slug: edlink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: edlink
tags:
- Education
- EdTech
- Rostering
- SIS
- LMS
- Integration
- Unified API
website: https://ed.link/
---
