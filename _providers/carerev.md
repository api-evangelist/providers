---
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The private application and partner-integration API behind the CareRev platform. api.carerev.com is a live, TLS-terminated API gateway (Istio/Envoy fronting a Ruby application) that serves the CareRev
  name: CareRev Platform API
  slug: platform
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.carerev.com/
- group: company
  title: ''
  type: About
  url: https://www.carerev.com/company
- group: other
  title: ''
  type: HowItWorks
  url: https://www.carerev.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://www.carerev.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://www.carerev.com/professionals/faq
- group: company
  title: ''
  type: Blog
  url: https://www.carerev.com/blog
- group: company
  title: ''
  type: News
  url: https://www.carerev.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CareRevolutions
- group: start
  title: ''
  type: SignUp
  url: https://app.carerev.com/new-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carerev.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carerev.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.carerev.com/carerev-careers
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carerev.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carerev-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.carerev.com/blog/the-joint-commission-and-carerev-partners-in-healthcare-excellence
- group: design
  title: ''
  type: Conformance
  url: conformance/carerev-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carerev-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carerev-llms.txt
- group: other
  title: ''
  type: Forge
  url: https://forgeglobal.com/carerev_stock/
created: '2026-08-02'
description: CareRev is a healthcare workforce management and on-demand labor marketplace that connects hospitals and health systems directly with local, credentialed clinical professionals — registered nurses, LPN/LVNs, CNAs, surgical and ER techs, medical assistants, respiratory therapists, phlebotomists and mental health techs — without a traditional staffing agency in the middle. Facilities post open shifts from their existing scheduling and HR systems and vetted clinicians browse, claim and self-schedule them in the CareRev mobile app, while CareRev handles credential verification, compliance and payment. The product line spans the CareRev Marketplace (external on-demand talent), IRP+ (internal resource pool control and float-pool visibility for a health system's own staff) and Smart Rates (dynamic rate modeling to control labor spend). CareRev is certified by The Joint Commission under its Health Care Staffing Services program and serves more than 650 facilities across the United States.
  Integration with a facility's VMS, scheduling and workforce-management stack (including UKG Dimensions via the UKG Connect Technology Partner Program) is delivered through private, partner-scoped API connections; CareRev publishes no public developer portal, API documentation or machine-readable API contract as of this profiling pass.
image: https://cdn.prod.website-files.com/5babc11099f97ef511cf24a6/62320df8e01070ecfbd91b6a_CR-logo-full-color_RGB.svg
layout: provider
modified: '2026-08-02'
name: CareRev
nav: Providers
network: true
overview: 'CareRev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Systems, Workforce Management, and Staffing.


  CareRev''s developer surface includes support, FAQ, engineering blog, product news, signup flow, and 14 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carerev/refs/heads/main/screenshots/carerev-2026-08-07T163002.png
security:
- kind: domain-security
  name: Carerev Domain Security
  slug: carerev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carerev
tags:
- Company
- Healthcare
- Health Systems
- Workforce Management
- Staffing
- Nursing
- Marketplace
- Scheduling
- Human Resources
- Labor Marketplace
website: https://www.carerev.com/
---
