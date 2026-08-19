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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Amazon Resilience Hub Agentic Access
  operation_count: 21
  slug: amazon-resilience-hub-agentic-access
  summary_line: 21 operations · 15 acting
api_count: 6
apis:
- description: Create and manage Resilience Hub applications.
  name: Amazon Resilience Hub Applications API
  slug: amazon-resilience-hub-applications-api
- description: Run and retrieve resilience assessments.
  name: Amazon Resilience Hub Assessments API
  slug: amazon-resilience-hub-assessments-api
- description: Retrieve alarm, SOP, and test recommendations.
  name: Amazon Resilience Hub Recommendations API
  slug: amazon-resilience-hub-recommendations-api
- description: Define RTO and RPO targets for applications.
  name: Amazon Resilience Hub Resiliency Policies API
  slug: amazon-resilience-hub-resiliency-policies-api
- description: Map and import resources into app versions.
  name: Amazon Resilience Hub Resource Management API
  slug: amazon-resilience-hub-resource-management-api
- description: Manage resource tags.
  name: Amazon Resilience Hub Tags API
  slug: amazon-resilience-hub-tags-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-resilience-hub-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-resilience-hub-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-resilience-hub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-resilience-hub-domain-security.yml
- group: auth
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
- name: Amazon Resilience Hub Finops
  service_category: API
  slug: amazon-resilience-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-resilience-hub.png
layout: provider
modified: '2026-05-19'
name: Amazon Resilience Hub
nav: Providers
network: true
overview: 'Amazon Resilience Hub publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Assessments API, Recommendations API, and 3 more. Tagged areas include Disaster Recovery, High Availability, Operations, and Resilience.


  Amazon Resilience Hub''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 11 more developer resources.'
plans:
- name: Amazon Resilience Hub Plans Pricing
  plan_count: 3
  slug: amazon-resilience-hub-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Amazon Resilience Hub Rate Limits
  slug: amazon-resilience-hub-rate-limits
score:
  band: thin
  composite: 32.6
  delta: -1.5
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 15.4
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-resilience-hub/refs/heads/main/screenshots/amazon-resilience-hub-2026-06-20T171808.png
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
- Operations
- Resilience
website: https://aws.amazon.com/resilience-hub/
---
