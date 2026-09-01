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
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navina-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.navina.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.navina.ai/articles
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.navina.ai/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.navina.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.navina.ai/legal/general-terms-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Navina-ai
- group: start
  title: ''
  type: Login
  url: https://app.navina.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.navina.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.navina.ai/
- group: auth
  title: ''
  type: Compliance
  url: conformance/navina-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/navina-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/navina-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/navina-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/navina-plans-pricing.yml
coverage:
  checked: '2026-08-26'
  detail: Navina ships an EHR-embedded clinical AI product and consumes EHR FHIR/HL7 APIs rather than publishing one — its 255-URL sitemap contains no developer, docs or API page, and api.navina.ai is an AWS API Gateway that answers every path, including /openapi.json and /mcp, with HTTP 403 "Missing Authentication Token".
  evidence:
  - status: 200
    url: https://www.navina.ai/sitemap.xml
  - status: 403
    url: https://api.navina.ai/openapi.json
  - status: 404
    url: https://www.navina.ai/openapi.json
  - status: 403
    url: https://docs.navina.ai/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Navina is a healthcare AI company whose clinician-facing copilot supports value-based care. It ingests data from electronic health records, health information exchanges, insurance claims and care-gap files, then reconciles it into a single "Patient Portrait" that surfaces risk-adjustment (HCC/RAF) insights, quality and care-gap management, ambient clinical documentation and network analytics at the point of care. Navina is delivered as an EHR-embedded application — integrated with Epic, Veradigm/Altera, athenahealth, eClinicalWorks and Cerner via HL7 v2/v3, FHIR and SMART on FHIR/OAuth2 — and is sold to physician groups, health systems, ACOs/MSOs and health plans. It is a consumer of EHR interoperability APIs rather than a publisher of a public developer API: no developer portal, documentation, API reference or machine-readable contract is published, and the api.navina.ai host is a fully authenticated backend.'
image: https://cdn.prod.website-files.com/65df77bb47a7104730575520/65df7e15c4b06e32101057f8_navina_webclip.png
layout: provider
modified: '2026-08-26'
name: Navina
nav: Providers
network: true
overview: 'Navina is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Clinical Decision Support, and Value-Based Care.


  Navina''s developer surface includes engineering blog and 14 more developer resources.'
plans:
- name: Navina Plans Pricing
  plan_count: 0
  slug: navina-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 20.7
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
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Navina Domain Security
  slug: navina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Navina Vulnerability Disclosure
  slug: navina-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Navina Trust Center
  slug: navina-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type II, HIPAA
slug: navina
tags:
- Company
- Healthcare
- Artificial Intelligence
- Clinical Decision Support
- Value-Based Care
- Risk Adjustment
- Electronic Health Records
- FHIR
- Interoperability
- Medical Coding
website: https://www.navina.ai/
---
