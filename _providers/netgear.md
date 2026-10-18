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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/llms/netgear-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netgear-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/well-known/netgear-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netgear-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/well-known/netgear-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netgear-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/hosts/netgear-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netgear-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/vendors/netgear-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netgear-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/packages/netgear-packages.yml
  title: ''
  type: SDKs
  url: packages/netgear-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/packages/netgear-packages.yml
  title: ''
  type: Packages
  url: packages/netgear-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.netgear.com/
- group: start
  title: ''
  type: SignUp
  url: https://my.netgear.com/register.aspx
- group: auth
  title: ''
  type: Security
  url: https://www.netgear.com/security/
- group: other
  title: ''
  type: Leadership
  url: https://www.netgear.com/about/management/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netgear
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/security/netgear-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netgear-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netgear/refs/heads/main/security/netgear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netgear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.netgear.com
- group: operate
  title: ''
  type: Support
  url: https://www.netgear.com/support/
- group: company
  title: ''
  type: Blog
  url: https://my.netgear.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netgear.com/about/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netgear.com/about/legal/
coverage:
  detail: Home page returns a JavaScript shell, preventing machine‑readable docs discovery.
  evidence:
  - status: 200
    url: https://www.netgear.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: NETGEAR is a global networking hardware company that designs, manufactures, and sells a wide range of wired and wireless networking products for consumers, small businesses, and enterprises. Their portfolio includes Wi‑Fi routers, mesh systems, switches, modems, and network-attached storage, serving millions of customers worldwide. NETGEAR focuses on delivering reliable connectivity, advanced security features, and easy‑to‑use management tools across home and business environments.
image: https://www.netgear.com/mobify/bundle/5212/static/img/brand-logo.svg
layout: provider
modified: '2026-10-13'
name: NETGEAR
nav: Providers
network: true
overview: 'NETGEAR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Hardware, Consumer, and Enterprise.


  NETGEAR''s developer surface includes signup flow, support, engineering blog, and 16 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Netgear Domain Security
  slug: netgear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netgear Vulnerability Disclosure
  slug: netgear-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: netgear
tags:
- Company
- Networking
- Hardware
- Consumer
- Enterprise
website: https://www.netgear.com
---
