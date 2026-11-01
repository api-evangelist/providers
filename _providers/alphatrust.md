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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/alphatrust/hosts/alphatrust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphatrust-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphatrust/vendors/alphatrust-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphatrust-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.alphatrust.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.alphatrust.com/release-notes
- group: auth
  href: https://artifacts.apis.io/alphatrust/security/alphatrust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphatrust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphatrust.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alphatrust.com/documentation/overview/product-overview
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.alphatrust.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.alphatrust.com/learn
- group: operate
  title: ''
  type: Support
  url: https://www.alphatrust.com/learn/services-support
- group: company
  title: ''
  type: Blog
  url: https://www.alphatrust.com/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alphatrust.com/getting-started/system-requirements/hardware-requirements
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 0
    url: https://api.alphatrust.com/openapi.json
  - status: 403
    url: https://api-reference.alphatrust.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: AlphaTrust provides a flexible and extensible electronic signature and document process automation solution. Their platform enables legally enforceable e-signatures, customizable workflows, and brandable user experiences. Established since 1998, AlphaTrust offers comprehensive API documentation, installation guides, and release notes to support integration across enterprises.
layout: provider
modified: '2026-10-19'
name: AlphaTrust
nav: Providers
network: true
overview: 'AlphaTrust is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Signature, Document Automation, and Enterprise.


  AlphaTrust''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 5 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 35.7
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alphatrust Domain Security
  slug: alphatrust-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alphatrust
tags:
- Company
- E-Signature
- Document Automation
- Enterprise
website: https://alphatrust.com/
---
