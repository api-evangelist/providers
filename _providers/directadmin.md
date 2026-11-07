---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: DirectAdmin offers a JSON‑based API and a legacy URL‑encoded API for managing hosting servers. Documentation is at the developer API page.
  name: DirectAdmin API
  slug: directadmin-api-2
- baseURL: https://download.directadmin.com
  baseurl_source: declared
  description: 'DirectAdmin API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: DirectAdmin API
  slug: directadmin-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/directadmin/plans/directadmin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/directadmin-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/directadmin/rules/directadmin-rules.yml
  title: ''
  type: Spectral
  url: rules/directadmin-rules.yml
- group: design
  href: https://artifacts.apis.io/directadmin/vocabulary/directadmin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/directadmin-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/directadmin/changelog/directadmin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/directadmin-changelog.yml
- group: auth
  href: https://artifacts.apis.io/directadmin/security/directadmin-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/directadmin-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/directadmin/conformance/directadmin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/directadmin-conformance.yml
- group: auth
  href: https://artifacts.apis.io/directadmin/well-known/directadmin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/directadmin-security.txt
- group: agent
  href: https://artifacts.apis.io/directadmin/well-known/directadmin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/directadmin-well-known.yml
- group: other
  href: https://artifacts.apis.io/directadmin/hosts/directadmin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/directadmin-hosts.yml
- group: other
  href: https://artifacts.apis.io/directadmin/vendors/directadmin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/directadmin-vendors.yml
- group: build
  href: https://artifacts.apis.io/directadmin/packages/directadmin-packages.yml
  title: ''
  type: SDKs
  url: packages/directadmin-packages.yml
- group: build
  href: https://artifacts.apis.io/directadmin/packages/directadmin-packages.yml
  title: ''
  type: Packages
  url: packages/directadmin-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://directadmin.com/pricing.php
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.directadmin.com/changelog/version-1.713.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.directadmin.com/getting-started/installation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.directadmin.com/
- group: auth
  href: https://artifacts.apis.io/directadmin/security/directadmin-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/directadmin-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/directadmin/security/directadmin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/directadmin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://directadmin.com/
coverage:
  checked: '2026-10-27'
  detail: Documentation page lists a Swagger JSON at /static/swagger.json which returns 404, and no OpenAPI spec is publicly accessible.
  evidence:
  - status: 404
    url: https://directadmin.com/static/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: DirectAdmin provides a powerful web-based control panel for managing web hosting servers. It enables administrators to handle domains, email accounts, databases, and server resources through an intuitive graphical interface. The platform supports automation, reseller management, and integrates with popular web services, offering a comprehensive solution for hosting providers and system administrators seeking efficient server control.
layout: provider
modified: '2026-10-27'
name: DirectAdmin
nav: Providers
network: true
overview: 'DirectAdmin is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hosting, Control Panel, Web Hosting, Server Management, and Automation.


  The DirectAdmin catalog on APIs.io includes 1 Spectral governance ruleset.


  DirectAdmin''s developer surface includes changelog, pricing, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Directadmin Plans Pricing
  plan_count: 3
  slug: directadmin-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: DirectAdmin API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: directadmin-rules
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.8
    catalog_earned_first_party: 12.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 17.9
    discoverability: 53.6
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.8
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
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/directadmin/directadmin-2026-11-03T130739.png
security:
- kind: domain-security
  name: Directadmin Domain Security
  slug: directadmin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Directadmin Vulnerability Disclosure
  slug: directadmin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: directadmin
tags:
- Hosting
- Control Panel
- Web Hosting
- Server Management
- Automation
website: https://directadmin.com/
---
