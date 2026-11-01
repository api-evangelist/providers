---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'SellViaApp API API as documented publicly: 84 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: SellViaApp API API
  slug: sellviaapp-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/sellviaapp/plans/sellviaapp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sellviaapp-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sellviaapp/rules/sellviaapp-rules.yml
  title: ''
  type: Spectral
  url: rules/sellviaapp-rules.yml
- group: design
  href: https://artifacts.apis.io/sellviaapp/vocabulary/sellviaapp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sellviaapp-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/sellviaapp/changelog/sellviaapp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sellviaapp-changelog.yml
- group: auth
  href: https://artifacts.apis.io/sellviaapp/authentication/sellviaapp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sellviaapp-authentication.yml
- group: design
  href: https://artifacts.apis.io/sellviaapp/errors/sellviaapp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sellviaapp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sellviaapp/conformance/sellviaapp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sellviaapp-conformance.yml
- group: other
  href: https://artifacts.apis.io/sellviaapp/hosts/sellviaapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sellviaapp-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sellviaapp.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sellviaapp.com/en/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://sellviaapp.com/en/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://sellviaapp.com/en/changelog
- group: auth
  href: https://artifacts.apis.io/sellviaapp/security/sellviaapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sellviaapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sellviaapp.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://sellviaapp.com/en/api-documentation
coverage:
  checked: '2026-10-21'
  detail: API documentation pages are JavaScript‑rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://sellviaapp.com/en/api-documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: SellViaApp API provides a comprehensive platform enabling businesses to create and manage mobile applications for their customers. The service offers endpoints for product catalog management, order processing, inventory synchronization, and user authentication, all delivered over a secure JSON API. Documentation is publicly available and includes detailed guides for integration, rate limiting, and error handling, allowing developers to seamlessly integrate mobile commerce capabilities into their existing systems.
image: https://sellviaapp.com/assets/images/og-sellviaapp.jpg
layout: provider
modified: '2026-10-21'
name: SellViaApp API
nav: Providers
network: true
overview: 'SellViaApp API is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Commerce, Integration, and Software-as-a-Service.


  The SellViaApp API catalog on APIs.io includes 1 Spectral governance ruleset.


  SellViaApp API''s developer surface includes changelog, authentication, pricing, documentation, and 11 more developer resources.'
plans:
- name: Sellviaapp Plans Pricing
  plan_count: 2
  slug: sellviaapp-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: SellViaApp API API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: sellviaapp-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.8
    catalog_earned_first_party: 8.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 9.2
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sellviaapp Authentication
  slug: sellviaapp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sellviaapp Domain Security
  slug: sellviaapp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sellviaapp
tags:
- Mobile
- Commerce
- Integration
- Software-as-a-Service
website: https://sellviaapp.com/en/
---
