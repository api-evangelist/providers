---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The University's own Shibboleth identity provider, entityID https://idp.unimelb.edu.au/idp/shibboleth, serving public SAML 2.0 metadata at that URL (verified 200 application/xml, 2026-08-19) with an I
  name: Shibboleth Identity Provider — SAML 2.0 Metadata
  slug: shibboleth-identity-provider
- description: TENANT RELATIONSHIP, recorded deliberately and with no contract saved. melbourne.figshare.com is the University of Melbourne's research data repository, registered with DataCite as client UNIMELB.REPO
  name: Melbourne Data — Research Data Repository (Figshare tenancy)
  slug: melbourne-data-figshare
- description: 'TENANT RELATIONSHIP. An Esri ArcGIS Hub site publishing University of Melbourne campus GIS layers — building, road and tree-canopy footprints. Verified live 2026-08-19: the site returned 200, the DCAT'
  name: Open Spatial Data Portal (Esri ArcGIS Hub tenancy)
  slug: spatial-open-data-arcgis-hub
- description: TENANT RELATIONSHIP. sso.unimelb.edu.au is an Okta Identity Cloud tenancy running under a University vanity hostname. The OpenID Connect discovery document and the RFC 8414 authorization-server metada
  name: University SSO — OpenID Connect Discovery (Okta tenancy)
  slug: sso-okta
- description: TENANT RELATIONSHIP, and a weak one. The University of Melbourne runs a Boomi-based internal API management programme and developer portal for staff and students. It is gated behind University authent
  name: Internal API Management Programme (Boomi tenancy) — Gated
  slug: boomi-internal-api-portal
- description: Repository content hierarchy
  name: University of Melbourne Core API
  slug: university-of-melbourne-core-api
- description: Spatial datasets held in the observatory
  name: University of Melbourne Datasets API
  slug: university-of-melbourne-datasets-api
- description: HAL root document
  name: University of Melbourne Discovery API
  slug: university-of-melbourne-discovery-api
- description: Open Archives Initiative Protocol for Metadata Harvesting 2.0
  name: University of Melbourne OAI PMH API
  slug: university-of-melbourne-oai-pmh-api
artifact_total: 26
common:
- group: company
  title: ''
  type: Website
  url: https://www.unimelb.edu.au/
- group: other
  title: ''
  type: OpenData
  url: https://sudo.eresearch.unimelb.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://minerva-access.unimelb.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.unimelb.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://dashboard.hpc.unimelb.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://handbook.unimelb.edu.au/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.unimelb.edu.au/generative-ai-taskforce
- group: auth
  title: ''
  type: Authentication
  url: https://sso.unimelb.edu.au/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.unimelb.edu.au/strategy/governance/compliance-obligations/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.unimelb.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/unimelb
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-melbourne/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-melbourne-sudo-geonode-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-melbourne-minerva-access-dspace-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-melbourne-minerva-access-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-melbourne-sudo-dataset.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-melbourne-minerva-access-community.json
- group: build
  title: ''
  type: Examples
  url: examples/README.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-melbourne-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-melbourne-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-melbourne-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-melbourne-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-melbourne-oai-metadata-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-melbourne-rules.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-melbourne-lifecycle.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-melbourne-organization.jsonld
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-melbourne-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-melbourne-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-melbourne-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-melbourne-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-melbourne-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Melbourne is Australia''s leading research university, a Group of Eight member founded in 1853 and ranked in the world top 25. Its programmable footprint is small, unmarketed and genuinely its own in two places — which is more than most of this cohort can say. The institution operates a public, unauthenticated JSON API over 7,417 spatial datasets in the Spatial Urban Data Observatory (GeoNode, on unimelb.edu.au), and it runs Minerva Access — a self-hosted DSpace 7.6 repository on its own ITS infrastructure — exposing both a HAL+JSON REST API and an OAI-PMH 2.0 harvesting endpoint whose fourteen metadata formats include two the Library built itself (`umbl`, and a `trove` crosswalk for the National Library of Australia). It also operates its own Shibboleth SAML 2.0 identity provider, registered in the Australian Access Federation and reachable as public metadata. None of these is documented as a product: there is no developer portal, no OpenAPI, no changelog,
  no status page, no rate-limit signal and no support channel for any of them, and the University publishes no machine-readable contract for anything it runs. Everything else that looks like a University of Melbourne API is a tenancy — Melbourne Data on Figshare, the open spatial portal on Esri ArcGIS Hub, web SSO on Okta, the internal API programme on Boomi. Those relationships are recorded here with `x-operator: tenant` and no vendor contract is stored under this slug.'
examples:
- key_count: 4
  name: University Of Melbourne Arcgis Hub Ogc Records Example
  slug: university-of-melbourne-arcgis-hub-ogc-records-example
- key_count: 3
  name: University Of Melbourne Minerva Access Communities Example
  slug: university-of-melbourne-minerva-access-communities-example
- key_count: 6
  name: University Of Melbourne Minerva Access Root Example
  slug: university-of-melbourne-minerva-access-root-example
- key_count: 31
  name: University Of Melbourne Sso Openid Configuration Example
  slug: university-of-melbourne-sso-openid-configuration-example
- key_count: 5
  name: University Of Melbourne Sudo Datasets Example
  slug: university-of-melbourne-sudo-datasets-example
finops:
- name: University Of Melbourne Finops
  service_category: Education
  slug: university-of-melbourne-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-melbourne.png
json_schemas:
- name: Minerva Access Community
  property_count: 8
  slug: university-of-melbourne-minerva-access-community
- name: SUDO Dataset
  property_count: 65
  slug: university-of-melbourne-sudo-dataset
jsonld:
- class_count: 29
  name: University Of Melbourne Context
  property_count: 3
  slug: university-of-melbourne-context
- class_count: 0
  name: University Of Melbourne Organization Context
  property_count: 0
  slug: university-of-melbourne-organization
layout: provider
modified: '2026-08-19'
name: University of Melbourne
nav: Providers
network: true
overview: 'University of Melbourne publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Core API, Datasets API, Discovery API, and 1 more. Tagged areas include University, Higher Education, Education, Australia, and Group of Eight.


  The University of Melbourne catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  University of Melbourne''s developer surface includes authentication, GitHub presence, code examples, and 29 more developer resources.'
plans:
- name: University Of Melbourne Plans Pricing
  plan_count: 2
  slug: university-of-melbourne-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of Melbourne Rate Limits
  slug: university-of-melbourne-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of Melbourne API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: university-of-melbourne-rules
scopes:
- name: University Of Melbourne Scopes
  scope_count: 0
  slug: university-of-melbourne-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 38.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 33.3
    contract_quality: 27.7
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 33.3
    operational_transparency: 26.3
  previous_composite: 38.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 68.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-melbourne/refs/heads/main/screenshots/university-of-melbourne-2026-06-20T200206.png
security:
- kind: authentication
  name: University Of Melbourne Authentication
  slug: university-of-melbourne-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Melbourne Domain Security
  slug: university-of-melbourne-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Melbourne Vulnerability Disclosure
  slug: university-of-melbourne-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-melbourne
tags:
- University
- Higher Education
- Education
- Australia
- Group of Eight
- Research
- Research Data
- Research Repository
- Open Data
- Geospatial
- Identity Federation
- Library
website: https://www.unimelb.edu.au/
---
