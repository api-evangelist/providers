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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.air.security/
- group: agent
  href: https://artifacts.apis.io/air/llms/air-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/air-llms.txt
- group: agent
  href: https://artifacts.apis.io/air/well-known/air-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/air-well-known.yml
- group: other
  href: https://artifacts.apis.io/air/hosts/air-hosts.yml
  title: ''
  type: Hosts
  url: hosts/air-hosts.yml
- group: other
  href: https://artifacts.apis.io/air/vendors/air-vendors.yml
  title: ''
  type: Vendors
  url: vendors/air-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.air.security/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.air.security/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.air.security/blog
- group: auth
  href: https://artifacts.apis.io/air/security/air-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/air-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/air/security/air-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/air-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.air.security/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.air.security/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: AIR is a technology company focused on providing secure, scalable, and intelligent cloud-based solutions for enterprise data management and analytics. Backed by Sequoia Capital, AIR leverages cutting‑edge AI and security technologies to help organizations streamline operations, ensure compliance, and unlock insights from their data assets. The company offers a suite of APIs for data ingestion, processing, storage, and visualization, targeting sectors such as finance, healthcare, and logistics. With a commitment to privacy and robust security, AIR aims to be a trusted partner for businesses seeking to modernize their data infrastructure and accelerate digital transformation.
image: https://cdn.prod.website-files.com/6a1557357aace3d4dbe73ca3/6a70a3e27f026e4579411005_a7e3040688d8615fef689d580611dc83_Open%20Graph.jpg
layout: provider
modified: '2026-10-23'
name: AIR
nav: Providers
network: true
overview: 'AIR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Cloud, AI, and Security.


  AIR''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Air Domain Security
  slug: air-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Air Trust Center
  slug: air-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: air
tags:
- Company
- Data
- Cloud
- AI
- Security
website: https://www.air.security/
---
