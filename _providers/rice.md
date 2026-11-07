---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rice Agentic Access
  operation_count: 5
  slug: rice-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Rice University's own Shibboleth/SAML 2.0 identity provider, publishing a live EntityDescriptor with an IDPSSODescriptor, a shibmd:Scope of rice.edu and support for SAML 1.1, SAML 2.0 and the Shibbole
  name: Rice Shibboleth SAML 2.0 Identity Provider
  slug: sso-shibboleth
- description: Rice's identity provider is registered in InCommon, the US research and education identity federation, and InCommon's metadata query service returns a signed EntityDescriptor for entityID https://idp.
  name: InCommon Federation registration
  slug: incommon-federation
- description: 'Rice University is a DataCite direct member, registered 2017-11-13 as provider `rice` (symbol RICE) under Fondren Library and linked to ROR https://ror.org/008zs3103. The membership carries eight DOI '
  name: DataCite membership — Fondren Library, Rice University
  slug: datacite
- description: Rice University's entry in the Research Organization Registry, ROR ID https://ror.org/008zs3103. It is the identifier DataCite's member record for Fondren Library points at, and the canonical machine-
  name: ROR registration — Rice University
  slug: ror
- description: Rice's public course catalog and schedule search, served from courses.rice.edu on Rice's own network (128.42.207.157, RICENET). It is an Ellucian Banner self-service interface (SWKSCAT) with a Rice-au
  name: Rice University Course Schedule
  slug: course-schedule
- description: 'The Rice Research Repository (R-3) is Fondren Library''s institutional repository, holding Rice theses, dissertations and scholarship back to 2005 and minting DOIs on Rice''s own DataCite prefixes. The '
  name: Rice Research Repository (DSpaceDirect tenancy) — REST API
  slug: repository-rest
- description: 'OAI-PMH 2.0 harvesting endpoint for the Rice Research Repository. Identify returns repositoryName "Rice Research Repository", repositoryIdentifier repository.rice.edu, adminEmail cds@rice.edu (Rice''s '
  name: Rice Research Repository (DSpaceDirect tenancy) — OAI-PMH
  slug: repository-oai
- baseURL: https://lg4tooqkr1.execute-api.us-east-1.amazonaws.com/prod
  baseurl_source: declared
  description: The public dataset catalog of the Urban Data Platform.
  name: Rice University Datasets API
  slug: rice-datasets-api
- baseURL: https://lg4tooqkr1.execute-api.us-east-1.amazonaws.com/prod
  baseurl_source: declared
  description: Controlled vocabularies the catalog's fields draw from.
  name: Rice University Reference API
  slug: rice-reference-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/rice/llms/rice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rice-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.rice.edu
- group: agent
  href: https://artifacts.apis.io/rice/agentic-access/rice-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rice-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/rice/rules/rice-rules.yml
  title: ''
  type: Spectral
  url: rules/rice-rules.yml
- group: design
  href: https://artifacts.apis.io/rice/json-ld/rice-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rice-context.jsonld
- group: design
  href: https://artifacts.apis.io/rice/vocabulary/rice-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rice-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rice/data-model/rice-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rice-data-model.yml
- group: design
  href: https://artifacts.apis.io/rice/errors/rice-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rice-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rice/conformance/rice-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rice-conformance.yml
- group: auth
  href: https://artifacts.apis.io/rice/well-known/rice-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rice-status-security.txt
- group: agent
  href: https://artifacts.apis.io/rice/well-known/rice-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rice-well-known.yml
- group: other
  href: https://artifacts.apis.io/rice/hosts/rice-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rice-hosts.yml
- group: build
  href: https://artifacts.apis.io/rice/integrations/rice-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/rice-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/rice/vendors/rice-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rice-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.rice.edu/
- group: other
  title: ''
  type: OpenData
  url: https://www.kinderudp.org/
- group: docs
  href: https://artifacts.apis.io/rice/openapi/_ae-authored/rice-kinder-udp-openapi.yml
  title: ''
  type: APIReference
  url: openapi/_ae-authored/rice-kinder-udp-openapi.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.rice.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.rice.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.rice.edu/
- group: other
  href: https://artifacts.apis.io/rice/identity-federation/rice-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/rice-identity-federation.yml
- group: other
  title: ''
  type: ResearchComputing
  url: https://researchcomputing.rice.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rice-crc
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RiceUniversity
- group: auth
  href: https://artifacts.apis.io/rice/authentication/rice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rice-authentication.yml
- group: design
  href: https://artifacts.apis.io/rice/conformance/rice-education-standards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rice-education-standards-conformance.yml
- group: design
  href: https://artifacts.apis.io/rice/errors/rice-errors.yml
  title: ''
  type: Errors
  url: errors/rice-errors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rice.edu/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.rice.edu/808
- group: operate
  title: ''
  type: Support
  url: https://kb.rice.edu/
- group: operate
  title: ''
  type: Status
  url: https://status.rice.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/rice-university/
- group: auth
  href: https://artifacts.apis.io/rice/security/rice-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rice-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/rice/plans/rice-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rice-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/rice/rate-limits/rice-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rice-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rice/finops/rice-finops.yml
  title: ''
  type: FinOps
  url: finops/rice-finops.yml
- group: other
  href: https://artifacts.apis.io/rice/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Rice University is a private research university in Houston, Texas. Its programmable footprint is small, and most of what appears to be Rice''s is not: the Rice Research Repository at repository.rice.edu is a CNAME to rice.dspacedirect.org and runs on DSpaceDirect, the Lyrasis-hosted DSpace service, so its REST and OAI-PMH contracts are the platform''s engineering on Rice''s content, recorded here as a tenancy rather than credited to Rice. What Rice genuinely operates is three things. It runs its own Shibboleth/SAML 2.0 identity provider at idp.rice.edu, on Rice''s own ARIN allocation behind an InCommon-issued certificate, and registers it in the InCommon federation — the strongest machine-readable contract on Rice''s public surface. It is a direct DataCite member (symbol RICE, eight prefixes, 2,169 DOIs) through Fondren Library. And its Kinder Institute for Urban Research operates the Urban Data Platform, a genuinely public, unauthenticated JSON API serving a 431-dataset Houston-region
  urban data catalog with its own controlled vocabularies and DataCite DOIs — undocumented, unadvertised, and the only self-operated callable API Rice has. There is no central developer portal, no llms.txt, no .well-known catalog, and the official RiceUniversity GitHub organization has zero public repositories; Rice''s Center for Research Computing publishes separately at github.com/rice-crc.'
examples:
- key_count: 2
  name: Rice Kinder Udp Dataset Detail Example
  slug: rice-kinder-udp-dataset-detail-example
- key_count: 3
  name: Rice Kinder Udp Datasets Example
  slug: rice-kinder-udp-datasets-example
- key_count: 2
  name: Rice Kinder Udp Lookups Example
  slug: rice-kinder-udp-lookups-example
- key_count: 2
  name: Rice Repository Dspace Root Example
  slug: rice-repository-dspace-root-example
finops:
- has_sources: true
  method: generated
  name: Rice Finops
  primary_unit: ''
  service_category: Education
  slug: rice-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rice.png
json_schemas:
- name: Rice Kinder Institute Urban Data Platform — Dataset
  property_count: 32
  slug: rice-kinder-udp-dataset
jsonld:
- class_count: 13
  name: Rice Context
  property_count: 5
  slug: rice-context
layout: provider
modified: '2026-09-01'
name: Rice University
nav: Providers
network: true
overview: 'Rice University publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datasets API, Reference API, and 7 more. Tagged areas include University, Higher Education, Education, United States, and Texas.


  The Rice University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rice University''s developer surface includes API reference, GitHub presence, authentication, support, status page, and 32 more developer resources.'
plans:
- name: Rice Plans Pricing
  plan_count: 2
  slug: rice-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Rice Rate Limits
  slug: rice-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Rice University API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: rice-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.0
    catalog_earned_first_party: 5.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 26.3
    contract_governance: 33.3
    contract_quality: 59.9
    developer_ergonomics: 38.1
    discoverability: 73.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/rice/rice-2026-06-20T193109.png
security:
- kind: authentication
  name: Rice Authentication
  slug: rice-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rice Domain Security
  slug: rice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rice
tags:
- University
- Higher Education
- Education
- United States
- Texas
- Private Research University
- Association of American Universities
- Research Data
- Open Data
- Research Repository
- Course Catalog
- Identity Federation
- Library
- Urban Research
website: https://www.rice.edu/
---
