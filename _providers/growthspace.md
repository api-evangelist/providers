---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 6
  name: Growthspace Agentic Access
  operation_count: 12
  slug: growthspace-agentic-access
  summary_line: 12 operations · 6 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://public-api-management-dot-growthspace-246311.oa.r.appspot.com
  baseurl_source: declared
  description: The Admin API from GrowthSpace — 6 operation(s) for admin.
  name: GrowthSpace Admin API
  slug: growthspace-admin-api
- baseURL: https://public-api-management-dot-growthspace-246311.oa.r.appspot.com
  baseurl_source: declared
  description: The Ah API from GrowthSpace — 1 operation(s) for ah.
  name: GrowthSpace Ah API
  slug: growthspace-ah-api
- baseURL: https://public-api-management-dot-growthspace-246311.oa.r.appspot.com
  baseurl_source: declared
  description: The @growthspace Engineering/public Api Management API from GrowthSpace — 1 operation(s) for @growthspace engineering/public api management.
  name: GrowthSpace @growthspace Engineering/public Api Management API
  slug: growthspace-growthspace-engineering-public-api-management-api
- baseURL: https://public-api-management-dot-growthspace-246311.oa.r.appspot.com
  baseurl_source: declared
  description: The Healthz API from GrowthSpace — 1 operation(s) for healthz.
  name: GrowthSpace Healthz API
  slug: growthspace-healthz-api
- baseURL: https://public-api-management-dot-growthspace-246311.oa.r.appspot.com
  baseurl_source: declared
  description: The Public API from GrowthSpace — 1 operation(s) for public.
  name: GrowthSpace Public API
  slug: growthspace-public-api
- baseURL: https://public-api-management-dot-growthspace-246311.oa.r.appspot.com
  baseurl_source: declared
  description: The Up Time Check API from GrowthSpace — 1 operation(s) for up time check.
  name: GrowthSpace Up Time Check API
  slug: growthspace-up-time-check-api
artifact_total: 12
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/growthspace-public-api-management-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/growthspace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/growthspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.growthspace.com/
- group: start
  title: ''
  type: Login
  url: https://app.growthspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.growthspace.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.growthspace.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.growthspace.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.growthspace.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/growthspace-engineering
- group: operate
  title: ''
  type: StatusPage
  url: https://status.growthspace.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.growthspace.com/about
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/growthspaceus/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Growthspaceus
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/growthspace-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/growthspace-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/growthspace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/growthspace-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/growthspace-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/growthspace-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/growthspace-packages.yml
- group: design
  title: ''
  type: Components
  url: components/growthspace-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/growthspace-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/growthspace-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/growthspace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/growthspace-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: Growthspace is a precision skill development platform for enterprise learning and talent teams. Using AI-driven matching it pairs individual employees and cohorts with a network of more than 2,800 vetted domain experts across 65+ countries and 80+ skill sets, then runs and measures the resulting development sprints — 1:1 skill development, group skill development, workshops, internal and external mentoring, and the ExpertX on-demand expert surface. The platform handles skill-gap assessment, program execution, scheduling, and outcome measurement in one place, with native integrations into HRIS systems, Microsoft Viva Learning, Slack, Zoom and Teams. Growthspace runs a Public API whose OAuth-style applications, scopes and tokens are provisioned from the admin console; the scope catalogue covers programs, participants, workshops, company, reporting and integration surfaces in read and write variants. Headquartered in New York with customers including Siemens, Microsoft, EY and
  Johnson & Johnson.
image: https://cdn.prod.website-files.com/685bf37fcc056cf0bb7be4d1/68d6feb8a89f53402a0a9c26_Frame%20626177.avif
layout: provider
modified: '2026-08-22'
name: GrowthSpace
nav: Providers
network: true
overview: 'GrowthSpace publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Ah API, @growthspace Engineering/public Api Management API, and 3 more. Tagged areas include Company, Learning and Development, Talent Development, Human Resources, and Coaching.


  GrowthSpace''s developer surface includes engineering blog, support, YouTube channel, authentication, and 23 more developer resources.'
plans:
- name: Growthspace Plans Pricing
  plan_count: 0
  slug: growthspace-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Growthspace Rate Limits
  slug: growthspace-rate-limits
scopes:
- name: Growthspace Scopes
  scope_count: 11
  slug: growthspace-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 32.0
    developer_ergonomics: 28.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/growthspace/refs/heads/main/screenshots/growthspace-2026-09-02T145640.png
security:
- kind: authentication
  name: Growthspace Authentication
  slug: growthspace-authentication
  summary_line: bearer-token/client-credentials · 1 scheme
- kind: domain-security
  name: Growthspace Domain Security
  slug: growthspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: growthspace
tags:
- Company
- Learning and Development
- Talent Development
- Human Resources
- Coaching
- Employee Experience
- Skills
- Workforce
- Enterprise Software
- Artificial Intelligence
website: https://www.growthspace.com/
---
