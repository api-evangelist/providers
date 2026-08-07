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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Orbit Agentic Access
  operation_count: 33
  slug: orbit-agentic-access
  summary_line: 33 operations · 15 acting
api_count: 9
apis:
- description: The Activities API from Orbit — 5 operation(s) for activities.
  name: Orbit Activities API
  slug: orbit-activities-api
- description: The Activity Types API from Orbit — 1 operation(s) for activity types.
  name: Orbit Activity Types API
  slug: orbit-activity-types-api
- description: The Members API from Orbit — 5 operation(s) for members.
  name: Orbit Members API
  slug: orbit-members-api
- description: The Notes API from Orbit — 2 operation(s) for notes.
  name: Orbit Notes API
  slug: orbit-notes-api
- description: The Organizations API from Orbit — 2 operation(s) for organizations.
  name: Orbit Organizations API
  slug: orbit-organizations-api
- description: The Reports API from Orbit — 1 operation(s) for reports.
  name: Orbit Reports API
  slug: orbit-reports-api
- description: The Users API from Orbit — 1 operation(s) for users.
  name: Orbit Users API
  slug: orbit-users-api
- description: The Webhooks API from Orbit — 2 operation(s) for webhooks.
  name: Orbit Webhooks API
  slug: orbit-webhooks-api
- description: The Workspaces API from Orbit — 2 operation(s) for workspaces.
  name: Orbit Workspaces API
  slug: orbit-workspaces-api
artifact_total: 55
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orbit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orbit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://orbit.love/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orbit.love/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/orbit-love
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orbitco
- group: other
  title: ''
  type: X
  url: https://x.com/OrbitModel
- group: company
  title: ''
  type: Blog
  url: https://orbit.love/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://orbit.love/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.orbit.love/
- group: commercial
  title: ''
  type: Plans
  url: plans/orbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orbit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/orbit-finops.yml
created: '2026-06-13'
description: Developer relations and community intelligence platform with a REST API for tracking member activities, measuring community growth, and managing developer advocates and contributors. Orbit was acquired by Postman in April 2024.
examples:
- key_count: 1
  name: Orbit Get User 200 Response
  slug: orbit-get-user-200-response
- key_count: 3
  name: Orbit Get Workspace Slug Activities 200 Response
  slug: orbit-get-workspace-slug-activities-200-response
- key_count: 2
  name: Orbit Get Workspace Slug Activities Id 200 Response
  slug: orbit-get-workspace-slug-activities-id-200-response
- key_count: 2
  name: Orbit Get Workspace Slug Activity Types 200 Response
  slug: orbit-get-workspace-slug-activity-types-200-response
- key_count: 3
  name: Orbit Get Workspace Slug Members 200 Response
  slug: orbit-get-workspace-slug-members-200-response
- key_count: 2
  name: Orbit Get Workspace Slug Members Find 200 Response
  slug: orbit-get-workspace-slug-members-find-200-response
- key_count: 2
  name: Orbit Get Workspace Slug Members Member Slug 200 Response
  slug: orbit-get-workspace-slug-members-member-slug-200-response
- key_count: 3
  name: Orbit Get Workspace Slug Members Member Slug Activities 200 Response
  slug: orbit-get-workspace-slug-members-member-slug-activities-200-response
- key_count: 3
  name: Orbit Get Workspace Slug Members Member Slug Notes 200 Response
  slug: orbit-get-workspace-slug-members-member-slug-notes-200-response
- key_count: 2
  name: Orbit Get Workspace Slug Organizations 200 Response
  slug: orbit-get-workspace-slug-organizations-200-response
- key_count: 1
  name: Orbit Get Workspace Slug Organizations Organization Id 200 Response
  slug: orbit-get-workspace-slug-organizations-organization-id-200-response
- key_count: 3
  name: Orbit Get Workspace Slug Organizations Organization Id Activities 200 Response
  slug: orbit-get-workspace-slug-organizations-organization-id-activities-200-response
- key_count: 2
  name: Orbit Get Workspace Slug Organizations Organization Id Members 200 Response
  slug: orbit-get-workspace-slug-organizations-organization-id-members-200-response
- key_count: 1
  name: Orbit Get Workspace Slug Reports 200 Response
  slug: orbit-get-workspace-slug-reports-200-response
- key_count: 2
  name: Orbit Get Workspace Slug Webhooks 200 Response
  slug: orbit-get-workspace-slug-webhooks-200-response
- key_count: 1
  name: Orbit Get Workspace Slug Webhooks Id 200 Response
  slug: orbit-get-workspace-slug-webhooks-id-200-response
- key_count: 2
  name: Orbit Get Workspaces 200 Response
  slug: orbit-get-workspaces-200-response
- key_count: 2
  name: Orbit Get Workspaces Workspace Slug 200 Response
  slug: orbit-get-workspaces-workspace-slug-200-response
- key_count: 2
  name: Orbit Post Workspace Slug Activities 201 Response
  slug: orbit-post-workspace-slug-activities-201-response
- key_count: 2
  name: Orbit Post Workspace Slug Members 200 Response
  slug: orbit-post-workspace-slug-members-200-response
- key_count: 2
  name: Orbit Post Workspace Slug Members 201 Response
  slug: orbit-post-workspace-slug-members-201-response
- key_count: 2
  name: Orbit Post Workspace Slug Members Member Slug Activities 201 Response
  slug: orbit-post-workspace-slug-members-member-slug-activities-201-response
- key_count: 1
  name: Orbit Post Workspace Slug Members Member Slug Identities 201 Response
  slug: orbit-post-workspace-slug-members-member-slug-identities-201-response
- key_count: 1
  name: Orbit Post Workspace Slug Members Member Slug Notes 201 Response
  slug: orbit-post-workspace-slug-members-member-slug-notes-201-response
finops:
- name: Orbit Finops
  service_category: ''
  slug: orbit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orbit.png
json_schemas:
- name: Activity And Identity
  property_count: 2
  slug: orbit-activity-and-identity
- name: Custom Activity
  property_count: 0
  slug: orbit-activity-with-member
- name: Custom Activity
  property_count: 10
  slug: orbit-activity
- name: Alert
  property_count: 4
  slug: orbit-alert
- name: Custom Or Post Activity
  property_count: 0
  slug: orbit-custom-or-post-activity
- name: Destination
  property_count: 3
  slug: orbit-destination
- name: Identity
  property_count: 7
  slug: orbit-identity
- name: Member And Identity
  property_count: 2
  slug: orbit-member-and-identity
- name: Member
  property_count: 20
  slug: orbit-member
- name: Note
  property_count: 1
  slug: orbit-note
- name: Organization
  property_count: 8
  slug: orbit-organization
- name: Content Activity
  property_count: 0
  slug: orbit-post-activity-with-member
- name: Content Activity
  property_count: 3
  slug: orbit-post-activity
- name: Webhook Subscription
  property_count: 7
  slug: orbit-webhook-subscription
jsonld:
- class_count: 12
  name: Orbit Context
  property_count: 40
  slug: orbit-context
layout: provider
modified: '2026-06-13'
name: Orbit
nav: Providers
network: true
overview: 'Orbit publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Activity Types API, Members API, and 6 more. Tagged areas include Developer Relations, Community Intelligence, DevRel, Community Management, and Member Tracking.


  The Orbit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Orbit''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Orbit Plans Pricing
  plan_count: 3
  slug: orbit-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 1
  name: Orbit Rate Limits
  slug: orbit-rate-limits
rules:
- name: Orbit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: orbit-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Orbit Authentication
  slug: orbit-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Orbit Domain Security
  slug: orbit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: orbit
tags:
- Developer Relations
- Community Intelligence
- DevRel
- Community Management
- Member Tracking
- Community Analytics
- Open Source
- Developer Engagement
website: https://orbit.love/
---
