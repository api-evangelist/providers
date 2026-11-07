---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The AngelList Investor Management API is a GraphQL API that enables programmatic access to the AngelList investor portal, supporting fund managers and investors in managing transactions, documents, an
  name: AngelList Investor Management API
  slug: investor-management-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/angellist/finops/angellist-finops.yml
  title: ''
  type: FinOps
  url: finops/angellist-finops.yml
- group: auth
  href: https://artifacts.apis.io/angellist/security/angellist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angellist-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/angellist
- group: company
  title: ''
  type: Website
  url: https://www.angellist.com/
- group: company
  title: ''
  type: Website
  url: https://wellfound.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.angellist.com/docs/overview
- group: docs
  title: ''
  type: GraphQL
  url: https://docs.angellist.com/graphql
- group: design
  title: ''
  type: DataModel
  url: https://docs.angellist.com/docs/angellist-data-model
- group: docs
  title: ''
  type: Documentation
  url: https://support.angellist.com/data-room/integrations/API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/angellist
- group: commercial
  title: ''
  type: TermsOfService
  url: https://venture.angellist.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://venture.angellist.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust-portal.angellist.com/
- group: auth
  href: https://artifacts.apis.io/angellist/security/angellist-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/angellist-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust-portal.angellist.com/
- group: company
  title: ''
  type: Blog
  url: https://www.angellist.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.angellist.com/
- group: other
  title: ''
  type: X
  url: https://x.com/angellistapi
- group: start
  title: ''
  type: Portal
  url: https://www.angellist.com/private-markets/investor-portal
- group: other
  title: ''
  type: Announcement
  url: https://wellfound.com/blog/angellist-talent-is-now-wellfound
- group: agent
  href: https://artifacts.apis.io/angellist/llms/angellist-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/angellist-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://support.angellist.com/llms.txt
- group: other
  href: https://artifacts.apis.io/angellist/a2a/angellist-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/angellist-a2a.yml
- group: agent
  href: https://artifacts.apis.io/angellist/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/angellist/skills/angellist-investor-management-platform.md
  title: ''
  type: AgentSkill
  url: skills/angellist-investor-management-platform.md
- group: agent
  href: https://artifacts.apis.io/angellist/well-known/angellist-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/angellist-well-known.yml
- group: auth
  href: https://artifacts.apis.io/angellist/authentication/angellist-authentication.yml
  title: ''
  type: Authentication
  url: authentication/angellist-authentication.yml
- group: auth
  href: https://artifacts.apis.io/angellist/scopes/angellist-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/angellist-scopes.yml
- group: design
  href: https://artifacts.apis.io/angellist/conventions/angellist-conventions.yml
  title: ''
  type: Conventions
  url: conventions/angellist-conventions.yml
- group: design
  href: https://artifacts.apis.io/angellist/errors/angellist-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/angellist-error-codes.yml
- group: design
  href: https://artifacts.apis.io/angellist/lifecycle/angellist-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/angellist-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/angellist/conformance/angellist-conformance.yml
  title: ''
  type: Conformance
  url: conformance/angellist-conformance.yml
- group: start
  href: https://artifacts.apis.io/angellist/sandbox/angellist-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/angellist-sandbox.yml
- group: build
  href: https://artifacts.apis.io/angellist/packages/angellist-packages.yml
  title: ''
  type: Packages
  url: packages/angellist-packages.yml
- group: commercial
  href: https://artifacts.apis.io/angellist/plans/angellist-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/angellist-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/angellist/rate-limits/angellist-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/angellist-rate-limits.yml
- group: docs
  href: https://artifacts.apis.io/angellist/graphql/angellist-graphql-probe.yml
  title: ''
  type: GraphQL
  url: graphql/angellist-graphql-probe.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.angellist.com/pricing
- group: start
  title: ''
  type: Login
  url: https://venture.angellist.com/v/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.angellist.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.angellist.com/graphql
- group: start
  title: ''
  type: GettingStarted
  url: https://support.angellist.com/investor-help/new/new-investor
- group: company
  title: ''
  type: Careers
  url: https://www.angellist.com/careers
created: '2026-03-24'
description: AngelList provides an investor management GraphQL API that enables fund managers and investors to programmatically manage transactions, entities, organizations, documents, and capital flows via the AngelList investor portal. The platform supports venture capital workflows including transaction lifecycle management, document signing, data rooms, and investor onboarding.
finops:
- has_sources: true
  method: derived
  name: Angellist Finops
  primary_unit: fund
  service_category: ''
  slug: angellist-finops
  template: false
graphqls:
- description: The AngelList Investor Management API is a GraphQL API that enables programmatic access to the AngelList investor portal, supporting fund managers and investors in managing transactions, documents, an
  name: AngelList GraphQL API
  slug: angellist-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/angellist.png
layout: provider
modified: '2026-09-02'
name: AngelList
nav: Providers
network: true
overview: 'AngelList is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Documents, Fund, Investing, Job, and Startups.


  AngelList''s developer surface includes documentation, engineering blog, support, developer portal, authentication, sandbox, pricing, and 36 more developer resources.'
plans:
- name: Angellist Plans Pricing
  plan_count: 2
  slug: angellist-plans-pricing
- name: Angellist Price Estimates
  plan_count: 0
  slug: angellist-price-estimates
random_paper: 3
rate_limits:
- limit_count: 0
  name: Angellist Rate Limits
  slug: angellist-rate-limits
scopes:
- name: Angellist Scopes
  scope_count: 4
  slug: angellist-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 15.8
  previous_composite: 47.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/angellist/angellist-2026-06-20T171953.png
security:
- kind: authentication
  name: Angellist Authentication
  slug: angellist-authentication
  summary_line: apiKey/openIdConnect/oauth2 · 3 schemes
- kind: domain-security
  name: Angellist Domain Security
  slug: angellist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Angellist Vulnerability Disclosure
  slug: angellist-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Angellist Trust Center
  slug: angellist-trust-center
  summary_line: SOC 2 Type II
skill_count: 1
skills:
- name: Angellist
  slug: angellist-investor-management-platform
slug: angellist
tags:
- Documents
- Fund
- Investing
- Job
- Startups
- Transaction
- Venture Capital
- A2A
website: https://www.angellist.com/
---
