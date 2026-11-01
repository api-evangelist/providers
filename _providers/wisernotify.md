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
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wisernotify.com/privacypolicy/
- group: commercial
  href: https://artifacts.apis.io/wisernotify/plans/wisernotify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wisernotify-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wisernotify/conformance/wisernotify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wisernotify-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wisernotify/llms/wisernotify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wisernotify-llms.txt
- group: other
  href: https://artifacts.apis.io/wisernotify/hosts/wisernotify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wisernotify-hosts.yml
- group: other
  href: https://artifacts.apis.io/wisernotify/vendors/wisernotify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wisernotify-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://wisernotify.com/security/
- group: company
  title: ''
  type: Blog
  url: https://wisernotify.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wisernotify
- group: auth
  href: https://artifacts.apis.io/wisernotify/security/wisernotify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wisernotify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wisernotify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://wisernotify.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wisernotify.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://wisernotify.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://wisernotify.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://wisernotify.com/pricing
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found on the provider's documentation site.
  evidence:
  - status: 404
    url: https://wisernotify.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: WiserNotify provides a notification platform that enables businesses to send real‑time alerts via email, SMS, push notifications, and webhooks. The service offers customizable templates, scheduling, audience segmentation, and analytics to track delivery and engagement. It integrates with popular SaaS tools and supports API‑first development, allowing developers to programmatically manage notifications, recipients, and reporting.
image: https://wisernotify.com/og-default.png
layout: provider
modified: '2026-10-27'
name: WiserNotify
nav: Providers
network: true
overview: 'WiserNotify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Notification, API, SaaS, and Real-time.


  WiserNotify''s developer surface includes engineering blog, documentation, getting-started guide, support, pricing, and 11 more developer resources.'
plans:
- name: Wisernotify Plans Pricing
  plan_count: 3
  slug: wisernotify-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wisernotify Domain Security
  slug: wisernotify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wisernotify
tags:
- Company
- Notification
- API
- SaaS
- Real-time
website: https://wisernotify.com/
---
