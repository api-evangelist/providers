---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/connectwise/llms/connectwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connectwise-llms.txt
- group: auth
  href: https://artifacts.apis.io/connectwise/well-known/connectwise-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connectwise-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/connectwise/well-known/connectwise-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connectwise-developer-security.txt
- group: agent
  href: https://artifacts.apis.io/connectwise/well-known/connectwise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connectwise-well-known.yml
- group: other
  href: https://artifacts.apis.io/connectwise/hosts/connectwise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectwise-hosts.yml
- group: other
  href: https://artifacts.apis.io/connectwise/vendors/connectwise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connectwise-vendors.yml
- group: build
  href: https://artifacts.apis.io/connectwise/packages/connectwise-packages.yml
  title: ''
  type: SDKs
  url: packages/connectwise-packages.yml
- group: build
  href: https://artifacts.apis.io/connectwise/packages/connectwise-packages.yml
  title: ''
  type: Packages
  url: packages/connectwise-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connectwise.com/company/terms
- group: operate
  title: ''
  type: Support
  url: https://www.connectwise.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.connectwise.com/
- group: start
  title: ''
  type: SignUp
  url: https://auth.connectwise.com/Account/Register?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dconnectwise.university%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%2520email%2520roles%2520approles%2520api.users%2520api.sts.admin%26redirect_uri%3Dhttps%253A%252F%252Funiversity.connectwise.com%252Funiversity%252Fauthentication%252FConnectwiseSsoCallback.aspx%26nonce%3De8b4840ab15c27fac2177a38df9805e276cc970ad03e7fcf758d04b4e337fe20%26response_mode%3Dform_post
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connectwise.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.connectwise.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.connectwise.com/company/press/coverage
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.connectwise.com/company/press/releases
- group: company
  title: ''
  type: Blog
  url: https://www.connectwise.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.connectwise.com/solutions/client-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://developer.connectwise.com/
- group: auth
  href: https://artifacts.apis.io/connectwise/security/connectwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connectwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.connectwise.com/
created: '2026-10-26'
description: ConnectWise provides a comprehensive suite of IT management software, including PSA, RMM, remote access, AI agents, and cybersecurity solutions. Their platform enables MSPs and IT departments to automate workflows, secure endpoints, and integrate with third‑party tools via documented APIs and developer resources.
image: https://www.connectwise.com/globalassets/media/icons/favicons/www/cw-schema-logo.png?ts=0507_160523
layout: provider
modified: '2026-10-26'
name: ConnectWise
nav: Providers
network: true
overview: 'ConnectWise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IT Management, MSP, PSA, RMM, and Remote Access.


  The ConnectWise catalog on APIs.io includes 1 Spectral governance ruleset.


  ConnectWise''s developer surface includes support, signup flow, pricing, changelog, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Connectwise Plans Pricing
  plan_count: 0
  slug: connectwise-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: ConnectWise API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: connectwise-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 50.0
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
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
  name: Connectwise Domain Security
  slug: connectwise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: connectwise
tags:
- IT Management
- MSP
- PSA
- RMM
- Remote Access
- Cybersecurity
website: https://www.connectwise.com/
---
