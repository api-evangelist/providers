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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sonicwall.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banyan-security/refs/heads/main/well-known/banyan-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banyan-security-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banyan-security/refs/heads/main/hosts/banyan-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banyan-security-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banyan-security/refs/heads/main/vendors/banyan-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banyan-security-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/banyan-security/refs/heads/main/packages/banyan-security-packages.yml
  title: ''
  type: SDKs
  url: packages/banyan-security-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/banyan-security/refs/heads/main/packages/banyan-security-packages.yml
  title: ''
  type: Packages
  url: packages/banyan-security-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sonicwall
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banyan-security/refs/heads/main/security/banyan-security-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/banyan-security-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banyan-security/refs/heads/main/security/banyan-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banyan-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sonicwall.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sonicwall.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.sonicwall.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.sonicwall.com/partner
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sonicwall.com/pricing
coverage:
  checked: '2026-09-27'
  detail: SonicWall documentation pages are rendered via JavaScript, preventing machine‑readable contract extraction.
  evidence:
  - status: 200
    url: https://www.sonicwall.com/resources
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Banyan Security, now part of SonicWall, provides zero‑trust security solutions that enable secure access to applications and data across hybrid environments. Acquired by SonicWall in 2024, the company’s technology integrates with SonicWall’s next‑generation firewalls to deliver granular, identity‑based controls, secure remote access, and continuous risk assessment for enterprises.
image: https://images-cms.sonicwall.com/v3/assets/blt281ecbfc2563bf9b/bltb535eb0fa055c26a/6814e81f2ac67ca901667c2a/SonicWall-Home-Social-Share-Facebook-OG.png
layout: provider
modified: '2026-09-27'
name: Banyan Security
nav: Providers
network: true
overview: 'Banyan Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Zero Trust, Networks, and Software-as-a-Service.


  Banyan Security''s developer surface includes engineering blog, documentation, support, pricing, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Banyan Security Domain Security
  slug: banyan-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Banyan Security Trust Center
  slug: banyan-security-trust-center
  summary_line: SOC 2, FIPS 140
slug: banyan-security
tags:
- Company
- Security
- Zero Trust
- Networks
- Software-as-a-Service
website: https://www.sonicwall.com/
---
