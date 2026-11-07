---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gitcoin Agentic Access
  operation_count: 13
  slug: gitcoin-agentic-access
  summary_line: 13 operations
api_count: 3
apis:
- description: GraphQL API for querying indexed on-chain data from the Gitcoin Grants Stack and Allo Protocol. Provides access to funding rounds, projects, applications, contributions, and quadratic funding match ca
  name: Gitcoin Grants Stack Indexer API
  slug: gitcoin-grants-stack-indexer-api
- baseURL: https://gitcoin.co/api/v0.1
  baseurl_source: declared
  description: Operations related to Gitcoin bounties
  name: Gitcoin Bounties API
  slug: gitcoin-bounties-api
- baseURL: https://gitcoin.co/api/v0.1
  baseurl_source: declared
  description: Operations for accessing contributor address data
  name: Gitcoin Contributors API
  slug: gitcoin-contributors-api
- baseURL: https://gitcoin.co/api/v0.1
  baseurl_source: declared
  description: Operations related to Gitcoin grants
  name: Gitcoin Grants API
  slug: gitcoin-grants-api
- baseURL: https://gitcoin.co/api/v0.1
  baseurl_source: declared
  description: The Model Analysis API from Gitcoin — 1 operation(s) for model analysis.
  name: Gitcoin Model Analysis API
  slug: gitcoin-model-analysis-api
- baseURL: https://gitcoin.co/api/v0.1
  baseurl_source: declared
  description: The Stamp API API from Gitcoin — 4 operation(s) for stamp api.
  name: Gitcoin Stamp API
  slug: gitcoin-stamp-api-api
artifact_total: 32
collections:
- collection_type: postman
  name: Gitcoin Core Bounties API
  slug: postman-gitcoin-bounties-api
- collection_type: postman
  name: Gitcoin Core Bounties Contributors API
  slug: postman-gitcoin-contributors-api
- collection_type: postman
  name: Gitcoin Core Bounties Grants API
  slug: postman-gitcoin-grants-api
- collection_type: postman
  name: Gitcoin Core Bounties Model Analysis API
  slug: postman-gitcoin-model-analysis-api
- collection_type: postman
  name: Gitcoin Core Bounties Rounds API
  slug: postman-gitcoin-rounds-api
- collection_type: postman
  name: Gitcoin Core Bounties Stamp API API
  slug: postman-gitcoin-stamp-api-api
- collection_type: open
  name: Gitcoin Core Bounties API
  slug: open-gitcoin-bounties-api
- collection_type: open
  name: Gitcoin Core Bounties Contributors API
  slug: open-gitcoin-contributors-api
- collection_type: open
  name: Gitcoin Core Bounties Grants API
  slug: open-gitcoin-grants-api
- collection_type: open
  name: Gitcoin Core Bounties Model Analysis API
  slug: open-gitcoin-model-analysis-api
- collection_type: open
  name: Gitcoin Core Bounties Rounds API
  slug: open-gitcoin-rounds-api
- collection_type: open
  name: Gitcoin Core Bounties Stamp API API
  slug: open-gitcoin-stamp-api-api
common:
- group: commercial
  href: https://artifacts.apis.io/gitcoin/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://artifacts.apis.io/gitcoin/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gitcoin/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/gitcoinco/grants-stack-indexer/issues
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gitcoin/overview
- group: agent
  href: https://artifacts.apis.io/gitcoin/agentic-access/gitcoin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitcoin-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gitcoin/security/gitcoin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitcoin-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gitcoin/authentication/gitcoin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitcoin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gitcoin.co/
- group: company
  title: ''
  type: Blog
  url: https://gitcoin.co/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitcoin.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitcoinco
- group: operate
  title: ''
  type: Support
  url: https://support.gitcoin.co/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/gitcoin
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/gitcoin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitcoin
- group: operate
  title: ''
  type: Forums
  url: https://gov.gitcoin.co/
- group: build
  title: ''
  type: PythonClient
  url: https://github.com/gitcoinco/python-api-client
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gitcoin.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitcoin.co/privacy
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/gitcoin/refs/heads/main/json-ld/context.jsonld
created: '2026-06-14'
description: Gitcoin is a public goods funding platform that enables communities to fund open-source software, research, and other digital public goods through quadratic funding, direct grants, and bounties. The platform provides REST APIs for querying grants, bounties, funding rounds, and project metadata, as well as the Gitcoin Passport Stamps API for verifiable credential scoring and identity verification.
examples:
- key_count: 34
  name: Bounty Example
  slug: bounty-example
- key_count: 7
  name: Passport Score Example
  slug: passport-score-example
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
graphqls:
- description: 'The Gitcoin Grants Stack Indexer exposes a GraphQL API built with PostGraphile, which introspects a PostgreSQL database and auto-generates a fully-typed GraphQL schema from the underlying tables. The '
  name: Gitcoin GraphQL API
  slug: gitcoin-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitcoin.png
json_schemas:
- name: Gitcoin Bounty
  property_count: 34
  slug: bounty
- name: Gitcoin Grant
  property_count: 16
  slug: grant
- name: Gitcoin Passport Stamp
  property_count: 3
  slug: passport-stamp
jsonld:
- class_count: 38
  name: context Context
  property_count: 17
  slug: context
layout: provider
modified: '2026-09-16'
name: Gitcoin
nav: Providers
network: true
overview: 'Gitcoin publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bounties API, Contributors API, Grants API, and 3 more. Tagged areas include Public Goods, Grants, Bounties, Quadratic Funding, and Web3.


  The Gitcoin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gitcoin''s developer surface includes authentication, engineering blog, documentation, support, and 17 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Gitcoin — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gitcoin-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.3
    catalog_earned_first_party: 0.0
    catalog_gap: 45.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 65.0
    developer_ergonomics: 50.0
    discoverability: 71.4
    operational_transparency: 10.5
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 60.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/gitcoin/gitcoin-2026-08-17T123547.png
security:
- kind: authentication
  name: Gitcoin Authentication
  slug: gitcoin-authentication
  summary_line: apiKey/openIdConnect · 4 schemes
- kind: domain-security
  name: Gitcoin Domain Security
  slug: gitcoin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gitcoin
tags:
- Public Goods
- Grants
- Bounties
- Quadratic Funding
- Web3
- Verifiable Credentials
- Identity
- Open Source
website: https://gitcoin.co/
---
