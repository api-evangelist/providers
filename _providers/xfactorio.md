---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.xfactor.io/
- group: company
  title: ''
  type: Blog
  url: https://www.xfactor.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.xfactor.io/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.xfactor.io/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xfactor.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xfactor.io/privacy-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XFactor-IO
- group: start
  title: ''
  type: Login
  url: https://app.xfactor.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/xfactorio-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.secureframe.com/ext/trust-center/xfactor-io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xfactorio-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xfactorio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xfactorio-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Xfactor.io ships only the closed app.xfactor.io SaaS product — its api.xfactor.io host answers an nginx-ingress "default backend - 404" at every OpenAPI, Swagger, GraphQL and docs path on the host root, no docs., developer. or mcp. subdomain resolves, the XFactor-IO GitHub organization has zero public repositories, and the complete 24-page site sitemap contains no developer, API or documentation page.
  evidence:
  - status: 404
    url: https://api.xfactor.io/openapi.json
  - status: 404
    url: https://api.xfactor.io/graphql
  - status: 200
    url: https://www.xfactor.io/page-sitemap.xml
  - status: 404
    url: https://www.xfactor.io/llms.txt
  - status: 200
    url: https://api.github.com/orgs/XFactor-IO/repos
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Xfactor.io is an AI-powered revenue operations platform founded by Mike Carpenter and backed by Accel and Lightspeed Venture Partners. Its Growth AI engine, together with the Xfactor Central, OpenInsights, and Simulation products, builds a live digital twin of a company's go-to-market operations — connecting CRM, pipeline, usage, and financial data so revenue teams can test decisions through simulation before rolling them out. The platform is delivered as a closed B2B SaaS application (app.xfactor.io) and does not publish a public API, developer portal, or client SDKs; security posture is documented on a Secureframe trust center with a SOC 2 Type II attestation.
image: https://www.xfactor.io/wp-content/uploads/2026/01/xf-logo-white-inline-1.png
layout: provider
modified: '2026-08-13'
name: Xfactor.io
nav: Providers
network: true
overview: 'Xfactor.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Services, Revenue Operations, Artificial Intelligence, and Analytics.


  Xfactor.io''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Xfactorio Plans Pricing
  plan_count: 0
  slug: xfactorio-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Xfactorio Rate Limits
  slug: xfactorio-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xfactorio/refs/heads/main/screenshots/xfactorio-2026-09-02T171115.png
security:
- kind: domain-security
  name: Xfactorio Domain Security
  slug: xfactorio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Xfactorio Trust Center
  slug: xfactorio-trust-center
  summary_line: SOC 2 Type II
slug: xfactorio
tags:
- Company
- Services
- Revenue Operations
- Artificial Intelligence
- Analytics
- Forecasting
- Go-To-Market
- Software-as-a-Service
website: https://www.xfactor.io/
---
