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
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://cake.com/security
- group: auth
  title: ''
  type: Security
  url: https://security.cake.com/
- group: agent
  href: https://artifacts.apis.io/pumble/llms/pumble-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pumble-llms.txt
- group: auth
  href: https://artifacts.apis.io/pumble/well-known/pumble-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pumble-security.txt
- group: auth
  href: https://artifacts.apis.io/pumble/well-known/pumble-plaky-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pumble-plaky-security.txt
- group: auth
  href: https://artifacts.apis.io/pumble/well-known/pumble-clockify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pumble-clockify-security.txt
- group: auth
  href: https://artifacts.apis.io/pumble/well-known/pumble-cake-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pumble-cake-security.txt
- group: agent
  href: https://artifacts.apis.io/pumble/well-known/pumble-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pumble-well-known.yml
- group: other
  href: https://artifacts.apis.io/pumble/hosts/pumble-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pumble-hosts.yml
- group: other
  href: https://artifacts.apis.io/pumble/vendors/pumble-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pumble-vendors.yml
- group: build
  href: https://artifacts.apis.io/pumble/packages/pumble-packages.yml
  title: ''
  type: SDKs
  url: packages/pumble-packages.yml
- group: build
  href: https://artifacts.apis.io/pumble/packages/pumble-packages.yml
  title: ''
  type: Packages
  url: packages/pumble-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://pumble.com/help/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pumble.com
- group: operate
  title: ''
  type: Roadmap
  url: https://pumble.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://pumble.com/pricing
- group: start
  title: ''
  type: Login
  url: https://pumble.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://pumble.com/help/getting-started/
- group: operate
  title: ''
  type: ChangeLog
  url: https://pumble.com/help/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://pumble.com/blog/
- group: auth
  href: https://artifacts.apis.io/pumble/security/pumble-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pumble-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pumble/security/pumble-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pumble-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pumble/security/pumble-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pumble-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pumble.com/
coverage:
  checked: '2026-10-26'
  detail: The provider's website offers HTML documentation but no discoverable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://pumble.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Pumble is a free business communication tool that offers team chat, voice calls, and file sharing in a single platform. It is designed for small to medium-sized businesses to improve internal collaboration with features like channels, direct messages, integrations, and searchable message history. The service emphasizes simplicity, security, and cross‑platform availability, supporting web, desktop, and mobile clients.
image: https://pumble.com/assets/images/redesign/og-images/homepage.png
layout: provider
modified: '2026-10-26'
name: Pumble
nav: Providers
network: true
overview: 'Pumble is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Pumble''s developer surface includes support, pricing, getting-started guide, changelog, engineering blog, and 19 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 39.3
    operational_transparency: 47.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pumble Domain Security
  slug: pumble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pumble Vulnerability Disclosure
  slug: pumble-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pumble Trust Center
  slug: pumble-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: pumble
tags:
- Company
website: https://pumble.com/
---
