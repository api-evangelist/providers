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
  score: 10.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Arbohq provides APIs for data services, 1099 filing, financial planning, and embedded finance as described on their documentation site.
  name: Arbohq API
  slug: arbohq-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbohq/refs/heads/main/vendors/arbohq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arbohq-vendors.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/arbohq/refs/heads/main/changelog/arbohq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/arbohq-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arbohq/refs/heads/main/well-known/arbohq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arbohq-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbohq/refs/heads/main/hosts/arbohq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arbohq-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.arbohq.com/
- group: start
  title: ''
  type: SignUp
  url: https://arbohq.com/sign-up
- group: operate
  title: ''
  type: ChangeLog
  url: https://arbohq.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arbohq
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbohq/refs/heads/main/security/arbohq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arbohq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arbohq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://arbohq.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://arbohq.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://arbohq.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://arbohq.com/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arbohq.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arbohq.com/legal/privacy-policy
coverage:
  checked: '2026-10-16'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://arbohq.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Arbohq provides an IRS‑Integrated Finance Platform designed for regulated teams such as accounting firms, lending underwriters, and government agencies. The solution automates transcript workflows, ensures compliance, and offers a suite of APIs for data services, 1099 filing, financial planning, and embedded finance, enabling secure, end‑to‑end financial operations.
image: https://framerusercontent.com/assets/BKiRtf1mKDgK7PTiqQzDzdlZnoc.png
layout: provider
modified: '2026-10-16'
name: Arbohq
nav: Providers
network: true
overview: 'Arbohq is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Regulated, Platform, and Integration.


  Arbohq''s developer surface includes changelog, support, signup flow, documentation, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arbohq Domain Security
  slug: arbohq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arbohq
tags:
- Finance
- Regulated
- Platform
- Integration
website: https://arbohq.com/
---
