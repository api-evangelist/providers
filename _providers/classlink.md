---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: OneRoster v1.1-compliant REST API for exchanging K-12 roster data—users, orgs, courses, classes, enrollments, academicSessions, demographics, and resources—between ClassLink Roster Server and third-pa
  name: ClassLink OneRoster API
  slug: classlink-oneroster-api
- description: OAuth 2.0 authorization code flow enabling third-party applications to authenticate users via ClassLink LaunchPad, obtain access tokens, and retrieve identity profile data including name, email, and d
  name: ClassLink OAuth2 / SSO API
  slug: classlink-oauth2-sso-api
- description: API providing district-level edtech usage analytics, application engagement metrics, and license utilization data gathered by ClassLink Analytics and Analytics+, enabling administrators and vendors to
  name: ClassLink Analytics API
  slug: classlink-analytics-api
- description: REST API for provisioning and managing application accounts within ClassLink, allowing administrators to automate creation, update, and deprovisioning of user accounts in connected applications throug
  name: ClassLink Application Provisioning API
  slug: classlink-application-provisioning-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/classlink-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/classlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.classlink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.classlink.com/s/classlink-partners-home
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/classlinkinc
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/classlinkinc/request-libraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/classlink
- group: other
  title: ''
  type: X
  url: https://twitter.com/classlink
- group: company
  title: ''
  type: Blog
  url: https://www.classlink.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.classlink.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.classlink.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/classlink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/classlink-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/classlink-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/classlink-context.jsonld
created: '2026-06-13'
description: ClassLink is an EdTech identity and access management platform purpose-built for K-12 school districts, providing single sign-on (SSO) to over 6,000 digital learning resources through its LaunchPad portal. The platform offers a OneRoster-compliant REST API for secure rostering and student data exchange, enabling automated provisioning and synchronization between student information systems and educational applications. ClassLink OneSync handles identity management and account provisioning integrations with any SIS, while Roster Server facilitates standards-based data sharing using OAuth 1.0 and OAuth 2.0. The Analytics and Analytics+ products expose usage telemetry APIs that help district administrators track edtech engagement and license utilization across all devices. ClassLink maintains open developer resources including multi-language request libraries (C#, Java, JavaScript, PHP, Ruby, Python, Go) on GitHub and a partner developer portal.
finops:
- name: Classlink Finops
  service_category: ''
  slug: classlink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/classlink.png
jsonld:
- class_count: 77
  name: Classlink Context
  property_count: 8
  slug: classlink-context
layout: provider
modified: '2026-06-13'
name: ClassLink
nav: Providers
network: true
overview: 'ClassLink publishes 1 API on the [APIs.io](https://apis.io/) network: OneRoster API. Tagged areas include EdTech, Education, Identity, Single Sign-On, and SSO.


  The ClassLink catalog on APIs.io includes 1 JSON-LD context.


  ClassLink''s developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Classlink Plans Pricing
  plan_count: 3
  slug: classlink-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Classlink Rate Limits
  slug: classlink-rate-limits
score:
  band: thin
  composite: 35.2
  delta: -4.5
  facets:
    commercial_clarity: 57.9
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/classlink/refs/heads/main/screenshots/classlink-2026-06-20T174447.png
security:
- kind: domain-security
  name: Classlink Domain Security
  slug: classlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Classlink Trust Center
  slug: classlink-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
slug: classlink
tags:
- EdTech
- Education
- Identity
- Single Sign-On
- SSO
- OneRoster
- Rostering
- Provisioning
- Analytics
- K-12
- LTI
- OAuth
- Student Data
website: https://www.classlink.com/
---
