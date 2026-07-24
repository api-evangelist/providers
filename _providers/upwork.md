---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Upwork Agentic Access
  operation_count: 13
  slug: upwork-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 7
apis:
- description: OAuth 2.0 token management for API access.
  name: Upwork Authentication API
  slug: upwork-authentication-api
- description: Access and manage freelance contracts including terms, milestones, and time entries.
  name: Upwork Contracts API
  slug: upwork-contracts-api
- description: Search and retrieve job postings on the Upwork marketplace.
  name: Upwork Jobs API
  slug: upwork-jobs-api
- description: Read and send messages within active contracts.
  name: Upwork Messages API
  slug: upwork-messages-api
- description: Team and organization management.
  name: Upwork Organizations API
  slug: upwork-organizations-api
- description: Query freelancer and client user profiles, skills, and ratings.
  name: Upwork Profiles API
  slug: upwork-profiles-api
- description: Financial and engagement reports for teams and organizations.
  name: Upwork Reports API
  slug: upwork-reports-api
artifact_total: 102
collections:
- collection_type: open
  name: Upwork GraphQL API
  slug: open-upwork-graphql-api
- collection_type: open
  name: Upwork REST API
  slug: open-upwork-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upwork-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upwork-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upwork-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/upwork-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upwork
- group: company
  title: ''
  type: Website
  url: https://www.upwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.upwork.com/developer/documentation/graphql/api/docs/index.html
- group: start
  title: ''
  type: Portal
  url: https://www.upwork.com/developer
- group: operate
  title: ''
  type: Support
  url: https://support.upwork.com/hc/en-us/sections/17976982721555-Upwork-API
- group: auth
  title: ''
  type: Authentication
  url: https://support.upwork.com/hc/en-us/articles/115015933448-API-authentication-and-security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upwork
- group: build
  title: Python SDK (OAuth2)
  type: GitHubRepository
  url: https://github.com/upwork/python-upwork-oauth2
- group: build
  title: Node.js SDK (OAuth2)
  type: GitHubRepository
  url: https://github.com/upwork/node-upwork-oauth2
- group: build
  title: Java SDK (OAuth2)
  type: GitHubRepository
  url: https://github.com/upwork/java-upwork-oauth2
- group: build
  title: Go SDK (OAuth2)
  type: GitHubRepository
  url: https://github.com/upwork/golang-upwork-oauth2
- group: build
  title: Ruby SDK (OAuth2)
  type: GitHubRepository
  url: https://github.com/upwork/ruby-upwork-oauth2
- group: build
  title: PHP SDK (OAuth2)
  type: GitHubRepository
  url: https://github.com/upwork/php-upwork-oauth2
- group: build
  title: Perl SDK (OAuth2)
  type: GitHubRepository
  url: https://github.com/upwork/perl-upwork-oauth2
- group: design
  title: ''
  type: JSONLD
  url: json-ld/upwork-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/upwork-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/upwork-vocabulary.yaml
created: '2026-03-16'
description: Upwork is a global freelancing platform that connects businesses with independent professionals through a talent marketplace. The Upwork API enables developers to integrate Upwork features into their applications, including job search, contract management, messaging, profile access, and webhook event subscriptions. The API is primarily GraphQL-based at api.upwork.com/graphql, with OAuth 2.0 authentication. Key resources include job postings, contracts, user profiles, messages, and freelancer search. The platform serves over 800,000 clients and 18 million freelancers across 180+ countries.
examples:
- key_count: 2
  name: Graphql Budget Example
  slug: graphql-budget-example
- key_count: 4
  name: Graphql Client Example
  slug: graphql-client-example
- key_count: 10
  name: Graphql Contract Example
  slug: graphql-contract-example
- key_count: 2
  name: Graphql Contract List Response Example
  slug: graphql-contract-list-response-example
- key_count: 11
  name: Graphql Freelancer Profile Example
  slug: graphql-freelancer-profile-example
- key_count: 2
  name: Graphql Freelancer Search Response Example
  slug: graphql-freelancer-search-response-example
- key_count: 3
  name: Graphql Graph Ql Error Example
  slug: graphql-graph-ql-error-example
- key_count: 3
  name: Graphql Graph Ql Request Example
  slug: graphql-graph-ql-request-example
- key_count: 2
  name: Graphql Graph Ql Response Example
  slug: graphql-graph-ql-response-example
- key_count: 11
  name: Graphql Job Example
  slug: graphql-job-example
- key_count: 3
  name: Graphql Job Search Response Example
  slug: graphql-job-search-response-example
- key_count: 1
  name: Graphql Message Create Example
  slug: graphql-message-create-example
- key_count: 6
  name: Graphql Message Example
  slug: graphql-message-example
- key_count: 2
  name: Graphql Message List Response Example
  slug: graphql-message-list-response-example
- key_count: 4
  name: Graphql O Auth Token Example
  slug: graphql-o-auth-token-example
- key_count: 3
  name: Graphql Paging Example
  slug: graphql-paging-example
- key_count: 2
  name: Graphql Skill Example
  slug: graphql-skill-example
- key_count: 5
  name: Rest Engagement Example
  slug: rest-engagement-example
- key_count: 1
  name: Rest Engagement List Response Example
  slug: rest-engagement-list-response-example
- key_count: 1
  name: Rest Report Response Example
  slug: rest-report-response-example
- key_count: 4
  name: Rest Team Example
  slug: rest-team-example
- key_count: 1
  name: Rest Team List Response Example
  slug: rest-team-list-response-example
features:
- description: Search and filter job postings using marketplaceJobPostingsSearch GraphQL query with full-text and faceted search.
  name: Job Search
- description: Access active and completed contracts, contract terms, milestones, and time entries.
  name: Contract Management
- description: Read and send messages within active contracts using GraphQL mutations.
  name: Messaging
- description: Query freelancer and client profiles, skills, portfolios, and ratings.
  name: Profile Access
- description: Subscribe to events for real-time notifications when contracts, jobs, or messages change.
  name: Webhook Subscriptions
- description: Secure API access using OAuth 2.0 authorization code grant flow with refresh token support.
  name: OAuth 2.0 Authentication
- description: Official SDKs for Python, Node.js, Java, Go, Ruby, PHP, and Perl with OAuth2 support.
  name: Multi-Language SDKs
- description: Interactive GraphQL API explorer at upwork.com/developer/explorer for testing queries.
  name: GraphQL Explorer
finops:
- name: Upwork Finops
  service_category: API
  slug: upwork-finops
graphqls:
- description: The primary Upwork API surface, providing GraphQL queries and mutations for job search, profile access, contract management, and messaging. Authentication uses OAuth 2.0 authorization code flow. The A
  name: Upwork GraphQL API
  slug: upwork-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upwork.png
integrations:
- description: Official Power BI connector for importing Upwork data into business intelligence dashboards.
  name: PowerBI Connector
- description: Standard OAuth 2.0 integration with any identity provider supporting authorization code flow.
  name: OAuth 2.0 Providers
- description: Real-time event streaming to external systems via Upwork subscription webhooks.
  name: Webhook Integration
json_schemas:
- name: Budget
  property_count: 2
  slug: graphql-budget
- name: Client
  property_count: 4
  slug: graphql-client
- name: ContractListResponse
  property_count: 2
  slug: graphql-contract-list-response
- name: Contract
  property_count: 10
  slug: graphql-contract
- name: FreelancerProfile
  property_count: 11
  slug: graphql-freelancer-profile
- name: FreelancerSearchResponse
  property_count: 2
  slug: graphql-freelancer-search-response
- name: GraphQLError
  property_count: 3
  slug: graphql-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: graphql-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: graphql-graph-ql-response
- name: Job
  property_count: 11
  slug: graphql-job
- name: JobSearchResponse
  property_count: 3
  slug: graphql-job-search-response
- name: MessageCreate
  property_count: 1
  slug: graphql-message-create
- name: MessageListResponse
  property_count: 2
  slug: graphql-message-list-response
- name: Message
  property_count: 6
  slug: graphql-message
- name: OAuthToken
  property_count: 4
  slug: graphql-o-auth-token
- name: Paging
  property_count: 3
  slug: graphql-paging
- name: Skill
  property_count: 2
  slug: graphql-skill
- name: EngagementListResponse
  property_count: 1
  slug: rest-engagement-list-response
- name: Engagement
  property_count: 5
  slug: rest-engagement
- name: ReportResponse
  property_count: 1
  slug: rest-report-response
- name: TeamListResponse
  property_count: 1
  slug: rest-team-list-response
- name: Team
  property_count: 4
  slug: rest-team
json_structures:
- name: Graphql Budget Structure
  property_count: 2
  slug: graphql-budget-structure
- name: Graphql Client Structure
  property_count: 4
  slug: graphql-client-structure
- name: Graphql Contract List Response Structure
  property_count: 2
  slug: graphql-contract-list-response-structure
- name: Graphql Contract Structure
  property_count: 10
  slug: graphql-contract-structure
- name: Graphql Freelancer Profile Structure
  property_count: 11
  slug: graphql-freelancer-profile-structure
- name: Graphql Freelancer Search Response Structure
  property_count: 2
  slug: graphql-freelancer-search-response-structure
- name: Graphql Graph Ql Error Structure
  property_count: 3
  slug: graphql-graph-ql-error-structure
- name: Graphql Graph Ql Request Structure
  property_count: 3
  slug: graphql-graph-ql-request-structure
- name: Graphql Graph Ql Response Structure
  property_count: 2
  slug: graphql-graph-ql-response-structure
- name: Graphql Job Search Response Structure
  property_count: 3
  slug: graphql-job-search-response-structure
- name: Graphql Job Structure
  property_count: 11
  slug: graphql-job-structure
- name: Graphql Message Create Structure
  property_count: 1
  slug: graphql-message-create-structure
- name: Graphql Message List Response Structure
  property_count: 2
  slug: graphql-message-list-response-structure
- name: Graphql Message Structure
  property_count: 6
  slug: graphql-message-structure
- name: Graphql O Auth Token Structure
  property_count: 4
  slug: graphql-o-auth-token-structure
- name: Graphql Paging Structure
  property_count: 3
  slug: graphql-paging-structure
- name: Graphql Skill Structure
  property_count: 2
  slug: graphql-skill-structure
- name: Rest Engagement List Response Structure
  property_count: 1
  slug: rest-engagement-list-response-structure
- name: Rest Engagement Structure
  property_count: 5
  slug: rest-engagement-structure
- name: Rest Report Response Structure
  property_count: 1
  slug: rest-report-response-structure
- name: Rest Team List Response Structure
  property_count: 1
  slug: rest-team-list-response-structure
- name: Rest Team Structure
  property_count: 4
  slug: rest-team-structure
jsonld:
- class_count: 24
  name: Upwork Context
  property_count: 61
  slug: upwork-context
layout: provider
modified: '2026-05-19'
name: Upwork
nav: Providers
network: true
overview: 'Upwork publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Jobs API, and 4 more. Tagged areas include Freelancing, Jobs, Talent, Marketplace, and Contracts.


  The Upwork catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Upwork''s developer surface includes authentication, documentation, developer portal, support, and 17 more developer resources.'
plans:
- name: Upwork Plans Pricing
  plan_count: 3
  slug: upwork-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Upwork Rate Limits
  slug: upwork-rate-limits
rules:
- name: Upwork API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: upwork-jsonschema-spectral-rules
- name: Upwork API Rules
  rule_count: 27
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 13
  slug: upwork-spectral-rules
scopes:
- name: Upwork Scopes
  scope_count: 9
  slug: upwork-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 54.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.7
    developer_ergonomics: 32.6
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upwork/refs/heads/main/screenshots/upwork-2026-06-20T200510.png
security:
- kind: authentication
  name: Upwork Authentication
  slug: upwork-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Upwork Domain Security
  slug: upwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upwork
tags:
- Freelancing
- Jobs
- Talent
- Marketplace
- Contracts
- Hiring
use_cases:
- description: Agencies and businesses managing a distributed freelancer workforce through programmatic contract and message access.
  name: Freelancer Management
- description: Applications tracking new job postings matching specific criteria using scheduled search queries.
  name: Job Monitoring
- description: Platforms building talent scoring, profile analysis, and market intelligence on freelancers.
  name: Talent Analytics
- description: Connecting Upwork client and contract data to CRM systems for unified client management.
  name: CRM Integration
- description: Building custom dashboards and reports from Upwork contract, billing, and engagement data.
  name: Automated Reporting
website: https://www.upwork.com/
---
