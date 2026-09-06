---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Batch EDI trading-partner interface for outside processors at Burns Harbor, Cleveland, Indiana Harbor and Kote, compliant with ANSI ASC X12 version 4010 over SFTP or an IBM Sterling VAN. Cleveland-Cli
  name: Cleveland-Cliffs EDI (ANSI X12 4010)
  slug: edi
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleveland-cliffs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleveland-cliffs
- group: company
  title: ''
  type: Website
  url: https://www.clevelandcliffs.com
- group: company
  title: ''
  type: Investor Relations
  url: https://www.clevelandcliffs.com/investors
- group: other
  title: ''
  type: Sustainability
  url: https://www.clevelandcliffs.com/sustainability
- group: company
  title: ''
  type: Newsroom
  url: https://www.clevelandcliffs.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.clevelandcliffs.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.clevelandcliffs.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clevelandcliffs.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clevelandcliffs.com/disclaimer
- group: company
  title: ''
  type: Blog
  url: https://www.clevelandcliffs.com/news/news-releases/rss
- group: docs
  title: ''
  type: Documentation
  url: https://www.clevelandcliffs.com/doing-business/for-outside-processors
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clevelandcliffs.com/doing-business/for-customers
- group: auth
  title: ''
  type: Compliance
  url: https://www.clevelandcliffs.com/doing-business/product-compliance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cleveland-cliffs-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cleveland-cliffs-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cleveland-cliffs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cleveland-cliffs-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cleveland-cliffs-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cleveland-cliffs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cleveland-cliffs-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cleveland-cliffs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cleveland-cliffs-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cleveland-cliffs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.clevelandcliffs.com/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cleveland-cliffs-llms.txt
created: '2026-03-21'
description: 'Cleveland-Cliffs is North America''s largest flat-rolled steel producer and supplier of iron ore pellets, operating an integrated business spanning mining, steelmaking, and downstream finishing for the automotive, infrastructure, and manufacturing markets. Cleveland-Cliffs does not publish a public developer portal, an OpenAPI/GraphQL contract, or any general-purpose REST API. Its documented machine-to-machine surface is batch EDI: ANSI ASC X12 version 4010 over SFTP or an IBM Sterling VAN, with 23 implementation guidelines and an X12 testing template published as public downloads for outside processors at Burns Harbor, Cleveland, Indiana Harbor and Kote. Its transactional applications (Outside Processors Portal, iSupplier, Customer Service Center, Vendor Inquiry) are login-gated, and the only machine-readable discovery documents it serves are OIDC and RFC 8414 metadata on its own Okta tenant at login.clevelandcliffs.com plus an RFC 9116 security.txt.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cleveland-cliffs.png
layout: provider
modified: '2026-09-05'
name: Cleveland-Cliffs
nav: Providers
network: true
overview: 'Cleveland-Cliffs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Iron Ore, Manufacturing, Mining, and Steel.


  Cleveland-Cliffs'' developer surface includes engineering blog, documentation, pricing, authentication, and 22 more developer resources.'
plans:
- name: Cleveland Cliffs Plans Pricing
  plan_count: 0
  slug: cleveland-cliffs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Cleveland Cliffs Rate Limits
  slug: cleveland-cliffs-rate-limits
scopes:
- name: Cleveland Cliffs Scopes
  scope_count: 7
  slug: cleveland-cliffs-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 7.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cleveland-cliffs/refs/heads/main/screenshots/cleveland-cliffs-2026-06-20T174506.png
security:
- kind: authentication
  name: Cleveland Cliffs Authentication
  slug: cleveland-cliffs-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Cleveland Cliffs Domain Security
  slug: cleveland-cliffs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cleveland Cliffs Vulnerability Disclosure
  slug: cleveland-cliffs-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cleveland-cliffs
tags:
- Automotive
- Iron Ore
- Manufacturing
- Mining
- Steel
- Steelmaking
- Supply Chain
website: https://www.clevelandcliffs.com
---
