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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Public API for Dataedo allowing integration with Dataedo portal, requires authorization token and appropriate license.
  name: Dataedo Public API
  slug: dataedo-public-api
- description: The Public API from Dataedo — 4 operation(s) for public.
  name: Dataedo Public API
  slug: dataedo-public-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/plans/dataedo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataedo-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/rules/dataedo-rules.yml
  title: ''
  type: Spectral
  url: rules/dataedo-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/changelog/dataedo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dataedo-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dataedo.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/conformance/dataedo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataedo-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/well-known/dataedo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataedo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/hosts/dataedo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataedo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/vendors/dataedo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataedo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataedo.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://dataedo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataedo.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/security/dataedo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dataedo-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dataedo/refs/heads/main/security/dataedo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataedo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataedo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dataedo.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dataedo.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dataedo.com/get-started/
- group: company
  title: ''
  type: Blog
  url: https://dataedo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dataedo.com/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.dataedo.com
- group: operate
  title: ''
  type: Support
  url: https://dataedo.com/add-ticket
coverage:
  checked: '2026-10-13'
  detail: Public API requires an authorization token and appropriate license, blocking unauthenticated access.
  evidence:
  - status: 200
    url: https://docs.dataedo.com/api
  reason: sales-gate
  state: gated
created: '2026-10-13'
description: Dataedo provides a comprehensive data governance and data quality platform for mid-size organizations. It offers a centralized AI‑ready data catalog, data lineage visualization, data quality rules, and governance tools to help businesses discover, organize, and trust their data. Features include metadata scanning, AI governance, compliance readiness, and extensive connector support for SQL Server, Snowflake, Power BI, Tableau, and more, enabling efficient data management and compliance.
image: https://strapi.dataedo.com:443/uploads/data_governance_1_ee46917a87.png
layout: provider
modified: '2026-10-13'
name: Dataedo
nav: Providers
network: true
overview: 'Dataedo is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Public API, and 1 more. Tagged areas include Data Governance, Data Quality, Metadata Management, Data Catalog, and Business Intelligence.


  The Dataedo catalog on APIs.io includes 1 Spectral governance ruleset.


  Dataedo''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, support, and 14 more developer resources.'
plans:
- name: Dataedo Plans Pricing
  plan_count: 3
  slug: dataedo-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Dataedo API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dataedo-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Dataedo Domain Security
  slug: dataedo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dataedo Trust Center
  slug: dataedo-trust-center
  summary_line: ISO 27001, GDPR
slug: dataedo
tags:
- Data Governance
- Data Quality
- Metadata Management
- Data Catalog
- Business Intelligence
website: https://dataedo.com
---
