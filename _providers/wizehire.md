---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Wizehire Agentic Access
  operation_count: 5
  slug: wizehire-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://scout.wizehire.com
  baseurl_source: declared
  description: 'Backend service for the Wizehire Scout Chrome extension — the AI recruiting assistant. Five operations over HTTP Bearer auth: a streaming (Server-Sent Events) agent chat endpoint that runs a LangGraph'
  name: Wizehire Scout Service API
  slug: wizehire-scout-service-api
artifact_total: 8
asyncapis:
- description: ''
  name: Wizehire Events
  slug: wizehire-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wizehire-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wizehire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wizehire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.wizehire.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.wizehire.com/en/
- group: company
  title: ''
  type: Blog
  url: https://wizehire.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://wizehire.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://wizehire.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://wizehire.com/signup
- group: start
  title: ''
  type: Login
  url: https://wizehire.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wizehire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wizehire.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WizeHire
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wizehire-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.wizehire.com/en/collections/2120794-integrations-tools
- group: docs
  title: ''
  type: APIReference
  url: https://scout.wizehire.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://wizehire.com/how-it-works
- group: auth
  title: ''
  type: Compliance
  url: https://wizehire.com/gdpr
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/wizehire-scout-service-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wizehire-scout-service-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wizehire-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wizehire-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wizehire-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wizehire-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wizehire-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wizehire-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/wizehire-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wizehire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wizehire-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wizehire-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-04'
description: Wizehire is a Houston, Texas hiring platform for small and mid-size businesses that combines an applicant tracking system with AI candidate matching (Talent Match), an AI recruiting assistant delivered as a Chrome extension (Scout), DISC+ personality and skills assessments, candidate texting, interview scheduling, expert human hiring coaches, and employee onboarding. Job posts syndicate to 100+ boards including Indeed, LinkedIn and ZipRecruiter, and the platform connects to HRIS, payroll, background-check and e-signature systems — ADP Workforce Now, RUN Powered by ADP, Ceridian Dayforce, Gusto, Paychex, Paycor, Paylocity, UKG, QuickBooks, Checkr and Dropbox Sign — plus Zapier and real-estate CRMs via a customer-issued API key. Wizehire serves real estate, insurance, dental, legal, automotive and hospitality operators, and publishes an NYC Local Law 144 AEDT bias audit for its automated employment decision tooling.
image: https://wizehire.com/wp-content/uploads/2026/08/homepage-preview.png
layout: provider
mcp_servers:
- description: ''
  name: WizeHire MCP Server
  slug: wizehire-mcp-server
modified: '2026-09-04'
name: WizeHire
nav: Providers
network: true
overview: 'WizeHire publishes 1 API on the [APIs.io](https://apis.io/) network: Scout Service API. Tagged areas include Hiring, Recruiting, Applicant Tracking, Human Resources, and Talent Assessment.


  The WizeHire catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WizeHire''s developer surface includes documentation, support, engineering blog, pricing, signup flow, API reference, getting-started guide, and 24 more developer resources.'
plans:
- name: Wizehire Plans Pricing
  plan_count: 3
  slug: wizehire-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Wizehire Rate Limits
  slug: wizehire-rate-limits
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 63.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Wizehire Authentication
  slug: wizehire-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wizehire Domain Security
  slug: wizehire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wizehire
tags:
- Hiring
- Recruiting
- Applicant Tracking
- Human Resources
- Talent Assessment
- Small Business
- Artificial Intelligence
- Job Boards
- Onboarding
- HR Tech
website: https://wizehire.com/
---
