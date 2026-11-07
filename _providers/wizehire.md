---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Wizehire Agentic Access
  operation_count: 5
  slug: wizehire-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 2
apis:
- baseURL: https://scout.wizehire.com
  baseurl_source: declared
  description: The agent API from WizeHire — 1 operation(s) for agent.
  name: WizeHire Agent API
  slug: wizehire-agent-api
- baseURL: https://scout.wizehire.com
  baseurl_source: declared
  description: The candidates API from WizeHire — 2 operation(s) for candidates.
  name: WizeHire Candidates API
  slug: wizehire-candidates-api
- baseURL: https://scout.wizehire.com
  baseurl_source: declared
  description: The health API from WizeHire — 1 operation(s) for health.
  name: WizeHire Health API
  slug: wizehire-health-api
- baseURL: https://scout.wizehire.com
  baseurl_source: declared
  description: The interviews API from WizeHire — 1 operation(s) for interviews.
  name: WizeHire Interviews API
  slug: wizehire-interviews-api
artifact_total: 17
asyncapis:
- description: ''
  name: Wizehire Events
  slug: wizehire-events
common:
- group: other
  href: https://artifacts.apis.io/wizehire/capabilities/wizehire-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wizehire-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/wizehire/agentic-access/wizehire-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wizehire-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wizehire/security/wizehire-domain-security.yml
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
  href: https://artifacts.apis.io/wizehire/llms/wizehire-llms.txt
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
  href: https://artifacts.apis.io/wizehire/openapi/_original/wizehire-scout-service-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/wizehire-scout-service-openapi.yml
- group: other
  href: https://artifacts.apis.io/wizehire/overlays/wizehire-scout-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wizehire-scout-service-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/wizehire/authentication/wizehire-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wizehire-authentication.yml
- group: design
  href: https://artifacts.apis.io/wizehire/conventions/wizehire-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wizehire-conventions.yml
- group: design
  href: https://artifacts.apis.io/wizehire/errors/wizehire-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wizehire-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wizehire/data-model/wizehire-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wizehire-data-model.yml
- group: design
  href: https://artifacts.apis.io/wizehire/lifecycle/wizehire-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wizehire-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wizehire/conformance/wizehire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wizehire-conformance.yml
- group: build
  href: https://artifacts.apis.io/wizehire/packages/wizehire-packages.yml
  title: ''
  type: Packages
  url: packages/wizehire-packages.yml
- group: commercial
  href: https://artifacts.apis.io/wizehire/plans/wizehire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wizehire-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/wizehire/rate-limits/wizehire-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wizehire-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/wizehire/mcp/wizehire-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wizehire-mcp.yml
- group: agent
  href: https://artifacts.apis.io/wizehire/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-04'
description: Wizehire is a Houston, Texas hiring platform for small and mid-size businesses that combines an applicant tracking system with AI candidate matching (Talent Match), an AI recruiting assistant delivered as a Chrome extension (Scout), DISC+ personality and skills assessments, candidate texting, interview scheduling, expert human hiring coaches, and employee onboarding. Job posts syndicate to 100+ boards including Indeed, LinkedIn and ZipRecruiter, and the platform connects to HRIS, payroll, background-check and e-signature systems — ADP Workforce Now, RUN Powered by ADP, Ceridian Dayforce, Gusto, Paychex, Paycor, Paylocity, UKG, QuickBooks, Checkr and Dropbox Sign — plus Zapier and real-estate CRMs via a customer-issued API key. Wizehire serves real estate, insurance, dental, legal, automotive and hospitality operators, and publishes an NYC Local Law 144 AEDT bias audit for its automated employment decision tooling.
finops:
- has_sources: true
  method: derived
  name: Wizehire Finops
  primary_unit: additional job
  service_category: ''
  slug: wizehire-finops
  template: false
image: https://wizehire.com/wp-content/uploads/2026/08/homepage-preview.png
layout: provider
mcp_servers:
- description: MCP server; 4 tools listed. A candidate, not confirmed as published by the provider.
  name: WizeHire MCP Server
  slug: wizehire-scout
modified: '2026-09-16'
name: WizeHire
nav: Providers
network: true
overview: 'WizeHire publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Candidates API, Health API, and 1 more. Tagged areas include Hiring, Recruiting, Applicant Tracking, Human Resources, and Talent Assessment.


  The WizeHire catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  WizeHire''s developer surface includes documentation, support, engineering blog, pricing, signup flow, API reference, getting-started guide, and 25 more developer resources.'
plans:
- name: Wizehire Plans Pricing
  plan_count: 6
  slug: wizehire-plans-pricing
- name: Wizehire Price Estimates
  plan_count: 0
  slug: wizehire-price-estimates
random_paper: 7
rate_limits:
- limit_count: 0
  name: Wizehire Rate Limits
  slug: wizehire-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: WizeHire API Rules
  rule_count: 48
  severity_counts:
    error: 42
    hint: 0
    info: 5
    warn: 1
  slug: wizehire-rules
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 50.0
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wizehire/wizehire-2026-10-11T194741.png
security:
- kind: authentication
  name: Wizehire Authentication
  slug: wizehire-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wizehire Domain Security
  slug: wizehire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Review top candidates for a Wizehire job
  slug: wizehire-review-top-candidates
- name: Schedule a Wizehire interview
  slug: wizehire-schedule-interview
- name: Drive a Wizehire Scout agent conversation
  slug: wizehire-scout-agent-turn
slug: wizehire
tags:
- Hiring
- Recruiting
- Applicant Tracking
- Human Resources
- Talent Assessment
- Small Business
- Artificial Intelligence
- Job Board
- Onboarding
website: https://wizehire.com/
---
