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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Palm HR REST API surface (api.palm.hr). Customers create API keys with granular permissions to push HR, attendance, and payroll data to ERPs and external tools. No public OpenAPI specification or deve
  name: Palm HR API
  slug: palm-hr-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/palmhr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://palmhr.net/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palmhr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://palmhr.net/en
- group: start
  title: ''
  type: Login
  url: https://palmhr.net/en/login
- group: commercial
  title: ''
  type: Pricing
  url: https://palmhr.net/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://palmhr.net/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://palmhr.net/en/privacy
- group: operate
  title: ''
  type: HelpCenter
  url: https://palmhr.crisp.help/en/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/palmhr-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/palmhr-well-known.yml
created: '2026-07-17'
description: Palm HR (palm.hr, operating on palmhr.net) is an HR management and payroll platform built specifically for the UAE and broader MENA region, trusted by organizations from startups to enterprises for local labor-law and WPS compliance. The platform spans people management (employee profiles, onboarding and offboarding, document management), attendance and time tracking (mobile check-in/out, timesheets, shift scheduling, project time), payroll automation (WPS-compliant processing, expenses, loans, multi-country and multi-currency), performance management, and recruiting, plus an outsourced-HR service. Palm HR exposes REST APIs with API keys carrying granular permissions so customers can push data to ERPs and external tools, and ships prebuilt integrations with accounting suites (Xero, QuickBooks, Zoho Books, Dynamics 365, NetSuite, Wafeq, Qoyod, Odoo, Tally), biometric devices (ZKTeco, CAMS), and automation platforms (Zapier, Make, Power Automate). The company is a portfolio company
  of Speedinvest. This profile was enriched from public web surfaces; no public OpenAPI specification or developer portal was discovered.
image: https://palmhr.net/apple-touch-icon.png
layout: provider
modified: '2026-07-20'
name: Palm HR
nav: Providers
network: true
overview: 'Palm HR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR, Human Resources, Payroll, and Attendance.


  Palm HR''s developer surface includes pricing and 10 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 16.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/palmhr/refs/heads/main/screenshots/palmhr-2026-08-07T191324.png
security:
- kind: domain-security
  name: Palmhr Domain Security
  slug: palmhr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Palmhr Vulnerability Disclosure
  slug: palmhr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: palmhr
tags:
- Company
- HR
- Human Resources
- Payroll
- Attendance
- Performance Management
- Recruiting
- WPS
- UAE
- MENA
website: https://palmhr.net/en
---
