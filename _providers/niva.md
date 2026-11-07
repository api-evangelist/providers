---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.niva.co
  baseurl_source: declared
  description: 'Niva API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Niva API
  slug: niva-api
artifact_total: 5
asyncapis:
- description: ''
  name: Niva Webhooks
  slug: niva-webhooks
common:
- group: design
  href: https://artifacts.apis.io/niva/rules/niva-rules.yml
  title: ''
  type: Spectral
  url: rules/niva-rules.yml
- group: design
  href: https://artifacts.apis.io/niva/vocabulary/niva-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/niva-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/niva/asyncapi/niva-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/niva-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/niva/authentication/niva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/niva-authentication.yml
- group: design
  href: https://artifacts.apis.io/niva/conformance/niva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/niva-conformance.yml
- group: agent
  href: https://artifacts.apis.io/niva/llms/niva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/niva-llms.txt
- group: other
  href: https://artifacts.apis.io/niva/hosts/niva-hosts.yml
  title: ''
  type: Hosts
  url: hosts/niva-hosts.yml
- group: other
  href: https://artifacts.apis.io/niva/vendors/niva-vendors.yml
  title: ''
  type: Vendors
  url: vendors/niva-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.niva.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.niva.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.niva.co/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.niva.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.niva.co/doc-598721
- group: docs
  title: ''
  type: Documentation
  url: https://docs.niva.co/
- group: auth
  href: https://artifacts.apis.io/niva/security/niva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/niva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.niva.co/
created: '2026-10-24'
description: Niva provides a global business identity platform that enables institutions to verify businesses faster, safer, and smarter using AI. Their solution automates KYB processes, helping fraud and compliance teams scale with real‑time verification, risk scoring, and seamless integration.
image: https://cdn.prod.website-files.com/6632427d943f9ecea1208656/66858682853bdfa9ddc6d6ac_Niva%20share%20image.jpg
layout: provider
modified: '2026-10-24'
name: Niva
nav: Providers
network: true
overview: 'Niva is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Identity Verification, Artificial Intelligence, and Compliance.


  The Niva catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Niva''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Niva API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: niva-rules
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 14.5
    contract_governance: 22.0
    contract_quality: 19.8
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/niva/niva-2026-11-03T140232.png
security:
- kind: authentication
  name: Niva Authentication
  slug: niva-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Niva Domain Security
  slug: niva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: niva
tags:
- Company
- Fintech
- Identity Verification
- Artificial Intelligence
- Compliance
website: https://www.niva.co/
---
