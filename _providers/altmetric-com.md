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
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for accessing Altmetric data such as metrics, details pages, and badges.
  name: Altmetric API
  slug: altmetric-api
- baseURL: https://www.altmetric.com
  baseurl_source: declared
  description: 'Altmetric API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Altmetric API
  slug: altmetric-com-api
artifact_total: 12
common:
- group: auth
  href: https://artifacts.apis.io/altmetric-com/well-known/altmetric-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/altmetric-com-status-security.txt
- group: design
  href: https://artifacts.apis.io/altmetric-com/rules/altmetric-com-rules.yml
  title: ''
  type: Spectral
  url: rules/altmetric-com-rules.yml
- group: design
  href: https://artifacts.apis.io/altmetric-com/json-ld/altmetric-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/altmetric-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/altmetric-com/vocabulary/altmetric-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/altmetric-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/altmetric-com/data-model/altmetric-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/altmetric-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/altmetric-com/changelog/altmetric-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/altmetric-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/altmetric-com/conformance/altmetric-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altmetric-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/altmetric-com/well-known/altmetric-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altmetric-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/altmetric-com/hosts/altmetric-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altmetric-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/altmetric-com/vendors/altmetric-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altmetric-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/altmetric-com/packages/altmetric-com-packages.yml
  title: ''
  type: SDKs
  url: packages/altmetric-com-packages.yml
- group: build
  href: https://artifacts.apis.io/altmetric-com/packages/altmetric-com-packages.yml
  title: ''
  type: Packages
  url: packages/altmetric-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altmetric.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://help.altmetric.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.altmetric.com/
- group: auth
  title: ''
  type: Security
  url: https://www.altmetric.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altmetric.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://altmetric.com/explorer/login
- group: company
  title: ''
  type: Blog
  url: https://www.altmetric.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.altmetric.com/en/categories/2060289-getting-started-with-altmetric
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/altmetric
- group: auth
  href: https://artifacts.apis.io/altmetric-com/security/altmetric-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/altmetric-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/altmetric-com/security/altmetric-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altmetric-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.altmetric.com/
- group: docs
  title: ''
  type: Documentation
  url: https://details-page-api-docs.altmetric.com/index.html
- group: docs
  title: ''
  type: ImplementationGuide
  url: https://implementation-docs.altmetric.com/
coverage:
  checked: '2026-11-01'
  detail: Documentation is public but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.altmetric.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Altmetric provides tools that track and analyze online attention markers to published research, helping scholars, institutions, and funders understand the impact and reach of their work across news outlets, social media, policy documents, and more. By aggregating mentions from a wide range of sources, Altmetric enables users to see where research is making a difference and to showcase its influence in the digital world.
image: https://wordpress-uploads-production.s3.amazonaws.com/uploads/2022/09/Altmetric_rgb.png
json_schemas:
- name: GetExplorerApiResearchOutputsDemographicsResponse
  property_count: 17
  slug: altmetric-com-get-explorer-api-research-outputs-demographics-response
- name: GetExplorerApiResearchOutputsJournalsResponse
  property_count: 39
  slug: altmetric-com-get-explorer-api-research-outputs-journals-response
- name: GetExplorerApiResearchOutputsMentionsResponse
  property_count: 4
  slug: altmetric-com-get-explorer-api-research-outputs-mentions-response
- name: GetV1FetchDoi101038News2011490Response
  property_count: 9
  slug: altmetric-com-get-v1-fetch-doi101038-news2011490-response
- name: GetVersionFetchIdentifiertypeIdResponse
  property_count: 9
  slug: altmetric-com-get-version-fetch-identifiertype-id-response
- name: GetVersionIdentifiertypeIdResponse
  property_count: 53
  slug: altmetric-com-get-version-identifiertype-id-response
jsonld:
- class_count: 6
  name: Altmetric Com Context
  property_count: 77
  slug: altmetric-com-context
layout: provider
modified: '2026-11-01'
name: Altmetric
nav: Providers
network: true
overview: 'Altmetric is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Research, Metrics, Analytics, Scholarly Communication, and Altmetrics.


  The Altmetric catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Altmetric''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, and 21 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Altmetric API Rules
  rule_count: 38
  severity_counts:
    error: 33
    hint: 0
    info: 4
    warn: 1
  slug: altmetric-com-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 24.8
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 38.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altmetric Com Domain Security
  slug: altmetric-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Altmetric Com Vulnerability Disclosure
  slug: altmetric-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: altmetric-com
tags:
- Research
- Metrics
- Analytics
- Scholarly Communication
- Altmetrics
website: https://www.altmetric.com/
---
