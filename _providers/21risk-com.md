---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic access to 21RISK data via a REST API and MCP server as described in the developer portal.
  name: 21RISK REST API
  slug: 21risk-rest-api
- baseURL: https://api.21risk.com
  baseurl_source: declared
  description: '21RISK API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: 21RISK API
  slug: 21risk-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/21risk-com/plans/21risk-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/21risk-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/21risk-com/rules/21risk-com-rules.yml
  title: ''
  type: Spectral
  url: rules/21risk-com-rules.yml
- group: design
  href: https://artifacts.apis.io/21risk-com/vocabulary/21risk-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/21risk-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/21risk-com/security/21risk-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/21risk-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/21risk-com/authentication/21risk-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/21risk-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/21risk-com/conformance/21risk-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/21risk-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/21risk-com/well-known/21risk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/21risk-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/21risk-com/hosts/21risk-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/21risk-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/21risk-com/vendors/21risk-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/21risk-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/21risk-com/security/21risk-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/21risk-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/21risk-com/security/21risk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/21risk-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://21risk.com/
- group: company
  title: ''
  type: Blog
  url: https://21risk.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.21risk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://21risk.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://21risk.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://21risk.com/docs/reports
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alexbjorlig
- group: commercial
  title: ''
  type: Pricing
  url: https://21risk.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://21risk.com/compliance/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://21risk.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.21risk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://21risk.com/compliance/customer-terms-of-services
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are HTML-only and no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://21risk.com/docs/introduction
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: '21RISK makes software for large industrial companies that streamlines how they work with property insurance: value collection, COPE information, sites master data, engineering reports, natcat and climate data, and claims.'
image: https://21risk.com/og-image-home.png
layout: provider
modified: '2026-10-31'
name: 21RISK
nav: Providers
network: true
overview: '21RISK is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Property Insurance, Industrial, Software, and Automation.


  The 21RISK catalog on APIs.io includes 1 Spectral governance ruleset.


  21RISK''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, signup flow, and 16 more developer resources.'
plans:
- name: 21Risk Com Plans Pricing
  plan_count: 2
  slug: 21risk-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: 21RISK API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: 21risk-com-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 34.5
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 39.5
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
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 23.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 21Risk Com Authentication
  slug: 21risk-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 21Risk Com Domain Security
  slug: 21risk-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 21Risk Com Vulnerability Disclosure
  slug: 21risk-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: 21risk-com
tags:
- Insurance
- Property Insurance
- Industrial
- Software
- Automation
website: https://21risk.com/
---
