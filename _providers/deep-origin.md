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
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/plans/deep-origin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deep-origin-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.deeporigin.com/security/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/llms/deep-origin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deep-origin-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/well-known/deep-origin-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deep-origin-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/well-known/deep-origin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deep-origin-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/hosts/deep-origin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deep-origin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/vendors/deep-origin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deep-origin-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/packages/deep-origin-packages.yml
  title: ''
  type: SDKs
  url: packages/deep-origin-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/packages/deep-origin-packages.yml
  title: ''
  type: Packages
  url: packages/deep-origin-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.deeporigin.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.deeporigin.com/news/biosimai-merger
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.deeporigin.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/security/deep-origin-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deep-origin-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deep-origin/refs/heads/main/security/deep-origin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deep-origin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deeporigin.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deeporigin.io
- group: docs
  title: ''
  type: APIReference
  url: https://www.deeporigin.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deeporigin.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deeporigin.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deeporigin.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.deeporigin.com/blog
coverage:
  checked: '2026-10-13'
  detail: Documentation site uses Docusaurus with JS rendering, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.deeporigin.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Deep Origin is an AI‑powered drug discovery platform that leverages advanced machine learning models to accelerate the identification of therapeutic candidates. The company offers a suite of tools including virtual screening, docking, and free‑energy calculations, providing full‑stack access to its models for pharmaceutical researchers. Deep Origin collaborates with partners on discovery projects, offers subscription access to its Balto AI assistant, and provides out‑licensing and co‑development opportunities for validated assets. Their platform aims to reduce the time and cost of drug development by improving accuracy and generalization in computational predictions.
image: https://deeporigin.com/images/og.png
layout: provider
modified: '2026-10-12'
name: Deep Origin
nav: Providers
network: true
overview: 'Deep Origin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Drug Discovery, Platform, and Biotechnology.


  Deep Origin''s developer surface includes documentation, API reference, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Deep Origin Plans Pricing
  plan_count: 1
  slug: deep-origin-plans-pricing
random_paper: 7
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deep Origin Domain Security
  slug: deep-origin-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Deep Origin Trust Center
  slug: deep-origin-trust-center
  summary_line: SOC 2, GDPR
slug: deep-origin
tags:
- Company
- Artificial Intelligence
- Drug Discovery
- Platform
- Biotechnology
website: https://www.deeporigin.com
---
