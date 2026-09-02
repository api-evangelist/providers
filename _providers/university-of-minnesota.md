---
access_model:
  confidence: medium
  label: Free, request-gated
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - probed
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-09-01'
api_count: 9
apis:
- description: Ten agricultural, climate and geospatial data APIs operated by GEMS Informatics at the University of Minnesota — biotic risk, climate, crop calendar, elevation, hydrology, land cover, market accessibi
  name: GEMS Informatics Exchange APIs
  slug: gems-exchange-apis
- description: A suite of APIs published by the OIT Integrations Team over the University's Common Data Layer — person, class, employee, student academic, organization, HR and term information. Served from a Univers
  name: Common Good APIs
  slug: common-good-apis
- description: A read-only JSON API over UMedia, the University of Minnesota Libraries digital collections platform. Any search or item URL returns JSON when ".json" is appended, with Blacklight bracket facet syntax
  name: UMedia Digital Collections JSON API
  slug: umedia-digital-collections
- description: The University of Minnesota Digital Conservancy, which also holds DRUM (Data Repository for the University of Minnesota), runs DSpace 10.0 on University infrastructure. Its OAI-PMH 2.0 endpoint answer
  name: UMN Digital Conservancy — OAI-PMH and DSpace REST
  slug: digital-conservancy-oai-pmh
- description: The University operates its own Shibboleth identity provider and publishes it through the InCommon federation as entityID urn:mace:incommon:umn.edu, with shibmd:Scope umn.edu and SAML 2.0 single sign-
  name: InCommon Identity Federation — University of Minnesota Shibboleth IdP
  slug: incommon-identity-federation
- description: The University of Minnesota is a DataCite direct member, symbol UMN, registered since 2018-12-19 and linked to ROR 017zqws13. It operates the repository client UMN.DRUM (Data Repository for the Univer
  name: DataCite membership — University of Minnesota
  slug: datacite-membership
- description: The University of Minnesota is Crossref member 10551, registering DOIs under prefixes 10.24926 and 10.64517. University of Minnesota Press (member 3779, prefix 10.5749) and University of Minnesota Mor
  name: Crossref membership — University of Minnesota
  slug: crossref-membership
- description: The University of Minnesota's Research Organization Registry identifier is https://ror.org/017zqws13. It is the identifier DataCite links the University's membership to, and the one that makes cross-r
  name: ROR registration — University of Minnesota
  slug: ror-registration
- description: The University's developer portal for the Common Good APIs runs as a UMN-specific tenant on Boomi's cloud at umn-prod-apigw.boomi.cloud, where it catalogues twenty-four APIs and holds their Swagger do
  name: Boomi API Developer Portal (UMN tenant)
  slug: boomi-api-developer-portal
- description: UMedia's digital objects are delivered over the IIIF Image API 2.1 from the Libraries' OCLC CONTENTdm instance at cdm16022.contentdm.oclc.org, which every UMedia record points to in its `object` and `
  name: UMedia IIIF image delivery (OCLC CONTENTdm tenant)
  slug: contentdm-iiif
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://twin-cities.umn.edu
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sites.google.com/umn.edu/integration-apis/home
- group: docs
  title: ''
  type: Documentation
  url: https://gems.umn.edu/gems-exchange-apis
- group: docs
  title: ''
  type: APIReference
  url: https://exchange-1.gems.msi.umn.edu/soil/v2/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UMNLibraries
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/GEMS-UMN
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-minnesota/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.umn.edu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.umn.edu
- group: operate
  title: ''
  type: Support
  url: https://it.umn.edu
- group: other
  title: ''
  type: ResearchRepository
  url: https://conservancy.umn.edu/server/oai/request?verb=Identify
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.lib.umn.edu
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aumn.edu
- group: other
  title: ''
  type: ResearchComputing
  url: https://rc.umn.edu
- group: other
  title: ''
  type: AIPolicy
  url: https://it.umn.edu/navigating-ai-umn
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-minnesota-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-minnesota-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-minnesota-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-minnesota-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-minnesota-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-minnesota-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-minnesota-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-minnesota-errors.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-minnesota-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-minnesota-vocabulary.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-minnesota-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-minnesota-lifecycle.yml
- group: build
  title: ''
  type: Examples
  url: examples/university-of-minnesota-examples.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Minnesota is a public land-grant research university whose flagship campus is in the Twin Cities. Its programmable footprint is small, real, and unevenly distributed: the one place it publishes machine-readable contracts of its own is GEMS Informatics, whose Exchange APIs serve agricultural, climate and geospatial data from exchange-1.gems.msi.umn.edu behind an api key and ship nine live OpenAPI 3.1 documents. Everything else is either gated, undocumented in machine terms, or somebody else''s contract running under the University''s name. The OIT Integrations Team''s Common Good APIs are institution-operated at integration-boomi.umn.edu but are approved per data custodian and their Swagger lives inside a tenant Boomi developer portal that answers no anonymous request. UMN Libraries operates a genuine JSON API over the UMedia digital collections and an OAI-PMH 2.0 endpoint for the Digital Conservancy, but publishes no contract for either, and UMedia''s image
  delivery runs on the Libraries'' OCLC CONTENTdm tenancy rather than on University infrastructure. The strongest institution-operated machine-readable surface the University has is not an API at all: it is the Shibboleth identity provider it publishes through InCommon as urn:mace:incommon:umn.edu. There is no central developer portal, no institution-wide API catalog, and no public API programme.'
examples:
- key_count: 7
  name: Conservancy Dspace Rest Root
  slug: conservancy-dspace-rest-root
- key_count: 2
  name: Datacite Provider Umn
  slug: datacite-provider-umn
- key_count: 1
  name: Gems Exchange Missing Apikey 401
  slug: gems-exchange-missing-apikey-401
- key_count: 57
  name: Umedia Item Response
  slug: umedia-item-response
finops:
- name: University Of Minnesota Finops
  service_category: Education
  slug: university-of-minnesota-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-minnesota.png
json_schemas:
- name: GEMS Informatics Exchange API schemas (University of Minnesota)
  property_count: 0
  slug: university-of-minnesota-gems-exchange-schemas
- name: UMedia digital object metadata record
  property_count: 69
  slug: university-of-minnesota-umedia-item
jsonld:
- class_count: 24
  name: University Of Minnesota Context
  property_count: 6
  slug: university-of-minnesota-context
layout: provider
modified: '2026-09-01'
name: University of Minnesota
nav: Providers
network: true
overview: 'University of Minnesota publishes 2 APIs on the [APIs.io](https://apis.io/) network: GEMS Informatics Exchange APIs and UMedia Digital Collections JSON API. Tagged areas include University, Higher Education, Education, Research, and United States.


  The University of Minnesota catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Minnesota''s developer surface includes documentation, API reference, support, authentication, code examples, and 24 more developer resources.'
plans:
- name: University Of Minnesota Plans Pricing
  plan_count: 2
  slug: university-of-minnesota-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: University Of Minnesota Rate Limits
  slug: university-of-minnesota-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of Minnesota API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: university-of-minnesota-rules
scopes:
- name: University Of Minnesota Scopes
  scope_count: 0
  slug: university-of-minnesota-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 30.7
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 3.8
    contract_quality: 65.3
    developer_ergonomics: 42.9
    discoverability: 74.1
    governance: 3.8
    operational_transparency: 26.3
  previous_composite: 23.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-minnesota/refs/heads/main/screenshots/university-of-minnesota-2026-06-20T200207.png
security:
- kind: authentication
  name: University Of Minnesota Authentication
  slug: university-of-minnesota-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Minnesota Domain Security
  slug: university-of-minnesota-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-minnesota
tags:
- University
- Higher Education
- Education
- Research
- United States
- Minnesota
- Big Ten
- Land Grant
- Public Research University
- Research Data
- Research Repository
- Open Data
- Geospatial
- Agriculture
- Climate
- Digital Collections
- Identity Federation
- Research Computing
website: https://twin-cities.umn.edu
---
