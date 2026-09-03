---
access_model:
  confidence: high
  label: Free · Open repository and harvesting endpoints · no signup
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: DSpace 7.6.1 HAL/JSON REST API for the University of Adelaide institutional repository "Adelaide Research & Scholarship", exposing communities, collections, items, bundles, bitstreams, discovery searc
  name: Adelaide Research & Scholarship REST API
  slug: dspace-rest
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for the "Adelaide Research & Scholarship" repository, on the same institution-operated host. Confirmed live 2026-08-30: Identify returns repositoryName "Adelai'
  name: Adelaide Research & Scholarship OAI-PMH
  slug: dspace-oai-pmh
- description: 'The institution''s own Shibboleth SAML 2.0 Identity Provider, serving machine-readable EntityDescriptor metadata from its own host. Confirmed live 2026-08-30: entityID urn:mace:federation.org.au:testfe'
  name: Adelaide University Shibboleth Identity Provider (SAML 2.0)
  slug: saml-idp
- description: The University's research-data repository runs on Figshare at the institution-specific host adelaide.figshare.com. The DATA, the DOIs and the curation are Adelaide's; the CONTRACT, the object model an
  name: Adelaide Figshare Research Data Repository — Adelaide tenancy
  slug: figshare-tenancy
- description: The University's LMS runs on Instructure Canvas at myuni.adelaide.edu.au. The tenancy, roster and course content are Adelaide's; the API contract is Instructure's. It is recorded because it carries th
  name: MyUni Learning Management System (Instructure Canvas) — Adelaide tenancy
  slug: myuni-canvas
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://adelaide.edu.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/universityofadelaide
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/uniofadelaide/
- group: other
  title: ''
  type: ResearchRepository
  url: https://digital.library.adelaide.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://adelaide.figshare.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://adelaide.edu.au/library/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://adelaide.edu.au/study/
- group: other
  title: ''
  type: IdentityFederation
  url: https://au-idp.adelaide.edu.au/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://md.aaf.edu.au/aaf-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://adelaide.edu.au/about/support/technology/
- group: other
  title: ''
  type: AIPolicy
  url: https://adelaide.edu.au/about/policies/academic-integrity-policy/
- group: other
  title: ''
  type: AIPolicy
  url: https://adelaide.edu.au/about/policies/cyber-security-policy/
- group: build
  title: ''
  type: AITooling
  url: https://app.chatmate.adelaide.edu.au/
- group: auth
  title: ''
  type: Authentication
  url: https://login.adelaide.edu.au/cas/login
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-adelaide-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-adelaide-education-standards.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-adelaide-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/university-of-adelaide-examples.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adelaide.edu.au/about/policies/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adelaide.edu.au/about/disclaimer/
- group: company
  title: ''
  type: Blog
  url: https://adelaide.edu.au/about/news/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-adelaide-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-adelaide-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-adelaide-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-adelaide-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Adelaide is a public research university in Adelaide, South Australia, founded in 1874 and a member of the Group of Eight. Since January 2026 it has been superseded by Adelaide University, the merged institution formed with the University of South Australia: ROR records the University of Adelaide (https://ror.org/00892tw58) as inactive with successor Adelaide University (https://ror.org/028g18b61), adelaide.edu.au now serves the merged institution, and its DataCite and Australian Access Federation records both read "Adelaide University". It operates no public developer program. A full crawl of the 10,326-URL adelaide.edu.au sitemap on 2026-08-30 returned no developer portal, no API reference, no open-data portal, and no OpenAPI under any path. Its genuinely institution-operated machine-readable surfaces are three: the DSpace 7.6.1 "Adelaide Research & Scholarship" repository at digital.library.adelaide.edu.au, which serves a keyless HAL/JSON REST API and a
  live OAI-PMH 2.0 endpoint under the institution''s own Handle prefix 2440; and the institution''s Shibboleth SAML 2.0 Identity Provider at au-idp.adelaide.edu.au, registered in the Australian Access Federation and scoped to adelaide.edu.au. Everything else that looks like an Adelaide API is a vendor contract running under an Adelaide name: adelaide.figshare.com is a Figshare tenancy, myuni.adelaide.edu.au is an Instructure Canvas tenancy exposing LTI 1.3 and OIDC discovery, and access.adelaide.edu.au is a PeopleSoft student system behind Okta SSO. This profile is deliberately thin because the footprint is thin.'
examples:
- key_count: 6
  name: University Of Adelaide Dspace Rest Root Response
  slug: university-of-adelaide-dspace-rest-root-response
finops:
- name: University Of Adelaide Finops
  service_category: Education
  slug: university-of-adelaide-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-adelaide.png
layout: provider
modified: '2026-08-30'
name: University of Adelaide
nav: Providers
network: true
overview: 'University of Adelaide publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Australia, and Group of Eight.


  University of Adelaide''s developer surface includes authentication, code examples, engineering blog, and 23 more developer resources.'
plans:
- name: University Of Adelaide Plans Pricing
  plan_count: 2
  slug: university-of-adelaide-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Adelaide Rate Limits
  slug: university-of-adelaide-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.8
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 3.8
    contract_quality: 10.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 3.8
    operational_transparency: 23.7
  previous_composite: 32.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-adelaide/refs/heads/main/screenshots/university-of-adelaide-2026-06-20T200125.png
security:
- kind: authentication
  name: University Of Adelaide Authentication
  slug: university-of-adelaide-authentication
  summary_line: saml2/cas/oidc · 4 schemes
- kind: domain-security
  name: University Of Adelaide Domain Security
  slug: university-of-adelaide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-adelaide
tags:
- University
- Higher Education
- Education
- Australia
- Group of Eight
- Research Repository
- Research Data
- Library
- OAI-PMH
- DSpace
- Identity Federation
- Shibboleth
- Metadata
- Course Catalog
website: https://adelaide.edu.au/
---
