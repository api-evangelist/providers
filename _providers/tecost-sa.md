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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.tecost.ch/
- group: company
  title: ''
  type: Blog
  url: https://www.tecost.ch/fr/actualites
- group: operate
  title: ''
  type: Support
  url: https://www.tecost.ch/fr/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tecost.ch/fr/protection-des-donnees
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tecost-sa
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tecost-sa-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tecost-sa-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tecost-sa-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/tecost-sa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tecost-sa-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: Tecost markets an openEHR-based Data Integration Hub plus HL7 and SOAP integration for the Carefolio suite, but every Carefolio host is customer-only — www.carefolio.ch answers nginx 403 to anonymous requests and tenant hosts such as daler.carefolio.ch redirect to a Microsoft Entra ID SAML sign-in — so no reference, WSDL or openEHR artifact is reachable without an active institutional tenant.
  evidence:
  - status: 403
    url: https://www.carefolio.ch/
  - status: 200
    url: https://daler.carefolio.ch/
  - status: 403
    url: https://www.tecost.ch/.well-known/security.txt
  - status: 404
    url: https://www.tecost.ch/openapi.json
  - status: 404
    url: https://www.carefolio.ch/rest/openehr/v1/definition/template/adl1.4
  reason: customer-only-docs
  state: gated
created: '2026-09-02'
description: Tecost SA is a Swiss health-information-technology company, founded in 1997 and based in Fribourg, that designs, develops, implements, hosts and operates clinical information systems for hospitals, clinics, psychiatric and rehabilitation institutions, long-term care facilities and home-care organizations across French- and German-speaking Switzerland. Its product line is the Carefolio suite — Acute, Rehabilitation, Psy, LongTerm, AtHome, Critical Care 3C, Network, Portal, Workshop, AI and the openEHR-based Carefolio DIH Data Integration Hub — alongside consulting, change management, custom development, 24/7 maintenance and SaaS operations. Tecost is a named industry partner of the openEHR Foundation and states that it is making openEHR the cornerstone of its clinical-data interoperability. It publishes no public developer portal, API reference or machine-readable contract; Carefolio is delivered as per-customer tenants behind Microsoft Entra ID single sign-on, so any integration
  contract reaches integrators under a commercial agreement rather than through a public surface.
image: https://www.tecost.ch/images/logo-tecost.svg
layout: provider
modified: '2026-09-02'
name: Tecost SA
nav: Providers
network: true
overview: 'Tecost SA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Electronic Health Records, and Clinical Information Systems.


  Tecost SA''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Tecost Sa Plans Pricing
  plan_count: 0
  slug: tecost-sa-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Tecost Sa Rate Limits
  slug: tecost-sa-rate-limits
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 8.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Tecost Sa Domain Security
  slug: tecost-sa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tecost-sa
tags:
- Company
- Health
- Healthcare
- Electronic Health Records
- Clinical Information Systems
- openEHR
- Interoperability
- Hospital Software
- Long-Term Care
- Home Care
- Switzerland
website: https://www.tecost.ch/
---
