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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/defined-networking/llms/defined-networking-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defined-networking-llms.txt
- group: auth
  href: https://artifacts.apis.io/defined-networking/well-known/defined-networking-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/defined-networking-security.txt
- group: auth
  href: https://artifacts.apis.io/defined-networking/well-known/defined-networking-defined-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/defined-networking-defined-security.txt
- group: auth
  href: https://artifacts.apis.io/defined-networking/well-known/defined-networking-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/defined-networking-api-security.txt
- group: agent
  href: https://artifacts.apis.io/defined-networking/well-known/defined-networking-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/defined-networking-well-known.yml
- group: other
  href: https://artifacts.apis.io/defined-networking/hosts/defined-networking-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defined-networking-hosts.yml
- group: other
  href: https://artifacts.apis.io/defined-networking/vendors/defined-networking-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defined-networking-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.defined.net/terms/
- group: auth
  title: ''
  type: Security
  url: https://www.defined.net/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.defined.net/privacy/
- group: company
  title: ''
  type: Blog
  url: https://defined.net/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://nebula.defined.net/docs/guides/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.defined.net/
- group: auth
  href: https://artifacts.apis.io/defined-networking/security/defined-networking-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/defined-networking-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/defined-networking/security/defined-networking-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defined-networking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.defined.net
coverage:
  checked: '2026-10-22'
  detail: The provider's website loads content via JavaScript, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://www.defined.net
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Defined Networking provides Managed Nebula, a managed overlay network that creates direct, encrypted connections between hosts without requiring VPN gateways or open inbound ports. The service supports remote access, drop‑in encryption, multi‑cloud deployment, and IoT/fleet telematics, enabling teams to securely connect laptops, servers, cloud instances, and mobile devices across NAT and firewalls.
image: https://www.defined.net/_astro/defined-og.BFgUxzT-_1C2TcO.webp
layout: provider
modified: '2026-10-22'
name: Defined Networking
nav: Providers
network: true
overview: 'Defined Networking is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Remote access, Encryption, Multi‑cloud, IoT, and NAT traversal.


  Defined Networking''s developer surface includes engineering blog, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Defined Networking Domain Security
  slug: defined-networking-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Defined Networking Vulnerability Disclosure
  slug: defined-networking-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: defined-networking
tags:
- Remote access
- Encryption
- Multi‑cloud
- IoT
- NAT traversal
- Identity
- Managed networking
website: https://www.defined.net
---
