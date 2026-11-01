---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'CiviCRM API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: CiviCRM API
  slug: civicrm-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/civicrm/rules/civicrm-rules.yml
  title: ''
  type: Spectral
  url: rules/civicrm-rules.yml
- group: design
  href: https://artifacts.apis.io/civicrm/vocabulary/civicrm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/civicrm-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/civicrm/cli/civicrm-cli.yml
  title: ''
  type: CLI
  url: cli/civicrm-cli.yml
- group: design
  href: https://artifacts.apis.io/civicrm/conformance/civicrm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/civicrm-conformance.yml
- group: other
  href: https://artifacts.apis.io/civicrm/hosts/civicrm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/civicrm-hosts.yml
- group: build
  href: https://artifacts.apis.io/civicrm/packages/civicrm-packages.yml
  title: ''
  type: SDKs
  url: packages/civicrm-packages.yml
- group: build
  href: https://artifacts.apis.io/civicrm/packages/civicrm-packages.yml
  title: ''
  type: Packages
  url: packages/civicrm-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://civicrm.org/help
- group: auth
  title: ''
  type: Security
  url: https://civicrm.org/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://civicrm.org/about/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://civicrm.org/user/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/civicrm/
- group: company
  title: ''
  type: Blog
  url: https://civicrm.org/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.civicrm.org/
- group: auth
  href: https://artifacts.apis.io/civicrm/security/civicrm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/civicrm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/civicrm/security/civicrm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/civicrm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://civicrm.org/
coverage:
  checked: '2026-10-27'
  detail: CiviCRM documentation provides HTML API reference but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.civicrm.org/dev/en/latest/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: CiviCRM is an open-source constituent relationship management (CRM) platform designed for non-profit, civic sector, and advocacy organizations. It provides a web-based suite of tools for managing contacts, fundraising, events, memberships, email communications, and case management, integrating with popular content management systems like WordPress, Joomla, and Drupal. The platform is community-driven, extensible via extensions, and supports multilingual deployments, helping organizations engage supporters and streamline operations.
layout: provider
modified: '2026-10-27'
name: CiviCRM
nav: Providers
network: true
overview: 'CiviCRM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source, CRM, Nonprofit, Community, and PHP.


  The CiviCRM catalog on APIs.io includes 1 Spectral governance ruleset.


  CiviCRM''s developer surface includes CLI, support, engineering blog, documentation, and 13 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: CiviCRM API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: civicrm-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 31.0
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Civicrm Domain Security
  slug: civicrm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Civicrm Vulnerability Disclosure
  slug: civicrm-vulnerability-disclosure
  summary_line: no policy recorded
slug: civicrm
tags:
- Open Source
- CRM
- Nonprofit
- Community
- PHP
- Extensions
website: https://civicrm.org/
---
