---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Peliqan Webhooks
  slug: peliqan-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/peliqan/plans/peliqan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/peliqan-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/peliqan/asyncapi/peliqan-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/peliqan-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/peliqan/authentication/peliqan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/peliqan-authentication.yml
- group: agent
  href: https://artifacts.apis.io/peliqan/llms/peliqan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/peliqan-llms.txt
- group: other
  href: https://artifacts.apis.io/peliqan/a2a/peliqan-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/peliqan-a2a.yml
- group: auth
  href: https://artifacts.apis.io/peliqan/well-known/peliqan-airtable-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/peliqan-airtable-security.txt
- group: agent
  href: https://artifacts.apis.io/peliqan/well-known/peliqan-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/peliqan-well-known.yml
- group: other
  href: https://artifacts.apis.io/peliqan/hosts/peliqan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peliqan-hosts.yml
- group: other
  href: https://artifacts.apis.io/peliqan/vendors/peliqan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/peliqan-vendors.yml
- group: build
  href: https://artifacts.apis.io/peliqan/packages/peliqan-packages.yml
  title: ''
  type: SDKs
  url: packages/peliqan-packages.yml
- group: build
  href: https://artifacts.apis.io/peliqan/packages/peliqan-packages.yml
  title: ''
  type: Packages
  url: packages/peliqan-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://peliqan.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.peliqan.io/
- group: auth
  title: ''
  type: Security
  url: https://peliqan.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://peliqan.io/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://help.peliqan.io/adminpulse-getting-started-in-peliqan
- group: auth
  href: https://artifacts.apis.io/peliqan/security/peliqan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peliqan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peliqan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.peliqan.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://peliqan.io/platform/
- group: commercial
  title: ''
  type: Pricing
  url: https://peliqan.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.eu.peliqan.io/signup
- group: company
  title: ''
  type: Blog
  url: https://peliqan.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.peliqan.io/contact-support
- group: operate
  title: ''
  type: Roadmap
  url: https://help.peliqan.io/feature-list-roadmap-and-architecture
created: '2026-10-21'
description: Peliqan provides an AI‑first data platform that unifies data ingestion, transformation, and reverse‑ETL across 300+ connectors. It offers a governed data warehouse with built‑in SQL, low‑code Python, and AI‑driven query capabilities, enabling secure MCP server access for AI agents. The platform emphasizes security with SOC 2, ISO 27001, and GDPR compliance, targeting enterprises seeking trustworthy, governed data for BI and AI workloads.
image: https://peliqan.io/wp-content/uploads/2026/06/Group-1000008957-1.webp
layout: provider
modified: '2026-10-21'
name: Peliqan
nav: Providers
network: true
overview: 'Peliqan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Platform, AI, ETL, and Reverse ETL.


  The Peliqan catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Peliqan''s developer surface includes authentication, getting-started guide, documentation, pricing, signup flow, engineering blog, support, and 18 more developer resources.'
plans:
- name: Peliqan Plans Pricing
  plan_count: 7
  slug: peliqan-plans-pricing
random_paper: 2
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 48.2
    operational_transparency: 39.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Peliqan Authentication
  slug: peliqan-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Peliqan Domain Security
  slug: peliqan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: peliqan
tags:
- Company
- Data Platform
- AI
- ETL
- Reverse ETL
website: https://peliqan.io/
---
