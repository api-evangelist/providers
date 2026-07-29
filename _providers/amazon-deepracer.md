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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amazon Deepracer Agentic Access
  operation_count: 10
  slug: amazon-deepracer-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 4
apis:
- description: Manage DeepRacer physical vehicles and their configurations
  name: Amazon DeepRacer Cars API
  slug: amazon-deepracer-cars-api
- description: Manage racing leaderboards and submissions
  name: Amazon DeepRacer Leaderboards API
  slug: amazon-deepracer-leaderboards-api
- description: Manage reinforcement learning models for autonomous racing
  name: Amazon DeepRacer Models API
  slug: amazon-deepracer-models-api
- description: Manage virtual and physical racing tracks
  name: Amazon DeepRacer Tracks API
  slug: amazon-deepracer-tracks-api
artifact_total: 53
collections:
- collection_type: postman
  name: Amazon DeepRacer Cars API
  slug: postman-amazon-deepracer-cars-api
- collection_type: postman
  name: Amazon DeepRacer Cars Leaderboards API
  slug: postman-amazon-deepracer-leaderboards-api
- collection_type: postman
  name: Amazon DeepRacer Cars Models API
  slug: postman-amazon-deepracer-models-api
- collection_type: postman
  name: Amazon DeepRacer Cars Tracks API
  slug: postman-amazon-deepracer-tracks-api
- collection_type: open
  name: Amazon DeepRacer API
  slug: open-amazon-deepracer
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-deepracer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-deepracer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-deepracer-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-deepracer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-deepracer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-deepracer-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/deepracer/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/deepracer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/deepracer/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/tag/aws-deepracer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/deepracer/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
created: '2026-03-16'
description: AWS DeepRacer is an autonomous 1/18th scale race car designed to test reinforcement learning (RL) models by racing on a physical track. It provides a fully autonomous driving platform that enables developers to get hands-on experience with machine learning through a fun and engaging racing experience.
examples:
- key_count: 6
  name: Car Example
  slug: car-example
- key_count: 2
  name: Error Example
  slug: error-example
- key_count: 7
  name: Leaderboard Example
  slug: leaderboard-example
- key_count: 6
  name: Leaderboard Submission Example
  slug: leaderboard-submission-example
- key_count: 2
  name: List Cars Response Example
  slug: list-cars-response-example
- key_count: 2
  name: List Leaderboard Submissions Response Example
  slug: list-leaderboard-submissions-response-example
- key_count: 2
  name: List Leaderboards Response Example
  slug: list-leaderboards-response-example
- key_count: 2
  name: List Models Response Example
  slug: list-models-response-example
- key_count: 2
  name: List Tracks Response Example
  slug: list-tracks-response-example
- key_count: 6
  name: Model Example
  slug: model-example
- key_count: 4
  name: Track Example
  slug: track-example
finops:
- name: Amazon Deepracer Finops
  service_category: API
  slug: amazon-deepracer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-deepracer.png
json_schemas:
- name: Car
  property_count: 6
  slug: car
- name: Error
  property_count: 2
  slug: error
- name: Leaderboard
  property_count: 7
  slug: leaderboard
- name: LeaderboardSubmission
  property_count: 6
  slug: leaderboard-submission
- name: ListCarsResponse
  property_count: 2
  slug: list-cars-response
- name: ListLeaderboardSubmissionsResponse
  property_count: 2
  slug: list-leaderboard-submissions-response
- name: ListLeaderboardsResponse
  property_count: 2
  slug: list-leaderboards-response
- name: ListModelsResponse
  property_count: 2
  slug: list-models-response
- name: ListTracksResponse
  property_count: 2
  slug: list-tracks-response
- name: Model
  property_count: 7
  slug: model
- name: Track
  property_count: 4
  slug: track
json_structures:
- name: Car Structure
  property_count: 0
  slug: car-structure
- name: Error Structure
  property_count: 0
  slug: error-structure
- name: Leaderboard Structure
  property_count: 0
  slug: leaderboard-structure
- name: Leaderboard Submission Structure
  property_count: 0
  slug: leaderboard-submission-structure
- name: List Cars Response Structure
  property_count: 0
  slug: list-cars-response-structure
- name: List Leaderboard Submissions Response Structure
  property_count: 0
  slug: list-leaderboard-submissions-response-structure
- name: List Leaderboards Response Structure
  property_count: 0
  slug: list-leaderboards-response-structure
- name: List Models Response Structure
  property_count: 0
  slug: list-models-response-structure
- name: List Tracks Response Structure
  property_count: 0
  slug: list-tracks-response-structure
- name: Model Structure
  property_count: 0
  slug: model-structure
- name: Track Structure
  property_count: 0
  slug: track-structure
jsonld:
- class_count: 0
  name: Amazon Deepracer Context
  property_count: 36
  slug: amazon-deepracer-context
layout: provider
modified: '2026-05-19'
name: Amazon DeepRacer
nav: Providers
network: true
overview: 'Amazon DeepRacer publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cars API, Leaderboards API, Models API, and 1 more. Tagged areas include Autonomous Vehicles, Machine Learning, Reinforcement Learning, and Robotics.


  The Amazon DeepRacer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon DeepRacer''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 12 more developer resources.'
plans:
- name: Amazon Deepracer Plans Pricing
  plan_count: 3
  slug: amazon-deepracer-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Amazon Deepracer Rate Limits
  slug: amazon-deepracer-rate-limits
rules:
- name: Amazon DeepRacer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-deepracer-jsonschema-spectral-rules
- name: Amazon DeepRacer API Rules
  rule_count: 26
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 10
  slug: amazon-deepracer-spectral-rules
score:
  band: strong
  composite: 63.8
  delta: -2.9
  facets:
    commercial_clarity: 81.6
    contract_quality: 72.0
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 66.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-deepracer/refs/heads/main/screenshots/amazon-deepracer-2026-06-20T171619.png
security:
- kind: authentication
  name: Amazon Deepracer Authentication
  slug: amazon-deepracer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Deepracer Domain Security
  slug: amazon-deepracer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Deepracer Vulnerability Disclosure
  slug: amazon-deepracer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Deepracer Trust Center
  slug: amazon-deepracer-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-deepracer
tags:
- Autonomous Vehicles
- Machine Learning
- Reinforcement Learning
- Robotics
website: https://aws.amazon.com/deepracer/
---
