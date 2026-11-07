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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 25.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Recast Software API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Recast Software API
  slug: recast-software-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/recast-software/rules/recast-software-rules.yml
  title: ''
  type: Spectral
  url: rules/recast-software-rules.yml
- group: design
  href: https://artifacts.apis.io/recast-software/vocabulary/recast-software-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/recast-software-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/recast-software/conformance/recast-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recast-software-conformance.yml
- group: agent
  href: https://artifacts.apis.io/recast-software/well-known/recast-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recast-software-well-known.yml
- group: other
  href: https://artifacts.apis.io/recast-software/hosts/recast-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recast-software-hosts.yml
- group: other
  href: https://artifacts.apis.io/recast-software/vendors/recast-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recast-software-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.recastsoftware.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://www.recastsoftware.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://auth.recastsoftware.com/Account/Register
- group: auth
  title: ''
  type: Security
  url: https://www.recastsoftware.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.recastsoftware.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.recastsoftware.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.recastsoftware.com
- group: company
  title: ''
  type: Blog
  url: https://www.recastsoftware.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.recastsoftware.com/help/application-workspace-migration-utility-getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RecastSoftware
- group: auth
  href: https://artifacts.apis.io/recast-software/security/recast-software-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/recast-software-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/recast-software/security/recast-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recast-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.recastsoftware.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recastsoftware.com/help
created: '2026-10-21'
description: Extend the power of Configuration Manager, Intune, and more to achieve compliance and reclaim efficiency with Recast. Recast provides automation and compliance solutions for modern workplaces, integrating with Microsoft Endpoint Manager and other IT management tools.
layout: provider
modified: '2026-10-21'
name: Recast Software
nav: Providers
network: true
overview: 'Recast Software is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Compliance, IT Management, and Microsoft.


  The Recast Software catalog on APIs.io includes 1 Spectral governance ruleset.


  Recast Software''s developer surface includes support, signup flow, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Recast Software API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: recast-software-rules
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 19.0
    discoverability: 54.5
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/recast-software/recast-software-2026-11-03T142046.png
security:
- kind: domain-security
  name: Recast Software Domain Security
  slug: recast-software-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Recast Software Vulnerability Disclosure
  slug: recast-software-vulnerability-disclosure
  summary_line: no policy recorded
slug: recast-software
tags:
- Company
- Automation
- Compliance
- IT Management
- Microsoft
website: https://www.recastsoftware.com
---
