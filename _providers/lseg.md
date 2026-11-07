---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - sandbox
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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-11-06'
api_count: 16
apis:
- baseURL: https://api-eit.refinitiv.com
  baseurl_source: declared
  description: 'LSEG API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: LSEG Intelligent Tagging (Open PermID) API
  slug: lseg-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Create, screen, update, archive, assign, link, and search screening cases; review and resolve screening results; enable ongoing screening and retrieve ongoing screening updates for KYC and third-party
  name: LSEG World-Check One Case API
  slug: lseg-world-check-one-case-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Retrieve MediaCheck adverse-media screening results, article metadata and content, attach or detach articles to cases, and mark articles as reviewed.
  name: LSEG World-Check One Media-Check API
  slug: lseg-world-check-one-media-check-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Enable, disable, and retrieve the MediaCheck smart filter on screening cases.
  name: LSEG World-Check One Smart Filter API
  slug: lseg-world-check-one-smart-filter-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Retrieve filtered audit events for screening cases to evidence compliance workflows.
  name: LSEG World-Check One Audit API
  slug: lseg-world-check-one-audit-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Retrieve and update the risk rating on a screening case.
  name: LSEG World-Check One Case Rating API
  slug: lseg-world-check-one-case-rating-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Create, retrieve, and delete relationships between screening cases.
  name: LSEG World-Check One Linked Cases API
  slug: lseg-world-check-one-linked-cases-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Retrieve groups, case templates, and resolution toolkits that govern how cases are created and results resolved.
  name: LSEG World-Check One Group API
  slug: lseg-world-check-one-group-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: List active users in the client account for case assignment.
  name: LSEG World-Check One User API
  slug: lseg-world-check-one-user-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Reference data for screening - countries, nationalities, providers, search filters, World-Check profiles and records, and PEP details.
  name: LSEG World-Check One Reference API
  slug: lseg-world-check-one-reference-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Maintain custom client watchlist sources and records for screening.
  name: LSEG World-Check One Client Watchlist API
  slug: lseg-world-check-one-client-watchlist-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Submit asynchronous case report requests, poll report status, and download completed reports.
  name: LSEG World-Check One Reporting API
  slug: lseg-world-check-one-reporting-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Report status listing, report error details, and report cancellation operations.
  name: LSEG World-Check One Upcoming API
  slug: lseg-world-check-one-upcoming-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Generate machine-readable zone (MRZ) data for passport verification.
  name: LSEG World-Check One Passport Check API
  slug: lseg-world-check-one-passport-check-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Zero Footprint Screening surface - synchronous screening, groups, case templates, reference data, and client watchlist maintenance without persisting case data.
  name: LSEG World-Check One Zero Footprint Screening API
  slug: lseg-world-check-one-zfs-api
- baseURL: https://api-worldcheck.refinitiv.com/v2
  baseurl_source: declared
  description: Retrieve information about the public API, including the current API version.
  name: LSEG World-Check One API Info API
  slug: lseg-world-check-one-api-info-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/lseg/capabilities/lseg-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lseg-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/lseg/rules/lseg-rules.yml
  title: ''
  type: Spectral
  url: rules/lseg-rules.yml
- group: design
  href: https://artifacts.apis.io/lseg/json-ld/lseg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lseg-context.jsonld
- group: design
  href: https://artifacts.apis.io/lseg/vocabulary/lseg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lseg-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lseg/data-model/lseg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lseg-data-model.yml
- group: design
  href: https://artifacts.apis.io/lseg/conformance/lseg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lseg-conformance.yml
- group: other
  href: https://artifacts.apis.io/lseg/hosts/lseg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lseg-hosts.yml
- group: build
  href: https://artifacts.apis.io/lseg/integrations/lseg-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/lseg-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/lseg/vendors/lseg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lseg-vendors.yml
- group: build
  href: https://artifacts.apis.io/lseg/packages/lseg-packages.yml
  title: ''
  type: SDKs
  url: packages/lseg-packages.yml
- group: build
  href: https://artifacts.apis.io/lseg/packages/lseg-packages.yml
  title: ''
  type: Packages
  url: packages/lseg-packages.yml
- group: agent
  href: https://artifacts.apis.io/lseg/well-known/lseg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lseg-well-known.yml
- group: design
  href: https://artifacts.apis.io/lseg/conventions/lseg-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lseg-conventions.yml
- group: start
  href: https://artifacts.apis.io/lseg/sandbox/lseg-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lseg-sandbox.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.lseg.com/en/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.lseg.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lseg.com/en/policies/privacy-statement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lseg.com/en
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lseg.com/en/api-catalog/app-studio/app-studio-web-sdk/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lseg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LSEG
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LSEG-API-Samples
- group: auth
  href: https://artifacts.apis.io/lseg/security/lseg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lseg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lseg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lseg.com/en/api-catalog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/documentation
- group: company
  title: ''
  type: Blog
  url: https://developers.lseg.com/en/article-catalog
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it; its MCP endpoint (support.lseg.com/mcp/v1) answers 401, so access sits behind a customer login
  evidence:
  - status: 401
    url: https://support.lseg.com/mcp/v1
  - status: 200
    url: https://www.lseg.com/
  reason: customer-only-docs
  state: gated
created: '2026-09-21'
description: LSEG (London Stock Exchange Group) is a leading global financial markets infrastructure and data provider, offering a broad range of services including data & analytics, FTSE Russell indices, trading venues, FX, post‑trade solutions and risk intelligence. It serves customers worldwide, enabling sustainable growth and stability through trusted data and innovative technology platforms.
image: https://www.lseg.com/content/dam/lseg/en_us/images/logos/thumbnail/lseg-default-social-image.jpg.transform/rect-768/q90/image.jpg
json_schemas:
- name: PostPermidCalaisRequest
  property_count: 3
  slug: lseg-post-permid-calais-request
- name: PostPermidCalaisResponse
  property_count: 1
  slug: lseg-post-permid-calais-response
- name: PostTagRsEnrichRequest
  property_count: 1
  slug: lseg-post-tag-rs-enrich-request
- name: PostTagRsEnrichResponse
  property_count: 1
  slug: lseg-post-tag-rs-enrich-response
jsonld:
- class_count: 4
  name: Lseg Context
  property_count: 4
  slug: lseg-context
layout: provider
modified: '2026-10-20'
name: LSEG
nav: Providers
network: true
overview: 'LSEG publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Intelligent Tagging (Open PermID) API, World-Check One Case API, World-Check One Media-Check API, and 13 more. Tagged areas include Company, Finance, Data, Infrastructure, and Markets.


  The LSEG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LSEG''s developer surface includes sandbox, support, getting-started guide, documentation, API reference, engineering blog, and 21 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: LSEG API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: lseg-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 51.2
    discoverability: 71.4
    operational_transparency: 2.6
  previous_composite: 42.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 6.3
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/lseg/lseg-2026-10-11T110608.png
security:
- kind: domain-security
  name: Lseg Domain Security
  slug: lseg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lseg
tags:
- Company
- Finance
- Data
- Infrastructure
- Markets
- Stock Exchange
- Market Data
- KYC
- Compliance
website: https://www.lseg.com/
---
