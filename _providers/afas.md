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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/afas/well-known/afas-afas-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/afas-afas-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.afas.nl/portal-bedrijfspagina/responsible-disclosure
- group: auth
  href: https://artifacts.apis.io/afas/well-known/afas-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/afas-www-security.txt
- group: auth
  href: https://artifacts.apis.io/afas/well-known/afas-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/afas-security.txt
- group: agent
  href: https://artifacts.apis.io/afas/well-known/afas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afas-well-known.yml
- group: other
  href: https://artifacts.apis.io/afas/hosts/afas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afas-hosts.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.afas.nl/roadmap
- group: company
  title: ''
  type: Newsroom
  url: https://www.afas.nl/media-pers/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.afas.nl/blog
- group: start
  href: https://artifacts.apis.io/afas/help/NL/SE/Inv_Setup_EInv_SetPref.htm
  title: ''
  type: GettingStarted
  url: /help/NL/SE/Inv_Setup_EInv_SetPref.htm
- group: docs
  title: ''
  type: Documentation
  url: https://help.afas.nl/
- group: auth
  href: https://artifacts.apis.io/afas/security/afas-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/afas-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/afas/security/afas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afas.nl/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://afas.nl/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: AFAS Software provides enterprise software solutions for HR, payroll, finance, and ERP, serving over 14,000 organizations in the Netherlands and beyond. Their platform integrates various business processes into a single system, enabling companies to streamline operations, improve employee satisfaction, and focus on core activities. AFAS emphasizes a unified approach to managing HR, finance, CRM, and project management, delivering cloud‑based and on‑premise options tailored to diverse business needs.
image: https://www.afas.nl/portal-product/afas-software-inspireert-beter-ondernemen/social%20media.jpg
layout: provider
modified: '2026-10-27'
name: AFAS Software
nav: Providers
network: true
overview: 'AFAS Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR, Payroll, ERP, and Software.


  AFAS Software''s developer surface includes engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afas Domain Security
  slug: afas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Afas Vulnerability Disclosure
  slug: afas-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: afas
tags:
- Company
- HR
- Payroll
- ERP
- Software
- Netherlands
website: https://afas.nl/
---
