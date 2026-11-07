---
access_model:
  confidence: high
  label: Free · no credential required
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Self-hosted DSpace 9.1 institutional repository on Vanderbilt''s own domain and infrastructure. The HAL REST API root at irbe.library.vanderbilt.edu/server/api advertises 80 link relations and reports '
  name: Vanderbilt Institutional Repository (VUIR)
  slug: institutional-repository
- description: OAI-PMH 2.0 harvesting endpoint for the Vanderbilt Institutional Repository. Identify returns repositoryName "Vanderbilt Institutional Repository", repositoryIdentifier ir.vanderbilt.edu and adminEmai
  name: Vanderbilt Institutional Repository OAI-PMH
  slug: institutional-repository-oai-pmh
- description: Vanderbilt's Okta organisation on its own custom domain onevu.vanderbilt.edu (CNAME to vanderbilt.customdomains.okta.com). Publishes a live OpenID Connect discovery document and SAML 2.0 IdP metadata.
  name: Vanderbilt Okta Identity Provider (OneVU)
  slug: onevu-identity
- description: 'The vanderbilt.edu Microsoft Entra ID tenant (ba5a7f39-e3be-4ab3-b450-67fa80faecad), publishing live OpenID Connect discovery and SAML 2.0 / WS-Federation metadata. A federation surface: shared platfo'
  name: Vanderbilt Microsoft Entra ID Tenant
  slug: entra-identity
- description: SAML 2.0 Service Provider metadata for the Vanderbilt Institutional Repository, entityID https://ir.vanderbilt.edu/shibboleth, served live from the repository host. The DiscoFeed names the Okta IdP it
  name: VUIR Shibboleth Service Provider
  slug: shibboleth-service-provider
- description: Vanderbilt's library discovery layer runs on Ex Libris Primo VE with the institution code 01VAN_INST and view vanui. catalog.library.vanderbilt.edu is a CNAME to vanderbilt.primo.exlibrisgroup.com, so
  name: Ex Libris Primo / Alma Library Discovery (01VAN_INST)
  slug: primo-discovery
- description: 'Vanderbilt University Library is Crossref member 6384, DOI prefix 10.15695, with 2,375 DOIs registered (164 current, 2,211 backfile) as of 2026-09-01. A registry membership: a fact about the instituti'
  name: Crossref Membership — Vanderbilt University Library
  slug: crossref-member
- description: Vanderbilt University is registered in the Research Organization Registry as https://ror.org/02vm5rt34. Distinct from Vanderbilt University Medical Center (05dq2gs74), Vanderbilt Health (05grhsk96) an
  name: ROR Registration — Vanderbilt University
  slug: ror
- baseURL: https://7itm2l2dz8.execute-api.us-east-1.amazonaws.com/prod
  baseurl_source: declared
  description: Broadcast and segment records in the archive.
  name: Vanderbilt University Broadcasts API
  slug: vanderbilt-broadcasts-api
- baseURL: https://7itm2l2dz8.execute-api.us-east-1.amazonaws.com/prod
  baseurl_source: declared
  description: Controlled vocabularies used to filter the archive.
  name: Vanderbilt University Metadata API
  slug: vanderbilt-metadata-api
- baseURL: https://7itm2l2dz8.execute-api.us-east-1.amazonaws.com/prod
  baseurl_source: declared
  description: Keyword and faceted search over broadcast segments.
  name: Vanderbilt University Search API
  slug: vanderbilt-search-api
- baseURL: https://7itm2l2dz8.execute-api.us-east-1.amazonaws.com/prod
  baseurl_source: declared
  description: Service identification.
  name: Vanderbilt University Service API
  slug: vanderbilt-service-api
- baseURL: https://7itm2l2dz8.execute-api.us-east-1.amazonaws.com/prod
  baseurl_source: declared
  description: SPARQL 1.1 query operations.
  name: Vanderbilt University SPARQL API
  slug: vanderbilt-sparql-api
artifact_total: 22
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://news.vanderbilt.edu/feed/
- group: company
  title: ''
  type: Website
  url: https://www.vanderbilt.edu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vanderbilt.edu/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heardlibrary
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/vanderbilt-data-science
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/vanderbilt-university/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ir.vanderbilt.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalog.library.vanderbilt.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://onevu.vanderbilt.edu/.well-known/openid-configuration
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.accre.vanderbilt.edu/
- group: design
  href: https://artifacts.apis.io/vanderbilt/conformance/vanderbilt-education-standards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vanderbilt-education-standards-conformance.yml
- group: auth
  href: https://artifacts.apis.io/vanderbilt/authentication/vanderbilt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vanderbilt-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vanderbilt/scopes/vanderbilt-scopes.yml
  title: ''
  type: Scopes
  url: scopes/vanderbilt-scopes.yml
- group: design
  href: https://artifacts.apis.io/vanderbilt/errors/vanderbilt-errors.yml
  title: ''
  type: Errors
  url: errors/vanderbilt-errors.yml
- group: build
  href: https://artifacts.apis.io/vanderbilt/examples/vanderbilt-examples.yml
  title: ''
  type: Examples
  url: examples/vanderbilt-examples.yml
- group: design
  href: https://artifacts.apis.io/vanderbilt/vocabulary/vanderbilt-linked-data-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vanderbilt-linked-data-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/vanderbilt/security/vanderbilt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vanderbilt-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/vanderbilt/plans/vanderbilt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vanderbilt-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vanderbilt/rate-limits/vanderbilt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vanderbilt-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vanderbilt/finops/vanderbilt-finops.yml
  title: ''
  type: FinOps
  url: finops/vanderbilt-finops.yml
- group: other
  href: https://artifacts.apis.io/vanderbilt/review.yml
  title: ''
  type: Review
  url: review.yml
- group: design
  href: https://artifacts.apis.io/vanderbilt/json-ld/vanderbilt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vanderbilt-context.jsonld
created: '2026-06-03'
description: 'Vanderbilt University is a private research university in Nashville, Tennessee. Its programmable footprint is real but narrow, and it does not live where a company''s would: there is no central developer portal, no API key, and no self-service onboarding anywhere on vanderbilt.edu. What exists is operated almost entirely by the Jean and Alexander Heard Libraries, and all of it is open to the public without a credential. Three surfaces were verified live on 2026-09-01: the Vanderbilt Television News Archive serverless API, which serves 98,371 network television news broadcasts and 969,224 news segments recorded continuously since 5 August 1968; a public SPARQL 1.1 endpoint at sparql.vanderbilt.edu holding 14.4 million triples of linked open data; and the Vanderbilt Institutional Repository, a self-hosted DSpace 9.1 deployment exposing both a HAL REST API and an OAI-PMH endpoint under the university''s own domain. Vanderbilt''s identity estate — an Okta org on onevu.vanderbilt.edu
  and a Microsoft Entra ID tenant for vanderbilt.edu — publishes live OpenID Connect discovery and SAML 2.0 metadata. Library discovery runs on Ex Libris Alma/Primo as a vendor tenancy (01VAN_INST) and is not Vanderbilt''s contract. The Azure API Management developer portal and the VUIT API Services catalog page recorded in the June 2026 profile were re-probed and are both dead; they have been removed rather than left standing as claims.'
finops:
- has_sources: true
  method: generated
  name: Vanderbilt Finops
  primary_unit: ''
  service_category: Education
  slug: vanderbilt-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vanderbilt.png
json_schemas:
- name: Vanderbilt Television News Archive
  property_count: 0
  slug: vanderbilt-television-news-archive
jsonld:
- class_count: 10
  name: Vanderbilt Context
  property_count: 4
  slug: vanderbilt-context
layout: provider
modified: '2026-10-06'
name: Vanderbilt University
nav: Providers
network: true
overview: 'Vanderbilt University publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Broadcasts API, Metadata API, Search API, and 10 more. Tagged areas include University, Higher Education, Education, Private Research University, and Research Data.


  The Vanderbilt University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vanderbilt University''s developer surface includes authentication, code examples, and 20 more developer resources.'
plans:
- name: Vanderbilt Plans Pricing
  plan_count: 2
  slug: vanderbilt-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Vanderbilt Rate Limits
  slug: vanderbilt-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Vanderbilt University API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 2
  slug: vanderbilt-rules
scopes:
- name: Vanderbilt Scopes
  scope_count: 0
  slug: vanderbilt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.0
    catalog_earned_first_party: 5.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 22.9
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vanderbilt/vanderbilt-2026-06-20T200807.png
security:
- kind: authentication
  name: Vanderbilt Authentication
  slug: vanderbilt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Vanderbilt Domain Security
  slug: vanderbilt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vanderbilt
tags:
- University
- Higher Education
- Education
- Private Research University
- Research Data
- Institutional Repository
- Linked Data
- SPARQL
- Digital Collections
- Television News Archive
- Identity Federation
- Library
- Nashville
- Tennessee
- United States
website: https://www.vanderbilt.edu/
---
