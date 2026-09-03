---
access_model:
  confidence: high
  label: Free and public for the harvesting and discovery surfaces; no public onboarding for the authorization server
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-09-02'
api_count: 3
apis:
- baseURL: https://eprints.qut.edu.au/cgi/oai2
  baseurl_source: declared
  description: Public, unauthenticated OAI-PMH 2.0 metadata harvesting interface for QUT's institutional research repository. All six verbs served. Advertises oai_dc, oai_bibl, oai_openaire and uketd_dc. Identify na
  name: QUT ePrints OAI-PMH 2.0
  slug: qut-eprints-oai-pmh-20
- baseURL: https://esoe.qut.edu.au/auth/realms/qut
  baseurl_source: declared
  description: QUT's enterprise single sign-on authorization server, a Keycloak deployment on QUT's own address space. Publishes OpenID Connect Discovery 1.0 metadata, an RFC 8414 authorization server metadata docum
  name: QUT ESOE OpenID Connect Provider
  slug: qut-esoe-openid-connect-provider
- description: QUT's self-hosted Shibboleth SAML 2.0 identity provider. Publishes per-entity metadata that dereferences from its own entityID, asserts shibmd:Scope qut.edu.au, and is registered in the Australian Acc
  name: QUT Shibboleth Identity Provider
  slug: qut-shibboleth-identity-provider
- baseURL: https://eprints.qut.edu.au/rest
  baseurl_source: declared
  description: The GNU EPrints REST dataset interface. The index is open and the payload is closed — /rest/, /rest/eprint/ and /rest/subject/ return 200 without credentials, while every individual record returns 401
  name: QUT ePrints REST Interface
  slug: qut-eprints-rest-interface
- description: A public agent plugin marketplace published by QUT eResearch, carrying one MCP server definition that wraps the QUT eResearch documentation site. Institution-authored and a rare find for a university.
  name: QUT eResearch Agent Plugin Marketplace
  slug: qut-eresearch-agent-plugin-marketplace
- description: QUT's library discovery layer runs on Ex Libris Primo VE / Alma under view id 61QUT_INST:QUT. The collection and the configuration are QUT's; the platform and any API contract are Ex Libris's. QUT pub
  name: QUT Library Discovery (Ex Libris Primo VE tenant)
  slug: qut-library-discovery-ex-libris-primo-ve-tenant
- description: QUT's learning management system, an Instructure Canvas tenancy on a QUT hostname, front-ended by Microsoft Entra ID sign-in. Canvas is an LTI 1.3 platform and exposes Instructure's REST API, but that
  name: QUT Canvas LMS (Instructure tenant)
  slug: qut-canvas-lms-instructure-tenant
- description: QUT contributes a named group to the Australian Research Data Commons national registry. A live query for group "Queensland University of Technology" returns 926 registry objects — 484 collections, 39
  name: QUT collection in ARDC Research Data Australia
  slug: qut-collection-in-ardc-research-data-australia
- description: 'QUT registers persistent identifiers with DataCite through the ARDC consortium. Two clients are evidenced: ARDCX.QUT1, a repository client registered 2020 holding 535 DOIs, and UUAG.IXKMSM, a RAiD reg'
  name: DataCite DOI and RAiD registration
  slug: datacite-doi-and-raid-registration
- description: QUT is a Crossref member, id 3230, primary-name "Queensland University of Technology", verified live against Crossref's member API. Recorded as a membership; Crossref's API is not QUT's contract.
  name: Crossref membership
  slug: crossref-membership
- description: QUT's Research Organization Registry identifier is https://ror.org/03pnv4752. The canonical machine-readable identifier for the institution itself, used across DataCite, Crossref and ORCID metadata.
  name: ROR registration
  slug: ror-registration
- description: QUT is a member of the Australian Access Federation, which is interfederated with eduGAIN. Five entity descriptors naming QUT appear in the production aggregate; three are QUT-operated (the IdP at idp
  name: Australian Access Federation membership
  slug: australian-access-federation-membership
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.qut.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/qut-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qut-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qut-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/qut-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/qut-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qut-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/qut-openapi-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/qut-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/qut-context.jsonld
- group: agent
  title: ''
  type: MCP
  url: mcp/qut-eresearch-docs-mcp.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.qut.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://qut.primo.exlibrisgroup.com/discovery/search?vid=61QUT_INST:QUT
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.qut.edu.au/research/office-of-eresearch
- group: docs
  title: ''
  type: Documentation
  url: https://www.library.qut.edu.au/about/collections/qut-eprints/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eresearchqut
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/qcr
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/queensland-university-of-technology/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qut-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qut-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qut-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qut-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Queensland University of Technology (QUT) is a public research university in Brisbane, Australia, serving around 50,000 students with an applied emphasis in teaching and research. It is not an API producer and it publishes no developer portal, no API keys and no OpenAPI of its own — but it is one of the few institutions in this cohort whose machine-readable surfaces are genuinely its own engineering rather than a vendor''s contract running under its name. Three surfaces were verified live on QUT-owned infrastructure inside APNIC allocation QUT-AU (AS7575), with no CNAME to a managed platform: the QUT ePrints OAI-PMH 2.0 repository interface at eprints.qut.edu.au, fully public and advertising oai_dc, oai_bibl, oai_openaire and uketd_dc; a self-hosted Shibboleth SAML 2.0 identity provider at idp.qut.edu.au registered in the Australian Access Federation and asserting the qut.edu.au scope; and a Keycloak OpenID Connect authorization server at esoe.qut.edu.au publishing a complete
  discovery document, JWKS, RFC 8414 metadata, dynamic client registration, PAR, CIBA and certificate-bound tokens, brokering interactive login to Microsoft Entra ID. QUT eResearch additionally publishes a public agent plugin marketplace carrying an MCP server definition, which is rare for a university — though the documentation host it targets, docs.eres.qut.edu.au, resolves publicly to an RFC 1918 private address and is unreachable from outside QUT. Everything else is bought: library discovery is an Ex Libris Primo VE tenancy, the LMS is Instructure Canvas, research data is contributed to ARDC''s national registry, and identity is registered in DataCite, Crossref and ROR. Those relationships are recorded here; their contracts are not, because they are not QUT''s. There is no open data portal, no course or timetable API, and no public route to a credential for the one authorization server QUT does run.'
examples:
- key_count: 55
  name: Qut Esoe Openid Configuration
  slug: qut-esoe-openid-configuration
finops:
- name: Qut Finops
  service_category: Education
  slug: qut-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qut.png
json_schemas:
- name: QUT ESOE OpenID Provider Metadata
  property_count: 24
  slug: qut-esoe-openid-configuration
- name: QUT ePrints OAI-PMH Identify Response
  property_count: 9
  slug: qut-oai-pmh-identify
- name: QUT ePrints OAI-PMH Metadata Format
  property_count: 3
  slug: qut-oai-pmh-metadata-format
jsonld:
- class_count: 24
  name: Qut Context
  property_count: 3
  slug: qut-context
layout: provider
modified: '2026-09-01'
name: Queensland University of Technology
nav: Providers
network: true
overview: 'Queensland University of Technology publishes 3 APIs on the [APIs.io](https://apis.io/) network: QUT ePrints OAI-PMH 2.0, QUT ESOE OpenID Connect Provider, and QUT ePrints REST Interface. Tagged areas include University, Higher Education, Education, Australia, and Research.


  The Queensland University of Technology catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Queensland University of Technology''s developer surface includes authentication, documentation, GitHub presence, and 20 more developer resources.'
plans:
- name: Qut Plans Pricing
  plan_count: 2
  slug: qut-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Qut Rate Limits
  slug: qut-rate-limits
rules:
- effective_rule_count: 9
  extends: []
  name: Queensland University of Technology API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: qut-openapi-rules
scopes:
- name: Qut Scopes
  scope_count: 0
  slug: qut-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 38.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 37.2
    developer_ergonomics: 21.4
    discoverability: 85.2
    governance: 11.4
    operational_transparency: 26.3
  previous_composite: 36.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: authentication
  name: Qut Authentication
  slug: qut-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Qut Domain Security
  slug: qut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qut
tags:
- University
- Higher Education
- Education
- Australia
- Research
- Research Repository
- Identity Federation
- OAI-PMH
- SAML
- OpenID Connect
- Institutional Repository
- Open Access
website: https://www.qut.edu.au/
---
