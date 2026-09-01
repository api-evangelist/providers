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
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Keyless, read-only HAL+JSON REST API of the university's self-hosted DSpace 8.2 / DSpace-CRIS (cris-2024.02.04) institutional repository, served from the university's own domain at repository.nottingh
  name: Repository@Nottingham DSpace REST API
  slug: repository-rest
- description: OAI-PMH 2.0 metadata-harvesting provider of the institution-hosted DSpace repository. Verified live 2026-08-30 — verb=Identify returns 200 text/xml with repositoryName "University of Nottingham Reposi
  name: Repository@Nottingham OAI-PMH (DSpace, institution-hosted)
  slug: repository-dspace-oai
- description: Institution-operated Shibboleth SAML 2.0 identity provider, registered and published as machine-readable metadata in the UK Access Management Federation aggregate. EntityID https://idp.nottingham.ac.u
  name: University of Nottingham Shibboleth Identity Provider (UK Access Management Federation)
  slug: identity-federation
- description: OAI-PMH 2.0 interface for the Worktribe-hosted Repository@Nottingham research-outputs showcase. Confirmed live 2026-08-30 — verb=Identify returns 200 with repositoryName "Repository@Nottingham", admin
  name: Repository@Nottingham OAI-PMH (Worktribe tenant)
  slug: repository-oai
- description: Library discovery and resource management on Ex Libris Alma and Primo VE, operated as a Nottingham tenant across all three campuses. Registered in the UK Access Management Federation as SAML service p
  name: NUsearch library discovery (Ex Libris Alma / Primo VE tenant)
  slug: library-discovery
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.nottingham.ac.uk/
- group: docs
  title: ''
  type: APIReference
  url: https://repository.nottingham.ac.uk/server/api
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.nottingham.ac.uk/library/research/open-access/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://nusearch.nottingham.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.ukfederation.org.uk/
- group: other
  title: ''
  type: OpenData
  url: https://citydataconnector.nottingham.ac.uk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://digitalresearch.nottingham.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.nottingham.ac.uk/studyingeffectively/ai/ai.aspx
- group: docs
  title: ''
  type: Documentation
  url: https://www.nottingham.ac.uk/research/open-research/open-research.aspx
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversityOfNottingham
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Health-Informatics-UoN
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nottingham-CTU
- group: operate
  title: ''
  type: Support
  url: https://www.nottingham.ac.uk/dts/help/it-support.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nottingham.ac.uk/utilities/terms.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nottingham.ac.uk/utilities/privacy/privacy.aspx
- group: company
  title: ''
  type: BlogRSS
  url: https://digitalresearch.nottingham.ac.uk/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-nottingham/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UniofNottingham
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-nottingham-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-nottingham-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-nottingham-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-nottingham-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-nottingham-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Nottingham is a public research university in Nottingham, United Kingdom — a founding Russell Group member with campuses in the UK, Malaysia (UNM) and Ningbo, China (UNNC). It runs no public developer portal and publishes no OpenAPI, and this profile does not pretend otherwise. What it does operate, on its own nottingham.ac.uk hosts, is three genuinely institution-run machine surfaces: a self-hosted DSpace 8.2 / DSpace-CRIS repository at repository.nottingham.ac.uk exposing a keyless read-only HAL+JSON REST API and an OAI-PMH 2.0 provider (oai_dc, qdc, mets, rdf, dim, etdms, uketd_dc and RIOXX v3.0, plus an OpenAIRE CERIF 1.1 base URL), and a Shibboleth SAML 2.0 identity provider registered in the UK Access Management Federation for all three campuses. Its ORCID member integration and its DataCite prefix 10.17639 (1,609 DOIs resolving to its own repository) are verifiable from public endpoints. Alongside these it is a tenant on two vendor platforms — a Worktribe-hosted
  Repository@Nottingham OAI-PMH interface and Ex Libris Alma/Primo VE library discovery (NUsearch) — whose contracts belong to those vendors, not to Nottingham. Student records, timetabling, module enrolment and the VLE are behind SSO and are not publicly documented APIs. Notably, the repository''s human Angular UI is behind an AWS WAF human-verification challenge while its machine API is entirely open.'
finops:
- name: University Of Nottingham Finops
  service_category: Education
  slug: university-of-nottingham-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-nottingham.png
jsonld:
- class_count: 8
  name: University Of Nottingham Context
  property_count: 5
  slug: university-of-nottingham-context
layout: provider
modified: '2026-08-30'
name: University of Nottingham
nav: Providers
network: true
overview: 'University of Nottingham publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Russell Group, and United Kingdom.


  The University of Nottingham catalog on APIs.io includes 1 JSON-LD context.


  University of Nottingham''s developer surface includes API reference, documentation, GitHub presence, support, and 20 more developer resources.'
plans:
- name: University Of Nottingham Plans Pricing
  plan_count: 2
  slug: university-of-nottingham-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: University Of Nottingham Rate Limits
  slug: university-of-nottingham-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 32.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-nottingham/refs/heads/main/screenshots/university-of-nottingham-2026-06-20T200211.png
security:
- kind: domain-security
  name: University Of Nottingham Domain Security
  slug: university-of-nottingham-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-nottingham
tags:
- Education
- Higher Education
- University
- Russell Group
- United Kingdom
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Library
- Research Computing
website: https://www.nottingham.ac.uk/
---
