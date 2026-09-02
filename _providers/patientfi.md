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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patientfi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patientfi.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.patientfi.com/
- group: operate
  title: ''
  type: Support
  url: https://provider.patientfi.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://provider.patientfi.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.patientfi.com/v2/admin/login
- group: start
  title: ''
  type: SignUp
  url: https://patientfi.com/book-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://patientfi.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://patientfi.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PatientFi
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.patientfi.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/patientfi-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/patientfi-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/patientfi-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://patientfi.com/lending-partners
- group: design
  title: ''
  type: Conformance
  url: conformance/patientfi-conformance.yml
coverage:
  checked: '2026-08-26'
  detail: PatientFi advertises "open APIs" on patientfi.com/enterprise/ and ships native in-workflow integrations with Nextech, PatientNow and ModMed, but no developer surface is published at all — developer.patientfi.com, docs.patientfi.com and api.patientfi.com do not exist in DNS, there is no /pricing/ or /developers/ page in the site sitemap, and the only route to the API is the "Book a Demo" enterprise partnership form.
  evidence:
  - status: 200
    url: https://patientfi.com/enterprise/
  - status: 0
    url: https://developer.patientfi.com/
  - status: 0
    url: https://docs.patientfi.com/
  - status: 0
    url: https://api.patientfi.com/
  - status: 200
    url: https://patientfi.com/book-a-demo/
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: PatientFi is an Irvine, California patient-financing company that lets healthcare practices offer patients pay-over-time plans for elective and medical procedures — aesthetics and plastic surgery, medspa, cosmetic dental, fertility, audiology and hair restoration. Practices enroll as partnered providers, send patients an application link by SMS or from their own website, and issue a "transaction" against an approved patient spending limit; the practice is funded within one to three business days while the patient repays a bank-originated loan. Approvals reach $60,000 across the full credit spectrum through a waterfall of bank and credit-union lending partners. PatientFi markets "open APIs" for enterprise practice-management integrations and ships native in-workflow integrations with Nextech, PatientNow and ModMed plus redirect integrations with Symplast and Aesthetic Record, but publishes no public developer portal, API reference or machine-readable specification — API access
  is arranged through an enterprise partnership.
image: https://patientfi.com/wp-content/uploads/2022/01/PatientFi-Primary-Logo-Laguna-1@2x.png
layout: provider
modified: '2026-08-26'
name: PatientFi
nav: Providers
network: true
overview: 'PatientFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include healthcare-financing, Patient Financing, Consumer Lending, Point of Sale Financing, and Buy Now Pay Later.


  PatientFi''s developer surface includes engineering blog, support, signup flow, pricing, and 12 more developer resources.'
plans:
- name: Patientfi Plans Pricing
  plan_count: 2
  slug: patientfi-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Patientfi Rate Limits
  slug: patientfi-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 23.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Patientfi Domain Security
  slug: patientfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Patientfi Trust Center
  slug: patientfi-trust-center
  summary_line: trust center published
slug: patientfi
tags:
- healthcare-financing
- Patient Financing
- Consumer Lending
- Point of Sale Financing
- Buy Now Pay Later
- Fintech
- Payments
- Embedded Finance
- Aesthetics
- Plastic Surgery
- Med Spa
- cosmetic-dental
- Fertility
- Audiology
- Practice Management
website: https://patientfi.com/
---
