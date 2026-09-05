---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 5.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Kiddom is a certified 1EdTech LTI Advantage 1.3 Tool (Assignment and Grade Services 2.0, Names and Role Provisioning Services 2.0, Deep Linking 2.0). The publicly reachable surface is the OIDC third-p
  name: Kiddom LTI 1.3 Tool Endpoints
  slug: lti
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.kiddom.co/
- group: docs
  title: ''
  type: Documentation
  url: https://support.kiddom.co/en/collections/19663428-rostering-and-integrations
- group: operate
  title: ''
  type: Support
  url: https://support.kiddom.co/en/
- group: company
  title: ''
  type: Blog
  url: https://www.kiddom.co/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kiddom
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kiddom.co/
- group: start
  title: ''
  type: Login
  url: https://app.kiddom.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kiddom.co/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kiddom.co/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://site.imsglobal.org/certifications/kiddom-inc/kiddom
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kiddom-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/kiddom-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kiddom-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kiddom-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kiddom-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/kiddom-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kiddom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kiddom-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kiddom-data-model.yml
coverage:
  checked: '2026-08-23'
  detail: Kiddom runs a real API host — api.kiddom.co answers live LTI 1.3 launch traffic — but its API documentation at https://api.kiddom.co/docs 302s to a Cloudflare Access sign-in at kiddomdata.cloudflareaccess.com, and no OpenAPI, GraphQL SDL, AsyncAPI, MCP server or agent card is served on any Kiddom host.
  evidence:
  - status: 302
    url: https://api.kiddom.co/docs
  - status: 404
    url: https://api.kiddom.co/openapi.json
  - status: 400
    url: https://api.kiddom.co/lti/login
  - status: 404
    url: https://www.kiddom.co/.well-known/api-catalog
  reason: partner-login
  state: gated
created: '2026-08-23'
description: 'Kiddom is a K-12 curriculum management, instruction and assessment platform used by school districts to implement high-quality instructional materials (HQIM), plan and pace lessons, deliver digital assignments, administer standards-aligned assessments, and analyze student performance data. The product is sold to districts rather than to developers: there is no public developer program, API key, or published API reference. Kiddom''s public machine-readable surface is its 1EdTech interoperability posture — it is certified as an LTI Advantage 1.3 Tool and as a OneRoster 1.1 REST Data Consumer, and it rosters from Clever, ClassLink, Google Classroom, Canvas, Schoology and Microsoft Teams. The only publicly reachable API endpoints are the LTI 1.3 launch pair on api.kiddom.co; the API documentation at api.kiddom.co/docs sits behind Cloudflare Access.'
image: https://cdn.prod.website-files.com/66e9f6c87b37d1a3552bd9b6/6a34797390dfc8ead8d6428a_Webflow_ShareImage%402x.png
layout: provider
modified: '2026-08-23'
name: Kiddom
nav: Providers
network: true
overview: 'Kiddom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, K-12, Curriculum, Learning Management, and Assessment.


  Kiddom''s developer surface includes documentation, support, engineering blog, authentication, and 15 more developer resources.'
plans:
- name: Kiddom Plans Pricing
  plan_count: 0
  slug: kiddom-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Kiddom Rate Limits
  slug: kiddom-rate-limits
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kiddom/refs/heads/main/screenshots/kiddom-2026-09-02T150033.png
security:
- kind: authentication
  name: Kiddom Authentication
  slug: kiddom-authentication
  summary_line: openIdConnect · 3 schemes
- kind: domain-security
  name: Kiddom Domain Security
  slug: kiddom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kiddom
tags:
- Education
- K-12
- Curriculum
- Learning Management
- Assessment
- EdTech
- Rostering
- Interoperability
- LTI
- OneRoster
- Analytics
website: https://www.kiddom.co/
---
