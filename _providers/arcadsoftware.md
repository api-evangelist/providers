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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/arcadsoftware/security/arcadsoftware-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arcadsoftware-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arcadsoftware/well-known/arcadsoftware-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcadsoftware-security.txt
- group: auth
  href: https://artifacts.apis.io/arcadsoftware/well-known/arcadsoftware-arcadsoftware-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcadsoftware-arcadsoftware-security.txt
- group: agent
  href: https://artifacts.apis.io/arcadsoftware/well-known/arcadsoftware-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcadsoftware-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcadsoftware/hosts/arcadsoftware-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcadsoftware-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcadsoftware/vendors/arcadsoftware-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcadsoftware-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arcadsoftware.com/privacy-policy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.arcadsoftware.com
- group: auth
  href: https://artifacts.apis.io/arcadsoftware/security/arcadsoftware-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcadsoftware-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arcadsoftware/security/arcadsoftware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcadsoftware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arcadsoftware.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://email.arcadsoftware.com/mcp
  - status: 403
    url: https://info.arcadsoftware.com/mcp
  - status: 200
    url: https://arcadsoftware.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: ARCAD Software provides enterprise content management and digital transformation solutions, enabling organizations to manage documents, workflows, and data across on-premises and cloud environments. Their platform offers robust features such as document capture, indexing, secure storage, collaborative editing, and integration with third‑party systems. ARCAD focuses on delivering scalable, compliant, and user‑friendly tools for sectors like healthcare, finance, and public administration, helping clients improve efficiency, reduce operational costs, and meet regulatory requirements.
image: https://www.arcadsoftware.com/wp-content/uploads/2025/09/arcad-software-logo-270.png
layout: provider
modified: '2026-10-20'
name: ARCAD Software
nav: Providers
network: true
overview: ARCAD Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise-Content-Management, Digital-Transformation, IBM-i, and DevOps.
random_paper: 14
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arcadsoftware Domain Security
  slug: arcadsoftware-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Arcadsoftware Vulnerability Disclosure
  slug: arcadsoftware-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arcadsoftware
tags:
- Company
- Enterprise-Content-Management
- Digital-Transformation
- IBM-i
- DevOps
website: https://www.arcadsoftware.com/
---
