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
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: API reference for EspoCRM, providing CRUD operations for CRM entities.
  name: EspoCRM API
  slug: espocrm-api
artifact_total: 2
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.espocrm.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.espocrm.com/plans/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.espocrm.com/extensions/sales-pack/release-notes/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/espocrm/refs/heads/main/security/espocrm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/espocrm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.espocrm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.espocrm.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.espocrm.com/espocrm-api/
- group: operate
  title: ''
  type: Support
  url: https://www.espocrm.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.espocrm.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.espocrm.com/tos/
coverage:
  checked: '2026-09-21'
  detail: Documentation is publicly available but no OpenAPI or other machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://docs.espocrm.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: EspoCRM is an open-source Customer Relationship Management (CRM) platform that enables businesses to manage their sales, marketing, and customer support processes. It offers a flexible, customizable solution with features such as lead management, opportunity tracking, activity streams, and integration capabilities. EspoCRM provides a modern web interface, role-based access control, and extensible architecture through extensions and API access, allowing developers to build custom workflows and integrate with external services. The platform is designed for small to medium-sized enterprises seeking a cost-effective, self-hosted CRM solution.
image: http://www.espocrm.com/images/free-crm-social.jpg
layout: provider
modified: '2026-09-21'
name: EspoCRM
nav: Providers
network: true
overview: 'EspoCRM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Open-Source, Sales, and Marketing.


  EspoCRM''s developer surface includes pricing, changelog, documentation, API reference, support, engineering blog, and 4 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    operational_transparency: 15.8
  previous_composite: 19.1
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Espocrm Domain Security
  slug: espocrm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: espocrm
tags:
- Company
- CRM
- Open-Source
- Sales
- Marketing
website: https://www.espocrm.com/
---
