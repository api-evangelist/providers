---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-06'
api_count: 6
apis:
- description: Housing properties.
  name: One Degree Housing API
  slug: one-degree-housing-api
- description: Physical locations, phones, and schedules.
  name: One Degree Locations API
  slug: one-degree-locations-api
- description: Programs/services offered by organizations.
  name: One Degree Opportunities API
  slug: one-degree-opportunities-api
- description: Social-service organizations.
  name: One Degree Organizations API
  slug: one-degree-organizations-api
- description: Property types, rating types, and guides.
  name: One Degree Reference API
  slug: one-degree-reference-api
- description: Community submissions.
  name: One Degree Submissions API
  slug: one-degree-submissions-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Search opportunities by location, then load the top result's details and schedule.
  name: One Degree — find and detail a nearby service
  slug: one-degree-find-services
artifact_total: 12
collections:
- collection_type: postman
  name: One Degree
  slug: postman-one-degree
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: one-degree-mcp.yml
  slug: one-degree-mcpyml
modified: '2026-07-20'
name: One Degree
nav: Providers
network: true
overview: 'One Degree publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Housing API, Locations API, Opportunities API, and 3 more. Tagged areas include Company, Nonprofit, Social Services, Community Resources, and Human Services.


  One Degree''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 83
score:
  band: developing
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.0
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.2
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
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- Nonprofit
- Social Services
- Community Resources
- Human Services
- Public Benefit
- Housing
- Open Data
- Civic Tech
- API
website: https://www.1degree.org/
---
