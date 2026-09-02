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
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: HotDoc's OpenID Connect / OAuth 2.0 authorization server (Rails/Doorkeeper) for clinic and partner sign-in. Discovery metadata (OIDC + RFC 8414) and a live RS256 JWKS are served publicly; authorizatio
  name: HotDoc OpenID Connect
  slug: hotdoc-openid-connect
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.hotdoc.com.au/
- group: start
  title: ''
  type: Portal
  url: https://practices.hotdoc.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.hotdoc.com.au/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.hotdoc.com.au/hc/en-gb
- group: commercial
  title: ''
  type: Pricing
  url: https://support.hotdoc.com.au/hc/en-gb/articles/9993384697753-How-much-does-HotDoc-cost
- group: start
  title: ''
  type: SignUp
  url: https://www.hotdoc.com.au/medical-centres/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://practices.hotdoc.com.au/terms-of-services-clinics/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://practices.hotdoc.com.au/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hotdoc.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/htdc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hotdoc
- group: auth
  title: ''
  type: Authentication
  url: authentication/hotdoc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hotdoc-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hotdoc-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hotdoc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://practices.hotdoc.com.au/security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hotdoc-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotdoc-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hotdoc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://practices.hotdoc.com.au/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/hotdoc-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hotdoc-llms.txt
created: '2026-07-24'
description: 'HotDoc is an Australian patient-engagement platform, founded in 2012 and headquartered in Melbourne, that connects patients with general practices, dentists, and specialists. Roughly one in three Australians use HotDoc to find and book healthcare, and the platform serves more than 21,000 practitioners across the country. Its clinic-facing SaaS provides online bookings, telehealth, appointment reminders, SMS recalls for clinical reminders and results, mobile and kiosk check-in, digital new-patient registration forms, online repeat prescription requests, and preventative-health outreach. HotDoc operates as an engagement layer on top of Australian practice-management systems (Best Practice, MedicalDirector, Zedmed, Genie, Cliniko, Nookal and others): a clinic connects HotDoc by entering its practice-management-system API key into the HotDoc dashboard, so HotDoc consumes those PMS APIs rather than publishing its own. HotDoc does operate a real OpenID Connect / OAuth 2.0 authorization
  server (Rails/Doorkeeper) for clinic and partner sign-in, served with live discovery metadata and a JWKS, but exposes no self-serve public developer portal, no documented third-party REST/OpenAPI, and no HL7 FHIR CapabilityStatement; its integration surface is partner/PMS-gated. HotDoc was acquired by Potentia in February 2026.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: HotDoc
nav: Providers
network: true
overview: 'HotDoc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Australia, Patient Engagement, Online Booking, and Appointment Scheduling.


  HotDoc''s developer surface includes developer portal, engineering blog, support, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 11
scopes:
- name: Hotdoc Scopes
  scope_count: 1
  slug: hotdoc-scopes
  summary_line: 1 scope · authorizationCode/implicit
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 39.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 73.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotdoc/refs/heads/main/screenshots/hotdoc-2026-07-25T221455.png
security:
- kind: authentication
  name: Hotdoc Authentication
  slug: hotdoc-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Hotdoc Domain Security
  slug: hotdoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hotdoc Vulnerability Disclosure
  slug: hotdoc-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Hotdoc Trust Center
  slug: hotdoc-trust-center
  summary_line: SOC 2 Type II
slug: hotdoc
tags:
- Healthcare
- Australia
- Patient Engagement
- Online Booking
- Appointment Scheduling
- Telehealth
- Practice Management
- Primary Care
- Digital Health
- e-Prescribing
website: https://www.hotdoc.com.au/
---
