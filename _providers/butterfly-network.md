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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/butterfly-network/refs/heads/main/plans/butterfly-network-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/butterfly-network-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/butterfly-network/refs/heads/main/well-known/butterfly-network-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/butterfly-network-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/butterfly-network/refs/heads/main/hosts/butterfly-network-hosts.yml
  title: ''
  type: Hosts
  url: hosts/butterfly-network-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/butterfly-network/refs/heads/main/vendors/butterfly-network-vendors.yml
  title: ''
  type: Vendors
  url: vendors/butterfly-network-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/butterfly-network/refs/heads/main/packages/butterfly-network-packages.yml
  title: ''
  type: SDKs
  url: packages/butterfly-network-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/butterfly-network/refs/heads/main/packages/butterfly-network-packages.yml
  title: ''
  type: Packages
  url: packages/butterfly-network-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.butterflynetwork.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.butterflynetwork.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.butterflynetwork.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ButterflyNetwork
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/butterfly-network/refs/heads/main/security/butterfly-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/butterfly-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.butterflynetwork.com
- group: company
  title: ''
  type: Blog
  url: https://www.butterflynetwork.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.butterflynetwork.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.butterflynetwork.com/hc/en-us
- group: company
  title: ''
  type: Careers
  url: https://www.butterflynetwork.com/careers
coverage:
  checked: '2026-10-06'
  detail: The provider's OpenAPI endpoint returns HTML instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://api.butterflynetwork.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Butterfly Network develops handheld, portable ultrasound devices and a cloud‑based imaging platform that enable clinicians to capture, store, and share diagnostic images at the point of care. The company offers a suite of products including the iQ series of probes, AI‑assisted image analysis, and a subscription service for data management and tele‑medicine integration, serving hospitals, clinics, and veterinary practices worldwide.
image: https://cdn.prod.website-files.com/5a0cbe08f1138d000147a9d4/65caed7297b68c8f21085042_Homepage.jpg
layout: provider
modified: '2026-10-06'
name: Butterfly Network
nav: Providers
network: true
overview: 'Butterfly Network is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Ultrasound, Healthcare, and Imaging.


  Butterfly Network''s developer surface includes engineering blog, pricing, support, and 13 more developer resources.'
plans:
- name: Butterfly Network Plans Pricing
  plan_count: 3
  slug: butterfly-network-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Butterfly Network Domain Security
  slug: butterfly-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: butterfly-network
tags:
- Company
- Medical Devices
- Ultrasound
- Healthcare
- Imaging
website: https://www.butterflynetwork.com
---
