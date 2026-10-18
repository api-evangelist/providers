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
- description: API for Bushel platform, details not publicly documented.
  name: Bushel API
  slug: bushel-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/plans/bushel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bushel-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/changelog/bushel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bushel-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/conformance/bushel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bushel-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/hosts/bushel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bushel-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/vendors/bushel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bushel-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/packages/bushel-packages.yml
  title: ''
  type: SDKs
  url: packages/bushel-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/packages/bushel-packages.yml
  title: ''
  type: Packages
  url: packages/bushel-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.bushelpowered.com/trust-center
- group: operate
  title: ''
  type: Support
  url: https://support.bushelpowered.com
- group: auth
  title: ''
  type: Security
  url: https://www.bushelpowered.com/category/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bushelpowered.com/privacy-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bushelpowered.com/farmers/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.bushelpowered.com/category/news
- group: other
  title: ''
  type: Leadership
  url: https://www.bushelpowered.com/agribusiness/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.bushelpowered.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bushelpowered.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.bushelpowered.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bushelpowered.com/farmers/cfc-getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bushelpowered
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bushel/refs/heads/main/security/bushel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bushel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bushelpowered.com/
coverage:
  checked: '2026-10-06'
  detail: OpenAPI endpoints on api.bushelpowered.com returned 404, and no machine‑readable spec was found on the developer portal.
  evidence:
  - status: 404
    url: https://api.bushelpowered.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Bushel provides software solutions for agriculture, offering tools for farm management, agribusiness CRM, commercial grain sales, payments, and digital services. Their platform connects farmers, agribusinesses, and partners to streamline operations, improve data insights, and enable modern agricultural workflows.
image: https://cdn.prod.website-files.com/69036d34b67c2b1bb700e2d3/6938632de4cf52aab456f1ba_b8cb10d7a2ba0101b9b2eaad8bc003f5_About%20Us_WeBuildSoftware.jpg
layout: provider
modified: '2026-10-06'
name: Bushel
nav: Providers
network: true
overview: 'Bushel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Farm Management, Software-as-a-Service, CRM, and Payments.


  Bushel''s developer surface includes changelog, support, pricing, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Bushel Plans Pricing
  plan_count: 3
  slug: bushel-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 60.7
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bushel Domain Security
  slug: bushel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bushel
tags:
- Agriculture
- Farm Management
- Software-as-a-Service
- CRM
- Payments
website: https://www.bushelpowered.com/
---
