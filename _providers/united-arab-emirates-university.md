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
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: The university's own single sign-on service, running on UAEU's registrable domain under a certificate issued to *.uaeu.ac.ae. It is the login point for UAEU applications — Banner Self-Service at ssb.u
  name: UAEU Enterprise Identity Service (OIDC / SAML 2.0 / SCIM 2.0)
  slug: uaeu-identity-service
- description: OAI-PMH 2.0 metadata harvesting endpoint for Scholarworks@UAEU, the university's open-access institutional repository. Verified live returning valid OAI-PMH XML with repositoryName "Scholarworks@UAEU"
  name: Scholarworks@UAEU OAI-PMH Repository Endpoint
  slug: scholarworks-oai-pmh
- description: UAEU's research information system and public research portal, at research.uaeu.ac.ae, which CNAMEs to uaeu.elsevierpure.com. The deployment serves a complete OpenAPI 3.0.1 document at /ws/api/openapi
  name: UAEU Research Portal (Elsevier Pure) — tenant deployment
  slug: pure-research-portal
- description: UAEU publishes open datasets as an organization account on the UAE federal open data portal operated by the Federal Competitiveness and Statistics Centre, built on CKAN. The operator is the UAE federa
  name: UAEU Open Data on the UAE Federal Open Data Portal (CKAN)
  slug: fcsc-open-data
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.uaeu.ac.ae/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uitsws
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/united-arab-emirates-university/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uaeu.ac.ae/en/website/terms_of_use.shtml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uaeu.ac.ae/en/website/privacy_policy.shtml
- group: company
  title: ''
  type: Blog
  url: https://www.uaeu.ac.ae/en/news/
- group: other
  title: ''
  type: IdentityFederation
  url: https://eisprod.uaeu.ac.ae/identity/metadata/saml2
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholarworks.uaeu.ac.ae/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://uaeu.on.worldcat.org/discovery
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.uaeu.ac.ae/en/catalog/
- group: other
  title: ''
  type: OpenData
  url: https://www.uaeu.ac.ae/en/open-data/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uaeu.ac.ae/en/about/pdfs/policies-2025/generative-ai-policy.pdf
- group: build
  title: ''
  type: Library
  url: https://www.uaeu.ac.ae/en/library/
- group: other
  title: ''
  type: Research
  url: https://research.uaeu.ac.ae/
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-arab-emirates-university-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/united-arab-emirates-university-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/united-arab-emirates-university-domain-standards.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-arab-emirates-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/united-arab-emirates-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/united-arab-emirates-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/united-arab-emirates-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'UAEU operates no public API program — no developer portal, no API key self-service, no UAEU-authored OpenAPI, and no agent surface. What machine readability exists falls into two buckets, neither of which is an API product. First, three standards-mandated discovery documents on the university''s own identity service (eisprod.uaeu.ac.ae): OIDC discovery, SAML 2.0 IdP metadata and a SCIM 2.0 ServiceProviderConfig, all 200 unauthenticated. These are saved as artifacts and are the only institution-operated machine-readable surface found. Second, a stack of vendor tenancies — bepress Digital Commons, Elsevier Pure, Blackboard, OCLC WorldCat, Springshare LibGuides, Ellucian Banner, and an organization account on the UAE federal open data portal. The Pure deployment publishes a complete Elsevier OpenAPI without authentication; it was found, read and deliberately not saved, because the contract is Elsevier''s. Every agent and API well-known path on www.uaeu.ac.ae (llms.txt, ai.txt, apis.json,
    openapi.json, .well-known/agent.json, .well-known/mcp.json, .well-known/ai-plugin.json, .well-known/security.txt) returns HTTP 200 with the site''s ~112KB HTML 404 page — soft-404s, credited to nothing.'
  evidence:
  - status: 200
    url: https://eisprod.uaeu.ac.ae/oauth2/oidcdiscovery/.well-known/openid-configuration
  - status: 200
    url: https://eisprod.uaeu.ac.ae/identity/metadata/saml2
  - status: 200
    url: https://eisprod.uaeu.ac.ae/scim2/ServiceProviderConfig
  - status: 200
    url: https://scholarworks.uaeu.ac.ae/do/oai/?verb=Identify
  - status: 200
    url: https://research.uaeu.ac.ae/ws/api/openapi.json
  - status: 401
    url: https://research.uaeu.ac.ae/ws/api/524/persons
  - status: 403
    url: https://opendata.fcsc.gov.ae/api/3/action/package_search?q=uaeu
  - status: 200
    url: https://www.uaeu.ac.ae/llms.txt
  - status: 200
    url: https://www.uaeu.ac.ae/.well-known/agent.json
  - status: 200
    url: https://api.github.com/orgs/uitsws/repos
  reason: no_public_api
  state: none
created: '2026-06-03'
description: 'United Arab Emirates University (UAEU) is the UAE''s national public research university, founded 1976 in Al Ain, Abu Dhabi. Its machine-readable footprint is small, and almost all of what appears under its name is a vendor''s contract running on a UAEU-branded host. Exactly one surface is institution-operated: the UAEU enterprise identity service at eisprod.uaeu.ac.ae, a WSO2 Identity Server deployment on the university''s own domain and certificate, which serves unauthenticated OpenID Connect discovery, SAML 2.0 IdP metadata and a SCIM 2.0 ServiceProviderConfig. Everything else is a tenancy. Scholarworks@UAEU (scholarworks.uaeu.ac.ae) answers OAI-PMH 2.0 but CNAMEs to dcuaeu.bepress.com and reports adminEmail dc-support@elsevier.com — bepress Digital Commons. research.uaeu.ac.ae CNAMEs to uaeu.elsevierpure.com and serves a complete 827-path Elsevier "Pure API" OpenAPI at /ws/api/openapi.json; that contract is Elsevier''s and is deliberately NOT saved in this repository. The
  LMS is a Blackboard tenant, library discovery is OCLC WorldCat, and UAEU''s open data is published as an organization account on the UAE federal portal rather than on its own infrastructure. UAEU does hold its own DataCite provider account (MIWJ) and Crossref membership (prefix 10.36771). There is no public developer portal, no self-service API program, no UAEU-authored OpenAPI, and no agent surface — every well-known path probed returns the site''s soft-404 page.'
finops:
- name: United Arab Emirates University Finops
  service_category: Education
  slug: united-arab-emirates-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-arab-emirates-university.png
jsonld:
- class_count: 13
  name: United Arab Emirates University Context
  property_count: 6
  slug: united-arab-emirates-university-context
layout: provider
modified: '2026-08-30'
name: United Arab Emirates University
nav: Providers
network: true
overview: 'United Arab Emirates University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, United Arab Emirates, and Middle East.


  The United Arab Emirates University catalog on APIs.io includes 1 JSON-LD context.


  United Arab Emirates University''s developer surface includes engineering blog, authentication, and 20 more developer resources.'
plans:
- name: United Arab Emirates University Plans Pricing
  plan_count: 2
  slug: united-arab-emirates-university-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: United Arab Emirates University Rate Limits
  slug: united-arab-emirates-university-rate-limits
scopes:
- name: United Arab Emirates University Scopes
  scope_count: 0
  slug: united-arab-emirates-university-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 34.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-arab-emirates-university/refs/heads/main/screenshots/united-arab-emirates-university-2026-06-20T200041.png
security:
- kind: authentication
  name: United Arab Emirates University Authentication
  slug: united-arab-emirates-university-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: United Arab Emirates University Domain Security
  slug: united-arab-emirates-university-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: united-arab-emirates-university
tags:
- University
- Higher Education
- Education
- United Arab Emirates
- Middle East
- Public Research University
- Identity Federation
- Research Repository
- Open Data
- OAI-PMH
- SCIM
- SAML
website: https://www.uaeu.ac.ae/en/
---
