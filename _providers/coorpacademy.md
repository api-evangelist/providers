---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-26'
api_count: 14
apis:
- description: Manages the Coorpacademy content repository per brand — external courses and external contents, skills and custom skills, certifications and certification snapshots, custom playlists, bulk external co
  name: Coorpacademy Content API
  slug: coorpacademy-content-api
- description: Brand (tenant) management for the Coorpacademy platform — create, read, update, delete and migrate brands, check brand existence, list brands, and extract SSO configuration from an uploaded SAML `meta
  name: Coorpacademy Platform API
  slug: coorpacademy-platform-api
- description: 'The learner progression engine — create and read progressions, record moves, answers, clue requests, resource views and extra-life accept/refuse decisions, plus a v2 analytics surface for completion, '
  name: Coorpacademy Progression API
  slug: coorpacademy-progression-api
- description: A separate aggregation service over the same progression data store, exposing DynamoDB-backed per-slide analytics and per-user completion and slide-count reads/writes under a /v1 prefix. 3 paths / 5 o
  name: Coorpacademy Progression Aggregations API
  slug: coorpacademy-progression-aggregations-api
- description: SCIM 2.0 user provisioning and de-provisioning for identity-manager integration, scoped per brand — list, create, find, PUT-update and PATCH-update users. Errors are returned in the SCIM error envelop
  name: Coorpacademy SCIM API
  slug: coorpacademy-scim-api
- description: Backing API for the Coorpacademy SCORM player — fetch slides, chapters, levels, exit nodes and clue payloads, post answers and moves, mark resources as viewed, accept/refuse extra lives, initialise pl
  name: Coorpacademy SCORM Content API
  slug: coorpacademy-scorm-content-api
- description: SCORM package storage and delivery — mint presigned S3 URLs for single and bulk SCORM uploads and serve root and nested files out of an unpacked SCORM resource. 4 paths / 4 operations. Key-gated via a
  name: Coorpacademy SCORM API
  slug: coorpacademy-scorm-api
- description: Transactional email service backed by Mandrill, exposing one operation per templated message the platform sends — onboarding, welcome, signup validation and self-validation, password reset, first-logi
  name: Coorpacademy Email API
  slug: coorpacademy-email-api
- description: Minimal-version gate for the Coorpacademy iOS and Android apps — read and update the minimum installable app version per key, plus a send-email operation. 2 paths / 3 operations. Key-gated via an `Api
  name: Coorpacademy Mobile API
  slug: coorpacademy-mobile-api
- description: Adaptive review mode — list the skills a given learner has available to review and fetch the next review slide for a learner and skill. 2 paths / 2 operations. Key-gated via an `authorization` header.
  name: Coorpacademy Review API
  slug: coorpacademy-review-api
- description: Serves files out of an unpacked H5P interactive-content resource, redirecting (301) to the stored asset. 1 path / 1 operation. Key-gated via a `token` header.
  name: Coorpacademy H5P API
  slug: coorpacademy-h5p-api
- description: Mints a presigned S3 URL for uploading external content of a given file extension. 1 path / 1 operation. The published spec declares no security scheme.
  name: Coorpacademy External Resources API
  slug: coorpacademy-external-resources-api
- description: Media upload and on-the-fly image resize. 1 path / 2 operations. The published spec declares no security scheme.
  name: Coorpacademy Media API
  slug: coorpacademy-media-api
- description: Renders a supplied URL to PDF — used to produce downloadable certificates and reports. 1 path / 1 operation. The published spec declares no security scheme.
  name: Coorpacademy PDF API
  slug: coorpacademy-pdf-api
artifact_total: 19
asyncapis:
- description: ''
  name: Coorpacademy Event Surface
  slug: coorpacademy-event-surface
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coorpacademy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coorpacademy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.coorpacademy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.coorpacademy.com/
- group: operate
  title: ''
  type: Support
  url: https://support.coorpacademy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.coorpacademy.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoorpAcademy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coorpacademy.com/mentions-legales/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coorpacademy.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://coorpacademy.status.io/
- group: start
  title: ''
  type: Login
  url: https://connect.coorpacademy.com/login
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coorpacademy-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coorpacademy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coorpacademy-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coorpacademy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/coorpacademy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coorpacademy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coorpacademy-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/coorpacademy-packages.yml
- group: design
  title: ''
  type: Components
  url: components/coorpacademy-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coorpacademy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/coorpacademy-plans-pricing.yml
created: '2026-08-17'
description: 'Coorpacademy is a Swiss-French corporate digital-learning platform, founded in 2013 and acquired by Australian edtech Go1 in April 2022, now marketed as "Coorpacademy by Go1". It sells a B2B SaaS learning experience platform built on inverted-pedagogy, gamified micro-learning: brand-scoped learning portals, a course and certification catalogue, skills taxonomies, learner progression and adaptive review, battles/leaderboards, and HR analytics. The platform is fronted by a public Swagger UI at api.coorpacademy.com that indexes fourteen internal-but-publicly-documented REST services — content, platform/brand management, progression, progression aggregations, SCIM 2.0 user provisioning, SCORM and SCORM-content players, H5P, transactional email, mobile, review mode, media, external upload and PDF rendering. Access to every service is key-gated; there is no self-serve developer signup, no published pricing, and no partner developer portal, so the specifications are the only machine-readable
  public surface.'
image: https://www.coorpacademy.com/assets/uploads/2025/08/cropped-Coorpacademyby-Go1-Charcoal.png
layout: provider
modified: '2026-08-17'
name: Coorpacademy
nav: Providers
network: true
overview: 'Coorpacademy publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Content API, Platform API, Progression API, and 11 more. Tagged areas include Company, Software-as-a-Service, Corporate Learning, LMS, and Learning Experience Platform.


  The Coorpacademy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coorpacademy''s developer surface includes API reference, documentation, support, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Coorpacademy Plans Pricing
  plan_count: 0
  slug: coorpacademy-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Coorpacademy Rate Limits
  slug: coorpacademy-rate-limits
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 52.9
    developer_ergonomics: 37.5
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 45.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Coorpacademy Authentication
  slug: coorpacademy-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Coorpacademy Domain Security
  slug: coorpacademy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coorpacademy
tags:
- Company
- Software-as-a-Service
- Corporate Learning
- LMS
- Learning Experience Platform
- EdTech
- E-Learning
- SCORM
- h5p
- SCIM
- User Provisioning
- Learning Analytics
- Skills
- Certifications
- Gamification
- France
- Switzerland
website: https://www.coorpacademy.com/
---
