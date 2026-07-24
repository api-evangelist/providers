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
- acting_count: 0
  human_in_the_loop: 0
  name: Gitcoin Agentic Access
  operation_count: 13
  slug: gitcoin-agentic-access
  summary_line: 13 operations
api_count: 7
apis:
- description: GraphQL API for querying indexed on-chain data from the Gitcoin Grants Stack and Allo Protocol. Provides access to funding rounds, projects, applications, contributions, and quadratic funding match ca
  name: Gitcoin Grants Stack Indexer API
  slug: gitcoin-grants-stack-indexer-api
- description: Operations related to Gitcoin bounties
  name: Gitcoin Bounties API
  slug: gitcoin-bounties-api
- description: Operations for accessing contributor address data
  name: Gitcoin Contributors API
  slug: gitcoin-contributors-api
- description: Operations related to Gitcoin grants
  name: Gitcoin Grants API
  slug: gitcoin-grants-api
- description: The Model Analysis API from Gitcoin — 1 operation(s) for model analysis.
  name: Gitcoin Model Analysis API
  slug: gitcoin-model-analysis-api
- description: Operations related to Gitcoin Grants funding rounds
  name: Gitcoin Rounds API
  slug: gitcoin-rounds-api
- description: The Stamp API API from Gitcoin — 4 operation(s) for stamp api.
  name: Gitcoin Stamp API API
  slug: gitcoin-stamp-api-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitcoin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitcoin-domain-security.yml
- group: auth
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
- name: Finops
  service_category: ''
  slug: finops
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
modified: '2026-06-14'
name: Gitcoin
nav: Providers
network: true
overview: 'Gitcoin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bounties API, Contributors API, Grants API, and 3 more. Tagged areas include Public Goods, Grants, Bounties, Quadratic Funding, and Web3.


  The Gitcoin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gitcoin''s developer surface includes authentication, engineering blog, documentation, support, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 35
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
rules:
- name: Gitcoin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gitcoin-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 76.5
    developer_ergonomics: 26.1
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 60.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
