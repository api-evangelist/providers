---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST API over Welcome to the Jungle Solutions recruiting and employer-branding data. Bearer-token (OAuth access token) authentication with a published scope model, JSON request and response bodies, pa
  name: Welcome to the Jungle Solutions API
  slug: welcome-to-the-jungle-solutions-api
- description: Undocumented first-party GraphQL API for the Welcome Kit / Welcome ATS platform, live at api.welcomekit.co/api/v1/graphql. Anonymous introspection is enabled and returned the complete schema (95 types
  name: Welcome Kit GraphQL API
  slug: welcome-to-the-jungle-welcomekit-graphql
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/welcome-to-the-jungle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.welcometothejungle.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.welcomekit.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.welcomekit.co/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.welcomekit.co/jobs-api/jobs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.welcomekit.co/master
- group: operate
  title: ''
  type: Support
  url: https://help.welcometothejungle.com/en
- group: company
  title: ''
  type: Blog
  url: https://solutions.welcometothejungle.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WTTJ
- group: commercial
  title: ''
  type: Pricing
  url: https://solutions.welcometothejungle.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://myaccount.welcometothejungle.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solutions.welcometothejungle.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solutions.welcometothejungle.com/en/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.welcomekit.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/welcome-to-the-jungle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/welcome-to-the-jungle-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/welcome-to-the-jungle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/welcome-to-the-jungle-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/welcome-to-the-jungle-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/welcome-to-the-jungle-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/welcome-to-the-jungle-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/welcome-to-the-jungle-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/welcome-to-the-jungle-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/welcome-to-the-jungle-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/welcome-to-the-jungle-packages.yml
- group: design
  title: ''
  type: Components
  url: components/welcome-to-the-jungle-components.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/welcome-to-the-jungle-conformance.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/welcome-to-the-jungle.graphql
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/welcome-to-the-jungle-tool-crosswalk.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/welcome-to-the-jungle-data-model.yml
created: '2026-09-04'
description: Welcome to the Jungle is a Paris-headquartered employer-branding and hiring platform. Its Welcome Hiring Suite bundles Welcome Employer Brand company showcases, Welcome ATS (historically shipped as Welcome Kit), Welcome Job Matching and Welcome Sourcing, alongside the welcometothejungle.com job board and media property. The company publishes the Welcome to the Jungle Solutions API — a token-gated REST API over jobs, departments, offices, candidates, candidate emails, documents, comments, employer-branding organizations, images, videos, analytics moves and WTTJ media articles — documented at developers.welcomekit.co and served from www.welcomekit.co/api/v1/external.
image: https://avatars.githubusercontent.com/u/13100706?v=4
layout: provider
modified: '2026-09-04'
name: Welcome to the Jungle
nav: Providers
network: true
overview: 'Welcome to the Jungle publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Recruiting, Applicant Tracking, and Jobs.


  Welcome to the Jungle''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Welcome To The Jungle Plans Pricing
  plan_count: 0
  slug: welcome-to-the-jungle-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Welcome To The Jungle Rate Limits
  slug: welcome-to-the-jungle-rate-limits
scopes:
- name: Welcome To The Jungle Scopes
  scope_count: 0
  slug: welcome-to-the-jungle-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Welcome To The Jungle Authentication
  slug: welcome-to-the-jungle-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Welcome To The Jungle Domain Security
  slug: welcome-to-the-jungle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: welcome-to-the-jungle
tags:
- Company
- Human Resources
- Recruiting
- Applicant Tracking
- Jobs
- Employer Branding
- Talent Acquisition
- HR Tech
- France
website: https://www.welcometothejungle.com/en
---
