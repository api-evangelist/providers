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
    error_semantics: false
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
  score: 7.9
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The first-party Mantra Health API. The host api.mantrahealth.com answers 200 with the plain-text banner "Mantra Health API" and exposes a GraphQL endpoint at /graphql that is served by Apollo Server (
  name: Mantra Health GraphQL API
  slug: mantra-health-graphql-api
- description: The WordPress REST API behind the mantrahealth.com marketing and resource site, served unauthenticated at /wp-json/. This is the content management surface for the public website (posts, pages, resour
  name: Mantra Health WordPress Content API
  slug: mantra-health-wordpress-content-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mantra-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mantrahealth.com/
- group: company
  title: ''
  type: Blog
  url: https://mantrahealth.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://mantrahealth.com/get-in-touch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mantrahealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mantrahealth.com/terms-and-conditions/
- group: start
  title: ''
  type: Login
  url: https://hub.mantrahealth.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mantrahealth
- group: operate
  title: ''
  type: StatusPage
  url: https://mantrahealth.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/mantra-health-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/mantra-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mantra-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mantra-health-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mantra-health-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mantra-health-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mantra-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mantra-health-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mantra-health-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Mantra Health demonstrably runs an API — api.mantrahealth.com answers 200 with the banner "Mantra Health API" and serves a live Apollo GraphQL endpoint, and the company status page lists API, SSO and 3rd Party Integrations components — but there is no developer portal, reference or spec anywhere on any host, GraphQL introspection is disabled so the schema returns GRAPHQL_VALIDATION_FAILED for every query outside an allowed set, and the site's only route to access is the institutional "Get in Touch" / "Get a quote" sales form.
  evidence:
  - status: 200
    url: https://api.mantrahealth.com/
  - status: 400
    url: https://api.mantrahealth.com/graphql
  - status: 404
    url: https://api.mantrahealth.com/openapi.json
  - status: 200
    url: https://mantrahealth.com/pricing/
  - status: 200
    url: https://mantrahealth.statuspage.io/api/v2/summary.json
  reason: sales-gate
  state: gated
created: '2026-08-25'
description: 'Mantra Health, Inc. is a New York-based digital mental health company that partners with colleges and universities to extend campus counseling centers with tele-mental health care. Its platform combines a partner clinic of licensed psychiatrists, therapists and wellness coaches with software used by students, campus staff and clinicians: the student-facing Mantra Hub, the Mantra Collaboration Portal used by campus counseling staff to co-manage care with Mantra providers, a provider portal, the Beacon offering, and ConnectNow 24/7 crisis and on-demand emotional support. Mantra operates a first-party API at api.mantrahealth.com backed by a GraphQL endpoint, and runs a public Atlassian status page whose components list an API, SSO and 3rd Party Integrations alongside the patient, provider, management and collaboration portals. Mantra publishes no public developer portal, API reference, SDK or machine-readable specification; the API is a customer/product surface reached through
  the campus contract rather than a self-serve developer program.'
image: https://i0.wp.com/mantrahealth.com/wp-content/uploads/2023/12/cropped-Mantra-Favicon.png?fit=192%2C192&ssl=1
layout: provider
modified: '2026-08-25'
name: Mantra Health
nav: Providers
network: true
overview: 'Mantra Health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Mental Health, Telehealth, and Higher Education.


  Mantra Health''s developer surface includes engineering blog, support, authentication, and 15 more developer resources.'
plans:
- name: Mantra Health Plans Pricing
  plan_count: 0
  slug: mantra-health-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Mantra Health Rate Limits
  slug: mantra-health-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 24.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 35.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mantra-health/refs/heads/main/screenshots/mantra-health-2026-09-02T150429.png
security:
- kind: authentication
  name: Mantra Health Authentication
  slug: mantra-health-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mantra Health Domain Security
  slug: mantra-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mantra Health Vulnerability Disclosure
  slug: mantra-health-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mantra Health Trust Center
  slug: mantra-health-trust-center
  summary_line: HIPAA, SOC 2, SOC 1, TX-RAMP
slug: mantra-health
tags:
- Company
- Healthcare
- Mental Health
- Telehealth
- Higher Education
- Digital Health
- Patient Engagement
- HIPAA
- GraphQL
website: https://mantrahealth.com/
---
