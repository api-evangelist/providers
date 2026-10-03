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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: GraphQL API for Avelios platform
  name: Avelios GraphQL API
  slug: avelios-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avelios/refs/heads/main/llms/avelios-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avelios-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avelios/refs/heads/main/well-known/avelios-customer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avelios-customer-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avelios/refs/heads/main/well-known/avelios-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avelios-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avelios/refs/heads/main/hosts/avelios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avelios-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avelios/refs/heads/main/vendors/avelios-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avelios-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.avelios.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avelios/refs/heads/main/security/avelios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avelios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avelios.com/en
- group: operate
  title: ''
  type: Support
  url: https://www.avelios.com/en/contact
- group: company
  title: ''
  type: Blog
  url: https://www.avelios.com/en/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avelios.com/en/imprint
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avelios.com/en/data-protection
created: '2026-09-26'
description: Avelios Medical provides a modular, data‑driven clinic platform that integrates digital treatment documentation, AI‑powered analytics, and automated administrative processes. Their operating system enables intelligent patient care across hospitals and clinics, offering SaaS solutions for digital infrastructure, treatment planning, and big‑data research. Founded to transform healthcare delivery, Avelios combines innovative software with a focus on data security and regulatory compliance, serving the European market and expanding globally.
layout: provider
modified: '2026-09-26'
name: Avelios
nav: Providers
network: true
overview: 'Avelios publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Software-as-a-Service, Digital Health, and Artificial Intelligence.


  Avelios'' developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 69.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avelios Domain Security
  slug: avelios-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: avelios
tags:
- Company
- Healthcare
- Software-as-a-Service
- Digital Health
- Artificial Intelligence
- Europe
website: https://www.avelios.com/en
---
