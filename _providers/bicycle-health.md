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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bicycle-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bicyclehealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bicyclehealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.bicyclehealth.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bicyclehealth.com/insurance-and-pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bicyclehealth.com/we-are-here-to-help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bicyclehealth.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bicyclehealth.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bicycle-Health
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bicycle-health-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bicycle-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bicycle-health-conformance.yml
coverage:
  checked: '2026-08-07'
  detail: Bicycle Health is a virtual OUD clinic, not a software vendor — its patient app is served by a private Express backend at api.bicyclehealth.com (GET / returns "Cannot GET /", GET /health returns 204) that publishes no spec, no docs host, and no developer program of any kind; the only machine-readable thing it ships is a patient-facing llms.txt for AI answer engines.
  evidence:
  - status: 204
    url: https://api.bicyclehealth.com/health
  - status: 404
    url: https://api.bicyclehealth.com/openapi.json
  - status: 0
    url: https://developers.bicyclehealth.com/
  - status: 404
    url: https://www.bicyclehealth.com/developers
  - status: 404
    url: https://www.bicyclehealth.com/.well-known/agent-card.json
  - status: 200
    url: https://www.bicyclehealth.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'Bicycle Health is a US telehealth provider of Medication for Addiction Treatment (MAT) for opioid use disorder (OUD), founded in 2017 by Ankit Gupta in Redwood City, California and delivering virtual care since 2020. Care is delivered entirely by secure video visit — intake, provider visits, treatment planning and ongoing support — with prescriptions sent electronically to a pharmacy near the patient. Medications offered include buprenorphine/naloxone (Suboxone), monthly injectable buprenorphine (Sublocade), weekly or monthly injectable buprenorphine (Brixadi) and monthly injectable naltrexone (Vivitrol), and the company also treats kratom and 7-hydroxymitragynine (7-OH) dependence. Bicycle Health accepts most major insurers including Medicaid (in most states it operates in), Medicare and TRICARE, states it has helped over 55,000 patients across 25+ US states, and was named a TIME100 Most Influential Company in 2022 and a Fast Company Most Innovative Company in 2024. It is
  a clinical care organization rather than a software vendor: it ships a patient web and mobile application backed by a private API host, but publishes no public developer program, API documentation, SDK or machine-readable contract.'
image: https://cdn.prod.website-files.com/61f7c8145fe6f608faa84b36/624155b2363584ddcd78b1a5_opengraph.png
layout: provider
modified: '2026-08-07'
name: Bicycle Health
nav: Providers
network: true
overview: 'Bicycle Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Digital Health.


  Bicycle Health''s developer surface includes engineering blog, support, pricing, signup flow, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bicycle-health/refs/heads/main/screenshots/bicycle-health-2026-08-07T162414.png
security:
- kind: domain-security
  name: Bicycle Health Domain Security
  slug: bicycle-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bicycle-health
tags:
- Company
- Health
- Healthcare
- Telehealth
- Digital Health
- Behavioral Health
- Addiction Treatment
- Opioid Use Disorder
- Medication for Addiction Treatment
- Virtual Care
website: https://www.bicyclehealth.com/
---
