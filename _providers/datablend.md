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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/datablend/plans/datablend-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datablend-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://datablend.com/security
- group: other
  href: https://artifacts.apis.io/datablend/hosts/datablend-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datablend-hosts.yml
- group: other
  href: https://artifacts.apis.io/datablend/vendors/datablend-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datablend-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://datablend.com/security
- group: docs
  title: ''
  type: Documentation
  url: https://dev.ml.datablend.com/
- group: auth
  href: https://artifacts.apis.io/datablend/security/datablend-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/datablend-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/datablend/security/datablend-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datablend-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datablend/security/datablend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datablend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datablend.com/
- group: operate
  title: ''
  type: Support
  url: https://datablend.com/contact
- group: company
  title: ''
  type: Blog
  url: https://datablend.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://datablend.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datablend.com/privacy-policy
created: '2026-10-20'
description: DataBlend, operating under eOne Solutions, provides an Integration Platform as a Service (iPaaS) enabling seamless data integration, virtualization, and migration across various enterprise systems. Their platform supports connectors for popular applications, offers data flow automation, and emphasizes security and compliance, catering to businesses seeking efficient data management solutions.
layout: provider
modified: '2026-10-20'
name: eOne Solutions
nav: Providers
network: true
overview: 'eOne Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include iPaaS, Data Integration, Data Virtualization, Data Migration, and Enterprise.


  eOne Solutions'' developer surface includes documentation, support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Datablend Plans Pricing
  plan_count: 4
  slug: datablend-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datablend Domain Security
  slug: datablend-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Datablend Vulnerability Disclosure
  slug: datablend-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Datablend Trust Center
  slug: datablend-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: datablend
tags:
- iPaaS
- Data Integration
- Data Virtualization
- Data Migration
- Enterprise
- SaaS
website: https://datablend.com/
---
