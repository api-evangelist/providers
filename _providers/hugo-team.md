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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: AI-powered customer support API
  name: Hugo API
  slug: hugo-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/hugo-team/hosts/hugo-team-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hugo-team-hosts.yml
- group: other
  href: https://artifacts.apis.io/hugo-team/vendors/hugo-team-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hugo-team-vendors.yml
- group: build
  href: https://artifacts.apis.io/hugo-team/packages/hugo-team-packages.yml
  title: ''
  type: SDKs
  url: packages/hugo-team-packages.yml
- group: build
  href: https://artifacts.apis.io/hugo-team/packages/hugo-team-packages.yml
  title: ''
  type: Packages
  url: packages/hugo-team-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hugo.ai/
- group: auth
  href: https://artifacts.apis.io/hugo-team/security/hugo-team-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hugo-team-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hugo.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hugoai
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation site is a JavaScript‑rendered single‑page app, so no machine‑readable spec is available.
  evidence:
  - status: 200
    url: https://hugo.ai/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Hugo AI is an AI‑powered customer support agent that resolves tickets faster, automates repetitive tasks, and serves customers 24/7. It connects to business tools via the Model Context Protocol (MCP), enabling real‑time data access and actions. Hugo offers a no‑code interface for quick deployment, supports multiple large language models, and provides enterprise‑grade encryption, EU data residency, and compliance. The platform includes performance analytics, customizable routing, and seamless integration with helpdesks, knowledge bases, and CRMs, helping teams reduce support workload and improve satisfaction.
image: https://hugo.ai/_ipx/s_92x28/common/logos/logo_full_white.svg
layout: provider
modified: '2026-10-29'
name: Hugo
nav: Providers
network: true
overview: Hugo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Customer Support, SaaS, Automation, and Enterprise.
random_paper: 15
scopes:
- name: Hugo Team Scopes
  scope_count: 0
  slug: hugo-team-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hugo Team Authentication
  slug: hugo-team-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hugo Team Domain Security
  slug: hugo-team-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hugo-team
tags:
- AI
- Customer Support
- SaaS
- Automation
- Enterprise
website: https://hugo.ai/
---
