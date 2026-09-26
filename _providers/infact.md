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
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'The HPZone GraphQL API exposes read access to the HPZone communicable-disease control record — cases, contacts, situations, enquiries, actions and contexts — over a single POST endpoint. Access is by '
  name: HPZone API
  slug: infact-hpzone-api
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/security/infact-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/authentication/infact-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infact-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/scopes/infact-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/infact-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/conventions/infact-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infact-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/data-model/infact-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infact-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/packages/infact-packages.yml
  title: ''
  type: Packages
  url: packages/infact-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/conformance/infact-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infact-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/lifecycle/infact-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/infact-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/plans/infact-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infact-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/rate-limits/infact-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/infact-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infact/refs/heads/main/llms/infact-llms.txt
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
random_paper: 13
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
  composite: 12.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 14.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
