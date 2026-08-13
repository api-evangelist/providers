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
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'The Gamelocker backend (gamelocker.unruly-studios.com) is a self-hosted GitLab instance that stores each learner''s coding "profiles" and game files as GitLab projects and repository files. It exposes '
  name: Unruly Gamelocker API
  slug: unruly-gamelocker-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.unrulysplats.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.unrulysplats.com/portal
- group: start
  title: ''
  type: SignUp
  url: https://www.unrulysplats.com/portal/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unrulysplats.com/memberships
- group: company
  title: ''
  type: Blog
  url: https://www.unrulysplats.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.unrulysplats.com/request-a-call
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unrulysplats.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unrulysplats.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unruly-studios
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unrulysplats.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/unruly-studios-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unruly-studios-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unruly-studios-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unruly-studios-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unruly-studios-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unruly-studios-domain-security.yml
created: '2026-07-17'
description: Unruly Studios makes Unruly Splats, programmable stompable floor buttons that teach children to code through active, physical STEM play. Students use a tablet or computer app to program Splats to light up, make sounds, and score points, building games, dance competitions, and math activities they play together in classrooms and gyms. Founded in 2015 in Boston by Bryanne Leeming and backed by Techstars, the Amazon Alexa Fund, AT&T, eCoast Angels, and LearnLaunch. Unruly's only machine API surface is an internal "Gamelocker" project store, a self-hosted GitLab instance that saves kids' coding projects as GitLab repositories and exposes GitLab's OAuth 2.0 / OpenID Connect and v4 REST API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unruly-studios.png
layout: provider
mcp_servers:
- description: ''
  name: unruly-studios-mcp.yml
  slug: unruly-studios-mcpyml
modified: '2026-07-21'
name: Unruly Studios
nav: Providers
network: true
overview: 'Unruly Studios publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, STEM, EdTech, and Coding.


  Unruly Studios'' developer surface includes signup flow, pricing, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 71
scopes:
- name: Unruly Studios Scopes
  scope_count: 0
  slug: unruly-studios-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.9
  provenance:
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Unruly Studios Authentication
  slug: unruly-studios-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Unruly Studios Domain Security
  slug: unruly-studios-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unruly-studios
tags:
- Company
- Education
- STEM
- EdTech
- Coding
- Kids
- Learning
- Hardware
website: https://www.unrulysplats.com/
---
