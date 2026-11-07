---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - authentication
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Light & Wonder Gateway is the partner hub where customers and studios manage games, roadmaps, reports, game assets and integrations ("Integrate our tools ... comprehensive documentation"). Integration
  name: Light & Wonder Gateway
  slug: gateway
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/light-and-wonder/lifecycle/light-and-wonder-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/light-and-wonder-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/light-and-wonder/hosts/light-and-wonder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/light-and-wonder-hosts.yml
- group: other
  href: https://artifacts.apis.io/light-and-wonder/vendors/light-and-wonder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/light-and-wonder-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://gateway.lnw.com/roadmap
- group: company
  title: ''
  type: Newsroom
  url: https://explore.lnw.com/newsroom/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lnw.com/
- group: company
  title: ''
  type: Blog
  url: https://explore.lnw.com/newsroom/
- group: auth
  href: https://artifacts.apis.io/light-and-wonder/security/light-and-wonder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/light-and-wonder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lnw.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.lnw.com/
- group: operate
  title: ''
  type: Support
  url: https://igaming.lnw.com/online-support-portal/
- group: operate
  title: ''
  type: Contact
  url: https://explore.lnw.com/contact-us/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gateway.lnw.com/
- group: start
  title: ''
  type: Login
  url: https://gateway.lnw.com/login
- group: operate
  title: ''
  type: HelpCenter
  url: https://explore.lnw.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://explore.lnw.com/privacy-policy/
- group: commercial
  title: ''
  type: LegalNotices
  url: https://explore.lnw.com/legal-notices/
- group: company
  title: ''
  type: Careers
  url: https://lnw.wd5.myworkdayjobs.com/LightWonderExternalCareers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightnwonder/
coverage:
  checked: '2026-10-20'
  detail: developer.lnw.com redirects to gateway.lnw.com, whose Integrations page only offers Demo, Okta customer and Auth0 internal sign-in (cms-gateway.lnw.com/api/connect/auth0), and no OpenAPI, GraphQL, AsyncAPI, WSDL or proto was found on gateway.lnw.com, portal.lnw.com, igaming.lnw.com or explore.lnw.com.
  evidence:
  - status: 200
    url: https://www.lnw.com/
  - status: 200
    url: https://developer.lnw.com/integrate
  - status: 200
    url: https://gateway.lnw.com/integrations
  - status: 404
    url: https://gateway.lnw.com/openapi.json
  - status: 404
    url: https://gateway.lnw.com/swagger.json
  reason: customer-only-docs
  state: gated
created: '2026-05-04'
description: Light & Wonder is a leading cross-platform global games company that develops and distributes gaming content across land-based casinos, mobile platforms, and online channels. The company's portfolio includes titles such as Dancing Drums Prosperity, Rainbow Riches, and Gold Fish, and includes subsidiaries SciPlay (mobile social gaming) and Grover Gaming. Light & Wonder operates customer-facing support portals for both gaming and iGaming partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/light-and-wonder.png
layout: provider
modified: '2026-10-20'
name: Light & Wonder
nav: Providers
network: true
overview: 'Light & Wonder is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Casinos, iGaming, Mobile Games, and Entertainment.


  Light & Wonder''s developer surface includes documentation, engineering blog, developer portal, support, and 15 more developer resources.'
plans:
- name: Light And Wonder Plans Pricing
  plan_count: 0
  slug: light-and-wonder-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Light And Wonder Rate Limits
  slug: light-and-wonder-rate-limits
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/light-and-wonder/light-and-wonder-2026-06-20T184512.png
security:
- kind: authentication
  name: Light And Wonder Authentication
  slug: light-and-wonder-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Light And Wonder Domain Security
  slug: light-and-wonder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: light-and-wonder
tags:
- Gaming
- Casinos
- iGaming
- Mobile Games
- Entertainment
- Slot Machines
- Social Gaming
website: https://www.lnw.com/
---
