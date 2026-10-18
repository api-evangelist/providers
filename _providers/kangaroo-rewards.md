---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 78
  human_in_the_loop: 4
  name: Kangaroo Rewards Agentic Access
  operation_count: 161
  slug: kangaroo-rewards-agentic-access
  summary_line: 161 operations · 78 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.kangaroorewards.com/
  baseurl_source: declared
  description: The core API from Kangaroo Rewards — 159 operation(s) for core.
  name: Kangaroo Rewards Core API
  slug: kangaroo-rewards-core-api
artifact_total: 5
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/agentic-access/kangaroo-rewards-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kangaroo-rewards-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/plans/kangaroo-rewards-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kangaroo-rewards-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/rules/kangaroo-rewards-rules.yml
  title: ''
  type: Spectral
  url: rules/kangaroo-rewards-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/conformance/kangaroo-rewards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kangaroo-rewards-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/llms/kangaroo-rewards-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kangaroo-rewards-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/well-known/kangaroo-rewards-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kangaroo-rewards-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/hosts/kangaroo-rewards-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kangaroo-rewards-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/packages/kangaroo-rewards-packages.yml
  title: ''
  type: SDKs
  url: packages/kangaroo-rewards-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/packages/kangaroo-rewards-packages.yml
  title: ''
  type: Packages
  url: packages/kangaroo-rewards-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loyalty.kangaroorewards.com/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kangaroorewards.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loyalty.kangaroorewards.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://loyalty.kangaroorewards.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.kangaroorewards.com/upload/media/api-license-agreement.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kangaroorewards
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kangaroo-rewards/refs/heads/main/security/kangaroo-rewards-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kangaroo-rewards-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kangaroorewards.com
- group: docs
  title: ''
  type: Documentation
  url: https://loyalty.kangaroorewards.com/
- group: docs
  title: ''
  type: APIReference
  url: https://loyalty.kangaroorewards.com/api/
created: '2026-10-13'
description: Kangaroo Rewards provides a comprehensive loyalty and rewards platform for businesses across various industries, offering tools such as loyalty management, email & SMS marketing, omnichannel campaigns, geofencing, gamification, QR code scanning, and workflow automation. Their solution integrates with major e‑commerce and POS systems like Shopify, WooCommerce, BigCommerce, and Lightspeed, enabling businesses to acquire, retain, and engage customers through personalized rewards and automated marketing. The platform also offers a white‑label app and loyalty tablet for seamless in‑store experiences, backed by robust reporting and seamless integrations.
image: https://loyalty.kangaroorewards.com/wp-content/uploads/2025/07/9E3673A8-2DA6-4EE2-9738-1654094C88D2.png
layout: provider
modified: '2026-10-13'
name: Kangaroo Rewards
nav: Providers
network: true
overview: 'Kangaroo Rewards publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Core API. Tagged areas include Company, Loyalty, Marketing, Software-as-a-Service, and Rewards.


  The Kangaroo Rewards catalog on APIs.io includes 1 Spectral governance ruleset.


  Kangaroo Rewards'' developer surface includes pricing, documentation, API reference, and 16 more developer resources.'
plans:
- name: Kangaroo Rewards Plans Pricing
  plan_count: 4
  slug: kangaroo-rewards-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Kangaroo Rewards API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: kangaroo-rewards-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 27.6
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Kangaroo Rewards Domain Security
  slug: kangaroo-rewards-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kangaroo-rewards
tags:
- Company
- Loyalty
- Marketing
- Software-as-a-Service
- Rewards
website: https://www.kangaroorewards.com
---
