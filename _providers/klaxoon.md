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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Klaxoon Agentic Access
  operation_count: 6
  slug: klaxoon-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: The Klaxoon API allows developers to integrate Klaxoon's collaborative features into their applications, enabling automation of board creation, activity management, and participant engagement. It incl
  name: Klaxoon API
  slug: klaxoon-api
- description: Adventure activity resources
  name: Klaxoon Adventures API
  slug: klaxoon-adventures-api
- description: Mission activity resources
  name: Klaxoon Missions API
  slug: klaxoon-missions-api
- description: Quiz activity resources and participant results
  name: Klaxoon Quizzes API
  slug: klaxoon-quizzes-api
- description: Survey activity resources and participant results
  name: Klaxoon Surveys API
  slug: klaxoon-surveys-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Klaxoon Adventures API
  slug: open-klaxoon-adventures-api
- collection_type: open
  name: Klaxoon Adventures Missions API
  slug: open-klaxoon-missions-api
- collection_type: open
  name: Klaxoon Adventures Quizzes API
  slug: open-klaxoon-quizzes-api
- collection_type: open
  name: Klaxoon Adventures Surveys API
  slug: open-klaxoon-surveys-api
- collection_type: open
  name: Klaxoon API
  slug: open-klaxoon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/klaxoon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klaxoon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klaxoon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/klaxoon-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klaxoon
- group: company
  title: ''
  type: Website
  url: https://www.klaxoon.com
- group: start
  title: ''
  type: Portal
  url: https://developers.klaxoon.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.klaxoon.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developers.klaxoon.com/docs/authentication
- group: docs
  title: ''
  type: Reference
  url: https://developers.klaxoon.com/klaxoon/reference
- group: company
  title: ''
  type: Blog
  url: https://www.klaxoon.com/blog
- group: start
  title: ''
  type: Signup
  url: https://app.klaxoon.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.klaxoon.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klaxoon.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klaxoon.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.klaxoon.com
- group: operate
  title: ''
  type: Support
  url: https://support.klaxoon.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/klaxoon
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.klaxoon.com/llms.txt
created: '2024-01-01'
description: Klaxoon is a collaborative platform that provides tools for team collaboration, brainstorming, meetings, and workshops. The platform includes features like boards, quizzes, surveys, and other interactive activities to enhance team productivity and engagement. Klaxoon publishes a developer portal with documentation for board integration, embedding, and enterprise audit and SCIM endpoints, but does not currently publish a public OpenAPI specification.
finops:
- name: Klaxoon Finops
  service_category: API
  slug: klaxoon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klaxoon.png
layout: provider
modified: '2026-04-28'
name: Klaxoon
nav: Providers
network: true
overview: 'Klaxoon publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Adventures API, Missions API, Quizzes API, and 1 more. Tagged areas include Collaboration, Meetings, Productivity, Team Collaboration, and Workshops.


  Klaxoon''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, support, and 12 more developer resources.'
plans:
- name: Klaxoon Plans Pricing
  plan_count: 3
  slug: klaxoon-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Klaxoon Rate Limits
  slug: klaxoon-rate-limits
scopes:
- name: Klaxoon Scopes
  scope_count: 10
  slug: klaxoon-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klaxoon/refs/heads/main/screenshots/klaxoon-2026-06-20T184103.png
security:
- kind: authentication
  name: Klaxoon Authentication
  slug: klaxoon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Klaxoon Domain Security
  slug: klaxoon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klaxoon
tags:
- Collaboration
- Meetings
- Productivity
- Team Collaboration
- Workshops
- Brainstorming
- Whiteboard
website: https://www.klaxoon.com
---
