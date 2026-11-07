---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Licensing APIs and tools that let AI companies automate content licensing from RSL Collective members under standardized RSL terms, pay royalties and deliver usage reports. The collective's license se
  name: RSL Collective Licensing APIs
  slug: rsl-collective-licensing-apis
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/rslcollective-org/plans/rslcollective-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rslcollective-org-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/rslcollective-org/changelog/rslcollective-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rslcollective-org-changelog.yml
- group: design
  href: https://artifacts.apis.io/rslcollective-org/conventions/rslcollective-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rslcollective-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/rslcollective-org/authentication/rslcollective-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rslcollective-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/rslcollective-org/lifecycle/rslcollective-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rslcollective-org-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rslcollective-org/errors/rslcollective-org-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/rslcollective-org-error-codes.yml
- group: design
  href: https://artifacts.apis.io/rslcollective-org/conformance/rslcollective-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rslcollective-org-conformance.yml
- group: other
  href: https://artifacts.apis.io/rslcollective-org/hosts/rslcollective-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rslcollective-org-hosts.yml
- group: build
  href: https://artifacts.apis.io/rslcollective-org/integrations/rslcollective-org-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/rslcollective-org-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/rslcollective-org/vendors/rslcollective-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rslcollective-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/rslcollective-org/security/rslcollective-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rslcollective-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rslcollective.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rslcollective.org/developers
- group: company
  title: ''
  type: About
  url: https://rslcollective.org/about
- group: company
  title: ''
  type: Newsroom
  url: https://rslcollective.org/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rslcollective.org/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rslcollective.org/legal/privacy
- group: other
  title: ''
  type: Standard
  url: https://rslstandard.org/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rslcollective
created: '2026-10-27'
description: 'RSL Collective (legal entity: RSL Internet Collective) is a nonprofit collective rights organization and licensing platform for the internet. It brings together online publishers, publishing platforms, ad networks and licensing agencies and uses the RSL (Really Simple Licensing) Standard to negotiate fair, standardized royalties from AI companies, including pay-per-output royalties, while offering AI companies standardized licensing terms and licensing APIs (access requested through its dashboard) to automate content licensing at scale, including encrypted proprietary content.'
image: https://rslcollective.org/favicon.png
layout: provider
modified: '2026-10-27'
name: RSL Collective
nav: Providers
network: true
overview: 'RSL Collective is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Licensing, Content Licensing, Collective Rights, and Publishers.


  RSL Collective''s developer surface includes changelog, authentication, and 17 more developer resources.'
plans:
- name: Rslcollective Org Plans Pricing
  plan_count: 1
  slug: rslcollective-org-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Rslcollective Org Rate Limits
  slug: rslcollective-org-rate-limits
scopes:
- name: Rslcollective Org Scopes
  scope_count: 0
  slug: rslcollective-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 67.0
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rslcollective-org/rslcollective-org-2026-11-03T142450.png
security:
- kind: authentication
  name: Rslcollective Org Authentication
  slug: rslcollective-org-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Rslcollective Org Domain Security
  slug: rslcollective-org-domain-security
  summary_line: TLSv1.3
slug: rslcollective-org
tags:
- Company
- AI Licensing
- Content Licensing
- Collective Rights
- Publishers
- Royalties
- Non-Profit
- RSL Standard
website: https://rslcollective.org/
---
