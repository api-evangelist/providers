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
- acting_count: 13
  human_in_the_loop: 0
  name: Greenhouse Agentic Access
  operation_count: 40
  slug: greenhouse-agentic-access
  summary_line: 40 operations · 13 acting
api_count: 16
apis:
- description: The Assessment Partner API enables assessment platforms (code testing, video interviewing, personality testing) to seamlessly integrate with the Greenhouse interview workflow.
  name: Greenhouse Assessment API
  slug: assessment
- description: The Audit Log API offers a record of important events, providing insight into who accessed or edited information in Greenhouse.
  name: Greenhouse Audit Log API
  slug: audit-log
- description: Recruiting Webhooks deliver event notifications for Greenhouse Recruiting activities such as candidate updates, application stage changes, and offers.
  name: Greenhouse Recruiting Webhooks
  slug: recruiting-webhooks
- description: Onboarding Webhooks deliver event notifications for Greenhouse Onboarding activities such as new hires and employee updates.
  name: Greenhouse Onboarding Webhooks
  slug: onboarding-webhooks
- description: The Applications API from Greenhouse — 5 operation(s) for applications.
  name: Greenhouse Applications API
  slug: greenhouse-applications-api
- description: The Candidates API from Greenhouse — 2 operation(s) for candidates.
  name: Greenhouse Candidates API
  slug: greenhouse-candidates-api
- description: The Departments API from Greenhouse — 2 operation(s) for departments.
  name: Greenhouse Departments API
  slug: greenhouse-departments-api
- description: The Education API from Greenhouse — 3 operation(s) for education.
  name: Greenhouse Education API
  slug: greenhouse-education-api
- description: The Graphql API from Greenhouse — 1 operation(s) for graphql.
  name: Greenhouse Graphql API
  slug: greenhouse-graphql-api
- description: The Greenhouse Job Board API API from Greenhouse — 1 operation(s) for greenhouse job board api.
  name: Greenhouse Greenhouse Job Board API API
  slug: greenhouse-greenhouse-job-board-api-api
- description: The Jobs API from Greenhouse — 3 operation(s) for jobs.
  name: Greenhouse Jobs API
  slug: greenhouse-jobs-api
- description: The Offices API from Greenhouse — 3 operation(s) for offices.
  name: Greenhouse Offices API
  slug: greenhouse-offices-api
- description: The Prospects API from Greenhouse — 1 operation(s) for prospects.
  name: Greenhouse Prospects API
  slug: greenhouse-prospects-api
- description: The Sections API from Greenhouse — 2 operation(s) for sections.
  name: Greenhouse Sections API
  slug: greenhouse-sections-api
- description: The Tracking API from Greenhouse — 1 operation(s) for tracking.
  name: Greenhouse Tracking API
  slug: greenhouse-tracking-api
- description: The Users API from Greenhouse — 3 operation(s) for users.
  name: Greenhouse Users API
  slug: greenhouse-users-api
artifact_total: 31
collections:
- collection_type: open
  name: Greenhouse Harvest API
  slug: open-greenhouse-harvest
- collection_type: open
  name: Greenhouse Candidate Ingestion API
  slug: open-greenhouse-ingestion
- collection_type: open
  name: Greenhouse Job Board API
  slug: open-greenhouse-job-board
- collection_type: open
  name: Greenhouse Onboarding API
  slug: open-greenhouse-onboarding
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/greenhouse-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/greenhouse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greenhouse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/greenhouse-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/greenhouse-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greenhouse-inc-
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/grnhse
created: '2025-01-07'
description: Greenhouse is an applicant tracking system (ATS) and recruiting software platform. It exposes a family of APIs and webhooks that let partners and customers manage candidates, jobs, applications, onboarding, audit logs, and assessment integrations.
finops:
- name: Greenhouse Finops
  service_category: Recruiting / ATS SaaS
  slug: greenhouse-finops
graphqls:
- description: A GraphQL API for Greenhouse Onboarding. Provides queries and mutations for employees, departments, locations, custom fields, teams, and pending hires.
  name: Greenhouse GraphQL API
  slug: greenhouse-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greenhouse.png
json_structures:
- name: Greenhouse Structure
  property_count: 0
  slug: greenhouse-structure
layout: provider
modified: '2026-05-19'
name: Greenhouse
nav: Providers
network: true
overview: 'Greenhouse publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Candidates API, Departments API, and 9 more. Tagged areas include ATS, Recruiting, Candidates, Jobs, and Onboarding.


  The Greenhouse catalog on APIs.io includes 1 Spectral governance ruleset.


  Greenhouse''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Greenhouse Plans Pricing
  plan_count: 3
  slug: greenhouse-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 4
  name: Greenhouse Rate Limits
  slug: greenhouse-rate-limits
rules:
- name: Greenhouse API Rules
  rule_count: 17
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 11
  slug: greenhouse-spectral-rules
scopes:
- name: Greenhouse Scopes
  scope_count: 6
  slug: greenhouse-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 38.7
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.6
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 27.1
    operational_transparency: 36.8
  previous_composite: 41.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/screenshots/greenhouse-2026-06-20T182356.png
security:
- kind: authentication
  name: Greenhouse Authentication
  slug: greenhouse-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Greenhouse Domain Security
  slug: greenhouse-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Greenhouse Vulnerability Disclosure
  slug: greenhouse-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: greenhouse
tags:
- ATS
- Recruiting
- Candidates
- Jobs
- Onboarding
- HR
---
