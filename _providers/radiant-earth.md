---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 5
  name: Radiant Earth Agentic Access
  operation_count: 31
  slug: radiant-earth-agentic-access
  summary_line: 31 operations · 19 acting · 5 human-in-the-loop
api_count: 2
apis:
- baseURL: https://source.coop/api/v1
  baseurl_source: declared
  description: The Accounts API from Radiant Earth — 6 operation(s) for accounts.
  name: Radiant Earth Accounts API
  slug: radiant-earth-accounts-api
- baseURL: https://source.coop/api/v1
  baseurl_source: declared
  description: The API Keys API from Radiant Earth — 3 operation(s) for api keys.
  name: Radiant Earth API Keys API
  slug: radiant-earth-api-keys-api
- baseURL: https://source.coop/api/v1
  baseurl_source: declared
  description: The Authentication API from Radiant Earth — 1 operation(s) for authentication.
  name: Radiant Earth Authentication API
  slug: radiant-earth-authentication-api
- baseURL: https://source.coop/api/v1
  baseurl_source: declared
  description: The Data Connections API from Radiant Earth — 3 operation(s) for data connections.
  name: Radiant Earth Data Connections API
  slug: radiant-earth-data-connections-api
- baseURL: https://source.coop/api/v1
  baseurl_source: declared
  description: The Memberships API from Radiant Earth — 6 operation(s) for memberships.
  name: Radiant Earth Memberships API
  slug: radiant-earth-memberships-api
- baseURL: https://source.coop/api/v1
  baseurl_source: declared
  description: The Repositories API from Radiant Earth — 4 operation(s) for repositories.
  name: Radiant Earth Repositories API
  slug: radiant-earth-repositories-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/agentic-access/radiant-earth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/radiant-earth-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/rules/radiant-earth-stac-api-spec-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/radiant-earth-stac-api-spec-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/rules/radiant-earth-rules.yml
  title: ''
  type: Spectral
  url: rules/radiant-earth-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/json-ld/radiant-earth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/radiant-earth-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/vocabulary/radiant-earth-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/radiant-earth-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/data-model/radiant-earth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/radiant-earth-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/components/radiant-earth-components.yml
  title: ''
  type: Components
  url: components/radiant-earth-components.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/cli/radiant-earth-cli.yml
  title: ''
  type: CLI
  url: cli/radiant-earth-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/changelog/radiant-earth-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/radiant-earth-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/conventions/radiant-earth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/radiant-earth-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/lifecycle/radiant-earth-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/radiant-earth-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/lifecycle/radiant-earth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/radiant-earth-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/errors/radiant-earth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/radiant-earth-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/conformance/radiant-earth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/radiant-earth-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/overlays/radiant-earth-source-cooperative-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/radiant-earth-source-cooperative-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/hosts/radiant-earth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/radiant-earth-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/vendors/radiant-earth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/radiant-earth-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/packages/radiant-earth-packages.yml
  title: ''
  type: SDKs
  url: packages/radiant-earth-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/packages/radiant-earth-packages.yml
  title: ''
  type: Packages
  url: packages/radiant-earth-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/authentication/radiant-earth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/radiant-earth-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/security/radiant-earth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/radiant-earth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://radiant.earth/
- group: company
  title: ''
  type: Blog
  url: https://radiant.earth/blog/
- group: other
  title: ''
  type: RSSFeed
  url: https://radiant.earth/index.xml
- group: company
  title: ''
  type: About
  url: https://radiant.earth/about/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/radiantearth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://radiant.earth/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://radiant.earth/privacy/
- group: other
  title: ''
  type: Donate
  url: https://radiant.earth/donate/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/radiantearth/stac-api-spec/blob/604ade6158de15b8ab068320ca41e25e2bf0e116/.circleci/.spectral.yml
created: '2026-10-09'
description: Radiant Earth is a 501(c)(3) non-profit working to increase shared understanding of our world by making data easier to access and use. Its initiatives include Source Cooperative, a data publishing utility for the web that lets trusted organizations and individuals publish data of any kind at any scale, and the Cloud-Native Geospatial Forum (CNG), which convenes vendor-neutral events and education for geospatial data practitioners. Through its GitHub organization (radiantearth) it stewards open geospatial specifications such as the SpatioTemporal Asset Catalog (STAC) API spec, and it provides fiscal sponsorship and support services to aligned data initiatives.
image: https://radiant.earth/homepage-og.webp
json_schemas:
- name: Account
  property_count: 6
  slug: radiant-earth-account
- name: APIKey
  property_count: 7
  slug: radiant-earth-apikey
- name: DataConnection
  property_count: 8
  slug: radiant-earth-data-connection
- name: Membership
  property_count: 7
  slug: radiant-earth-membership
- name: RedactedAPIKey
  property_count: 6
  slug: radiant-earth-redacted-apikey
- name: Repository
  property_count: 9
  slug: radiant-earth-repository
jsonld:
- class_count: 27
  name: Radiant Earth Context
  property_count: 49
  slug: radiant-earth-context
layout: provider
modified: '2026-10-09'
name: Radiant Earth
nav: Providers
network: true
overview: 'Radiant Earth publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, API Keys API, Authentication API, and 3 more. Tagged areas include Company, Non-Profit, Open Data, Geospatial, and Earth Observation.


  The Radiant Earth catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Radiant Earth''s developer surface includes CLI, changelog, authentication, engineering blog, and 26 more developer resources.'
plans:
- name: Radiant Earth Plans Pricing
  plan_count: 0
  slug: radiant-earth-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Radiant Earth Rate Limits
  slug: radiant-earth-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Radiant Earth API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: radiant-earth-rules
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Radiant Earth — stac api spec rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: radiant-earth-stac-api-spec-spectral-rules
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 66.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/radiant-earth/refs/heads/main/screenshots/radiant-earth-2026-10-11T113104.png
security:
- kind: authentication
  name: Radiant Earth Authentication
  slug: radiant-earth-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Radiant Earth Domain Security
  slug: radiant-earth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: radiant-earth
tags:
- Company
- Non-Profit
- Open Data
- Geospatial
- Earth Observation
- Cloud-Native Geospatial
- STAC
- Data Publishing
website: https://radiant.earth/
---
