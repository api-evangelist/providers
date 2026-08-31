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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/genomind-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genomind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://genomind.com/
- group: company
  title: ''
  type: Blog
  url: https://genomind.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://genomind.com/help/
- group: operate
  title: ''
  type: HelpCenter
  url: https://genomind.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://genomind.com/cost-and-coverage/
- group: start
  title: ''
  type: SignUp
  url: https://gateway.genomind.com/Register
- group: start
  title: ''
  type: Login
  url: https://portal.genomind.com/Account/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://genomind.com/patient-consent-financial-agreement-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://genomind.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://genomind.com/compliance/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genomind-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/genomind-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/genomind-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/genomind-rate-limits.yml
coverage:
  checked: '2026-08-21'
  detail: 'Genomind runs no developer site at all: every path on portal.genomind.com — including /swagger, /api/ and /graphql — returns the ASP.NET login shell, the EMR ordering surface it markets (Epic, athenahealth, NextGen Healthcare, DrChrono, Practice Fusion) is a per-health-system contracted HL7 v2 lab orders/results interface arranged through a "Get Started" sales form with no public reference or message profile, and the only machine-readable document on any Genomind host is the marketing site''s auto-enabled WordPress /wp-json index.'
  evidence:
  - status: 200
    url: https://genomind.com/who-we-support/providers/get-started/
  - status: 404
    url: https://genomind.com/openapi.json
  - status: 404
    url: https://portal.genomind.com/swagger/v1/swagger.json
  reason: sales-gate
  state: gated
created: '2026-08-21'
description: Genomind is a US precision-medicine company in mental health, built around the Genomind Professional PGx pharmacogenetic test — a 26-gene panel (15 pharmacodynamic, 11 pharmacokinetic) used by clinicians to assess gene-drug and drug-drug interaction risk across more than 700 medications. Alongside the CLIA-certified, CAP-accredited laboratory it operates a Precision Medicine Software product, a provider portal, a patient gateway and a partner portal, and it has built lab orders-and-results interfaces into EMR/EHR systems including Epic, athenahealth, NextGen Healthcare, DrChrono, Practice Fusion, iSalus and MedEnt. Genomind publishes no public developer program, API reference or machine-readable specification; its integration surface is a contracted HL7 v2 lab interface arranged per health system. In July 2026 Vanta Diagnostics acquired key Genomind assets, including the genetics lab, clinical operations and the direct-to-provider business, and the provider portal now carries
  Vanta Diagnostics branding.
image: https://genomind.com/wp-content/uploads/2021/12/cropped-genomind_tag_full_color_pos_rgb.png
layout: provider
modified: '2026-08-21'
name: Genomind
nav: Providers
network: true
overview: 'Genomind is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Genomics, and Pharmacogenomics.


  Genomind''s developer surface includes engineering blog, support, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Genomind Plans Pricing
  plan_count: 1
  slug: genomind-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Genomind Rate Limits
  slug: genomind-rate-limits
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Genomind Domain Security
  slug: genomind-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Genomind Trust Center
  slug: genomind-trust-center
  summary_line: CLIA, CAP, New York State clinical laboratory permit, Rhode Island clinical laboratory license, Pennsylvania clinical laboratory license, California clinical laboratory license, Maryland clinical laboratory license
slug: genomind
tags:
- Company
- Health
- Healthcare
- Genomics
- Pharmacogenomics
- Precision Medicine
- Mental Health
- Diagnostics
- Laboratory
- Clinical Decision Support
- HIPAA
- EHR Integration
website: https://genomind.com/
---
