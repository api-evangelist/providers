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
- group: other
  href: https://artifacts.apis.io/murj/vendors/murj-vendors.yml
  title: ''
  type: Vendors
  url: vendors/murj-vendors.yml
- group: auth
  title: ''
  type: Compliance
  url: https://murj.com/security/
- group: agent
  href: https://artifacts.apis.io/murj/llms/murj-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/murj-llms.txt
- group: auth
  href: https://artifacts.apis.io/murj/well-known/murj-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/murj-help-security.txt
- group: agent
  href: https://artifacts.apis.io/murj/well-known/murj-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/murj-well-known.yml
- group: other
  href: https://artifacts.apis.io/murj/hosts/murj-hosts.yml
  title: ''
  type: Hosts
  url: hosts/murj-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://murj.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://help.murj.com/en/
- group: auth
  title: ''
  type: Security
  url: https://murj.com/security/
- group: company
  title: ''
  type: Blog
  url: https://murj.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.murj.com/
- group: auth
  href: https://artifacts.apis.io/murj/security/murj-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/murj-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/murj/security/murj-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/murj-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://murj.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://help.murj.com/mcp
  - status: 200
    url: https://murj.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Murj provides a suite of software solutions for cardiology practices, including a CIED management platform, integrated heart‑failure monitoring, ambulatory cardiac monitoring, remote patient monitoring, pulmonary artery pressure monitoring, and clinical services. The products are designed to help clinics manage cardiac devices and patient data, streamline workflows, and improve care delivery.
layout: provider
modified: '2026-10-24'
name: Murj
nav: Providers
network: true
overview: 'Murj is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cardiac Device Management, Remote Patient Monitoring, Heart Failure Monitoring, Ambulatory Cardiac Monitoring, and Pulmonary Artery Pressure Monitoring.


  Murj''s developer surface includes support, engineering blog, documentation, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Murj Domain Security
  slug: murj-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Murj Trust Center
  slug: murj-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: murj
tags:
- Cardiac Device Management
- Remote Patient Monitoring
- Heart Failure Monitoring
- Ambulatory Cardiac Monitoring
- Pulmonary Artery Pressure Monitoring
- Clinical Services
website: https://murj.com
---
