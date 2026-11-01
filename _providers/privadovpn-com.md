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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/privadovpn-com/plans/privadovpn-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/privadovpn-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/privadovpn-com/cli/privadovpn-com-cli.yml
  title: ''
  type: CLI
  url: cli/privadovpn-com-cli.yml
- group: agent
  href: https://artifacts.apis.io/privadovpn-com/llms/privadovpn-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/privadovpn-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/privadovpn-com/well-known/privadovpn-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/privadovpn-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/privadovpn-com/hosts/privadovpn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/privadovpn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/privadovpn-com/vendors/privadovpn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/privadovpn-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://privadovpn.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.privadovpn.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.privadovpn.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privadovpn.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://privadovpn.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://privadovpn.com/company/media/
- group: start
  title: ''
  type: Login
  url: https://app.privadovpn.com/sign-in
- group: company
  title: ''
  type: Blog
  url: https://blog.privadovpn.com
- group: start
  title: ''
  type: GettingStarted
  url: https://support.privadovpn.com/kb/article/840-2wire-router-setup-for-smart-dns-proxy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/privadovpn
- group: auth
  href: https://artifacts.apis.io/privadovpn-com/security/privadovpn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/privadovpn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://privadovpn.com/
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://privadovpn.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: PrivadoVPN offers a comprehensive online security suite combining high‑speed VPN services with antivirus, ad‑blocking, parental controls, smart DNS, and email relay. Built on AES‑256 encryption and a strict no‑log policy, it provides unlimited device connections, SOCKS5 proxy, kill‑switch, and multi‑platform apps for Windows, macOS, Android, iOS, and popular browsers. The service targets privacy‑focused consumers and businesses seeking robust protection against tracking, malware, and data leaks.
layout: provider
modified: '2026-10-25'
name: Privado
nav: Providers
network: true
overview: 'Privado is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include VPN, Security, Privacy, Antivirus, and Ad‑Blocking.


  Privado''s developer surface includes CLI, support, pricing, engineering blog, getting-started guide, and 13 more developer resources.'
plans:
- name: Privadovpn Com Plans Pricing
  plan_count: 3
  slug: privadovpn-com-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 46.4
    operational_transparency: 21.1
  provenance:
    mcp: derived
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
  name: Privadovpn Com Domain Security
  slug: privadovpn-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: privadovpn-com
tags:
- VPN
- Security
- Privacy
- Antivirus
- Ad‑Blocking
website: https://privadovpn.com/
---
