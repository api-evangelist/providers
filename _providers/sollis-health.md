---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: First-party backend API for the Sollis Health Member Portal (mp.sollishealth.com), the members-only web application used to book appointments, view records and manage membership. Authentication is Mic
  name: Sollis Health Member Portal API
  slug: member-portal-api
- description: First-party backend API for the Sollis Health Navigator Dashboard (navigator.sollishealth.com), the internal clinical and care-coordination console used by Sollis staff. Exposes versioned resource pat
  name: Sollis Health Navigator API
  slug: navigator-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sollis-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sollishealth.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/sollis-health-stock
- group: start
  title: ''
  type: SignUp
  url: https://www.sollishealth.com/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sollishealth.com/membership
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sollishealth.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sollishealth.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.sollishealth.com/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.sollishealth.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.sollishealth.com/blog
- group: company
  title: ''
  type: Press
  url: https://www.sollishealth.com/press
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/sollishealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sollishealth
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sollis-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sollis-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sollis-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sollis-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sollis-health-conformance.yml
coverage:
  checked: '2026-08-05'
  detail: Sollis Health runs two real first-party APIs — mp-api.sollishealth.com behind the members-only portal and navigator-api.sollishealth.com behind the staff clinical console, both secured by its Azure AD B2C tenant — but it sells concierge memberships, not software, and offers no developer program, portal, SDK, sandbox or API reference of any kind; both origins return a hard JSON 404 for every OpenAPI/Swagger discovery path and 401 on a real resource path.
  evidence:
  - status: 401
    url: https://navigator-api.sollishealth.com/v1/regions
  - status: 404
    url: https://navigator-api.sollishealth.com/swagger/v1/swagger.json
  - status: 404
    url: https://mp-api.sollishealth.com/openapi.json
  - status: 404
    url: https://www.sollishealth.com/developers
  - status: 200
    url: https://www.sollishealth.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: Sollis Health is a members-only concierge medicine and 24/7 private emergency care company operating staffed medical centers in New York and the Hamptons, Southern and Northern California, and South Florida. Membership provides unlimited access to emergency-trained physicians, on-site imaging and laboratory diagnostics, house calls, virtual visits, travel medicine, specialist coordination, care navigation and patient advocacy. Sollis is a membership service rather than insurance, and it complements rather than replaces a member's existing clinicians. Individual, family, pediatric and corporate memberships are sold, along with a Platinum tier and bespoke employer plans. Sollis operates its own member-facing software — a Member Portal and an internal Navigator clinical dashboard — backed by first-party APIs secured with Microsoft Entra External ID (Azure AD B2C); those APIs are not published as a public developer program.
image: https://content.sollishealth.com/images/sollis_logo.png
layout: provider
modified: '2026-08-05'
name: Sollis Health
nav: Providers
network: true
overview: 'Sollis Health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Concierge Medicine, and Urgent Care.


  Sollis Health''s developer surface includes signup flow, pricing, support, FAQ, engineering blog, authentication, and 12 more developer resources.'
random_paper: 14
scopes:
- name: Sollis Health Scopes
  scope_count: 2
  slug: sollis-health-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sollis Health Authentication
  slug: sollis-health-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Sollis Health Domain Security
  slug: sollis-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sollis-health
tags:
- Company
- Health
- Healthcare
- Concierge Medicine
- Urgent Care
- Emergency Care
- Membership
- Telehealth
- HIPAA
website: https://www.sollishealth.com/
---
