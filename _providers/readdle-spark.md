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
- description: Spark Mail provides email client features and AI-powered reply capabilities. Documentation is available at the guides page.
  name: Spark Mail API
  slug: spark-mail-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/readdle-spark/plans/readdle-spark-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/readdle-spark-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/readdle-spark/security/readdle-spark-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/readdle-spark-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/readdle-spark/conformance/readdle-spark-conformance.yml
  title: ''
  type: Conformance
  url: conformance/readdle-spark-conformance.yml
- group: other
  href: https://artifacts.apis.io/readdle-spark/hosts/readdle-spark-hosts.yml
  title: ''
  type: Hosts
  url: hosts/readdle-spark-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sparkmailapp.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://sparkmailapp.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sparkmailapp.com/legal/privacy-web
- group: commercial
  title: ''
  type: Pricing
  url: https://sparkmailapp.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://sparkmailapp.com/guides/ai-email-reply
- group: company
  title: ''
  type: Blog
  url: https://sparkmailapp.com/blog
- group: auth
  href: https://artifacts.apis.io/readdle-spark/security/readdle-spark-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/readdle-spark-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/readdle-spark/security/readdle-spark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/readdle-spark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sparkmailapp.com/
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://sparkmailapp.com/guides/ai-email-reply
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Spark Mail, developed by Readdle, is a smart email client focused on helping users achieve inbox zero and stay organized. It offers features like a focused inbox, snoozing, smart notifications, and powerful search across iOS, macOS, Android, and Windows platforms, aiming to boost productivity for personal and professional communication.
image: https://cdn-rdstaticassets.readdle.com/assets/spark/spark3/common/share-banner/default.png?1793018697
layout: provider
modified: '2026-10-27'
name: Spark Mail (Readdle)
nav: Providers
network: true
overview: 'Spark Mail (Readdle) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Productivity, iOS, macOS, and Android.


  Spark Mail (Readdle)''s developer surface includes support, pricing, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Readdle Spark Plans Pricing
  plan_count: 4
  slug: readdle-spark-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
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
- kind: domain-security
  name: Readdle Spark Domain Security
  slug: readdle-spark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Readdle Spark Vulnerability Disclosure
  slug: readdle-spark-vulnerability-disclosure
  summary_line: no policy recorded
slug: readdle-spark
tags:
- Email
- Productivity
- iOS
- macOS
- Android
website: https://sparkmailapp.com/
---
