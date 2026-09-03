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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The HPZone GraphQL API exposes read access to the HPZone communicable-disease control record — cases, contacts, situations, enquiries, actions and contexts — over a single POST endpoint. Access is by '
  name: HPZone API
  slug: infact-hpzone-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infact.solutions/
- group: operate
  title: ''
  type: Support
  url: https://infact.solutions/contact-us/
- group: auth
  title: ''
  type: Authentication
  url: authentication/infact-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/infact-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infact-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infact-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/infact-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infact-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infact-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/infact-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infact-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infact-llms.txt
created: '2026-09-02'
description: 'InFact (InFact UK Ltd, trading as Infact — Solutions in public health) builds software for communicable-disease control and public-health service delivery. Founded in 2003 by Dr Chakib Kara-Zaitri and Bob Hamilton, the company''s flagship product HPZone is an integrated suite for infectious-disease control built on two decades of frontline work with the national health services of the United Kingdom and the Netherlands: HPCore for case, contact and outbreak management with decision-support protocols and enquiry handling, EpiQ for epidemiological questionnaires, and HPInsight for surveillance dashboards, reporting and modelling. A second product line, Ampara (the successor to SHDirect), covers the clinic patient journey from triage through consultation, diagnostics, prescribing and follow-up. InFact is a Silver Industry Partner of openEHR International. HPZone exposes a credential-gated GraphQL API over cases, contacts, situations, enquiries, actions and contexts; the API exists
  and is in production use by national public-health bodies, but InFact publishes no public developer portal, reference or machine-readable contract.'
layout: provider
modified: '2026-09-02'
name: InFact
nav: Providers
network: true
overview: 'InFact publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Public Health, Healthcare, and Epidemiology.


  InFact''s developer surface includes support, authentication, and 11 more developer resources.'
plans:
- name: Infact Plans Pricing
  plan_count: 0
  slug: infact-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Infact Rate Limits
  slug: infact-rate-limits
scopes:
- name: Infact Scopes
  scope_count: 0
  slug: infact-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.6
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
- kind: authentication
  name: Infact Authentication
  slug: infact-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Infact Domain Security
  slug: infact-domain-security
  summary_line: TLSv1.3 · DMARC
slug: infact
tags:
- Company
- Health
- Public Health
- Healthcare
- Epidemiology
- Disease Surveillance
- Outbreak Management
- Contact Tracing
- Electronic Health Records
- openEHR
- GraphQL
- Government
website: https://infact.solutions/
---
