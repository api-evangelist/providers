---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://data.1degree.org/v1
  baseurl_source: declared
  description: Housing properties.
  name: One Degree Housing API
  slug: one-degree-housing-api
- baseURL: https://data.1degree.org/v1
  baseurl_source: declared
  description: Physical locations, phones, and schedules.
  name: One Degree Locations API
  slug: one-degree-locations-api
- baseURL: https://data.1degree.org/v1
  baseurl_source: declared
  description: Programs/services offered by organizations.
  name: One Degree Opportunities API
  slug: one-degree-opportunities-api
- baseURL: https://data.1degree.org/v1
  baseurl_source: declared
  description: Social-service organizations.
  name: One Degree Organizations API
  slug: one-degree-organizations-api
- baseURL: https://data.1degree.org/v1
  baseurl_source: declared
  description: Property types, rating types, and guides.
  name: One Degree Reference API
  slug: one-degree-reference-api
- baseURL: https://data.1degree.org/v1
  baseurl_source: declared
  description: Community submissions.
  name: One Degree Submissions API
  slug: one-degree-submissions-api
arazzos:
- description: Search opportunities by location, then load the top result's details and schedule.
  name: One Degree — find and detail a nearby service
  slug: one-degree-find-services
artifact_total: 17
collections:
- collection_type: postman
  name: One Degree
  slug: postman-one-degree
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: One Degree Resource Server Housing API
  slug: open-one-degree-housing-api
- collection_type: open
  name: One Degree Resource Server Housing Locations API
  slug: open-one-degree-locations-api
- collection_type: open
  name: One Degree Resource Server Housing Opportunities API
  slug: open-one-degree-opportunities-api
- collection_type: open
  name: One Degree Resource Server Housing Organizations API
  slug: open-one-degree-organizations-api
- collection_type: open
  name: One Degree Resource Server Housing Reference API
  slug: open-one-degree-reference-api
- collection_type: open
  name: One Degree Resource Server Housing Submissions API
  slug: open-one-degree-submissions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/one-degree-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://about.1degree.org/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/1deg/resource-server-api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/1deg/resource-server-api-docs/blob/main/README.md
- group: company
  title: ''
  type: Website
  url: https://www.1degree.org/
- group: company
  title: ''
  type: Blog
  url: https://about.1degree.org/latest-news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.1degree.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.1degree.org/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1deg
- group: operate
  title: ''
  type: Support
  url: https://about.1degree.org/contact-us/
- group: start
  title: ''
  type: SignUp
  url: http://socialservicedata.org/api/get-key/
- group: build
  title: ''
  type: Postman
  url: postman/one-degree.postman_collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/one-degree-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/one-degree-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/one-degree-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/one-degree-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/one-degree-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/one-degree-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/one-degree-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/one-degree-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/one-degree-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/one-degree-find-services.yml
created: '2026-07-17'
description: One Degree is a California-based 501(c)(3) nonprofit technology organization that empowers low-income and underserved individuals, families, and social-service professionals to find and access life-changing benefits and services. Its Resource Server API exposes a curated, community- maintained database of social-service resources — organizations and the opportunities (programs and services) they offer, along with locations, phones, schedules, ratings, tags, comments, images, properties, guides, and housing properties. The API is designed for interoperability with third-party services so communities can coordinate and deliver social services more effectively. It is a read-focused REST API served at data.1degree.org/v1, authenticated with an api_key query parameter and HMAC-SHA256 request signatures for write verbs. Resource data is licensed under Creative Commons Attribution-NonCommercial 4.0 International.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/one-degree.png
layout: provider
modified: '2026-07-20'
name: One Degree
nav: Providers
network: true
overview: 'One Degree publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Housing API, Locations API, Opportunities API, and 3 more. Tagged areas include Company, Non-Profit, Social Services, Community Resources, and Human Services.


  One Degree''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 48.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/one-degree/refs/heads/main/screenshots/one-degree-2026-08-07T190242.png
security:
- kind: authentication
  name: One Degree Authentication
  slug: one-degree-authentication
  summary_line: apiKey/custom-signature · 2 schemes
- kind: domain-security
  name: One Degree Domain Security
  slug: one-degree-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: one-degree
tags:
- Company
- Non-Profit
- Social Services
- Community Resources
- Human Services
- Public Benefit
- Housing
- Open Data
- Civic Tech
website: https://www.1degree.org/
---
