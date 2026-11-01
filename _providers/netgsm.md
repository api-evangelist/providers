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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/netgsm/llms/netgsm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netgsm-llms.txt
- group: auth
  href: https://artifacts.apis.io/netgsm/well-known/netgsm-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netgsm-support-security.txt
- group: agent
  href: https://artifacts.apis.io/netgsm/well-known/netgsm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netgsm-well-known.yml
- group: other
  href: https://artifacts.apis.io/netgsm/hosts/netgsm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netgsm-hosts.yml
- group: other
  href: https://artifacts.apis.io/netgsm/vendors/netgsm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netgsm-vendors.yml
- group: build
  href: https://artifacts.apis.io/netgsm/packages/netgsm-packages.yml
  title: ''
  type: SDKs
  url: packages/netgsm-packages.yml
- group: build
  href: https://artifacts.apis.io/netgsm/packages/netgsm-packages.yml
  title: ''
  type: Packages
  url: packages/netgsm-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.center.netgsm.com.tr/servicedesk/customer/portals
- group: company
  title: ''
  type: Blog
  url: https://blog.netgsm.com.tr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netgsm
- group: auth
  href: https://artifacts.apis.io/netgsm/security/netgsm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netgsm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.netgsm.com.tr/
coverage:
  checked: '2026-10-27'
  detail: The developer portal at https://portal.netgsm.com.tr returns HTML that redirects and appears to require JavaScript to access API documentation, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://portal.netgsm.com.tr
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Netgsm is a Turkish telecommunications provider offering a wide range of digital communication services, including SMS, voice, virtual numbers, IoT/M2M data lines, cloud PBX, and custom API integrations. Their platform enables businesses to send bulk SMS, manage OTP, integrate WhatsApp, and utilize VoIP solutions, all accessible via documented APIs for developers.
image: https://cdn.netgsm.com.tr/images/logos/netgsm/dark/netgsm-logo.svg
layout: provider
modified: '2026-10-27'
name: Netgsm
nav: Providers
network: true
overview: 'Netgsm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SMS, VoIP, Internet, OTP, and IoT.


  Netgsm''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Netgsm Domain Security
  slug: netgsm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: netgsm
tags:
- SMS
- VoIP
- Internet
- OTP
- IoT
website: https://www.netgsm.com.tr/
---
