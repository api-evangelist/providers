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
- description: API for CustomersAI platform providing visitor identity and data enrichment.
  name: CustomersAI API
  slug: customersai-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/customersai/refs/heads/main/plans/customersai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/customersai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/customersai/refs/heads/main/conformance/customersai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/customersai-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/customersai/refs/heads/main/hosts/customersai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/customersai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/customersai/refs/heads/main/vendors/customersai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/customersai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.customers.ai/
- group: operate
  title: ''
  type: Support
  url: https://customers.ai/help
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/customersai/refs/heads/main/security/customersai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/customersai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://customers.ai
- group: docs
  title: ''
  type: Documentation
  url: https://customers.ai/developer-tools
- group: commercial
  title: ''
  type: Pricing
  url: https://customers.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://customers.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://customers.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://customers.ai/inboxer-lifetime-deal-terms-conditions
coverage:
  checked: '2026-10-12'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://customers.ai/developer-tools
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: CustomersAI provides an AI‑powered customer data platform that helps ecommerce brands unify first‑party data, generate visitor IDs, and boost marketing ROI. It integrates with Shopify, Klaviyo and other tools to enable accurate audience segmentation, automated email flows, and advanced analytics, turning raw visitor behavior into actionable insights for higher conversion rates.
image: https://customers.ai/wp-content/uploads/2026/03/customersai-logo.jpg
layout: provider
modified: '2026-10-12'
name: Customersai
nav: Providers
network: true
overview: 'Customersai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketing, E-Commerce, and Data.


  Customersai''s developer surface includes support, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Customersai Plans Pricing
  plan_count: 1
  slug: customersai-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
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
    score: 21.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Customersai Domain Security
  slug: customersai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: customersai
tags:
- Company
- Artificial Intelligence
- Marketing
- E-Commerce
- Data
website: https://customers.ai
---
