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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/unraid/changelog/unraid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/unraid-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://unraid.net/policies
- group: agent
  href: https://artifacts.apis.io/unraid/llms/unraid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unraid-llms.txt
- group: auth
  href: https://artifacts.apis.io/unraid/well-known/unraid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/unraid-security.txt
- group: auth
  href: https://artifacts.apis.io/unraid/well-known/unraid-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/unraid-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/unraid/well-known/unraid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unraid-well-known.yml
- group: other
  href: https://artifacts.apis.io/unraid/hosts/unraid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unraid-hosts.yml
- group: other
  href: https://artifacts.apis.io/unraid/vendors/unraid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unraid-vendors.yml
- group: build
  href: https://artifacts.apis.io/unraid/packages/unraid-packages.yml
  title: ''
  type: SDKs
  url: packages/unraid-packages.yml
- group: build
  href: https://artifacts.apis.io/unraid/packages/unraid-packages.yml
  title: ''
  type: Packages
  url: packages/unraid-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://unraid.net/about/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.unraid.net/go/release-notes/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unraid
- group: auth
  href: https://artifacts.apis.io/unraid/security/unraid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/unraid-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/unraid/security/unraid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unraid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unraid.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unraid.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unraid.net/API/
- group: start
  title: ''
  type: GettingStarted
  url: https://unraid.net/getting-started
- group: operate
  title: ''
  type: Support
  url: https://unraid.net/support
- group: company
  title: ''
  type: Blog
  url: https://unraid.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://unraid.net/pricing
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 0
    url: https://api.unraid.net/openapi.json
  - status: 404
    url: https://docs.unraid.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Unraid provides a flexible, easy-to-use operating system for self‑hosted servers, network‑attached storage, Docker containers and virtual machines. It enables users to combine drives of any size, run applications via Community Apps, and manage VMs, all through a web UI. The platform is supported by an active community, extensive documentation, and paid support options, making it suitable for hobbyists and professionals building homelab solutions.
image: https://cdn.craft.cloud/481d40bf-939a-4dc1-918d-b4d4b48b7c04/assets/uploads/seo-unraid.png?fit=cover&height=630&width=1200&s=yWE9ELjfTAbKS4xyb1a9IqTpA9av92S02h0X9I4afdE
layout: provider
modified: '2026-10-28'
name: Unraid
nav: Providers
network: true
overview: 'Unraid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Operating System, Network‑Attached Storage, Docker, Virtual Machines, and Self‑Hosting.


  Unraid''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Unraid Domain Security
  slug: unraid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unraid Vulnerability Disclosure
  slug: unraid-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: unraid
tags:
- Operating System
- Network‑Attached Storage
- Docker
- Virtual Machines
- Self‑Hosting
- Homelab
website: https://unraid.net/
---
