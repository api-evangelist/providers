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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DBSync provides a data integration and replication platform with a developer portal at https://www.mydbsync.com/developers.
  name: DBSync API
  slug: dbsync-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/mydbsync/vendors/mydbsync-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mydbsync-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/mydbsync/plans/mydbsync-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mydbsync-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mydbsync/conformance/mydbsync-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mydbsync-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mydbsync/llms/mydbsync-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mydbsync-llms.txt
- group: auth
  href: https://artifacts.apis.io/mydbsync/well-known/mydbsync-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mydbsync-calendly-security.txt
- group: agent
  href: https://artifacts.apis.io/mydbsync/well-known/mydbsync-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mydbsync-well-known.yml
- group: other
  href: https://artifacts.apis.io/mydbsync/hosts/mydbsync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mydbsync-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mydbsync.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.mydbsync.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mydbsync.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mydbsync.com/pricing
- group: start
  title: ''
  type: Login
  url: https://engage.mydbsync.com/login/index.php
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.mydbsync.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mydbsync.com/solution/financial-services#collapse-3dad4e06871043c79b01
- group: docs
  title: ''
  type: Documentation
  url: https://dev.mydbsync.com/
- group: auth
  href: https://artifacts.apis.io/mydbsync/security/mydbsync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mydbsync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mydbsync.com/
created: '2026-10-21'
description: DBSync provides a data integration and replication platform enabling real-time bidirectional sync across a wide array of applications and databases. The company offers cloud workflow automation, AI‑agents for intelligent document processing, and SaaS replication solutions for enterprises. Its platform supports Salesforce, QuickBooks, Microsoft Dynamics, Shopify, and many other systems, delivering data accuracy, disaster recovery, and migration capabilities. DBSync serves finance, banking, legal, and IT sectors with robust data warehousing and order‑to‑cash automation.
image: https://www.mydbsync.com/wp-content/uploads/2026/01/data-integration-and-replication.webp
layout: provider
modified: '2026-10-21'
name: DBSync
nav: Providers
network: true
overview: 'DBSync is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, Replication, Cloud Workflow, AI Agents, and Enterprise.


  DBSync''s developer surface includes support, pricing, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Mydbsync Plans Pricing
  plan_count: 3
  slug: mydbsync-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mydbsync Domain Security
  slug: mydbsync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mydbsync
tags:
- Data Integration
- Replication
- Cloud Workflow
- AI Agents
- Enterprise
website: https://mydbsync.com/
---
