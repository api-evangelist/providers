---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Ecmwf Agentic Access
  operation_count: 54
  slug: ecmwf-agentic-access
  summary_line: 54 operations · 17 acting
api_count: 6
apis:
- baseURL: https://cds.climate.copernicus.eu/api/retrieve/v1
  baseurl_source: declared
  description: OGC API - Processes compliant REST API that enables the submission of processing tasks (data retrieval) to the ECMWF Data Stores system (Climate, Atmosphere and Early Warning Data Stores), with job mo
  name: ECMWF Data Stores Processing API
  slug: ecmwf-data-stores-processing-api
- baseURL: https://cds.climate.copernicus.eu/api/catalogue/v1
  baseurl_source: declared
  description: STAC compliant API to access the ECMWF Data Stores catalogues - dataset collections, search, licences and keyword vocabularies, and dataset messages and changelogs.
  name: ECMWF Data Stores STAC Catalogue API
  slug: ecmwf-data-stores-stac-catalogue-api
- baseURL: https://cds.climate.copernicus.eu/api/profiles/v1
  baseurl_source: declared
  description: REST API to handle user authentication and users' data for the ECMWF Data Stores (OIDC and personal access token verification, licence acceptance, starred datasets and profile vocabularies).
  name: ECMWF Data Stores Profile API
  slug: ecmwf-data-stores-profile-api
- description: Programmatic access to ECMWF data archives (MARS and public datasets) through the ECMWF Web API at api.ecmwf.int, used by the ecmwf-api-client Python library with a personal API key. No machine-readab
  name: ECMWF Web API
  slug: ecmwf-web-api
artifact_total: 36
common:
- group: agent
  href: https://artifacts.apis.io/ecmwf/agentic-access/ecmwf-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ecmwf-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ecmwf/rules/ecmwf-rules.yml
  title: ''
  type: Spectral
  url: rules/ecmwf-rules.yml
- group: design
  href: https://artifacts.apis.io/ecmwf/json-ld/ecmwf-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ecmwf-context.jsonld
- group: design
  href: https://artifacts.apis.io/ecmwf/vocabulary/ecmwf-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ecmwf-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ecmwf/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ecmwf/data-model/ecmwf-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ecmwf-data-model.yml
- group: design
  href: https://artifacts.apis.io/ecmwf/conventions/ecmwf-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ecmwf-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ecmwf/authentication/ecmwf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ecmwf-authentication.yml
- group: design
  href: https://artifacts.apis.io/ecmwf/lifecycle/ecmwf-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ecmwf-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ecmwf/errors/ecmwf-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ecmwf-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ecmwf/conformance/ecmwf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecmwf-conformance.yml
- group: other
  href: https://artifacts.apis.io/ecmwf/overlays/ecmwf-catalogue-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ecmwf-catalogue-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ecmwf/well-known/ecmwf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecmwf-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecmwf/hosts/ecmwf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecmwf-hosts.yml
- group: build
  href: https://artifacts.apis.io/ecmwf/integrations/ecmwf-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/ecmwf-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/ecmwf/packages/ecmwf-packages.yml
  title: ''
  type: SDKs
  url: packages/ecmwf-packages.yml
- group: build
  href: https://artifacts.apis.io/ecmwf/packages/ecmwf-packages.yml
  title: ''
  type: Packages
  url: packages/ecmwf-packages.yml
- group: auth
  href: https://artifacts.apis.io/ecmwf/security/ecmwf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecmwf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ecmwf.int/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ecmwf.int/en/forecasts/documentation-and-support
- group: docs
  title: ''
  type: APIReference
  url: https://www.ecmwf.int/en/computing/software/ecmwf-web-api
- group: docs
  title: ''
  type: Documentation
  url: https://confluence.ecmwf.int/display/WEBAPI
- group: other
  title: ''
  type: OpenData
  url: https://data.ecmwf.int/
- group: operate
  title: ''
  type: Support
  url: https://www.ecmwf.int/en/support
- group: company
  title: ''
  type: Blog
  url: https://www.ecmwf.int/en/about/media-centre/science-blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.ecmwf.int/en/about/media-centre/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ecmwf
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ecmwf.int/en/forecasts/accessing-forecasts/licences-available
- group: start
  title: ''
  type: SignUp
  url: https://www.ecmwf.int/user/register
- group: start
  title: ''
  type: Login
  url: https://www.ecmwf.int/user/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ecmwf.int/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ecmwf.int/en/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecmwf.int/en/privacy
created: '2026-10-18'
description: ECMWF, the European Centre for Medium-Range Weather Forecasts, is an intergovernmental organisation that is both a research institute and a 24/7 operational service, producing global numerical weather predictions and other data for its Member and Co-operating States and the broader community. It operates one of the largest supercomputer facilities and meteorological data archives in the world, and offers programmatic data access through the ECMWF Web API and its Free & Open Data portal.
image: https://www.ecmwf.int/themes/ecmwf/logo.svg
json_schemas:
- name: Collection
  property_count: 13
  slug: ecmwf-collection
- name: Collections
  property_count: 4
  slug: ecmwf-collections
- name: Content
  property_count: 8
  slug: ecmwf-content
- name: DeleteJob
  property_count: 12
  slug: ecmwf-delete-job
- name: FormData
  property_count: 8
  slug: ecmwf-form-data
- name: GetJob
  property_count: 12
  slug: ecmwf-get-job
- name: GetProcess
  property_count: 12
  slug: ecmwf-get-process
- name: LandingPage
  property_count: 8
  slug: ecmwf-landing-page
- name: Licence
  property_count: 9
  slug: ecmwf-licence
- name: MinimalUserInfo
  property_count: 4
  slug: ecmwf-minimal-user-info
- name: PostProcessExecute
  property_count: 12
  slug: ecmwf-post-process-execute
- name: PostProcessExecution
  property_count: 12
  slug: ecmwf-post-process-execution
- name: RequestCost
  property_count: 6
  slug: ecmwf-request-cost
- name: ThematicActivities
  property_count: 1
  slug: ecmwf-thematic-activities
- name: UserCreationData
  property_count: 7
  slug: ecmwf-user-creation-data
- name: UserData
  property_count: 6
  slug: ecmwf-user-data
- name: UserInfo
  property_count: 16
  slug: ecmwf-user-info
- name: UserPAT
  property_count: 3
  slug: ecmwf-user-pat
jsonld:
- class_count: 102
  name: Ecmwf Context
  property_count: 176
  slug: ecmwf-context
layout: provider
modified: '2026-10-18'
name: ECMWF
nav: Providers
network: true
overview: 'ECMWF publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Stores Processing API, Data Stores STAC Catalogue API, Data Stores Profile API, and 1 more. Tagged areas include Company, Weather, Meteorology, Forecasting, and Climate.


  The ECMWF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ECMWF''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Ecmwf Plans Pricing
  plan_count: 0
  slug: ecmwf-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Ecmwf Rate Limits
  slug: ecmwf-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ECMWF API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 5
  slug: ecmwf-rules
scopes:
- name: Ecmwf Scopes
  scope_count: 0
  slug: ecmwf-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 58.5
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ecmwf Authentication
  slug: ecmwf-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ecmwf Domain Security
  slug: ecmwf-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 6
skills:
- name: ecmwf-accept-dataset-licences
  slug: ecmwf-accept-dataset-licences
- name: ecmwf-discover-datasets
  slug: ecmwf-discover-datasets
- name: ecmwf-execute-process-and-retrieve-results
  slug: ecmwf-execute-process-and-retrieve-results
- name: ecmwf-manage-account-and-token
  slug: ecmwf-manage-account-and-token
- name: ecmwf-manage-jobs
  slug: ecmwf-manage-jobs
- name: ecmwf-retrieve-dataset
  slug: ecmwf-retrieve-dataset
slug: ecmwf
tags:
- Company
- Weather
- Meteorology
- Forecasting
- Climate
- Open Data
- Research
- Intergovernmental
website: https://www.ecmwf.int/
---
