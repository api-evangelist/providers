---
access_model:
  confidence: medium
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Amazon Resilience Hub Agentic Access
  operation_count: 21
  slug: amazon-resilience-hub-agentic-access
  summary_line: 21 operations · 12 acting
api_count: 7
apis:
- baseURL: https://resiliencehub.amazonaws.com
  baseurl_source: declared
  description: Create and manage Resilience Hub applications.
  name: Amazon Resilience Hub Applications API
  slug: amazon-resilience-hub-applications-api
- baseURL: https://resiliencehub.amazonaws.com
  baseurl_source: declared
  description: Run and retrieve resilience assessments.
  name: Amazon Resilience Hub Assessments API
  slug: amazon-resilience-hub-assessments-api
- baseURL: https://resiliencehub.amazonaws.com
  baseurl_source: declared
  description: Retrieve alarm, SOP, and test recommendations.
  name: Amazon Resilience Hub Recommendations API
  slug: amazon-resilience-hub-recommendations-api
- baseURL: https://resiliencehub.amazonaws.com
  baseurl_source: declared
  description: Define RTO and RPO targets for applications.
  name: Amazon Resilience Hub Resiliency Policies API
  slug: amazon-resilience-hub-resiliency-policies-api
- baseURL: https://resiliencehub.amazonaws.com
  baseurl_source: declared
  description: Map and import resources into app versions.
  name: Amazon Resilience Hub Resource Management API
  slug: amazon-resilience-hub-resource-management-api
- baseURL: https://resiliencehub.amazonaws.com
  baseurl_source: declared
  description: Manage resource tags.
  name: Amazon Resilience Hub Tags API
  slug: amazon-resilience-hub-tags-api
- baseURL: https://resiliencehub.amazonaws.com
  baseurl_source: declared
  description: The Resilience Hub Operations API from Amazon Resilience Hub — 41 operation(s) for resilience hub operations.
  name: Amazon Resilience Hub Resilience Hub Operations API
  slug: amazon-resilience-hub-operations-api
artifact_total: 22
collections:
- collection_type: open
  name: Amazon Resilience Hub Applications API
  slug: open-amazon-resilience-hub-applications-api
- collection_type: open
  name: Amazon Resilience Hub Applications Assessments API
  slug: open-amazon-resilience-hub-assessments-api
- collection_type: open
  name: Amazon Resilience Hub Applications Recommendations API
  slug: open-amazon-resilience-hub-recommendations-api
- collection_type: open
  name: Amazon Resilience Hub Applications Resiliency Policies API
  slug: open-amazon-resilience-hub-resiliency-policies-api
- collection_type: open
  name: Amazon Resilience Hub Applications Resource Management API
  slug: open-amazon-resilience-hub-resource-management-api
- collection_type: open
  name: Amazon Resilience Hub Applications Tags API
  slug: open-amazon-resilience-hub-tags-api
- collection_type: open
  name: Amazon Resilience Hub
  slug: open-amazon-resilience-hub
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-resilience-hub/plans/amazon-resilience-hub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-resilience-hub-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-resilience-hub/rate-limits/amazon-resilience-hub-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-resilience-hub-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-resilience-hub/finops/amazon-resilience-hub-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-resilience-hub-finops.yml
- group: agent
  href: https://artifacts.apis.io/amazon-resilience-hub/agentic-access/amazon-resilience-hub-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-resilience-hub-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-resilience-hub/security/amazon-resilience-hub-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-resilience-hub-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-resilience-hub/security/amazon-resilience-hub-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-resilience-hub-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-resilience-hub/security/amazon-resilience-hub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-resilience-hub-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-resilience-hub/authentication/amazon-resilience-hub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-resilience-hub-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/resilience-hub/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/resilience-hub/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/resilience-hub/
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
  url: https://aws.amazon.com/blogs/architecture/tag/aws-resilience-hub/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/resiliencehub/
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
description: AWS Resilience Hub provides a central place to define, validate, and track the resilience of your AWS applications. It assesses your application against your Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets and provides actionable recommendations to improve resilience.
finops:
- has_sources: false
  method: generated
  name: Amazon Resilience Hub Finops
  primary_unit: request
  service_category: API
  slug: amazon-resilience-hub-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-resilience-hub.png
layout: provider
modified: '2026-05-19'
name: Amazon Resilience Hub
nav: Providers
network: true
overview: 'Amazon Resilience Hub is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Assessments API, Recommendations API, and 4 more. Tagged areas include Disaster Recovery, High Availability, and Resilience.


  Amazon Resilience Hub''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Resilience Hub Plans Pricing
  plan_count: 3
  slug: amazon-resilience-hub-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Amazon Resilience Hub Rate Limits
  slug: amazon-resilience-hub-rate-limits
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 57.1
    discoverability: 62.5
    operational_transparency: 39.5
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 37.5
      derived: 5
      marker_coverage: 75.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amazon-resilience-hub/amazon-resilience-hub-2026-06-20T171808.png
security:
- kind: authentication
  name: Amazon Resilience Hub Authentication
  slug: amazon-resilience-hub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Resilience Hub Domain Security
  slug: amazon-resilience-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Resilience Hub Vulnerability Disclosure
  slug: amazon-resilience-hub-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Resilience Hub Trust Center
  slug: amazon-resilience-hub-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-resilience-hub
tags:
- Disaster Recovery
- High Availability
- Resilience
website: https://aws.amazon.com/resilience-hub/
---
