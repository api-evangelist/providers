---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: The ONC-certified § 170.315(g)(10) Standardized API for Patient and Population Services. A HL7 FHIR R4 (4.0.1) RESTful server conforming to the US Core Implementation Guide v3.1.1, exposing 24 resourc
  name: Carefluence Open API R4
  slug: openapi-r4
- description: The first-party OpenID Connect / OAuth 2.0 authorization server that issues every token the Carefluence Open API R4 accepts, and the administration portal where developers register applications and re
  name: Carefluence SMART on FHIR Authorization Server
  slug: authorization-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carefluence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carefluence.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.carefluence.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.carefluence.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.carefluence.com/
- group: build
  title: ''
  type: Postman
  url: https://api.carefluence.com/
- group: operate
  title: ''
  type: Support
  url: https://carefluence.com/reach-us/
- group: company
  title: ''
  type: Blog
  url: https://carefluence.com/news-blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://carefluence.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://carefluence.com/onc-certification/
- group: start
  title: ''
  type: SignUp
  url: https://core.carefluence.com/cf.admin.core/Account/RegisterDeveloper
- group: start
  title: ''
  type: Login
  url: https://core.carefluence.com/cf.admin.core/Account/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carefluence.com/openapi-terms-conditions/
- group: auth
  title: ''
  type: Compliance
  url: https://carefluence.com/onc-certification/
- group: auth
  title: ''
  type: Certification
  url: https://chpl.healthit.gov/#/listing/10922
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carefluence/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/carefluence
- group: auth
  title: ''
  type: Authentication
  url: authentication/carefluence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/carefluence-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carefluence-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carefluence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carefluence-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carefluence-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/carefluence-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/carefluence-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/carefluence-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carefluence-well-known.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/carefluence-openapi-r4-capabilitystatement.json
- group: design
  title: ''
  type: Components
  url: components/carefluence-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/carefluence-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/carefluence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carefluence-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carefluence-llms.txt
created: '2026-09-02'
description: Carefluence is a US health-IT interoperability vendor whose product is an ONC-certified, FHIR-based Open API platform that EHR, telehealth, remote patient monitoring, HIE and health-analytics vendors license to reach regulatory compliance and to exchange clinical data with other systems. The Carefluence Open API R4 was certified on 2022-06-29 under CHPL ID 15.04.04.2657.Care.R4.01.0.220629 against ONC criteria 170.315 (d)(1,3,9-10,12-13) and (g)(4-7,9-10), including the § 170.315(g)(10) Standardized API for Patient and Population Services; the company states it was the first FHIR-based Open API product to earn ONC 2015 Edition certification, in July 2016, and was an early participant in the Argonaut Project. The platform is a FHIR R4 server (US Core IG v3.1.1, 24 resource types) fronted by a first-party SMART on FHIR OAuth 2.0 / OpenID Connect authorization server, with a data translator for HL7 v2 and C-CDA normalization, adapters for non-FHIR back ends, a built-in integration
  engine, an asynchronous FHIRops product, and an announced Model Context Protocol server for AI agents.
image: https://carefluence.com/wp-content/uploads/2018/04/Logo-WHT-nds1740.png
layout: provider
modified: '2026-09-02'
name: Carefluence
nav: Providers
network: true
overview: 'Carefluence publishes 1 API on the [APIs.io](https://apis.io/) network: Open API R4. Tagged areas include Company, Healthcare, Interoperability, FHIR, and HL7.


  Carefluence''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Carefluence Plans Pricing
  plan_count: 0
  slug: carefluence-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Carefluence Rate Limits
  slug: carefluence-rate-limits
scopes:
- name: Carefluence Scopes
  scope_count: 51
  slug: carefluence-scopes
  summary_line: 51 scopes
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 40.9
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 47.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 61.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Carefluence Authentication
  slug: carefluence-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Carefluence Domain Security
  slug: carefluence-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carefluence
tags:
- Company
- Healthcare
- Interoperability
- FHIR
- HL7
- SMART on FHIR
- Electronic Health Records
- Clinical Data
- Health IT
- ONC Certified
- USCDI
- OAuth 2.0
- Telehealth
- Health Information Exchange
website: https://carefluence.com/
---
