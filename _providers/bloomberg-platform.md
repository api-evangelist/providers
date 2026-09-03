---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: The foundational API layer of the Bloomberg Platform providing real-time, reference, and historical data access through a socket-based protocol with SDKs for multiple programming languages.
  name: Bloomberg Open API (BLPAPI)
  slug: blpapi
- description: Cloud-native connectivity to Bloomberg data enabling access from AWS, Azure, and Google Cloud environments without on-premises Bloomberg infrastructure.
  name: Bloomberg Cloud Connect
  slug: bloomberg-cloud-api
- description: Authentication and authorization services for the Bloomberg Platform providing entitlement management, user authentication, and access control for Bloomberg data and applications.
  name: Bloomberg Identity and Access Management
  slug: bloomberg-identity-api
artifact_total: 17
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bloomberg/blpapi-node/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bloomberg/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bloomberg/.github/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-platform-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: The Bloomberg Platform is the integrated technology infrastructure underpinning all Bloomberg professional products and services. It encompasses the data distribution network, cloud and on-premises deployment options, API connectivity layer, identity and access management, and enterprise integration capabilities that connect Bloomberg data and analytics to client systems.
features:
- description: BLPAPI socket protocol for real-time data connectivity.
  name: API Connectivity
- description: Cloud-native Bloomberg data access from major cloud platforms.
  name: Cloud Deployment
- description: B-PIPE and Server API for on-premises enterprise data integration.
  name: On-Premises Integration
- description: Enterprise authentication and entitlement management.
  name: Identity Management
- description: Redundant infrastructure for mission-critical data connectivity.
  name: High Availability
- description: Optimized data delivery for latency-sensitive trading applications.
  name: Low Latency
finops:
- name: Bloomberg Platform Finops
  service_category: API
  slug: bloomberg-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-platform.png
layout: provider
modified: '2026-08-27'
name: Bloomberg Platform
nav: Providers
network: true
overview: 'Bloomberg Platform publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Platform, Infrastructure, Data Distribution, API Gateway, and Integration.


  Bloomberg Platform''s developer surface includes developer portal, documentation, support, and 8 more developer resources.'
plans:
- name: Bloomberg Platform Plans Pricing
  plan_count: 3
  slug: bloomberg-platform-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Bloomberg Platform Rate Limits
  slug: bloomberg-platform-rate-limits
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 40.0
  previous_composite: 22.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-platform/refs/heads/main/screenshots/bloomberg-platform-2026-06-20T173451.png
security:
- kind: domain-security
  name: Bloomberg Platform Domain Security
  slug: bloomberg-platform-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-platform
tags:
- Platform
- Infrastructure
- Data Distribution
- API Gateway
- Integration
- Bloomberg
use_cases:
- description: Integrate Bloomberg data into enterprise technology stacks.
  name: Enterprise Integration
- description: Migrate Bloomberg data consumption to cloud-native architectures.
  name: Cloud Migration
- description: Build low-latency trading systems on the Bloomberg Platform.
  name: Trading Infrastructure
- description: Develop enterprise data platforms consuming Bloomberg data.
  name: Data Platform Development
website: https://www.bloomberg.com/professional/
---
