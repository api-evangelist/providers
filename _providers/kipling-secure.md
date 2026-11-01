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
api_count: 1
apis:
- description: Kipling Secure provides an AI Detection & Response platform for MSPs and SMBs.
  name: Kipling Secure API
  slug: kipling-secure-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kiplingsecure.ai/
- group: other
  href: https://artifacts.apis.io/kipling-secure/hosts/kipling-secure-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kipling-secure-hosts.yml
- group: other
  href: https://artifacts.apis.io/kipling-secure/vendors/kipling-secure-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kipling-secure-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.kiplingsecure.ai/
- group: auth
  href: https://artifacts.apis.io/kipling-secure/security/kipling-secure-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kipling-secure-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kipling-secure/security/kipling-secure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kipling-secure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kiplingsecure.ai/
- group: company
  title: ''
  type: Blog
  url: https://kiplingsecure.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kiplingsecure.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://kiplingsecure.ai/contact-us
coverage:
  checked: '2026-10-29'
  detail: Docs are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://dev.kiplingsecure.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Kipling Secure provides an AI Detection & Response (AIDR) platform tailored for Managed Service Providers (MSPs) and SMBs. The solution helps organizations discover AI usage across their environments, govern AI adoption, detect policy violations, and offer AI security services, turning AI risk management into a recurring revenue stream. Backed by leading technology ecosystems, Kipling Secure aims to give MSPs visibility into AI data flows, ensure compliance, and protect sensitive business information.
image: https://cdn.prod.website-files.com/6a2798ce5023070d26cd3c56/6a3013ab8100ea701f1d1891_home.png
layout: provider
modified: '2026-10-29'
name: Kipling Secure
nav: Providers
network: true
overview: 'Kipling Secure is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Security, MSP, and SaaS.


  Kipling Secure''s developer surface includes documentation, engineering blog, support, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kipling Secure Domain Security
  slug: kipling-secure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kipling Secure Trust Center
  slug: kipling-secure-trust-center
  summary_line: SOC 2, ISO 27001
slug: kipling-secure
tags:
- Company
- AI
- Security
- MSP
- SaaS
website: https://kiplingsecure.ai/
---
