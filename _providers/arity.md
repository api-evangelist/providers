---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-17'
api_count: 7
apis:
- baseURL: https://api.arity.com
  baseurl_source: declared
  description: The Activation API from Arity — 1 operation(s) for activation.
  name: Arity Activation API
  slug: arity-activation-api
- baseURL: https://api.arity.com
  baseurl_source: declared
  description: The Authentication API from Arity — 2 operation(s) for authentication.
  name: Arity Authentication API
  slug: arity-authentication-api
- baseURL: https://api.arity.com
  baseurl_source: declared
  description: The Booking API Documentation API from Arity — 2 operation(s) for booking api documentation.
  name: Arity Booking API Documentation API
  slug: arity-booking-api-documentation-api
- baseURL: https://api.arity.com
  baseurl_source: declared
  description: The PreQualCredit API from Arity — 5 operation(s) for prequalcredit.
  name: Arity Pre Qual Credit API
  slug: arity-prequalcredit-api
- baseURL: https://api.arity.com
  baseurl_source: declared
  description: The Registration API from Arity — 8 operation(s) for registration.
  name: Arity Registration API
  slug: arity-registration-api
- baseURL: https://api.arity.com
  baseurl_source: declared
  description: The Scoring API from Arity — 2 operation(s) for scoring.
  name: Arity Scoring API
  slug: arity-scoring-api
- baseURL: https://api.arity.com
  baseurl_source: declared
  description: The Trip Intelligence API from Arity — 4 operation(s) for trip intelligence.
  name: Arity Trip Intelligence API
  slug: arity-trip-intelligence-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/rules/arity-rules.yml
  title: ''
  type: Spectral
  url: rules/arity-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/errors/arity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arity-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/conformance/arity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arity-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/well-known/arity-prod-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arity-prod-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/well-known/arity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arity-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/hosts/arity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/vendors/arity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arity-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://arity.com/move/pricing-through-personalization-key-takeaways-from-robert-nendorf-2/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/scopes/arity-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/arity-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arity/refs/heads/main/security/arity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.arity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.arity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.arity.com/
- group: build
  title: ''
  type: PostmanCollection
  url: https://apidocs.arity.com/api/collections/2966050/TW76E5ZE?segregateAuth=true&versionTag=latest
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.arity.com/
- group: build
  title: ''
  type: SDKs
  url: https://arity.com/products/arity-sdk/
- group: start
  title: ''
  type: Login
  url: https://arity.com/customer-login/
- group: company
  title: ''
  type: Newsroom
  url: https://arity.com/news-insights/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://arity.com/articles/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arity.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://arity.com/arity-services-data-support/
- group: operate
  title: ''
  type: Contact
  url: https://arity.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://prod.help.arity.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arity
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://arity.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Arity is a mobility data and analytics company founded by Allstate. It collects and analyzes driving behavior data from mobile devices and connected vehicles to power telematics-based insurance pricing, crash detection, audience and marketing products, and road and traffic analytics. Developers integrate through the Arity Driving Engine (OAuth token, trip intelligence, user registration, groups, driving scores, activation), a Booking API and a PreQualCredit API, documented as a Postman collection at apidocs.arity.com, plus the Arity mobile SDK.
image: https://arity.com/wp-content/uploads/2025/12/arity_social-sharing-tile.png
layout: provider
modified: '2026-10-13'
name: Arity
nav: Providers
network: true
overview: 'Arity is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Activation API, Authentication API, Booking API Documentation API, and 4 more. Tagged areas include Company, Telematics, Mobility Data, Insurance, and Driving Behavior.


  The Arity catalog on APIs.io includes 1 Spectral governance ruleset.


  Arity''s developer surface includes pricing, documentation, API reference, authentication, engineering blog, support, and 19 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Arity API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: arity-rules
scopes:
- name: Arity Scopes
  scope_count: 0
  slug: arity-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 40.6
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 77.8
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Arity Domain Security
  slug: arity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arity
tags:
- Company
- Telematics
- Mobility Data
- Insurance
- Driving Behavior
- Analytics
- Location Data
website: https://arity.com
---
