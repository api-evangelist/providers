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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Babelway provides a REST API for its integration platform, documented at the REST API client guide.
  name: Babelway REST API
  slug: babelway-rest-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/babelway/plans/babelway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/babelway-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/babelway/conformance/babelway-conformance.yml
  title: ''
  type: Conformance
  url: conformance/babelway-conformance.yml
- group: agent
  href: https://artifacts.apis.io/babelway/llms/babelway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/babelway-llms.txt
- group: other
  href: https://artifacts.apis.io/babelway/hosts/babelway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/babelway-hosts.yml
- group: other
  href: https://artifacts.apis.io/babelway/vendors/babelway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/babelway-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.babelway.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.babelway.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.babelway.com/pricing-plans-babelway/
- group: company
  title: ''
  type: Newsroom
  url: https://www.babelway.com/resources/news/tls-security-changes/
- group: docs
  title: ''
  type: Documentation
  url: https://www.babelway.com/resources/category/guides/
- group: company
  title: ''
  type: Blog
  url: https://www.babelway.com/resources/category/blog/
- group: auth
  href: https://artifacts.apis.io/babelway/security/babelway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/babelway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://babelway.com/
coverage:
  checked: '2026-10-20'
  detail: The REST API documentation page is rendered via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.babelway.com/protocol/rest-api-client/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Babelway, now part of Tradeshift, provides a cloud‑based B2B integration platform that enables companies to exchange electronic documents such as invoices, purchase orders, and shipping notices across a wide range of standards (X12, EDIFACT, UBL, XML) and protocols (Peppol, AS2, FTP, SFTP, REST). The service offers a visual workflow builder, automated mapping, and a managed network for secure data transmission, helping businesses accelerate digital transformation and reduce manual processing costs.
image: https://www.babelway.com/wp-content/uploads/2026/06/How-to-Prepare-for-the-French-PDP-with-Babelway-1024x576.png
layout: provider
modified: '2026-10-19'
name: Tradeshift
nav: Providers
network: true
overview: 'Tradeshift is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Tradeshift''s developer surface includes pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Babelway Plans Pricing
  plan_count: 8
  slug: babelway-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Babelway Domain Security
  slug: babelway-domain-security
  summary_line: TLSv1.3 · HSTS
slug: babelway
tags:
- Company
website: https://babelway.com/
---
