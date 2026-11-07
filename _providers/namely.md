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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Comments API from Namely — 3 operation(s) for comments.
  name: Namely Comments API
  slug: namely-comments-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Company Info API from Namely — 1 operation(s) for company info.
  name: Namely Company Info API
  slug: namely-company-info-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Company Resources API from Namely — 5 operation(s) for company resources.
  name: Namely Company Resources API
  slug: namely-company-resources-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Countries API from Namely — 2 operation(s) for countries.
  name: Namely Countries API
  slug: namely-countries-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Events API from Namely — 2 operation(s) for events.
  name: Namely Events API
  slug: namely-events-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Groups API from Namely — 3 operation(s) for groups.
  name: Namely Groups API
  slug: namely-groups-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Groups & Teams API from Namely — 7 operation(s) for groups & teams.
  name: Namely Groups & Teams API
  slug: namely-groups-teams-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Home Feed API from Namely — 10 operation(s) for home feed.
  name: Namely Home Feed API
  slug: namely-home-feed-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Job Tier API from Namely — 2 operation(s) for job tier.
  name: Namely Job Tier API
  slug: namely-job-tier-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Job Title API from Namely — 2 operation(s) for job title.
  name: Namely Job Title API
  slug: namely-job-title-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Jobs Info API from Namely — 4 operation(s) for jobs info.
  name: Namely Jobs Info API
  slug: namely-jobs-info-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Likes API from Namely — 1 operation(s) for likes.
  name: Namely Likes API
  slug: namely-likes-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Namely System Info API from Namely — 2 operation(s) for namely system info.
  name: Namely System Info API
  slug: namely-namely-system-info-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Notifications API from Namely — 2 operation(s) for notifications.
  name: Namely Notifications API
  slug: namely-notifications-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Profile Fields API from Namely — 4 operation(s) for profile fields.
  name: Namely Profile Fields API
  slug: namely-profile-fields-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Profile Fields Sections API from Namely — 2 operation(s) for profile fields sections.
  name: Namely Profile Fields Sections API
  slug: namely-profile-fields-sections-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Profiles API from Namely — 3 operation(s) for profiles.
  name: Namely Profiles API
  slug: namely-profiles-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Reports API from Namely — 1 operation(s) for reports.
  name: Namely Reports API
  slug: namely-reports-api
- baseURL: https://{company}.namely.com/api/v1
  baseurl_source: declared
  description: The Teams API from Namely — 1 operation(s) for teams.
  name: Namely Teams API
  slug: namely-teams-api
artifact_total: 27
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://namely.com/feed/
- group: other
  href: https://artifacts.apis.io/namely/capabilities/namely-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/namely-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/namely/security/namely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/namely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://namely.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.namely.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.namely.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.namely.com/docs/namely-api/12dab89109ded-namely-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.namely.com/docs/namely-api/72f9086e4f0e7-introduction
- group: auth
  href: https://artifacts.apis.io/namely/authentication/namely-authentication.yml
  title: ''
  type: Authentication
  url: authentication/namely-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://namely.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://namely.com/employee-support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/namely
- group: commercial
  title: ''
  type: Pricing
  url: https://namely.com/lp/pricing/
- group: start
  title: ''
  type: Login
  url: https://namely.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://namely.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://namely.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.namely.com/
- group: operate
  href: https://artifacts.apis.io/namely/changelog/namely-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/namely-changelog.yml
- group: design
  href: https://artifacts.apis.io/namely/lifecycle/namely-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/namely-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/namely/conventions/namely-conventions.yml
  title: ''
  type: Conventions
  url: conventions/namely-conventions.yml
- group: design
  href: https://artifacts.apis.io/namely/conformance/namely-conformance.yml
  title: ''
  type: Conformance
  url: conformance/namely-conformance.yml
- group: design
  href: https://artifacts.apis.io/namely/data-model/namely-data-model.yml
  title: ''
  type: DataModel
  url: data-model/namely-data-model.yml
- group: design
  href: https://artifacts.apis.io/namely/errors/namely-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/namely-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/namely/rate-limits/namely-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/namely-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/namely/plans/namely-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/namely-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/namely/packages/namely-packages.yml
  title: ''
  type: Packages
  url: packages/namely-packages.yml
- group: build
  href: https://artifacts.apis.io/namely/packages/namely-packages.yml
  title: ''
  type: SDKs
  url: packages/namely-packages.yml
- group: start
  href: https://artifacts.apis.io/namely/sandbox/namely-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/namely-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/namely/mcp/namely-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/namely-mcp.yml
- group: agent
  href: https://artifacts.apis.io/namely/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/namely/overlays/namely-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/namely-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://namely.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/namely/llms/namely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/namely-llms.txt
created: '2026-08-26'
description: Namely is a mid-market Human Capital Management (HCM) platform combining HR, payroll, onboarding, benefits administration, time and attendance, performance management and applicant tracking, delivered as a multi-tenant SaaS on customer subdomains. It publishes a public developer portal on Stoplight carrying a Swagger 2.0 contract for its REST API v1 (39 paths, 54 operations, 95 schemas) covering employee profiles, the tenant-specific profile field schema, groups and teams, job titles and tiers, company resources, the social home feed, notifications and reports. Alongside the REST API, Namely runs a SCIM 2.0 provisioning surface acting as the source of record for identity providers such as Okta, and supports SAML 2.0 single sign-on as a service provider. Authentication is either a 3-legged OAuth 2.0 authorization code grant for partner integrations or a Personal Access Token for a customer's own integrations, both minted inside the customer's own tenant. Namely merged into the
  combined Vensure Employer Solutions / PrismHR organisation in September 2022.
finops:
- has_sources: true
  method: derived
  name: Namely Finops
  primary_unit: employee
  service_category: ''
  slug: namely-finops
  template: false
image: https://namely.com/wp-content/uploads/2023/11/Namely.svg
layout: provider
modified: '2026-10-06'
name: Namely
nav: Providers
network: true
overview: 'Namely publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comments API, Company Info API, Company Resources API, and 16 more. Tagged areas include Human Resources, HCM, Payroll, Employee Data, and Onboarding.


  The Namely catalog on APIs.io includes 1 Spectral governance ruleset.


  Namely''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 26 more developer resources.'
plans:
- name: Namely Plans Pricing
  plan_count: 4
  slug: namely-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Namely Rate Limits
  slug: namely-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Namely API Rules
  rule_count: 48
  severity_counts:
    error: 35
    hint: 0
    info: 2
    warn: 11
  slug: namely-rules
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 31.8
    contract_quality: 43.9
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 59.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/namely/namely-2026-09-02T150721.png
security:
- kind: authentication
  name: Namely Authentication
  slug: namely-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Namely Domain Security
  slug: namely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: namely-employee-directory-sync
  slug: namely-employee-directory-sync
- name: namely-profile-schema-management
  slug: namely-profile-schema-management
slug: namely
tags:
- Human Resources
- HCM
- Payroll
- Employee Data
- Onboarding
- Benefits
- Applicant Tracking
- Performance Management
- SCIM
- SSO
- Identity Provisioning
- Workforce Management
- Identity Federation
- Employee Benefits
website: https://namely.com/
---
