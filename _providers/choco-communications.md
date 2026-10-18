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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Choco Communications platform, enabling restaurant‑supplier interactions and ordering automation.
  name: Choco Communications API
  slug: choco-communications-api
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/choco-communications/refs/heads/main/vendors/choco-communications-vendors.yml
  title: ''
  type: Vendors
  url: vendors/choco-communications-vendors.yml
- group: auth
  title: ''
  type: Compliance
  url: https://choco.com/us/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/choco-communications/refs/heads/main/llms/choco-communications-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/choco-communications-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/choco-communications/refs/heads/main/well-known/choco-communications-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/choco-communications-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/choco-communications/refs/heads/main/well-known/choco-communications-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/choco-communications-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/choco-communications/refs/heads/main/hosts/choco-communications-hosts.yml
  title: ''
  type: Hosts
  url: hosts/choco-communications-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://choco.com/us/terms-for-vendor-referral-campaign
- group: operate
  title: ''
  type: Support
  url: https://help.choco.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://choco.com/us/register-to-the-webinar
- group: auth
  title: ''
  type: Security
  url: https://legal.choco.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://choco.com/us/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://choco.com/us/press
- group: docs
  title: ''
  type: Documentation
  url: https://help.choco.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/choco-communications/refs/heads/main/security/choco-communications-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/choco-communications-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/choco-communications/refs/heads/main/security/choco-communications-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/choco-communications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://choco.com/
coverage:
  checked: '2026-10-08'
  detail: Help center pages render HTML without exposing machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://help.choco.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Choco Communications provides an AI‑powered growth platform for food distributors, enabling automated ordering, digital storefronts, sales tools, and payment solutions. The platform helps businesses increase margins, reduce waste, and streamline restaurant‑supplier communication through real‑time insights and integrated CRM features.
image: https://choco.com/assets/_1200x630_crop_center-center_none/meta-Image.jpg
layout: provider
modified: '2026-10-08'
name: Choco Communications
nav: Providers
network: true
overview: 'Choco Communications is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Food Distribution, AI Platform, E-Commerce, CRM, and Sales Tools.


  Choco Communications'' developer surface includes support, signup flow, pricing, documentation, and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Choco Communications Domain Security
  slug: choco-communications-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Choco Communications Trust Center
  slug: choco-communications-trust-center
  summary_line: SOC 2
slug: choco-communications
tags:
- Food Distribution
- AI Platform
- E-Commerce
- CRM
- Sales Tools
- ERP Integration
website: https://choco.com/
---
