---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-03'
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
  name: Namely Namely System Info API
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
artifact_total: 23
common:
- group: auth
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
  title: ''
  type: ChangeLog
  url: changelog/namely-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/namely-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/namely-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/namely-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/namely-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/namely-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/namely-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/namely-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/namely-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/namely-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/namely-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/namely-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/namely-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://namely.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/namely-llms.txt
created: '2026-08-26'
description: Namely is a mid-market Human Capital Management (HCM) platform combining HR, payroll, onboarding, benefits administration, time and attendance, performance management and applicant tracking, delivered as a multi-tenant SaaS on customer subdomains. It publishes a public developer portal on Stoplight carrying a Swagger 2.0 contract for its REST API v1 (39 paths, 54 operations, 95 schemas) covering employee profiles, the tenant-specific profile field schema, groups and teams, job titles and tiers, company resources, the social home feed, notifications and reports. Alongside the REST API, Namely runs a SCIM 2.0 provisioning surface acting as the source of record for identity providers such as Okta, and supports SAML 2.0 single sign-on as a service provider. Authentication is either a 3-legged OAuth 2.0 authorization code grant for partner integrations or a Personal Access Token for a customer's own integrations, both minted inside the customer's own tenant. Namely merged into the
  combined Vensure Employer Solutions / PrismHR organisation in September 2022.
image: https://namely.com/wp-content/uploads/2023/11/Namely.svg
layout: provider
modified: '2026-08-26'
name: Namely
nav: Providers
network: true
overview: 'Namely publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Company Info API, Company Resources API, and 16 more. Tagged areas include HR, HCM, Payroll, Employee Data, and Onboarding.


  Namely''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 24 more developer resources.'
plans:
- name: Namely Plans Pricing
  plan_count: 4
  slug: namely-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Namely Rate Limits
  slug: namely-rate-limits
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 45.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 56.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/namely/refs/heads/main/screenshots/namely-2026-09-02T150721.png
security:
- kind: authentication
  name: Namely Authentication
  slug: namely-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Namely Domain Security
  slug: namely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: namely
tags:
- HR
- HCM
- Payroll
- Employee Data
- Onboarding
- Benefits
- Applicant Tracking
- Performance Management
- SCIM
- Single Sign-On
- Identity Provisioning
- Workforce Management
website: https://namely.com/
---
