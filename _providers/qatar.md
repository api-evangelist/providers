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
api_count: 2
apis:
- description: 'Qatar University''s own OpenID Connect provider, running on a WSO2 Identity Server at sso.qu.edu.qa. It publishes a complete OpenID Connect Discovery 1.0 document, a live JWKS serving an RS256 signing '
  name: Qatar University Single Sign-On (OpenID Connect / OAuth 2.0)
  slug: qu-sso-oidc
- description: The same host publishes a SAML 2.0 IDPSSODescriptor at /identity/metadata/saml2, entityID `sso.qu.edu.qa`, with separate signing and encryption key descriptors, HTTP-POST and HTTP-Redirect single sign
  name: Qatar University SAML 2.0 Identity Provider
  slug: qu-sso-saml
- description: Qatar University Press self-hosts Open Journal Systems 3.3.0.7 at journals.qu.edu.qa and exposes an anonymous OAI-PMH 2.0 endpoint, site-wide and per journal. It identifies as "QU Press Open Journal S
  name: QU Press Open Journal System OAI-PMH API
  slug: qupress-oai
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
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.qu.edu.qa/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/qatar-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qatar-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qatar-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/qatar-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/qatar-errors.yml
- group: build
  title: ''
  type: Examples
  url: examples/examples.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/qatar-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qatar-lifecycle.yml
- group: design
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
  title: ''
  type: DomainSecurity
  url: security/qatar-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qatar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qatar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qatar-finops.yml
- group: other
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
- name: Qatar Finops
  service_category: Education
  slug: qatar-finops
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
overview: 'Qatar University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Single Sign-On (OpenID Connect / OAuth 2.0) and QU Press Open Journal System OAI-PMH API. Tagged areas include Education, Higher Education, University, Qatar, and Middle East.


  The Qatar University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qatar University''s developer surface includes authentication, code examples, documentation, and 19 more developer resources.'
plans:
- name: Qatar Plans Pricing
  plan_count: 2
  slug: qatar-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Qatar Rate Limits
  slug: qatar-rate-limits
rules:
- effective_rule_count: 0
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
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 10.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 3.8
    contract_quality: 26.1
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 3.8
    operational_transparency: 21.1
  previous_composite: 19.5
  provenance:
    conformance: derived
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
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/qatar/refs/heads/main/screenshots/qatar-2026-06-20T192353.png
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
- OpenID Connect
website: https://www.qu.edu.qa/
---
