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
  scored_at: '2026-09-03'
api_count: 9
apis:
- description: CWRU's own Shibboleth Identity Provider, entityID urn:mace:incommon:case.edu. Every SingleSignOnService binding in the production descriptor is on CWRU's own registrable domain — https://login.case.ed
  name: CWRU Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
- description: CWRU runs an Apereo CAS deployment at login.case.edu as its campus single sign-on service. The CAS 3.0 protocol validation endpoint /cas/p3/serviceValidate answers unauthenticated with a well-formed c
  name: CWRU Apereo CAS single sign-on (login.case.edu)
  slug: apereo-cas
- description: An open OAI-PMH 2.0 metadata provider on CWRU's own host. Identify reports repositoryName "Scholarly Commons @ Case Western Reserve University", repositoryIdentifier commons.case.edu, earliestDatestam
  name: Scholarly Commons @ CWRU — OAI-PMH 2.0 provider
  slug: scholarly-commons-oai-pmh
- description: CWRU's Microsoft Entra ID tenant, dc1c97ee-7a12-4624-9a01-9ad4f05d1311, resolved from the case.edu domain hint. OpenID Connect discovery answers unauthenticated at https://login.microsoftonline.com/ca
  name: CWRU Microsoft Entra ID tenant (OIDC + SAML metadata)
  slug: entra-id-tenant
- description: CWRU is a registered Crossref member, id 7530, primary-name "Case Western Reserve University", holding six DOI prefixes (10.18062, 10.18581, 10.18582, 10.18695, 10.28953, 10.20411) and 475 deposited D
  name: Crossref member registration — Case Western Reserve University (member 7530)
  slug: crossref-member
- description: CWRU's Research Organization Registry record, https://ror.org/051fd9666, established 1826, domain case.edu, located in Cleveland, Ohio, US. External identifiers cross-walk to Crossref Funder IDs 10000
  name: ROR organization record — Case Western Reserve University (051fd9666)
  slug: ror-record
- description: CWRU's institutional analytics platform, hosted on its own domain at data.case.edu. The unauthenticated Tableau REST serverInfo endpoint reports productVersion 2025.1.5 (build 20251.25.0724.1105), pre
  name: CWRU Tableau Server deployment (data.case.edu)
  slug: tableau-server
- description: CWRU's library discovery layer is an Ex Libris Primo view operated through the OhioLINK consortium. digital.case.edu — a CWRU-owned hostname — redirects to ohiolink-cwru.primo.exlibrisgroup.com with t
  name: CWRU library discovery — Ex Libris Primo view 01OHIOLINK_CWRU:CWRUC
  slug: primo-discovery-view
- description: The 2026-27 General Bulletin, CWRU's authoritative course catalog, runs on Leepfrog CourseLeaf at bulletin.case.edu — a CWRU host, a vendor product. It publishes a sitemap (https://bulletin.case.edu/s
  name: CWRU General Bulletin — Leepfrog CourseLeaf catalog (bulletin.case.edu)
  slug: courseleaf-bulletin
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://case.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://case.edu/utech/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cwru
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/case-western-reserve-university/
- group: company
  title: ''
  type: Blog
  url: https://case.edu/news/
- group: operate
  title: ''
  type: Support
  url: https://cwru.teamdynamix.com/TDClient/126/Portal/Home/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://case.edu/utech/policies/legal-privacy-notice/
- group: auth
  title: ''
  type: Authentication
  url: https://login.case.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Acase.edu
- group: other
  title: ''
  type: ResearchRepository
  url: https://commons.case.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ohiolink-cwru.primo.exlibrisgroup.com/discovery/search?vid=01OHIOLINK_CWRU:CWRUC
- group: learn
  title: ''
  type: CourseCatalog
  url: https://bulletin.case.edu/
- group: other
  title: ''
  type: OpenData
  url: https://case.edu/registrar/general/statistics-and-data
- group: other
  title: ''
  type: ResearchComputing
  url: https://case.edu/utech/departments/research-computing-and-infrastructure-services
- group: other
  title: ''
  type: AIPolicy
  url: https://case.edu/ai/governance-policies
- group: build
  title: ''
  type: AITooling
  url: https://case.edu/ai/tools-resources
- group: design
  title: ''
  type: Conformance
  url: conformance/case-western-reserve-university-domain-standards.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/case-western-reserve-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/case-western-reserve-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/case-western-reserve-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/case-western-reserve-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/case-western-reserve-university-context.jsonld
- group: other
  title: ''
  type: ProductPage
  url: https://researchguides.case.edu/discovery
created: '2026-06-03'
description: 'Case Western Reserve University (CWRU) is a private research university in Cleveland, Ohio, founded 1826 and a member of the Association of American Universities. It operates no public developer portal and no public API program: api.case.edu, developer.case.edu and developers.case.edu do not resolve, case.edu/llms.txt and /.well-known/security.txt both return 404, and its GitHub organization (github.com/cwru) holds six repositories of which four are archived web-template tooling last touched in 2016-17. What CWRU does operate, and what this profile records, is a small set of genuinely institution-run identity and harvesting surfaces — a Shibboleth SAML 2.0 Identity Provider on login.case.edu registered in InCommon (urn:mace:incommon:case.edu, scoped to case.edu and eight school subdomains), an Apereo CAS single sign-on service on the same host, and an open OAI-PMH 2.0 provider for Scholarly Commons at commons.case.edu — alongside tenancies it holds on other people''s platforms
  (bepress Digital Commons, Ex Libris Primo through the OhioLINK consortium, Tableau Server, Leepfrog CourseLeaf, Microsoft Entra ID) and its registration in the Crossref and ROR registries. Every entry below carries an x-operator saying who actually runs the thing described. No vendor contract is saved under CWRU''s name.'
finops:
- name: Case Western Reserve University Finops
  service_category: Education
  slug: case-western-reserve-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/case-western-reserve-university.png
jsonld:
- class_count: 14
  name: Case Western Reserve University Context
  property_count: 4
  slug: case-western-reserve-university-context
layout: provider
modified: '2026-09-01'
name: Case Western Reserve University
nav: Providers
network: true
overview: 'Case Western Reserve University publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Private Research University, and Association of American Universities.


  The Case Western Reserve University catalog on APIs.io includes 1 JSON-LD context.


  Case Western Reserve University''s developer surface includes documentation, engineering blog, support, authentication, and 20 more developer resources.'
plans:
- name: Case Western Reserve University Plans Pricing
  plan_count: 2
  slug: case-western-reserve-university-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Case Western Reserve University Rate Limits
  slug: case-western-reserve-university-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/case-western-reserve-university/refs/heads/main/screenshots/case-western-reserve-university-2026-06-20T174030.png
security:
- kind: authentication
  name: Case Western Reserve University Authentication
  slug: case-western-reserve-university-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Case Western Reserve University Domain Security
  slug: case-western-reserve-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: case-western-reserve-university
tags:
- Education
- Higher Education
- University
- Private Research University
- Association of American Universities
- Research
- Identity Federation
- Shibboleth
- SAML
- OAI-PMH
- Research Repository
- Library
- Course Catalog
- Crossref
- Cleveland
- Ohio
- United States
website: https://case.edu/
---
