---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Safe Browsing Agentic Access
  operation_count: 4
  slug: google-safe-browsing-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 4
apis:
- description: The fullHashes:find API from Google Safe Browsing — 1 operation(s) for fullhashes:find.
  name: Google Safe Browsing fullHashes:find API
  slug: google-safe-browsing-fullhashes-find-api
- description: The threatLists API from Google Safe Browsing — 1 operation(s) for threatlists.
  name: Google Safe Browsing threatLists API
  slug: google-safe-browsing-threatlists-api
- description: The threatListUpdates:fetch API from Google Safe Browsing — 1 operation(s) for threatlistupdates:fetch.
  name: Google Safe Browsing threatListUpdates:fetch API
  slug: google-safe-browsing-threatlistupdates-fetch-api
- description: The threatMatches:find API from Google Safe Browsing — 1 operation(s) for threatmatches:find.
  name: Google Safe Browsing threatMatches:find API
  slug: google-safe-browsing-threatmatches-find-api
artifact_total: 19
collections:
- collection_type: postman
  name: Google Safe Browsing fullHashes:find API
  slug: postman-google-safe-browsing-fullhashes-find-api
- collection_type: postman
  name: Google Safe Browsing fullHashes:find threatLists API
  slug: postman-google-safe-browsing-threatlists-api
- collection_type: postman
  name: Google Safe Browsing fullHashes:find threatListUpdates:fetch API
  slug: postman-google-safe-browsing-threatlistupdates-fetch-api
- collection_type: postman
  name: Google Safe Browsing fullHashes:find threatMatches:find API
  slug: postman-google-safe-browsing-threatmatches-find-api
- collection_type: open
  name: Google Safe Browsing API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-safe-browsing/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-safe-browsing-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-safe-browsing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-safe-browsing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-safe-browsing-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/safe-browsing
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/safe-browsing/v4/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/safe-browsing
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/safe-browsing/v4/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/safe-browsing/v4/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google Safe Browsing API enables client applications to check web resources (most commonly URLs) against Google-generated lists of unsafe web resources including malware, social engineering, unwanted software, and potentially harmful applications.
finops:
- name: Google Safe Browsing Finops
  service_category: API
  slug: google-safe-browsing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-safe-browsing.png
json_schemas:
- name: Google Safe Browsing Threat Match
  property_count: 6
  slug: ThreatMatch
jsonld:
- class_count: 9
  name: context Context
  property_count: 1
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Safe Browsing
nav: Providers
network: true
overview: 'Google Safe Browsing publishes 4 APIs on the [APIs.io](https://apis.io/) network, including fullHashes:find API, threatLists API, threatListUpdates:fetch API, and 1 more. Tagged areas include Google, Malware, Safe Browsing, Security, and Threats.


  The Google Safe Browsing catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Safe Browsing''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, and 10 more developer resources.'
plans:
- name: Google Safe Browsing Plans Pricing
  plan_count: 3
  slug: google-safe-browsing-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 5
  name: Google Safe Browsing Rate Limits
  slug: google-safe-browsing-rate-limits
rules:
- name: Google Safe Browsing API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-safe-browsing-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.5
  delta: -3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.3
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-safe-browsing/refs/heads/main/screenshots/google-safe-browsing-2026-06-20T182229.png
security:
- kind: authentication
  name: Google Safe Browsing Authentication
  slug: google-safe-browsing-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Safe Browsing Domain Security
  slug: google-safe-browsing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Safe Browsing Vulnerability Disclosure
  slug: google-safe-browsing-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-safe-browsing
tags:
- Google
- Malware
- Safe Browsing
- Security
- Threats
- URLs
website: https://developers.google.com/safe-browsing
---
