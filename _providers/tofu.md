---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://enrich.tofuhq.com
  - https://www.npmjs.com/package/@tofuhq/enrich
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Credit-metered company and people data enrichment. Two entities — company (keyed on domain or LinkedIn URL) and person (keyed on LinkedIn profile URL or business email) — with a structured filter gram
  name: Tofu Enrich API
  slug: tofu-enrich-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://tofuhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tofuhq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://enrich.tofuhq.com
- group: company
  title: ''
  type: Blog
  url: https://tofuhq.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tofuhq.com
- group: start
  title: ''
  type: Login
  url: https://login.tofuhq.com
- group: start
  title: ''
  type: SignUp
  url: https://tofuhq.com/lp/request-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tofuhq.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tofuhq.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://tofuhq.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TofuHQ
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tofu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tofu-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tofu-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tofu-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tofu-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/tofu-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/tofu-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tofu-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tofu-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tofu-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tofu-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tofu-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tofu-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tofu-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tofu-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tofu-changelog.yml
created: '2026-07-17'
description: 'Tofu (tofuhq.com) is an agentic go-to-market platform for B2B revenue teams, running always-on marketing and sales campaigns across email, LinkedIn and landing pages inside a team''s existing GTM stack. Three agents — Research, Create and Launch — scale 1:1 ABM to hundreds of accounts, covering outbound prospecting, lead nurture, event follow-up, sales acceleration, stalled-deal re-engagement and customer expansion, and integrating with Salesforce, HubSpot, Marketo, Outreach and Salesloft. Tofu also ships a public, self-serve developer product: the Enrich API (api.enrich.tofuhq.com), a credit-metered company and people data API covering firmographics, funding, headcount, hiring, web traffic, competitors and verified business emails. It is deliberately agent-first — the documented interface is a first-party CLI (@tofuhq/enrich) driven by a published Agent Skill rather than an SDK, and its two schema endpoints answer unauthenticated. Backed by Index Ventures; Tofu states it is
  SOC 2 certified.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tofu.png
layout: provider
modified: '2026-08-13'
name: Tofu
nav: Providers
network: true
overview: 'Tofu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Marketing, Go-To-Market, and Sales.


  Tofu''s developer surface includes documentation, engineering blog, signup flow, CLI, authentication, changelog, and 22 more developer resources.'
plans:
- name: Tofu Plans Pricing
  plan_count: 3
  slug: tofu-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Tofu Rate Limits
  slug: tofu-rate-limits
scopes:
- name: Tofu Scopes
  scope_count: 4
  slug: tofu-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 38.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tofu/refs/heads/main/screenshots/tofu-2026-09-02T163839.png
security:
- kind: authentication
  name: Tofu Authentication
  slug: tofu-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Tofu Domain Security
  slug: tofu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tofu
tags:
- Company
- Ai Ml
- Marketing
- Go-To-Market
- Sales
- Automation
- CRM
- Campaigns
- Data Enrichment
- Company Data
- People Data
- Lead Generation
- Agents
- Contact Data
website: https://tofuhq.com
---
