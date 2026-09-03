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
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: 'mConsole is CODE24''s modern EPD (electronic health record). CODE24 states that the record has a software interface (API) with which other care systems can read and write care data back into mConsole, '
  name: mConsole EPD API
  slug: mconsole-epd-api
- description: Connect24 is CODE24's data-transformation service. CODE24 documents it as using a FHIR REST API for reading and writing information, collecting and transforming patient health data in line with the Du
  name: Connect24 FHIR API
  slug: connect24-fhir-api
- description: Router24 is CODE24's DVA (dienstverlener zorgaanbieders) solution under the Dutch MedMij afsprakenstelsel. CODE24 states that Router24 fulfils both the authentication role and the resource-server role
  name: Router24 MedMij DVA
  slug: router24-medmij-dva
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/code24-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.code24.nl/
- group: docs
  title: ''
  type: Documentation
  url: https://www.code24.nl/epd-koppelingen-en-integraties
- group: operate
  title: ''
  type: Support
  url: https://support.code24.nl
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.code24.nl
- group: start
  title: ''
  type: Login
  url: https://klanten.code24.nl
- group: company
  title: ''
  type: Blog
  url: https://blog.code24.nl
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/code24-nl
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.code24.nl/privacyverklaring
- group: auth
  title: ''
  type: Security
  url: https://www.code24.nl/kwetsbaarheid-melden
- group: operate
  title: ''
  type: Contact
  url: https://www.code24.nl/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.code24.nl/faq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/code24/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/code24-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/code24-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/code24-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/code24-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/code24-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/code24-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/code24-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: CODE24 states plainly that mConsole has a read/write API and that Connect24 is a FHIR REST API, but every reference for them sits behind a customer login — klanten.code24.nl 303-redirects every anonymous request to /login and support.code24.nl lands on an Atlassian Jira Service Management sign-in — while www.code24.nl is a Squarespace marketing site with no developer section and no api./developer./docs. subdomain resolving.
  evidence:
  - status: 303
    url: https://klanten.code24.nl/.well-known/openid-configuration
  - status: 200
    url: https://support.code24.nl/
  - status: 404
    url: https://www.code24.nl/openapi.json
  - status: 200
    url: https://www.code24.nl/epd-koppelingen-en-integraties
  reason: customer-only-docs
  state: gated
created: '2026-09-02'
description: 'CODE24 B.V. is a Dutch healthcare software company in Alkmaar that builds mConsole, a modern, modular electronic health record (EPD) for care and mental-health (GGZ) organisations, together with a family of "24" modules — Lab24, Opname24 (admissions), CrisisMonitor24, CTB24, Connect24, Router24, Dynaform24, Financieel24 and DataWarehouse24. Its architectural position is that a modern EPD must be open: care data is stored in standardised form using openEHR archetypes and Dutch zibs (zorginformatiebouwstenen), and every record is readable and writable through a software interface (API) so other care systems can be integrated without duplicate data entry. Connect24 exposes a FHIR REST API for collecting and transforming patient data to the Dutch MedMij standard; Router24 is a MedMij-qualified DVA that performs the authentication and resource-server roles for routing data to personal health environments (PGOs). CODE24 is also a Value Added Reseller of the Cadasto openEHR open data
  platform. The API surface is real but commercial: no developer portal, no public API reference and no machine-readable contract are published on any CODE24 host.'
image: https://images.squarespace-cdn.com/content/62ac82df30de9f006ca4a9b6/66dbfa59-47b3-4354-8491-fa6de60ac444/CODE24_logo.png
layout: provider
modified: '2026-09-02'
name: Code24
nav: Providers
network: true
overview: 'Code24 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Electronic Health Records, openEHR, and FHIR.


  Code24''s developer surface includes documentation, support, engineering blog, FAQ, and 16 more developer resources.'
plans:
- name: Code24 Plans Pricing
  plan_count: 0
  slug: code24-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Code24 Rate Limits
  slug: code24-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 23.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Code24 Domain Security
  slug: code24-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Code24 Vulnerability Disclosure
  slug: code24-vulnerability-disclosure
  summary_line: contact published
slug: code24
tags:
- Company
- Healthcare
- Electronic Health Records
- openEHR
- FHIR
- MedMij
- Interoperability
- Mental Health
- Netherlands
- Health Data
website: https://www.code24.nl/
---
