---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 4
apis:
- baseURL: https://chatapi.viber.com/pa
  baseurl_source: declared
  description: The Account API from Rakuten Viber — 1 operation(s) for account.
  name: Rakuten Viber Account API
  slug: viber-account-api
- baseURL: https://chatapi.viber.com/pa
  baseurl_source: declared
  description: The Messages API from Rakuten Viber — 2 operation(s) for messages.
  name: Rakuten Viber Messages API
  slug: viber-messages-api
- baseURL: https://chatapi.viber.com/pa
  baseurl_source: declared
  description: The Users API from Rakuten Viber — 2 operation(s) for users.
  name: Rakuten Viber Users API
  slug: viber-users-api
- baseURL: https://chatapi.viber.com/pa
  baseurl_source: declared
  description: The Webhooks API from Rakuten Viber — 1 operation(s) for webhooks.
  name: Rakuten Viber Webhooks API
  slug: viber-webhooks-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/viber/rules/viber-rules.yml
  title: ''
  type: Spectral
  url: rules/viber-rules.yml
- group: design
  href: https://artifacts.apis.io/viber/conformance/viber-conformance.yml
  title: ''
  type: Conformance
  url: conformance/viber-conformance.yml
- group: other
  href: https://artifacts.apis.io/viber/hosts/viber-hosts.yml
  title: ''
  type: Hosts
  url: hosts/viber-hosts.yml
- group: other
  href: https://artifacts.apis.io/viber/vendors/viber-vendors.yml
  title: ''
  type: Vendors
  url: vendors/viber-vendors.yml
- group: build
  href: https://artifacts.apis.io/viber/packages/viber-packages.yml
  title: ''
  type: SDKs
  url: packages/viber-packages.yml
- group: build
  href: https://artifacts.apis.io/viber/packages/viber-packages.yml
  title: ''
  type: Packages
  url: packages/viber-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viber.com/en/terms
- group: auth
  title: ''
  type: Security
  url: https://www.viber.com/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Viber
- group: company
  title: ''
  type: Website
  url: https://www.viber.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.viber.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.viber.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://help.viber.com/hc/en-us
- group: auth
  href: https://artifacts.apis.io/viber/security/viber-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/viber-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/viber/security/viber-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viber-domain-security.yml
created: '2026-10-13'
description: Rakuten Viber is a messaging and calling app. Its developer hub publishes the Viber REST Bot API (chatapi.viber.com/pa) for building bots that send and receive messages, with webhook callbacks and official Node.js and Python SDKs.
image: https://www.viber.com/app/uploads/social-sharing-image-2026.png
layout: provider
modified: '2026-10-13'
name: Rakuten Viber
nav: Providers
network: true
overview: 'Rakuten Viber is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Messages API, Users API, and 1 more. Tagged areas include Company, Messaging, Chatbots, and Communications.


  The Rakuten Viber catalog on APIs.io includes 1 Spectral governance ruleset.


  Rakuten Viber''s developer surface includes documentation, support, and 13 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Rakuten Viber API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: viber-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 12.2
    developer_ergonomics: 28.6
    discoverability: 62.5
    operational_transparency: 7.9
  previous_composite: 23.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/viber/viber-2026-11-03T145807.png
security:
- kind: domain-security
  name: Viber Domain Security
  slug: viber-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Viber Vulnerability Disclosure
  slug: viber-vulnerability-disclosure
  summary_line: no policy recorded
slug: viber
tags:
- Company
- Messaging
- Chatbots
- Communications
website: https://www.viber.com
---
