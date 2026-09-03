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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://theclinician.com/
- group: company
  title: ''
  type: Blog
  url: https://theclinician.com/#insights
- group: operate
  title: ''
  type: Support
  url: https://theclinician.com/#contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theclinician
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theclinician.com/#/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theclinician.com/#/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/12125971
- group: auth
  title: ''
  type: Security
  url: https://theclinician.com/security/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/the-clinician-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-clinician-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-clinician-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-clinician-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-clinician-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/the-clinician-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-clinician-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/the-clinician-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-clinician-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/the-clinician-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-clinician-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: The Clinician markets an "API-driven architecture" and an "OMOP Clinical Events API" on theclinician.com but serves no developer portal, no API reference and no contract of any kind — /docs, /developers, /api, /developer, /openapi.json, /swagger.json and /api-docs all return 404, the sitemap lists only the homepage, five /insights articles and the disclosure policy, and every integration call to action is "Book a demo" or "Request the security pack".
  evidence:
  - status: 404
    url: https://theclinician.com/developers
  - status: 404
    url: https://theclinician.com/openapi.json
  - status: 200
    url: https://theclinician.com/sitemap.xml
  - status: 200
    url: https://theclinician.com/.well-known/security.txt
  reason: sales-gate
  state: gated
created: '2026-09-02'
description: The Clinician is a New Zealand-headquartered digital health company whose product, The Clinician Platform (TCP, formerly ZEDOC), is an outcomes-intelligence layer for value-based healthcare. TCP captures patient-reported outcome and experience measures (PROMs, PREMs, CROMs) omnichannel over SMS, email, web and native mobile in 20+ languages, scores and benchmarks them automatically against MCID thresholds, runs configurable digital care pathways with a threshold-triggered alert engine, and returns outcomes to the EMR via FHIR. It sits alongside an EMR/PAS rather than replacing it, and the company markets an API-driven architecture aligned with HL7 FHIR (incl. SMART-on-FHIR), HL7 v2.x, openEHR and DICOM, plus an OMOP Clinical Events API. No public API reference, developer portal or machine-readable contract is published — API access runs through an enterprise sales engagement.
image: https://theclinician.com/og-image.png
layout: provider
modified: '2026-09-02'
name: The Clinician
nav: Providers
network: true
overview: 'The Clinician is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Patient Reported Outcomes, and PROMs.


  The Clinician''s developer surface includes engineering blog, support, authentication, and 16 more developer resources.'
plans:
- name: The Clinician Plans Pricing
  plan_count: 0
  slug: the-clinician-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: The Clinician Rate Limits
  slug: the-clinician-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: The Clinician Authentication
  slug: the-clinician-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: The Clinician Domain Security
  slug: the-clinician-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: The Clinician Vulnerability Disclosure
  slug: the-clinician-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: the-clinician
tags:
- Company
- Healthcare
- Health IT
- Patient Reported Outcomes
- PROMs
- Value-Based Care
- Clinical Data
- Interoperability
- FHIR
- openEHR
- Digital Health
- New Zealand
website: https://theclinician.com/
---
