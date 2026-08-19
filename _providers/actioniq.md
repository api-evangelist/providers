---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'The ActionIQ Profile API provides real-time access to customer identities, attributes, and audience membership within milliseconds. It powers inbound decisioning use cases such as web personalization '
  name: ActionIQ Profile API
  slug: profile-api
- description: ActionIQ provides a real-time REST API endpoint for streaming customer event data into the platform. The ingestion API supports push-based streaming from in-house systems, enabling businesses to captu
  name: ActionIQ Data Ingestion API
  slug: data-ingestion-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actioniq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.actioniq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.actioniq.com/actioniq-help-center
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ActionIQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/actioniq
- group: company
  title: ''
  type: Blog
  url: https://www.actioniq.com/blog/
- group: other
  title: ''
  type: X
  url: https://twitter.com/actioniqinc
- group: operate
  title: ''
  type: Support
  url: https://www.uniphore.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uniphore.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniphore.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/actioniq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/actioniq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/actioniq-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/actioniq-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/actioniq-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/actioniq-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/actioniq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/actioniq-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/actioniq-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/actioniq-lifecycle.yml
coverage:
  checked: '2026-08-13'
  detail: The ActionIQ API reference is a GitBook space at docs.actioniq.com/actioniq-help-center gated by an Auth0 visitor-auth integration — every path 307s to integrations.gitbook.com, then 302s to login.actioniq.com/authorize and ends on an Auth0 error page — while the live production host api.actioniq.com answers 403 Forbidden from AWS API Gateway on every path, so no OpenAPI, error catalog, or rate-limit header could be read anonymously.
  evidence:
  - status: 400
    url: https://docs.actioniq.com/actioniq-help-center
  - status: 403
    url: https://api.actioniq.com/openapi.json
  - status: 301
    url: https://www.actioniq.com/library/
  - status: 200
    url: https://status.actioniq.com/
  reason: customer-only-docs
  state: gated
created: '2026-06-13'
description: ActionIQ is an enterprise customer data platform (CDP) that provides a REST API for managing customer profiles, building audiences, orchestrating campaigns, and activating data across marketing channels. The platform offers a Profile API for real-time personalization, enabling businesses to access customer identities, attributes, and audience membership within milliseconds to power web personalization, call center decisioning, and real-time customer experiences. ActionIQ was acquired by Uniphore in December 2024 and is now offered as part of Uniphore's composable CDP platform.
finops:
- name: Actioniq Finops
  service_category: ''
  slug: actioniq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/actioniq.png
jsonld:
- class_count: 0
  name: Actioniq Context
  property_count: 7
  slug: actioniq-context
layout: provider
modified: '2026-08-13'
name: ActionIQ
nav: Providers
network: true
overview: 'ActionIQ publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Data Platform, CDP, Audience Management, Real-Time Personalization, and Marketing Orchestration.


  The ActionIQ catalog on APIs.io includes 1 JSON-LD context.


  ActionIQ''s developer surface includes documentation, engineering blog, support, and 17 more developer resources.'
plans:
- name: Actioniq Plans Pricing
  plan_count: 1
  slug: actioniq-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 0
  name: Actioniq Rate Limits
  slug: actioniq-rate-limits
score:
  band: thin
  composite: 28.6
  delta: -0.8
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 7.0
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 29.4
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/actioniq/refs/heads/main/screenshots/actioniq-2026-06-20T164035.png
security:
- kind: domain-security
  name: Actioniq Domain Security
  slug: actioniq-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Actioniq Vulnerability Disclosure
  slug: actioniq-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Actioniq Trust Center
  slug: actioniq-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO/IEC 27017:2015, ISO/IEC 27018:2019, PCI DSS v4.0.1, HIPAA, GDPR, NIST CSF, CASA Tier 2, EU AI Act, FIPS 140-2, FIPS 140-3
slug: actioniq
tags:
- Customer Data Platform
- CDP
- Audience Management
- Real-Time Personalization
- Marketing Orchestration
- Data Activation
- Enterprise
- REST API
website: https://www.actioniq.com
---
