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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Sana Labs Agentic Access
  operation_count: 56
  slug: sana-labs-agentic-access
  summary_line: 56 operations · 36 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The Assignments API from Sana — 1 operation(s) for assignments.
  name: Sana Assignments API
  slug: sana-labs-assignments-api
- description: The Authentication API from Sana — 1 operation(s) for authentication.
  name: Sana Authentication API
  slug: sana-labs-authentication-api
- description: The Courses API from Sana — 6 operation(s) for courses.
  name: Sana Courses API
  slug: sana-labs-courses-api
- description: The Groups API from Sana — 4 operation(s) for groups.
  name: Sana Groups API
  slug: sana-labs-groups-api
- description: The Insights API from Sana — 2 operation(s) for insights.
  name: Sana Insights API
  slug: sana-labs-insights-api
- description: The Paths API from Sana — 2 operation(s) for paths.
  name: Sana Paths API
  slug: sana-labs-paths-api
- description: The Programs API from Sana — 3 operation(s) for programs.
  name: Sana Programs API
  slug: sana-labs-programs-api
- description: The Reporting API from Sana — 3 operation(s) for reporting.
  name: Sana Reporting API
  slug: sana-labs-reporting-api
- description: The Teamspaces API from Sana — 3 operation(s) for teamspaces.
  name: Sana Teamspaces API
  slug: sana-labs-teamspaces-api
- description: The Users API from Sana — 7 operation(s) for users.
  name: Sana Users API
  slug: sana-labs-users-api
- description: The xAPI API from Sana — 2 operation(s) for xapi.
  name: Sana xAPI API
  slug: sana-labs-xapi-api
artifact_total: 18
collections:
- collection_type: open
  name: Sana API
  slug: open-sana-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sana-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sana-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sana-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sanalabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sana-labs
- group: company
  title: ''
  type: Website
  url: https://www.sana.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sana.ai/api-docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/sana-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sana-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sana-labs-finops.yml
created: '2026-06-21'
description: Sana is an AI-native knowledge and learning company (Stockholm, Sweden; now part of Workday) behind Sana AI / Sana Agents and the Sana Learn platform. It builds expert AI agents and assistants grounded in a company's knowledge, plus an AI-first LMS/LXP. Sana exposes a tenant-scoped REST API (OAuth 2.0 client credentials) for user, group, program, course, content, and reporting management, along with xAPI and SCIM integration surfaces.
finops:
- name: Sana Labs Finops
  service_category: AI and Machine Learning
  slug: sana-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sana-labs.png
layout: provider
modified: '2026-06-21'
name: Sana
nav: Providers
network: true
overview: 'Sana publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Authentication API, Courses API, and 8 more. Tagged areas include AI, Knowledge, Learning, LMS, and Agents.


  Sana''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Sana Labs Plans Pricing
  plan_count: 3
  slug: sana-labs-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 2
  name: Sana Labs Rate Limits
  slug: sana-labs-rate-limits
score:
  band: thin
  composite: 34.7
  delta: -3.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sana Labs Authentication
  slug: sana-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sana Labs Domain Security
  slug: sana-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sana-labs
tags:
- AI
- Knowledge
- Learning
- LMS
- Agents
website: https://www.sana.ai
---
