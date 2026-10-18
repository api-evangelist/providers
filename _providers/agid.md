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
    error_semantics: derived
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
  score: 16.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: SOAP interface definitions published by AgID for the exchange of protocolled electronic administrative documents between Areas of Homogeneous Organization (AOO mittente / AOO destinataria), part of Ag
  name: AgID Protocollo Comunicazione AOO (SOAP interface)
  slug: protocollo-comunicazione-aoo
artifact_total: 7
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/rules/agid-dati-semantic-schema-editor-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/agid-dati-semantic-schema-editor-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/conventions/agid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agid-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/lifecycle/agid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agid-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/errors/agid-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/agid-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/conformance/agid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agid-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/well-known/agid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agid-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/well-known/agid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agid-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/hosts/agid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/vendors/agid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agid-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.agid.gov.it/en/intervention-areas/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.agid.gov.it/en/news/pdnd-guidelines-update
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/security/agid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agid-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/security/agid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agid.gov.it/it
- group: docs
  title: ''
  type: Guidelines
  url: https://www.agid.gov.it/it/linee-guida
- group: company
  title: ''
  type: Blog
  url: https://www.agid.gov.it/it/stampa-e-comunicazione
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgID
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agid.gov.it/it/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agid.gov.it/it/note-legali
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AgidGov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agenzia-italia-digitale
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCxJmOWf__YcLgB19gy5dGQQ
- group: build
  title: ''
  type: Tools
  url: https://italia.github.io/api-oas-checker/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/teamdigitale/dati-semantic-schema-editor/blob/80bf9d6cfd2dc9b146401e990972a2a0d1943198/.spectral/rulesets/.openapirc.yml
created: '2026-10-09'
description: AgID (Agenzia per l'Italia Digitale) is the Italian government agency for digital innovation in the public administration, describing itself as "innovazione al servizio della PA e dei cittadini. Regolamentazione e certificazioni digitali." It publishes national technical guidelines (Linee Guida), oversees accessibility, open data and open-source reuse, and maintains public repositories under the AgID GitHub organization. It surfaced via the API Evangelist harvest backlog through a Spectral ruleset for Italian OpenAPI guidelines (the Italian OpenAPI Checker).
image: https://www.agid.gov.it/sites/agid/files/2024-04/logo-agid.svg
layout: provider
modified: '2026-10-09'
name: AgID (Agenzia per l'Italia Digitale)
nav: Providers
network: true
overview: 'AgID (Agenzia per l''Italia Digitale) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Public Sector, Italy, and Digital Transformation.


  The AgID (Agenzia per l''Italia Digitale) catalog on APIs.io includes 1 Spectral governance ruleset.


  AgID (Agenzia per l''Italia Digitale)''s developer surface includes engineering blog, YouTube channel, tooling, and 21 more developer resources.'
plans:
- name: Agid Plans Pricing
  plan_count: 0
  slug: agid-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Agid Rate Limits
  slug: agid-rate-limits
rules:
- authorship: provider
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: AgID (Agenzia per l'Italia Digitale) — dati semantic schema editor rules
  rule_count: 50
  severity_counts:
    error: 23
    hint: 11
    info: 4
    warn: 12
  slug: agid-dati-semantic-schema-editor-spectral-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.0
    catalog_earned_first_party: 18.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.0
  facets:
    access_clarity: 21.1
    contract_governance: 59.1
    contract_quality: 24.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 21.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/agid/refs/heads/main/screenshots/agid-2026-10-11T135820.png
security:
- kind: authentication
  name: Agid Authentication
  slug: agid-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agid Domain Security
  slug: agid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agid Vulnerability Disclosure
  slug: agid-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agid
tags:
- Company
- Government
- Public Sector
- Italy
- Digital Transformation
- Guidelines
- Spectral
website: https://www.agid.gov.it/it
---
