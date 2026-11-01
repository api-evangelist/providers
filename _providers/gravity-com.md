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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/gravity-com/hosts/gravity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gravity-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gravity-com/vendors/gravity-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gravity-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gravity
- group: auth
  href: https://artifacts.apis.io/gravity-com/security/gravity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gravity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gravity.com/
- group: company
  title: ''
  type: Blog
  url: https://gravity.com/blog/
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec not found at standard endpoints (e.g., https://api.gravity.com/openapi.json DNS error, https://gravity.com/openapi.json 404).
  evidence:
  - status: DNS error
    url: https://api.gravity.com/openapi.json
  - status: 404
    url: https://gravity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Gravity provides a suite of WordPress plugins, including Gravity Forms and Gravity Flow, enabling businesses to create advanced forms, automate workflows, and integrate with numerous services. The company offers a marketplace of trusted developers and regularly runs promotional discounts, such as the Black Friday 2026 ecosystem price drops.
image: https://gravity.com/wp-content/uploads/2026/10/Twitter-Ecosystem-40-Off.png
layout: provider
modified: '2026-10-29'
name: Gravity
nav: Providers
network: true
overview: 'Gravity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WordPress, Forms, Automation, and Marketplace.


  Gravity''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Gravity Com Plans Pricing
  plan_count: 3
  slug: gravity-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Gravity Com Rate Limits
  slug: gravity-com-rate-limits
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gravity Com Authentication
  slug: gravity-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Gravity Com Domain Security
  slug: gravity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gravity Com Vulnerability Disclosure
  slug: gravity-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Gravity Com Trust Center
  slug: gravity-com-trust-center
  summary_line: HIPAA, GDPR
slug: gravity-com
tags:
- Company
- WordPress
- Forms
- Automation
- Marketplace
website: https://gravity.com/
---
