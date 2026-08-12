---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Runsignup Agentic Access
  operation_count: 21
  slug: runsignup-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 9
apis:
- description: Manage participant corrals for wave start events.
  name: RunSignup Corrals API
  slug: runsignup-corrals-api
- description: Manage age group and category divisions for accurate results processing.
  name: RunSignup Divisions API
  slug: runsignup-divisions-api
- description: Retrieve donation and fundraising data associated with race registrations.
  name: RunSignup Donations API
  slug: runsignup-donations-api
- description: Manage race participants including registration, editing, deletion, bib/chip assignment, and participant data retrieval.
  name: RunSignup Participants API
  slug: runsignup-participants-api
- description: List, search, and retrieve race and event information including details, events, schedules, and registration settings.
  name: RunSignup Races API
  slug: runsignup-races-api
- description: Reference data such as countries and states used across the API.
  name: RunSignup Reference API
  slug: runsignup-reference-api
- description: Submit, import, and retrieve race results including finishing times, result sets, and full results with place and time data.
  name: RunSignup Results API
  slug: runsignup-results-api
- description: Manage teams and groups for team-based race events.
  name: RunSignup Teams API
  slug: runsignup-teams-api
- description: Manage user accounts and authentication for the RunSignup platform.
  name: RunSignup Users API
  slug: runsignup-users-api
artifact_total: 24
collections:
- collection_type: open
  name: RunSignup API
  slug: open-runsignup
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runsignup-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runsignup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runsignup-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/runsignup-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/runsignup-com
- group: company
  title: ''
  type: Website
  url: https://runsignup.com
- group: docs
  title: ''
  type: Documentation
  url: https://runsignup.com/API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RunSignUp-Team
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/RunSignUp-Team/OpenSource
- group: company
  title: ''
  type: Blog
  url: https://runsignup.blog
- group: operate
  title: ''
  type: Support
  url: https://runsignup.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://runsignup.com/pricing
created: '2025-02-06'
description: RunSignup is an all-in-one race registration and event management platform serving running events, triathlons, cycling events, and obstacle courses. Their open REST API enables race directors, timing companies, affiliates, and technology partners to integrate race registration, participant management, results posting, fundraising, volunteer management, and event analytics into their own applications. The API supports OAuth 2.0 authentication and covers 100+ endpoints across 29 categories for comprehensive event lifecycle management.
examples:
- key_count: 2
  name: Runsignup Get Races Example
  slug: runsignup-get-races-example
- key_count: 2
  name: Runsignup Post Results Example
  slug: runsignup-post-results-example
finops:
- name: Runsignup Finops
  service_category: API
  slug: runsignup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runsignup.png
json_schemas:
- name: RunSignup Race
  property_count: 19
  slug: runsignup-race
json_structures:
- name: Runsignup Race Structure
  property_count: 0
  slug: runsignup-race-structure
jsonld:
- class_count: 0
  name: Runsignup Context
  property_count: 7
  slug: runsignup-context
layout: provider
modified: '2026-05-19'
name: RunSignup
nav: Providers
network: true
overview: 'RunSignup publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Corrals API, Divisions API, Donations API, and 6 more. Tagged areas include Race Registration, Event Management, Running, Sports, and Fitness.


  The RunSignup catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RunSignup''s developer surface includes authentication, documentation, engineering blog, support, pricing, and 7 more developer resources.'
plans:
- name: Runsignup Plans Pricing
  plan_count: 3
  slug: runsignup-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Runsignup Rate Limits
  slug: runsignup-rate-limits
rules:
- name: RunSignup API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: runsignup-jsonschema-spectral-rules
- name: RunSignup API Rules
  rule_count: 16
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 7
  slug: runsignup-rules
scopes:
- name: Runsignup Scopes
  scope_count: 2
  slug: runsignup-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 43.7
  delta: -8.5
  facets:
    commercial_clarity: 26.3
    contract_quality: 68.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/runsignup/refs/heads/main/screenshots/runsignup-2026-06-20T193255.png
security:
- kind: authentication
  name: Runsignup Authentication
  slug: runsignup-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Runsignup Domain Security
  slug: runsignup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: runsignup
tags:
- Race Registration
- Event Management
- Running
- Sports
- Fitness
- Timing
- Fundraising
website: https://runsignup.com
---
