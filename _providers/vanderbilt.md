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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Public read API behind tvnews.vanderbilt.edu, self-identifying as the "TVNA Serverless API" v1.0.0. Search, browse and retrieve United States network television news broadcasts and segments recorded c
  name: Vanderbilt Television News Archive API
  slug: television-news-archive
- description: Public, unauthenticated SPARQL 1.1 Protocol endpoint on Vanderbilt's own domain, operated by the Heard Libraries' Linked Data, Wikidata and Semantic Web working groups. Holds 14,366,116 triples across
  name: Vanderbilt Libraries SPARQL Endpoint
  slug: sparql
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
artifact_total: 18
common:
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
  title: ''
  type: Conformance
  url: conformance/vanderbilt-education-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vanderbilt-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/vanderbilt-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/vanderbilt-errors.yml
- group: build
  title: ''
  type: Examples
  url: examples/vanderbilt-examples.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vanderbilt-linked-data-vocabulary.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vanderbilt-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vanderbilt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vanderbilt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vanderbilt-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vanderbilt-context.jsonld
created: '2026-06-03'
description: 'Vanderbilt University is a private research university in Nashville, Tennessee. Its programmable footprint is real but narrow, and it does not live where a company''s would: there is no central developer portal, no API key, and no self-service onboarding anywhere on vanderbilt.edu. What exists is operated almost entirely by the Jean and Alexander Heard Libraries, and all of it is open to the public without a credential. Three surfaces were verified live on 2026-09-01: the Vanderbilt Television News Archive serverless API, which serves 98,371 network television news broadcasts and 969,224 news segments recorded continuously since 5 August 1968; a public SPARQL 1.1 endpoint at sparql.vanderbilt.edu holding 14.4 million triples of linked open data; and the Vanderbilt Institutional Repository, a self-hosted DSpace 9.1 deployment exposing both a HAL REST API and an OAI-PMH endpoint under the university''s own domain. Vanderbilt''s identity estate — an Okta org on onevu.vanderbilt.edu
  and a Microsoft Entra ID tenant for vanderbilt.edu — publishes live OpenID Connect discovery and SAML 2.0 metadata. Library discovery runs on Ex Libris Alma/Primo as a vendor tenancy (01VAN_INST) and is not Vanderbilt''s contract. The Azure API Management developer portal and the VUIT API Services catalog page recorded in the June 2026 profile were re-probed and are both dead; they have been removed rather than left standing as claims.'
finops:
- name: Vanderbilt Finops
  service_category: Education
  slug: vanderbilt-finops
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
modified: '2026-09-01'
name: Vanderbilt University
nav: Providers
network: true
overview: 'Vanderbilt University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Vanderbilt Television News Archive API and Vanderbilt Libraries SPARQL Endpoint. Tagged areas include University, Higher Education, Education, Private Research University, and Research Data.


  The Vanderbilt University catalog on APIs.io includes 1 JSON-LD context.


  Vanderbilt University''s developer surface includes authentication, code examples, and 19 more developer resources.'
plans:
- name: Vanderbilt Plans Pricing
  plan_count: 2
  slug: vanderbilt-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Vanderbilt Rate Limits
  slug: vanderbilt-rate-limits
scopes:
- name: Vanderbilt Scopes
  scope_count: 0
  slug: vanderbilt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 17.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 15.2
    contract_quality: 26.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 26.3
  previous_composite: 18.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/vanderbilt/refs/heads/main/screenshots/vanderbilt-2026-06-20T200807.png
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
