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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/srv-us/hosts/srv-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/srv-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/srv-us/vendors/srv-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/srv-us-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.srv.us/
- group: auth
  href: https://artifacts.apis.io/srv-us/security/srv-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/srv-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://srv.us/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages exist but provide no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract files.
  evidence:
  - status: 200
    url: https://docs.srv.us/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: srv-us provides a platform for exposing local services over TLS online, enabling developers to securely share services without complex networking. The service offers simple SSH tunneling, automated certificate management, and integrates with various development tools. It targets developers needing quick, secure exposure of local applications for testing, demos, or collaboration, emphasizing ease of use and robust security.
layout: provider
modified: '2026-10-29'
name: srv-us
nav: Providers
network: true
overview: 'srv-us is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Platform, TLS, SSH, DeveloperTools, and OpenSource.


  srv-us'' developer surface includes documentation and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Srv Us Domain Security
  slug: srv-us-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: srv-us
tags:
- Platform
- TLS
- SSH
- DeveloperTools
- OpenSource
- Company
website: https://srv.us/
---
