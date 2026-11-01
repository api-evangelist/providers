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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: KingswaySoft provides integration toolkit APIs documented on their developer portal.
  name: KingswaySoft API
  slug: kingswaysoft-api-2
- description: 'KingswaySoft API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: KingswaySoft API
  slug: kingswaysoft-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/kingswaysoft/rules/kingswaysoft-rules.yml
  title: ''
  type: Spectral
  url: rules/kingswaysoft-rules.yml
- group: design
  href: https://artifacts.apis.io/kingswaysoft/vocabulary/kingswaysoft-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kingswaysoft-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/kingswaysoft/changelog/kingswaysoft-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kingswaysoft-changelog.yml
- group: design
  href: https://artifacts.apis.io/kingswaysoft/conformance/kingswaysoft-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kingswaysoft-conformance.yml
- group: other
  href: https://artifacts.apis.io/kingswaysoft/hosts/kingswaysoft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kingswaysoft-hosts.yml
- group: other
  href: https://artifacts.apis.io/kingswaysoft/vendors/kingswaysoft-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kingswaysoft-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.kingswaysoft.com/connectors/api/stripe/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kingswaysoft.com/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.kingswaysoft.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kingswaysoft.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.kingswaysoft.com/about-us/news
- group: start
  title: ''
  type: Login
  url: https://www.kingswaysoft.com/Store/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kingswaysoft.com/about-us/careers/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.kingswaysoft.com/products/ssis-integration-toolkit/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.kingswaysoft.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kingswaysoft.com/products/integration-gateway/help-manual/installation-and-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KingswaySoft
- group: auth
  href: https://artifacts.apis.io/kingswaysoft/security/kingswaysoft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kingswaysoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kingswaysoft.com/
coverage:
  checked: '2026-10-20'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.kingswaysoft.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: KingswaySoft provides data integration solutions, offering the SSIS Integration Toolkit and a wide range of connectors for enterprise applications such as Dynamics 365, Salesforce, NetSuite, and more. Their platform enables seamless data movement between systems, supporting both on-premises and cloud environments, and includes JDBC drivers, integration gateway, and extensive documentation for developers.
layout: provider
modified: '2026-10-20'
name: KingswaySoft
nav: Providers
network: true
overview: 'KingswaySoft is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, ETL, Microsoft SSIS, Connectors, and Enterprise.


  The KingswaySoft catalog on APIs.io includes 1 Spectral governance ruleset.


  KingswaySoft''s developer surface includes changelog, support, engineering blog, getting-started guide, and 15 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: KingswaySoft API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: kingswaysoft-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 9.2
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kingswaysoft Domain Security
  slug: kingswaysoft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kingswaysoft
tags:
- Data Integration
- ETL
- Microsoft SSIS
- Connectors
- Enterprise
website: https://kingswaysoft.com/
---
