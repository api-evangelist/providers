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
- description: SecDim offers a developer security training platform with wargames, secure coding challenges, AI‑assisted code review coaching, and hands‑on labs.
  name: SecDim API
  slug: secdim-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/secdim-com/llms/secdim-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secdim-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-secdim-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secdim-com-secdim-security.txt
- group: commercial
  href: https://artifacts.apis.io/secdim-com/plans/secdim-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/secdim-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://secdim.com/security-disclosure-policy/
- group: auth
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secdim-com-support-security.txt
- group: auth
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secdim-com-security.txt
- group: auth
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-play-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secdim-com-play-security.txt
- group: auth
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-id-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secdim-com-id-security.txt
- group: auth
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-discuss-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secdim-com-discuss-security.txt
- group: auth
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secdim-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/secdim-com/well-known/secdim-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/secdim-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/secdim-com/hosts/secdim-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/secdim-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/secdim-com/vendors/secdim-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/secdim-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secdim.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://secdim.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secdim.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://secdim.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/secdim
- group: auth
  href: https://artifacts.apis.io/secdim-com/security/secdim-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/secdim-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/secdim-com/security/secdim-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secdim-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://secdim.com/
- group: operate
  title: ''
  type: Support
  url: https://support.secdim.com
- group: company
  title: ''
  type: Blog
  url: https://secdim.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://secdim.com/pricing/
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://api.secdim.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: SecDim provides a developer security training platform offering wargames, secure coding challenges, AI‑assisted code review coaching, and hands‑on labs for teams, governments, and educational institutions. Its platform includes a library of real‑world incident‑based challenges, integration with development workflows, and resources such as tutorials, documentation, and community support, aiming to improve secure coding practices across the software development lifecycle.
image: https://secdim.com/assets/images/og.png
layout: provider
modified: '2026-10-31'
name: secdim-com
nav: Providers
network: true
overview: 'secdim-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Training, AI, and Developer.


  secdim-com''s developer surface includes support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Secdim Com Plans Pricing
  plan_count: 4
  slug: secdim-com-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Secdim Com Domain Security
  slug: secdim-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Secdim Com Vulnerability Disclosure
  slug: secdim-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: secdim-com
tags:
- Company
- Security
- Training
- AI
- Developer
website: https://secdim.com/
---
