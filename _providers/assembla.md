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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: ''
  name: Assembla API
  slug: assembla-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/plans/assembla-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/assembla-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://get.assembla.com/security/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/llms/assembla-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assembla-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/well-known/assembla-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assembla-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/vendors/assembla-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assembla-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/packages/assembla-packages.yml
  title: ''
  type: SDKs
  url: packages/assembla-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/packages/assembla-packages.yml
  title: ''
  type: Packages
  url: packages/assembla-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.assembla.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://get.assembla.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.assembla.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.assembla.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.assembla.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/assembla
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/security/assembla-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/assembla-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assembla/refs/heads/main/security/assembla-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assembla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.assembla.com/
coverage:
  checked: 2026-09-22
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://api-docs.assembla.cc/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Assembla provides managed cloud hosting for Perforce, Subversion (SVN) and Git repositories, along with integrated project management tools. Their platform offers enterprise‑grade security, SOC 2 Type II compliance, GDPR adherence, and AI‑powered DevOps assistance. Serving over 1.5 million users for more than two decades, Assembla delivers scalable, secure version‑control hosting, code review, ticketing, sprint planning, and extensive integrations with tools like Slack, Jira, and CI/CD pipelines.
layout: provider
modified: '2026-09-22'
name: Assembla
nav: Providers
network: true
overview: 'Assembla publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Version Control, Cloud Hosting, DevOps, Project Management, and Security.


  Assembla''s developer surface includes pricing and 15 more developer resources.'
plans:
- name: Assembla Plans Pricing
  plan_count: 3
  slug: assembla-plans-pricing
random_paper: 4
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 72.2
    operational_transparency: 15.8
  previous_composite: 28.4
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Assembla Domain Security
  slug: assembla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Assembla Trust Center
  slug: assembla-trust-center
  summary_line: SOC 2, GDPR
slug: assembla
tags:
- Version Control
- Cloud Hosting
- DevOps
- Project Management
- Security
website: https://www.assembla.com/
---
