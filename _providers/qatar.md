---
access_model:
  confidence: high
  label: Free · anonymous read on metadata endpoints, institutional affiliation for identity
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - scopes
  - lifecycle
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: The same host publishes a SAML 2.0 IDPSSODescriptor at /identity/metadata/saml2, entityID `sso.qu.edu.qa`, with separate signing and encryption key descriptors, HTTP-POST and HTTP-Redirect single sign
  name: Qatar University SAML 2.0 Identity Provider
  slug: qu-sso-saml
- description: QSpace is Qatar University's institutional repository — 66,950 records, DSpace 7.6, administered by Qatar University Library at quspace@qu.edu.qa, with every item carrying a persistent identifier unde
  name: QSpace Institutional Repository (Open Repository tenant)
  slug: qspace
- description: Qatar University's learning management system is a Blackboard Learn SaaS tenant at elearning.qu.edu.qa. The Anthology Blackboard Learn REST API is reachable on the tenant — /learn/api/public/v1/system
  name: Qatar University Blackboard Learn (Anthology tenant)
  slug: blackboard-learn
- description: Qatar University Library's research guides, including the QSpace institutional-repository guide that is the only public documentation for the repository, run on Springshare LibGuides. Springshare's Li
  name: Qatar University Library Research Guides (Springshare tenant)
  slug: libguides
- description: Qatar University runs Ellucian Banner Self-Service at mybanner.qu.edu.qa, on its own network (netname QUNET). The host answers 200 with a real Banner menu, so the system is live and institution-hosted
  name: Qatar University Student Information System (Ellucian Banner)
  slug: banner-sis
- description: Qatar University is registered in ROR as https://ror.org/00yhnba62 — status active, established 1973, domain qu.edu.qa, located in Doha, Qatar — cross-walked to Funder Registry 501100004252, GRID grid
  name: Research Organization Registry membership
  slug: ror
- description: Qatar University Press is a Crossref member in its own right — member 11655, DOI prefix 10.29117, 2,533 DOIs registered (510 current, 2,023 backfile) — covering the journals it publishes at journals.q
  name: Crossref membership (Qatar University Press)
  slug: crossref
- description: Qatar University holds Handle.Net prefix 10576 and every QSpace item carries a persistent identifier under it, resolving through hdl.handle.net to the repository. The prefix registration is Qatar Univ
  name: Handle.Net naming authority 10576
  slug: handle
- baseURL: https://sso.qu.edu.qa
  baseurl_source: declared
  description: OpenID Connect Dynamic Client Registration.
  name: Qatar University Client Registration API
  slug: qatar-client-registration-api
- baseURL: https://sso.qu.edu.qa
  baseurl_source: declared
  description: Provider metadata and signing keys.
  name: Qatar University Discovery API
  slug: qatar-discovery-api
- baseURL: https://sso.qu.edu.qa
  baseurl_source: declared
  description: The six OAI-PMH 2.0 protocol verbs, site-wide and per journal.
  name: Qatar University OAI PMH API
  slug: qatar-oai-pmh-api
- baseURL: https://sso.qu.edu.qa
  baseurl_source: declared
  description: Authorization, user info and session management.
  name: Qatar University OpenID Connect API
  slug: qatar-openid-connect-api
- baseURL: https://sso.qu.edu.qa/samlsso
  baseurl_source: declared
  description: Token issuance, introspection and revocation.
  name: Qatar University O Auth API
  slug: qatar-oauth-api
artifact_total: 27
common:
- group: company
  title: ''
  type: Website
  url: https://www.qu.edu.qa/
- group: other
  href: https://artifacts.apis.io/qatar/identity-federation/qatar-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/qatar-identity-federation.yml
- group: design
  href: https://artifacts.apis.io/qatar/conformance/qatar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qatar-conformance.yml
- group: auth
  href: https://artifacts.apis.io/qatar/authentication/qatar-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qatar-authentication.yml
- group: auth
  href: https://artifacts.apis.io/qatar/scopes/qatar-scopes.yml
  title: ''
  type: Scopes
  url: scopes/qatar-scopes.yml
- group: design
  href: https://artifacts.apis.io/qatar/errors/qatar-errors.yml
  title: ''
  type: Errors
  url: errors/qatar-errors.yml
- group: build
  href: https://artifacts.apis.io/qatar/examples/examples.yml
  title: ''
  type: Examples
  url: examples/examples.yml
- group: design
  href: https://artifacts.apis.io/qatar/vocabulary/qatar-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qatar-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/qatar/lifecycle/qatar-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qatar-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/qatar/rules/qatar-rules.yml
  title: ''
  type: Rules
  url: rules/qatar-rules.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://qspace.qu.edu.qa/
- group: other
  title: ''
  type: ScholarlyPublishing
  url: https://journals.qu.edu.qa/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.qu.edu.qa/en-us/library/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.qu.edu.qa/en-us/students/registration/
- group: other
  title: ''
  type: Research
  url: https://www.qu.edu.qa/en-us/research/
- group: docs
  title: ''
  type: Documentation
  url: https://libguides.qu.edu.qa/quir
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/qatar-university/
- group: auth
  href: https://artifacts.apis.io/qatar/security/qatar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qatar-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/qatar/plans/qatar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qatar-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/qatar/rate-limits/qatar-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qatar-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/qatar/finops/qatar-finops.yml
  title: ''
  type: FinOps
  url: finops/qatar-finops.yml
- group: other
  href: https://artifacts.apis.io/qatar/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Qatar University is the national public research university of the State of Qatar, in Doha, founded 1973 and registered as https://ror.org/00yhnba62. Its institution-operated programmable footprint is small, real, and not where the June 2026 profile said it was. That pass recorded QSpace — the institutional repository at qspace.qu.edu.qa — as Qatar University''s own API. It is not: qspace.qu.edu.qa CNAMEs to qataru.cname.openrepository.com and terminates on Amazon eu-west-1, making it a tenant of Open Repository, a commercial hosted-DSpace service. The 66,950 records, the Handle prefix 10576 and the administrative contact are Qatar University''s; the DSpace REST and OAI-PMH contracts are the hosting platform''s engineering, and they are recorded here as a tenancy rather than saved as Qatar University''s contracts. What the earlier pass missed is the part Qatar University actually runs. It operates its own identity provider at sso.qu.edu.qa — a WSO2 Identity Server on QUNET,
  its own RIPE allocation — publishing both a SAML 2.0 IdP metadata document and a complete OpenID Connect discovery document, which together are the strongest machine-readable contract in this profile. Qatar University Press self-hosts Open Journal Systems 3.3.0.7 at journals.qu.edu.qa, also on QUNET, serving an anonymous OAI-PMH 2.0 endpoint over eight journals and 3,186 records in Arabic and English, and registers DOIs as Crossref member 11655 under prefix 10.29117. Learning is a Blackboard Learn tenant and library guides are a Springshare tenant. There is no developer portal, no changelog, no status page, no API terms of service, and no published OpenAPI for anything — and there is an institutional API gateway at api.qu.edu.qa that fronts a live production API pool while publishing no route, documentation or access path whatsoever. Three verified defects sit on the surfaces Qatar University does run: sso.qu.edu.qa and journals.qu.edu.qa both serve an incomplete TLS chain that a default
  client cannot verify, the SAML entityID is a bare hostname rather than a URI so the IdP cannot be federated as published, and the OAI-PMH endpoint emits record identifiers that its own GetRecord verb rejects.'
examples:
- key_count: 4
  name: Qatar Crossref Member
  slug: qatar-crossref-member
- key_count: 3
  name: Qatar Handle Resolution
  slug: qatar-handle-resolution
- key_count: 27
  name: Qatar Qu Sso Openid Configuration
  slug: qatar-qu-sso-openid-configuration
- key_count: 11
  name: Qatar Ror Record
  slug: qatar-ror-record
finops:
- has_sources: true
  method: generated
  name: Qatar Finops
  primary_unit: ''
  service_category: Education
  slug: qatar-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qatar.png
json_schemas:
- name: QU Press OAI-PMH Record (JSON projection)
  property_count: 3
  slug: qatar-oai-pmh-record.schema
- name: Qatar University SSO — OpenID Provider Metadata
  property_count: 27
  slug: qatar-qu-sso-openid-configuration.schema
jsonld:
- class_count: 33
  name: Qatar Context
  property_count: 0
  slug: qatar-context
layout: provider
modified: '2026-09-01'
name: Qatar University
nav: Providers
network: true
overview: 'Qatar University publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Client Registration API, Discovery API, OAI PMH API, and 10 more. Tagged areas include Education, Higher Education, University, Qatar, and Middle East.


  The Qatar University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qatar University''s developer surface includes authentication, code examples, documentation, and 19 more developer resources.'
plans:
- name: Qatar Plans Pricing
  plan_count: 2
  slug: qatar-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Qatar Rate Limits
  slug: qatar-rate-limits
rules:
- authorship: derived
  effective_rule_count: 0
  extends: []
  name: Qatar University API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: qatar-rules
scopes:
- name: Qatar Scopes
  scope_count: 0
  slug: qatar-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 3.8
    contract_quality: 24.1
    developer_ergonomics: 21.4
    discoverability: 71.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - qatar
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 20.2
  provenance:
    conformance: derived
    contracts:
      callable: 80.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/qatar/qatar-2026-06-20T192353.png
security:
- kind: authentication
  name: Qatar Authentication
  slug: qatar-authentication
  summary_line: none/oauth2/openIdConnect/saml · 7 schemes
- kind: domain-security
  name: Qatar Domain Security
  slug: qatar-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: qatar
tags:
- Education
- Higher Education
- University
- Qatar
- Middle East
- Research
- Identity Federation
- Scholarly Publishing
- Research Repository
- Open Access
- OAI-PMH
- SAML
website: https://www.qu.edu.qa/
---
