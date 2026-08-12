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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Instructure Agentic Access
  operation_count: 23
  slug: instructure-agentic-access
  summary_line: 23 operations · 5 acting
api_count: 15
apis:
- description: The Canvas GraphQL API provides a flexible query interface for Canvas LMS data, allowing developers to request exactly the fields they need and reduce over-fetching. It follows the Relay Object Identi
  name: Canvas GraphQL API
  slug: canvas-graphql-api
- description: The Instructure Data Access Platform API provides bulk data query capabilities for Canvas data, enabling institutions and developers to access large datasets for analytics, reporting, and data warehou
  name: Data Access Platform (DAP) API
  slug: data-access-platform-api
- description: The Canvas Studio API provides programmatic access to Canvas Studio, Instructure's video and media platform, enabling account administrators and developers to manage media assets, captions, analytics,
  name: Canvas Studio API
  slug: canvas-studio-api
- description: The ExternalTool API from Instructure — 1 operation(s) for externaltool.
  name: Instructure ExternalTool API
  slug: instructure-externaltool-api
- description: The Lti::AccountExternalTool API from Instructure — 2 operation(s) for lti::accountexternaltool.
  name: Instructure Lti::AccountExternalTool API
  slug: instructure-lti-accountexternaltool-api
- description: The Lti::AccountLookup API from Instructure — 1 operation(s) for lti::accountlookup.
  name: Instructure Lti::AccountLookup API
  slug: instructure-lti-accountlookup-api
- description: The Lti::DataService API from Instructure — 2 operation(s) for lti::dataservice.
  name: Instructure Lti::DataService API
  slug: instructure-lti-dataservice-api
- description: The Lti::IMS::Authentication API from Instructure — 1 operation(s) for lti::ims::authentication.
  name: Instructure Lti::IMS::Authentication API
  slug: instructure-lti-ims-authentication-api
- description: The Lti::IMS::DynamicRegistration API from Instructure — 3 operation(s) for lti::ims::dynamicregistration.
  name: Instructure Lti::IMS::DynamicRegistration API
  slug: instructure-lti-ims-dynamicregistration-api
- description: The Lti::IMS::LineItem API from Instructure — 2 operation(s) for lti::ims::lineitem.
  name: Instructure Lti::IMS::LineItem API
  slug: instructure-lti-ims-lineitem-api
- description: The Lti::IMS::NamesAndRole API from Instructure — 2 operation(s) for lti::ims::namesandrole.
  name: Instructure Lti::IMS::NamesAndRole API
  slug: instructure-lti-ims-namesandrole-api
- description: The Lti::IMS::Result API from Instructure — 2 operation(s) for lti::ims::result.
  name: Instructure Lti::IMS::Result API
  slug: instructure-lti-ims-result-api
- description: The Lti::MembershipService API from Instructure — 1 operation(s) for lti::membershipservice.
  name: Instructure Lti::MembershipService API
  slug: instructure-lti-membershipservice-api
- description: The Lti::ToolConfigurationsApi API from Instructure — 3 operation(s) for lti::toolconfigurationsapi.
  name: Instructure Lti::ToolConfigurationsApi API
  slug: instructure-lti-toolconfigurationsapi-api
- description: The Security API from Instructure — 2 operation(s) for security.
  name: Instructure Security API
  slug: instructure-security-api
artifact_total: 48
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instructure-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/instructure-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/instructure-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instructure-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instructure-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/instructure-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.instructure.com
- group: docs
  title: ''
  type: Documentation
  url: https://developerdocs.instructure.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/instructure
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instructure
- group: company
  title: ''
  type: Blog
  url: https://www.instructure.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instructure.com/canvas/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instructure.com/
- group: other
  title: ''
  type: X
  url: https://x.com/instructure
- group: commercial
  title: ''
  type: Plans
  url: plans/instructure-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instructure-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/instructure-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/instructure-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/instructure-context.jsonld
created: '2026-06-13'
description: Instructure is an EdTech company best known for Canvas LMS, a widely adopted learning management system used by thousands of educational institutions and organizations worldwide. The platform provides a comprehensive REST API and GraphQL API enabling developers to programmatically access and manage courses, enrollments, assignments, grades, discussions, and institutional data. Instructure also offers the Data Access Platform (DAP) for bulk data queries, New Quizzes API, Canvas Studio API, and support for LTI 1.3 integrations. Authentication is handled via OAuth2 with per-token dynamic rate limiting, and all API responses are returned in JSON over HTTPS.
examples:
- key_count: 2
  name: Instructure Externaltool Examples
  slug: instructure-externaltool-examples
- key_count: 2
  name: Instructure Lti Accountexternaltool Examples
  slug: instructure-lti-accountexternaltool-examples
- key_count: 2
  name: Instructure Lti Accountlookup Examples
  slug: instructure-lti-accountlookup-examples
- key_count: 2
  name: Instructure Lti Dataservice Examples
  slug: instructure-lti-dataservice-examples
- key_count: 2
  name: Instructure Lti Ims Authentication Examples
  slug: instructure-lti-ims-authentication-examples
- key_count: 2
  name: Instructure Lti Ims Dynamicregistration Examples
  slug: instructure-lti-ims-dynamicregistration-examples
- key_count: 2
  name: Instructure Lti Ims Lineitem Examples
  slug: instructure-lti-ims-lineitem-examples
- key_count: 2
  name: Instructure Lti Ims Namesandrole Examples
  slug: instructure-lti-ims-namesandrole-examples
- key_count: 2
  name: Instructure Lti Ims Result Examples
  slug: instructure-lti-ims-result-examples
- key_count: 2
  name: Instructure Lti Membershipservice Examples
  slug: instructure-lti-membershipservice-examples
- key_count: 2
  name: Instructure Lti Toolconfigurationsapi Examples
  slug: instructure-lti-toolconfigurationsapi-examples
- key_count: 2
  name: Instructure Security Examples
  slug: instructure-security-examples
finops:
- name: Instructure Finops
  service_category: ''
  slug: instructure-finops
graphqls:
- description: The Canvas LMS GraphQL API provides a flexible query interface for Canvas LMS data, allowing developers to request exactly the fields they need and reduce over-fetching. It follows the Relay Object Id
  name: Instructure Canvas GraphQL API
  slug: instructure-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instructure.png
json_schemas:
- name: Lti Accountexternaltool Get Response
  property_count: 52
  slug: Lti-AccountExternalTool-GET-response
- name: Lti Accountlookup Get Response
  property_count: 7
  slug: Lti-AccountLookup-GET-response
- name: Lti Ims Dynamicregistration Get Response
  property_count: 3
  slug: Lti-IMS-DynamicRegistration-GET-response
- name: Lti Ims Dynamicregistration Post Response
  property_count: 11
  slug: Lti-IMS-DynamicRegistration-POST-response
- name: Lti Ims Lineitem Get Response
  property_count: 6
  slug: Lti-IMS-LineItem-GET-response
- name: Lti Ims Namesandrole Get Response
  property_count: 3
  slug: Lti-IMS-NamesAndRole-GET-response
- name: Lti Ims Result Get Response
  property_count: 5
  slug: Lti-IMS-Result-GET-response
- name: Lti Membershipservice Get Response
  property_count: 6
  slug: Lti-MembershipService-GET-response
- name: Security Get Response
  property_count: 14
  slug: Security-GET-response
jsonld:
- class_count: 63
  name: Instructure Context
  property_count: 22
  slug: instructure-context
layout: provider
modified: '2026-06-13'
name: Instructure
nav: Providers
network: true
overview: 'Instructure publishes 12 APIs on the [APIs.io](https://apis.io/) network, including ExternalTool API, Lti::AccountExternalTool API, Lti::AccountLookup API, and 9 more. Tagged areas include EdTech, Education, LMS, Canvas, and Courses.


  The Instructure catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Instructure''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Instructure Plans Pricing
  plan_count: 3
  slug: instructure-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 0
  name: Instructure Rate Limits
  slug: instructure-rate-limits
rules:
- name: Instructure API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: instructure-jsonschema-spectral-rules
scopes:
- name: Instructure Scopes
  scope_count: 17
  slug: instructure-scopes
  summary_line: 17 scopes · authorizationCode
score:
  band: developing
  composite: 48.9
  delta: -0.5
  facets:
    commercial_clarity: 57.9
    contract_quality: 58.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instructure/refs/heads/main/screenshots/instructure-2026-06-20T183421.png
security:
- kind: authentication
  name: Instructure Authentication
  slug: instructure-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Instructure Domain Security
  slug: instructure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Instructure Vulnerability Disclosure
  slug: instructure-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Instructure Trust Center
  slug: instructure-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: instructure
tags:
- EdTech
- Education
- LMS
- Canvas
- Courses
- Enrollments
- Assignments
- Grades
- Discussions
- GraphQL
- LTI
- Learning Management
website: https://www.instructure.com
---
