---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-09-25'
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
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/security/carefluence-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/authentication/carefluence-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carefluence-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/scopes/carefluence-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/carefluence-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/conformance/carefluence-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carefluence-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/errors/carefluence-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carefluence-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/lifecycle/carefluence-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/carefluence-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/conventions/carefluence-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carefluence-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/data-model/carefluence-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carefluence-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/packages/carefluence-packages.yml
  title: ''
  type: Packages
  url: packages/carefluence-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/packages/carefluence-packages.yml
  title: ''
  type: SDKs
  url: packages/carefluence-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/well-known/carefluence-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carefluence-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/fhir/carefluence-openapi-r4-capabilitystatement.json
  title: ''
  type: CapabilityStatement
  url: fhir/carefluence-openapi-r4-capabilitystatement.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/components/carefluence-components.yml
  title: ''
  type: Components
  url: components/carefluence-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/sandbox/carefluence-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/carefluence-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/plans/carefluence-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carefluence-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/rate-limits/carefluence-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/carefluence-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carefluence/refs/heads/main/llms/carefluence-llms.txt
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
overview: 'Carefluence publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Open API R4, and 1 more. Tagged areas include Company, Healthcare, Interoperability, FHIR, and HL7.


  Carefluence''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Carefluence Plans Pricing
  plan_count: 0
  slug: carefluence-plans-pricing
random_paper: 5
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
  composite: 44.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 38.7
    developer_ergonomics: 66.1
    discoverability: 66.1
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
    score: 38.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- Authentication
- Telehealth
- Health Information Exchange
website: https://carefluence.com/
---
