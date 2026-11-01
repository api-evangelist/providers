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
    event_surface_described: unknown
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
  score: 10.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/stitch-data/plans/stitch-data-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stitch-data-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/stitch-data/changelog/stitch-data-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stitch-data-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.qlik.com/
- group: design
  href: https://artifacts.apis.io/stitch-data/conformance/stitch-data-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stitch-data-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stitch-data/well-known/stitch-data-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stitch-data-status-security.txt
- group: agent
  href: https://artifacts.apis.io/stitch-data/well-known/stitch-data-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stitch-data-well-known.yml
- group: other
  href: https://artifacts.apis.io/stitch-data/hosts/stitch-data-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stitch-data-hosts.yml
- group: other
  href: https://artifacts.apis.io/stitch-data/vendors/stitch-data-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stitch-data-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.stitchdata.com/integrations/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stitchdata.com/terms-of-use-october-2018-update/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stitchdata.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.stitchdata.com/signup/
- group: auth
  title: ''
  type: Security
  url: https://www.stitchdata.com/platform/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stitchdata.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stitchdata.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.stitchdata.com/company/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stitchdata
- group: docs
  title: ''
  type: Documentation
  url: https://www.stitchdata.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.stitchdata.com/docs/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stitchdata.com/docs/getting-started/basic-concepts-system-overview
- group: auth
  href: https://artifacts.apis.io/stitch-data/security/stitch-data-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stitch-data-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/stitch-data/security/stitch-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stitch-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stitchdata.com/
coverage:
  checked: '2026-10-26'
  detail: Documentation is provided as HTML pages without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.stitchdata.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Stitch Data provides a cloud-first, fully managed data integration platform that enables businesses to quickly replicate data from a wide variety of sources into data warehouses and lakes. As a Talend product, Stitch offers simple, scalable ELT pipelines, automated schema handling, and robust security, helping organizations accelerate analytics and data-driven decision making.
layout: provider
modified: '2026-10-26'
name: Stitch Data
nav: Providers
network: true
overview: 'Stitch Data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include data integration, ETL, data pipelines, cloud data, and data warehouse.


  Stitch Data''s developer surface includes changelog, signup flow, pricing, documentation, getting-started guide, and 18 more developer resources.'
plans:
- name: Stitch Data Plans Pricing
  plan_count: 3
  slug: stitch-data-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 46.4
    operational_transparency: 55.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stitch Data Domain Security
  slug: stitch-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stitch Data Trust Center
  slug: stitch-data-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP
slug: stitch-data
tags:
- data integration
- ETL
- data pipelines
- cloud data
- data warehouse
- data lake
website: https://www.stitchdata.com/
---
