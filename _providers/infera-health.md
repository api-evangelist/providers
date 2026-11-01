---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 16.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/infera-health/vendors/infera-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infera-health-vendors.yml
- group: agent
  href: https://artifacts.apis.io/infera-health/llms/infera-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infera-health-llms.txt
- group: agent
  href: https://artifacts.apis.io/infera-health/well-known/infera-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/infera-health-well-known.yml
- group: other
  href: https://artifacts.apis.io/infera-health/hosts/infera-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infera-health-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infera.com/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infera.com/docs/privacy
- group: company
  title: ''
  type: Blog
  url: https://infera.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inferahealth.com/
- group: auth
  href: https://artifacts.apis.io/infera-health/security/infera-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infera-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inferahealth.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://inferahealth.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Infera offers an AI‑driven compliance platform for medical device manufacturers. The software connects existing engineering tools such as Jira, GitHub, and CAD to automatically import, trace, and manage requirements, risk analyses, verification protocols, release records, and document control within a single living record. It supports standards including ISO 13485, ISO 14971, IEC 62304, FDA QMS, and EU MDR/IVDR for teams ranging from startups to enterprises.
image: https://infera.com/logo_li.png
layout: provider
modified: '2026-10-24'
name: Infera Health
nav: Providers
network: true
overview: 'Infera Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Medical Devices, AI, Software, and Risk Management.


  Infera Health''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Infera Health Domain Security
  slug: infera-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: infera-health
tags:
- Compliance
- Medical Devices
- AI
- Software
- Risk Management
- Verification
- Release Management
- Document Control
website: https://inferahealth.com/
---
