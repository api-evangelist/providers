---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-10'
api_count: 32
apis:
- description: The admin API from NoBueno — 51 operation(s) for admin.
  name: NoBueno admin API
  slug: nobueno-admin-api
- description: The bitcoin API from NoBueno — 1 operation(s) for bitcoin.
  name: NoBueno bitcoin API
  slug: nobueno-bitcoin-api
- description: The categories API from NoBueno — 2 operation(s) for categories.
  name: NoBueno categories API
  slug: nobueno-categories-api
- description: The cities API from NoBueno — 4 operation(s) for cities.
  name: NoBueno cities API
  slug: nobueno-cities-api
- description: The companies API from NoBueno — 7 operation(s) for companies.
  name: NoBueno companies API
  slug: nobueno-companies-api
- description: The countries API from NoBueno — 2 operation(s) for countries.
  name: NoBueno countries API
  slug: nobueno-countries-api
- description: The credits API from NoBueno — 2 operation(s) for credits.
  name: NoBueno credits API
  slug: nobueno-credits-api
- description: The currencies API from NoBueno — 2 operation(s) for currencies.
  name: NoBueno currencies API
  slug: nobueno-currencies-api
- description: The devices API from NoBueno — 2 operation(s) for devices.
  name: NoBueno devices API
  slug: nobueno-devices-api
- description: The fields API from NoBueno — 1 operation(s) for fields.
  name: NoBueno fields API
  slug: nobueno-fields-api
- description: The forgot API from NoBueno — 3 operation(s) for forgot.
  name: NoBueno forgot API
  slug: nobueno-forgot-api
- description: The jobs API from NoBueno — 18 operation(s) for jobs.
  name: NoBueno jobs API
  slug: nobueno-jobs-api
- description: The languages API from NoBueno — 1 operation(s) for languages.
  name: NoBueno languages API
  slug: nobueno-languages-api
- description: The login API from NoBueno — 1 operation(s) for login.
  name: NoBueno login API
  slug: nobueno-login-api
- description: The matches API from NoBueno — 2 operation(s) for matches.
  name: NoBueno matches API
  slug: nobueno-matches-api
- description: The me API from NoBueno — 2 operation(s) for me.
  name: NoBueno me API
  slug: nobueno-me-api
- description: The messages API from NoBueno — 6 operation(s) for messages.
  name: NoBueno messages API
  slug: nobueno-messages-api
- description: The notifications API from NoBueno — 2 operation(s) for notifications.
  name: NoBueno notifications API
  slug: nobueno-notifications-api
- description: The profile API from NoBueno — 2 operation(s) for profile.
  name: NoBueno profile API
  slug: nobueno-profile-api
- description: The public API from NoBueno — 2 operation(s) for public.
  name: NoBueno public API
  slug: nobueno-public-api
- description: The refresh API from NoBueno — 1 operation(s) for refresh.
  name: NoBueno refresh API
  slug: nobueno-refresh-api
- description: The register API from NoBueno — 1 operation(s) for register.
  name: NoBueno register API
  slug: nobueno-register-api
- description: The review API from NoBueno — 2 operation(s) for review.
  name: NoBueno review API
  slug: nobueno-review-api
- description: The roles API from NoBueno — 2 operation(s) for roles.
  name: NoBueno roles API
  slug: nobueno-roles-api
- description: The skill-categories API from NoBueno — 3 operation(s) for skill-categories.
  name: NoBueno skill-categories API
  slug: nobueno-skill-categories-api
- description: The skills API from NoBueno — 3 operation(s) for skills.
  name: NoBueno skills API
  slug: nobueno-skills-api
- description: The user_block API from NoBueno — 2 operation(s) for user_block.
  name: NoBueno user_block API
  slug: nobueno-user-block-api
- description: The user_report API from NoBueno — 1 operation(s) for user_report.
  name: NoBueno user_report API
  slug: nobueno-user-report-api
- description: The users API from NoBueno — 13 operation(s) for users.
  name: NoBueno users API
  slug: nobueno-users-api
- description: The v2 API from NoBueno — 8 operation(s) for v2.
  name: NoBueno v2 API
  slug: nobueno-v2-api
- description: The webrtc-configs API from NoBueno — 1 operation(s) for webrtc-configs.
  name: NoBueno webrtc-configs API
  slug: nobueno-webrtc-configs-api
- description: The work-experience API from NoBueno — 2 operation(s) for work-experience.
  name: NoBueno work-experience API
  slug: nobueno-work-experience-api
artifact_total: 35
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/nobueno-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nobueno-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nobueno-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nobueno-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nobueno-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nobueno-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nobueno-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/nobueno-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nobueno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nobueno.com
created: '2026-07-17'
description: NoBueno is a job-and-candidate matching platform (a 500 Global portfolio company) built around its Django REST Framework "Jungle API". The API powers job postings, candidate profiles and work experience, hiring-company and employer records, scored job-to-candidate matching, a skills / roles / disciplines taxonomy, recruiter-candidate messaging, and notifications. Authentication is a bearer token obtained via login / register, and list endpoints use page-number pagination with free-text search, ordering, and field-level filtering.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nobueno.png
layout: provider
mcp_servers:
- description: ''
  name: nobueno-mcp.yml
  slug: nobueno-mcpyml
modified: '2026-07-20'
name: NoBueno
nav: Providers
network: true
overview: 'NoBueno publishes 32 APIs on the [APIs.io](https://apis.io/) network, including admin API, bitcoin API, categories API, and 29 more. Tagged areas include Company, Jobs, Recruiting, Hiring, and Talent.


  NoBueno''s developer surface includes authentication and 10 more developer resources.'
random_paper: 62
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 45.7
    developer_ergonomics: 14.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 25.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Nobueno Authentication
  slug: nobueno-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Nobueno Domain Security
  slug: nobueno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nobueno
tags:
- Company
- Jobs
- Recruiting
- Hiring
- Talent
- Matching
- Human Resources
- Candidates
website: https://nobueno.com
---
