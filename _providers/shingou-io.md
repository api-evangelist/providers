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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://shingou.io/terms
- group: agent
  href: https://artifacts.apis.io/shingou-io/llms/shingou-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shingou-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/shingou-io/well-known/shingou-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shingou-io-security.txt
- group: agent
  href: https://artifacts.apis.io/shingou-io/well-known/shingou-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shingou-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/shingou-io/hosts/shingou-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shingou-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/shingou-io/vendors/shingou-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shingou-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/shingou-io/security/shingou-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/shingou-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/shingou-io/security/shingou-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shingou-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shingou.io/
- group: docs
  title: ''
  type: Documentation
  url: https://shingou.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://shingou.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://shingou.io/docs
- group: operate
  title: ''
  type: Support
  url: https://shingou.io/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shingou.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shingou.io/privacy
coverage:
  checked: '2026-10-31'
  detail: The provider's documentation at https://shingou.io/docs does not publish a machine‑readable OpenAPI/GraphQL/AsyncAPI spec and attempts to fetch common spec URLs return 404.
  evidence:
  - status: 200
    url: https://shingou.io/docs
  - status: 404
    url: https://api.shingou.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Shingou provides a point-in-time crypto market sentiment API that delivers hourly sentiment scores for cryptocurrency symbols. The service aggregates news, applies LLM scoring, and offers a transparent, verifiable log of data. Free tier includes 1,000 requests per day, with paid plans for higher volume and additional features. The platform includes comprehensive documentation, demo, research, integrations, and status pages.
image: https://shingou.io/logo.png
layout: provider
modified: '2026-10-31'
name: shingou-io
nav: Providers
network: true
overview: 'shingou-io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Sentiment, API, and Data.


  shingou-io''s developer surface includes documentation, API reference, getting-started guide, support, and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Shingou Io Domain Security
  slug: shingou-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shingou Io Vulnerability Disclosure
  slug: shingou-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: shingou-io
tags:
- Company
- Crypto
- Sentiment
- API
- Data
website: https://shingou.io/
---
