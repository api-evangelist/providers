---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Migration support for the Nasdaq Calypso capital markets platform, enabling migration of data and configurations between Calypso environments. Typical engagements cover version upgrades, data model tr
  name: Calypso Migration
  slug: calypso-migration
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calypso-migration-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/calypso-migration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/calypso-migration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/calypso-migration-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/calypso-migration-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calypso-migration-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.nasdaq.com/products/fintech/calypso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasdaq.com/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nasdaq.com/legal
- group: learn
  title: ''
  type: Training
  url: https://calypsoeducation.nasdaq.com/
coverage:
  checked: '2026-09-05'
  detail: Nasdaq Calypso's API and migration-tooling reference is issued only to licensed institutions through the Calypso support and client ITSM portals — the public nasdaq.com Calypso pages are marketing that end in a Contact Us form, and the old documentation domain www.calypso.com now refuses connections on both port 80 and port 443.
  evidence:
  - status: 200
    url: https://www.nasdaq.com/products/fintech/calypso/delivery-management-and-services
  - status: 0
    url: https://www.calypso.com/
  - status: 0
    url: https://support.calypso.com/
  - status: 404
    url: https://www.nasdaq.com/openapi.json
  - status: 404
    url: https://www.nasdaq.com/.well-known/api-catalog
  reason: customer-only-docs
  state: gated
created: '2024-01-15'
description: Nasdaq Calypso Migration services support financial institutions in migrating data and configurations between Calypso environments. Calypso (formerly Adenza / Calypso Technology) is a cross-asset front-to-back capital markets technology platform used by banks, asset managers, central banks, and clearing houses worldwide. Migration capabilities cover upgrading between Calypso versions, moving between on-premise and cloud deployments, and consolidating multiple Calypso installations. These services are delivered through Nasdaq professional services rather than a public developer API.
finops:
- name: Calypso Migration Finops
  service_category: API
  slug: calypso-migration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calypso-migration.png
layout: provider
modified: '2026-09-05'
name: Calypso Migration
nav: Providers
network: true
overview: 'Calypso Migration publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Capital Markets, Data Migration, Financial Technology, Migration, and Trading.


  Calypso Migration''s developer surface includes training material and 9 more developer resources.'
plans:
- name: Calypso Migration Plans Pricing
  plan_count: 0
  slug: calypso-migration-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Calypso Migration Rate Limits
  slug: calypso-migration-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 46.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calypso-migration/refs/heads/main/screenshots/calypso-migration-2026-06-20T173907.png
security:
- kind: domain-security
  name: Calypso Migration Domain Security
  slug: calypso-migration-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Calypso Migration Vulnerability Disclosure
  slug: calypso-migration-vulnerability-disclosure
  summary_line: disclosure policy published
slug: calypso-migration
tags:
- Capital Markets
- Data Migration
- Financial Technology
- Migration
- Trading
website: https://www.nasdaq.com/products/fintech/calypso
---
