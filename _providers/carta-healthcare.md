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
  url: security/carta-healthcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carta.healthcare/
- group: company
  title: ''
  type: Blog
  url: https://www.carta.healthcare/resource-library/#blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://www.carta.healthcare/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carta.healthcare/gdpr-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.carta.healthcare/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cartahealthcare
- group: company
  title: ''
  type: Careers
  url: https://www.carta.healthcare/careers/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.carta.healthcare/news-and-pr/
- group: design
  title: ''
  type: Conformance
  url: conformance/carta-healthcare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.carta.healthcare/news-and-pr/carta-healthcare-successfully-completes-type-2-soc-2-examination-with-an-unqualified-opinion/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carta-healthcare-llms.txt
coverage:
  checked: '2026-08-09'
  detail: Carta Healthcare sells AI-assisted clinical registry abstraction directly into hospital EMR environments under enterprise agreements, and its entire public surface is a WordPress marketing site whose 154-URL Yoast sitemap contains no developer, docs, or API page; no api/docs/developer/app/portal subdomain resolves, and the only machine-readable endpoint on the domain is WordPress core's own /wp-json/.
  evidence:
  - status: 404
    url: https://www.carta.healthcare/openapi.json
  - status: 404
    url: https://www.carta.healthcare/llms.txt
  - status: 404
    url: https://www.carta.healthcare/.well-known/agent-card.json
  - status: 200
    url: https://www.carta.healthcare/sitemap_index.xml
  - status: 200
    url: https://www.carta.healthcare/wp-json/
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: Carta Healthcare, Inc. is a San Francisco based clinical data management company that applies a "Hybrid Intelligence" model — proprietary AI paired with certified human clinical abstractors — to extract, validate and submit structured clinical data on behalf of hospitals and health systems. Its product family covers Voyager (the underlying AI data platform trained on electronic medical record content), Lighthouse and Atlas (AI-assisted clinical registry abstraction and submission, including the ACC NCDR, STS/ACC TVT and Vascular Quality Initiative registries), Navigator (clinical data intelligence and analytics), Harbor (cohort selection and clinical trial matching) and outsourced expert abstraction services. Carta Healthcare is an NCDR certified software vendor and has completed a Type 2 SOC 2 examination with an unqualified opinion covering security, availability and confidentiality. The company sells and integrates directly with hospital EMR environments under enterprise
  agreements; it publishes no public developer program, API documentation, or machine-readable API contract on its public web surface.
image: https://www.carta.healthcare/wp-content/uploads/2025/06/Carta-logo.png
layout: provider
modified: '2026-08-09'
name: Carta Healthcare
nav: Providers
network: true
overview: 'Carta Healthcare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Health IT, Clinical Data, Artificial Intelligence, and Data Abstraction.


  Carta Healthcare''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 13.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Carta Healthcare Domain Security
  slug: carta-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carta-healthcare
tags:
- Healthcare
- Health IT
- Clinical Data
- Artificial Intelligence
- Data Abstraction
- Clinical Registries
- Electronic Medical Records
- Analytics
- HIPAA
- Company
website: https://www.carta.healthcare/
---
