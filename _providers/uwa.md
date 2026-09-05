---
access_model:
  confidence: medium
  label: Free · Open harvesting endpoint, no key required
  onboarding: open
  pricing: free
  public: true
  source:
  - probes
  - authentication
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.research-repository.uwa.edu.au/ws/oai
  baseurl_source: declared
  description: An open, unauthenticated OAI-PMH 2.0 metadata harvesting endpoint operated by UWA on its own host. All six protocol verbs returned 200 on 2026-08-30 with no credential presented. Identify reports admi
  name: UWA Research Repository OAI-PMH
  slug: oai-pmh
- description: UWA operates its own Shibboleth identity provider and publishes signed SAML 2.0 federation metadata at https://idp.uwa.edu.au/idp/shibboleth (200, 5,081 bytes). The document is an EntityDescriptor wit
  name: UWA Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: UWA runs a Microsoft Azure API Management estate on its own domains. The developer portal at api-portal.uwa.edu.au returns 200 but serves the stock unbranded Azure APIM shell — title "Home - Microsoft
  name: UWA API Gateway and Developer Portal (Azure API Management)
  slug: developer-portal
- description: UWA's research information system and public research portal, running on Elsevier Pure at research-repository.uwa.edu.au with a CRIS web service at api.research-repository.uwa.edu.au/ws/api/524. The d
  name: UWA Profiles and Research Repository (Elsevier Pure tenancy)
  slug: research-repository
- description: UWA Library discovery, served from onesearch.library.uwa.edu.au and redirecting to an Ex Libris Primo VE application scoped to vid=61UWA_INST. The tenancy is UWA's; the discovery platform, its APIs an
  name: UWA Library OneSearch (Ex Libris Primo VE tenancy)
  slug: library-catalog
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.uwa.edu.au/
- group: company
  title: ''
  type: Blog
  url: https://www.uwa.edu.au/news
- group: operate
  title: ''
  type: Support
  url: https://www.uwa.edu.au/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uwa.edu.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uwa.edu.au/disclaimer-copyright
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uwa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-university-of-western-australia/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/uwanews
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-portal.uwa.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.uwa.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://research-repository.uwa.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://onesearch.library.uwa.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.handbooks.uwa.edu.au/
- group: other
  title: ''
  type: AIPolicy
  url: https://guides.library.uwa.edu.au/artificial_intelligence
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uwa.edu.au/students/-/media/project/uwa/uwa/students/academic-support/using-artificial-intelligence-tools-at-uwa---a-guide-for-students-(2026).pdf
- group: auth
  title: ''
  type: Authentication
  url: authentication/uwa-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uwa-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uwa-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uwa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uwa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uwa-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Western Australia (UWA) is a public research university in Perth, Western Australia, a member of the Group of Eight, and ranked in the top 100 of the QS World University Rankings. Its programmable footprint is small, and most of what appears to be a UWA API is not: the research repository at research-repository.uwa.edu.au runs on Elsevier Pure and its /ws/api/524 web service is Elsevier''s contract, and library discovery at onesearch.library.uwa.edu.au is Ex Libris Primo VE under tenant 61UWA_INST. Both are real UWA services and neither is UWA engineering. What UWA genuinely operates and exposes is narrower and more interesting: a fully open, unauthenticated OAI-PMH 2.0 harvesting endpoint at api.research-repository.uwa.edu.au/ws/oai serving 167 sets across five metadata formats with no key required, and a Shibboleth SAML 2.0 identity provider publishing signed federation metadata at idp.uwa.edu.au/idp/shibboleth. UWA also runs a Microsoft Azure API Management
  estate — a developer portal at api-portal.uwa.edu.au and a live gateway at api.uwa.edu.au — but the product catalog sits behind sign-in and the portal''s own signup path returns 404, so nothing there is publicly enumerable. No open data portal, no public course or timetable API, and no first-party OpenAPI of any kind was found.'
finops:
- name: Uwa Finops
  service_category: Education
  slug: uwa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uwa.png
layout: provider
modified: '2026-08-30'
name: University of Western Australia
nav: Providers
network: true
overview: 'University of Western Australia publishes 1 API on the [APIs.io](https://apis.io/) network: UWA Research Repository OAI-PMH. Tagged areas include Education, Higher Education, University, Australia, and Group of Eight.


  University of Western Australia''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Uwa Plans Pricing
  plan_count: 2
  slug: uwa-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Uwa Rate Limits
  slug: uwa-rate-limits
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 47.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uwa/refs/heads/main/screenshots/uwa-2026-06-20T200736.png
security:
- kind: authentication
  name: Uwa Authentication
  slug: uwa-authentication
  summary_line: none/apiKey/saml2 · 3 schemes
- kind: domain-security
  name: Uwa Domain Security
  slug: uwa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: uwa
tags:
- Education
- Higher Education
- University
- Australia
- Group of Eight
- Perth
- Research
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- Library
website: https://www.uwa.edu.au/
---
