---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/holmusk-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/holmusk-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/holmusk-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/holmusk-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/holmusk-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://app.neuroblu.ai/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/holmusk-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/holmusk-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/holmusk-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/holmusk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/holmusk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.holmusk.com/
- group: other
  title: ''
  type: Product
  url: https://www.neuroblu.ai/
- group: start
  title: ''
  type: Login
  url: https://app.neuroblu.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.holmusk.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://info.holmusk.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Holmusk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neuroblu.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neuroblu.ai/platform-privacy-statement
- group: auth
  title: ''
  type: Compliance
  url: https://policy.holmusk.com/
coverage:
  checked: '2026-08-22'
  detail: 'Holmusk ships NeuroBlu as a hosted analytics product for research teams and markets no API at all: neither holmusk.com nor neuroblu.ai contains the word API outside blog prose, /developers 404s on both, there is no self-serve signup (every call to action is a "Request a demo" form), and the only machine-facing host, app.neuroblu.ai, answers every path including /openapi.json and /.well-known/agent-card.json with the same 827-byte React shell whose one XHR path (/api/rwe/...) is the application''s own authenticated internal layer, not an integration surface.'
  evidence:
  - status: 404
    url: https://www.holmusk.com/developers
  - status: 404
    url: https://www.neuroblu.ai/developers
  - status: 200
    url: https://app.neuroblu.ai/openapi.json
  - status: 404
    url: https://www.neuroblu.ai/.well-known/api-catalog
  - status: 200
    url: https://app.neuroblu.ai/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Holmusk is a health data science company building real-world evidence (RWE) infrastructure for neuropsychiatry and behavioral health. Its flagship product, NeuroBlu, pairs NeuroBlu Data — a de-identified, NLP-enriched longitudinal dataset covering 46.5M+ US patients across 20+ years of inpatient, outpatient, emergency, crisis and community care — with NeuroBlu Analytics, a hosted research platform offering no-code cohort building (Cohort Explorer), Data Explorer, Category Mapper and an in-platform R / Python / SQL code studio. Customers are pharma R&D, medical affairs, market access/HEOR, payors and health systems. Holmusk is headquartered in Singapore with offices in New York, London and Basel, and also ships MindLinc and MAST behavioral-health software. The NeuroBlu common data model is being aligned with the OHDSI OMOP Common Data Model. As of this profile Holmusk publishes no public developer program, API reference, or machine-readable API contract; the platform and its
  data dictionary are reachable only after a commercial agreement and login at app.neuroblu.ai.
image: https://cdn.prod.website-files.com/6078f42d748b85659b713f70/607950e3293570d1a0a53b03_Navbar%3ALogo.svg
layout: provider
modified: '2026-08-22'
name: Holmusk
nav: Providers
network: true
overview: 'Holmusk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Real-World Evidence, Behavioral Health, and Mental Health.


  Holmusk''s developer surface includes changelog, support, engineering blog, and 17 more developer resources.'
plans:
- name: Holmusk Plans Pricing
  plan_count: 0
  slug: holmusk-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Holmusk Rate Limits
  slug: holmusk-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 23.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Holmusk Domain Security
  slug: holmusk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Holmusk Vulnerability Disclosure
  slug: holmusk-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Holmusk Trust Center
  slug: holmusk-trust-center
  summary_line: HITRUST CSF, HIPAA / HITECH
slug: holmusk
tags:
- Company
- Healthcare
- Real-World Evidence
- Behavioral Health
- Mental Health
- Neuropsychiatry
- Clinical Data
- Data Analytics
- Life Sciences
- HIPAA
website: https://www.holmusk.com/
---
