---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The internet-facing REST services that power the Carrum Health member application (my.carrumhealth.com): core-service (accounts, episodes, profiles), care-service, message-service, price-service and u'
  name: Carrum Health Platform Services
  slug: carrum-health-platform-services
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carrum-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carrumhealth.com/
- group: company
  title: ''
  type: Blog
  url: https://carrumhealth.com/carrum-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://carrumhealth.com/carrum-blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://carrumhealth.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://my.carrumhealth.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carrumhealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carrumhealth.com/privacy-statement/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carrumhealth
- group: auth
  title: ''
  type: TrustCenter
  url: security/carrum-health-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.carrumhealth.com/
- group: company
  title: ''
  type: Newsroom
  url: https://carrumhealth.com/newsroom/
- group: company
  title: ''
  type: Careers
  url: https://carrumhealth.com/careers/
- group: other
  title: ''
  type: Accessibility
  url: https://carrumhealth.com/accessibility-statement/
- group: other
  title: ''
  type: MobileApplication
  url: https://apps.apple.com/us/app/carrum-health/id1403041263
- group: other
  title: ''
  type: MobileApplication
  url: https://play.google.com/store/apps/details?id=com.carrumhealth.patientapp
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/carrum-health_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carrum-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carrum-health-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carrum-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carrum-health-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/carrum-health-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carrum-health-llms.txt
created: '2026-08-01'
description: 'Carrum Health operates a value-based Centers of Excellence (COE) platform that connects self-insured employers and their members with a curated national network of surgical, cancer and substance-use-care providers under upfront bundled payments. Founded in 2014, the company pairs a member-facing mobile and web application with a care-navigation team so members are guided through the full episode of care with no deductibles, co-pays or surprise bills, and a 30-day warranty on each procedure. Carrum sells to employers and benefits consultants and integrates with health plans, TPAs and point-solution partners such as Hinge Health, Sword Health, AccessHope, Teladoc and Accolade. Carrum publishes no public developer program: there is no public API portal, OpenAPI definition, SDK or documentation host. The platform is backed by a set of internet-facing REST services (core, care, message, price and upload) discovered in the public member-application bundle, each of which serves an
  HTTP Basic-gated /api-docs surface, and core-service publishes an A2A agent registry at /.well-known/agents.json that is currently empty.'
image: https://carrumhealth.com/wp-content/uploads/2026/06/Color-Logo.png
layout: provider
modified: '2026-08-01'
name: Carrum Health
nav: Providers
network: true
overview: 'Carrum Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Benefits, Centers of Excellence, and Value-Based Care.


  Carrum Health''s developer surface includes engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carrum-health/refs/heads/main/screenshots/carrum-health-2026-08-07T163029.png
security:
- kind: authentication
  name: Carrum Health Authentication
  slug: carrum-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Carrum Health Domain Security
  slug: carrum-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carrum Health Trust Center
  slug: carrum-health-trust-center
  summary_line: trust center published
slug: carrum-health
tags:
- Company
- Healthcare
- Health Benefits
- Centers of Excellence
- Value-Based Care
- Bundled Payments
- Employee Benefits
- Surgery
- Care Navigation
- Digital Health
website: https://carrumhealth.com/
---
