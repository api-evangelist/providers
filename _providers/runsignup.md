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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Runsignup Agentic Access
  operation_count: 21
  slug: runsignup-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 1
apis:
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Manage participant corrals for wave start events.
  name: RunSignup Corrals API
  slug: runsignup-corrals-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Manage age group and category divisions for accurate results processing.
  name: RunSignup Divisions API
  slug: runsignup-divisions-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Retrieve donation and fundraising data associated with race registrations.
  name: RunSignup Donations API
  slug: runsignup-donations-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Manage race participants including registration, editing, deletion, bib/chip assignment, and participant data retrieval.
  name: RunSignup Participants API
  slug: runsignup-participants-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: List, search, and retrieve race and event information including details, events, schedules, and registration settings.
  name: RunSignup Races API
  slug: runsignup-races-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Reference data such as countries and states used across the API.
  name: RunSignup Reference API
  slug: runsignup-reference-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Submit, import, and retrieve race results including finishing times, result sets, and full results with place and time data.
  name: RunSignup Results API
  slug: runsignup-results-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Manage teams and groups for team-based race events.
  name: RunSignup Teams API
  slug: runsignup-teams-api
- baseURL: https://runsignup.com/Rest
  baseurl_source: declared
  description: Manage user accounts and authentication for the RunSignup platform.
  name: RunSignup Users API
  slug: runsignup-users-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RunSignup Corrals API
  slug: open-runsignup-corrals-api
- collection_type: open
  name: RunSignup Corrals Divisions API
  slug: open-runsignup-divisions-api
- collection_type: open
  name: RunSignup Corrals Donations API
  slug: open-runsignup-donations-api
- collection_type: open
  name: RunSignup Corrals Participants API
  slug: open-runsignup-participants-api
- collection_type: open
  name: RunSignup Corrals Races API
  slug: open-runsignup-races-api
- collection_type: open
  name: RunSignup Corrals Reference API
  slug: open-runsignup-reference-api
- collection_type: open
  name: RunSignup Corrals Results API
  slug: open-runsignup-results-api
- collection_type: open
  name: RunSignup Corrals Teams API
  slug: open-runsignup-teams-api
- collection_type: open
  name: RunSignup Corrals Users API
  slug: open-runsignup-users-api
- collection_type: open
  name: RunSignup API
  slug: open-runsignup
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/RunSignUp-Team/OpenSource/issues
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


  RunSignup''s developer surface includes authentication, documentation, engineering blog, support, pricing, and 8 more developer resources.'
plans:
- name: Runsignup Plans Pricing
  plan_count: 3
  slug: runsignup-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Runsignup Rate Limits
  slug: runsignup-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RunSignup API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: runsignup-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: RunSignup API Rules
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
  composite: 39.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.5
    catalog_earned_first_party: 0.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 63.2
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
