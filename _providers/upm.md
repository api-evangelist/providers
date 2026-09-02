---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'OAI-PMH 2.0 metadata harvesting for the Universiti Putra Malaysia Institutional Repository, running EPrints 3.3.16. Identify, ListMetadataFormats, ListSets, ListIdentifiers, ListRecords and GetRecord '
  name: PSASIR Institutional Repository — OAI-PMH 2.0
  slug: psasir-oai-pmh
- description: 'Unauthenticated read interfaces the repository serves alongside OAI-PMH, all verified live on 2026-09-01: an EPrints REST dataset browser at /rest/ with per-item XML at /rest/eprint/{id}.xml, a per-it'
  name: PSASIR EPrints REST, Export and OpenSearch
  slug: psasir-eprints-rest
- description: OAI-PMH 2.0 metadata harvesting for MyAgric, the Malaysian Agricultural Repository, a national-scope agricultural collection UPM hosts and operates on a second EPrints 3.3.16 deployment. Identify, Lis
  name: MyAgric — Malaysian Agricultural Repository OAI-PMH 2.0
  slug: myagric-oai-pmh
- description: UPM's own Shibboleth identity provider, publishing conforming SAML 2.0 and SAML 1.1 metadata at its entityID (HTTP 200, application/xml, verified 2026-09-01). Asserts the scope upm.edu.my, carries HTT
  name: UPM Shibboleth SAML 2.0 Identity Provider
  slug: saml-idp
- description: 'Universiti Putra Malaysia''s identity provider is registered in eduGAIN, the global identity interfederation, through SIFULAN — the Malaysian Access Federation — as eduGAIN entity 672307, registration '
  name: eduGAIN / SIFULAN federation membership
  slug: edugain-sifulan
- description: Universiti Putra Malaysia is a Crossref member in its own right, member id 27687, holding DOI prefix 10.47836 with 5,871 registered DOIs (3,105 current, 2,766 backfile) as of 2026-09-01. The prefix ca
  name: Crossref membership — DOI prefix 10.47836
  slug: crossref-member
- description: Universiti Putra Malaysia holds ROR identifier https://ror.org/02e91jd64, cross-walked in the ROR record to GRID grid.11142.37, ISNI 0000 0001 2231 800X, Wikidata Q1458579 and five Crossref Funder Reg
  name: ROR organization record
  slug: ror
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://upm.edu.my/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-putra-malaysia/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.upm.edu.my/
- group: other
  title: ''
  type: ResearchRepository
  url: http://psasir.upm.edu.my/
- group: other
  title: ''
  type: ResearchRepository
  url: http://myagric.upm.edu.my/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/upm-identity-federation.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upm-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upm-education-standards-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/upm-errors.yml
- group: build
  title: ''
  type: Examples
  url: examples/upm-examples.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/upm-eprints-record-schema.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upm-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/upm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/upm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Putra Malaysia (UPM) is a Malaysian public research university in Serdang, Selangor, founded as an agricultural college in 1931 and known as Universiti Pertanian Malaysia until 1997. UPM operates no developer portal, publishes no OpenAPI definition, issues no API keys and runs no self-service developer programme — and it does not need one to have a real programmable footprint. Four machine-readable surfaces were verified live on 2026-09-01, and all four are operated by the institution itself rather than by a vendor under its name. PSASIR, the institutional repository, runs EPrints 3.3.16 inside UPM''s own campus network allocation and answers a full OAI-PMH 2.0 harvest as well as an anonymous EPrints REST, export and OpenSearch interface offering twenty output representations. MyAgric, the Malaysian Agricultural Repository, is a second and distinct EPrints deployment UPM hosts on the same network, with its own repository identifier and its own OAI-PMH endpoint. UPM
  publishes conforming SAML 2.0 metadata for its own Shibboleth identity provider at idf.upm.edu.my, registered in eduGAIN through SIFULAN, the Malaysian Access Federation, since 2020. UPM is also a Crossref member in its own right, holding DOI prefix 10.47836 across roughly 5,900 registered DOIs for its Pertanika and UPM Press journals. What UPM does not have is any interface for its student, staff and administrative systems: the Putra portal, SMP and the study portal sit behind UPM-ID single sign-on with no public contract, there is no open-data portal, no course-catalog API, no institutional GitHub organisation, and no llms.txt, sitemap or security.txt on the main site.'
examples:
- key_count: 17
  name: Upm Psasir Eprint Export
  slug: upm-psasir-eprint-export
finops:
- name: Upm Finops
  service_category: Education
  slug: upm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upm.png
json_schemas:
- name: UPM PSASIR EPrints record (JSON export)
  property_count: 18
  slug: upm-eprints-record
jsonld:
- class_count: 15
  name: Upm Context
  property_count: 1
  slug: upm-context
layout: provider
modified: '2026-09-01'
name: Universiti Putra Malaysia
nav: Providers
network: true
overview: 'Universiti Putra Malaysia publishes 3 APIs on the [APIs.io](https://apis.io/) network: PSASIR Institutional Repository — OAI-PMH 2.0, PSASIR EPrints REST, Export and OpenSearch, and MyAgric — Malaysian Agricultural Repository OAI-PMH 2.0. Tagged areas include University, Higher Education, Education, Malaysia, and Public Research University.


  The Universiti Putra Malaysia catalog on APIs.io includes 1 JSON-LD context.


  Universiti Putra Malaysia''s developer surface includes authentication, code examples, and 14 more developer resources.'
plans:
- name: Upm Plans Pricing
  plan_count: 2
  slug: upm-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Upm Rate Limits
  slug: upm-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 47.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 28.1
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.3
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
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upm/refs/heads/main/screenshots/upm-2026-06-20T200449.png
security:
- kind: authentication
  name: Upm Authentication
  slug: upm-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Upm Domain Security
  slug: upm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upm
tags:
- University
- Higher Education
- Education
- Malaysia
- Public Research University
- Research Data
- Institutional Repository
- Open Access
- OAI-PMH
- Identity Federation
- Shibboleth
- Agriculture
- Scholarly Publishing
website: https://upm.edu.my/
---
