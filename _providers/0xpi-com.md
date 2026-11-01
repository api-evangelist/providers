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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Ringback missed‑call text‑back service documentation
  name: Ringback
  slug: ringback
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/0xpi-com/plans/0xpi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/0xpi-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/0xpi-com/llms/0xpi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0xpi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/0xpi-com/well-known/0xpi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/0xpi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/0xpi-com/hosts/0xpi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0xpi-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/0xpi-com/packages/0xpi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/0xpi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/0xpi-com/packages/0xpi-com-packages.yml
  title: ''
  type: Packages
  url: packages/0xpi-com-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ringback.0xpi.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://ringback.0xpi.com/help
- group: auth
  href: https://artifacts.apis.io/0xpi-com/security/0xpi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0xpi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://0xpi.com/
- group: company
  title: ''
  type: Blog
  url: https://0xpi.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0xpi.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0xpi.com/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daleweaver1981
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://ringback.0xpi.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 0xpi is an independent software studio based in Seattle, Washington that builds AI‑powered tools for marketers, businesses, students, and buyers. Its product suite includes SDSentry for OSHA compliance, PantryPOS food‑pantry software, Ringback missed‑call text‑back, AdCreator AI for ads and SEO, AI Site Builder, Scholarize study tools, and Prime Reviews Pro. The company offers free trials and subscription pricing, with each product providing its own terms of service and privacy policy.
image: https://0xpi.com/0xpi.png
layout: provider
modified: '2026-10-29'
name: 0xpi-com
nav: Providers
network: true
overview: '0xpi-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Tools, SEO, Software, and Marketing.


  0xpi-com''s developer surface includes documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: 0Xpi Com Plans Pricing
  plan_count: 2
  slug: 0xpi-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: 0Xpi Com Rate Limits
  slug: 0xpi-com-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 0Xpi Com Domain Security
  slug: 0xpi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 0xpi-com
tags:
- AI
- Tools
- SEO
- Software
- Marketing
- Education
- Compliance
website: https://0xpi.com/
---
