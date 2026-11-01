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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/amaka/plans/amaka-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amaka-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/amaka/conformance/amaka-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amaka-conformance.yml
- group: other
  href: https://artifacts.apis.io/amaka/hosts/amaka-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amaka-hosts.yml
- group: other
  href: https://artifacts.apis.io/amaka/vendors/amaka-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amaka-vendors.yml
- group: auth
  href: https://artifacts.apis.io/amaka/security/amaka-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amaka-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amaka.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://amaka.com/
- group: docs
  title: ''
  type: Documentation
  url: https://amaka.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://amaka.com/help
- group: operate
  title: ''
  type: Support
  url: https://amaka.com/help-desk
- group: company
  title: ''
  type: Blog
  url: https://amaka.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://amaka.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amaka.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amaka.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation site does not expose any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://amaka.com/help/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Amaka provides accounting integrations and business automation tools, leveraging AI to import bills, reconcile accounts, and connect e‑commerce platforms with major accounting software such as Xero, QuickBooks, Sage, and MYOB. Serving over 65,000 small businesses globally, Amaka offers a free core tier and premium plans with advanced automation, AI‑driven bookkeeping, and dedicated support.
image: http://amaka.com/wp-content/uploads/2023/09/amaka-accounting-integrations-og.png
layout: provider
modified: '2026-10-27'
name: Amaka
nav: Providers
network: true
overview: 'Amaka is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Automation, AI, and Integration.


  Amaka''s developer surface includes documentation, API reference, support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Amaka Plans Pricing
  plan_count: 3
  slug: amaka-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amaka Domain Security
  slug: amaka-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amaka
tags:
- Company
- Accounting
- Automation
- AI
- Integration
website: https://amaka.com/
---
