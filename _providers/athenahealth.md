---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The athenaOne proprietary REST API suite provides over 800 endpoints covering patient management, scheduling, clinical data, revenue cycle, and care coordination. Requires OAuth 2.0 authentication and
  name: athenaOne APIs
  slug: athenaone-apis
- description: athenahealth FHIR R4 APIs provide standards-based access to clinical and administrative data. Supports SMART on FHIR scopes for compliant patient and provider-facing applications. Includes FHIR Subscr
  name: FHIR APIs
  slug: fhir-apis
- description: FHIR API Server for athenaPractice and athenaFlow products, enabling developers to build integrations with athenahealth's on-premise and hybrid deployment products using FHIR R4 standards.
  name: athenaFlex (athenaPractice/athenaFlow) API
  slug: athenaflex-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athenahealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.athenahealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athenahealth.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.athenahealth.com/developer-portal
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/athenahealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/athenahealth
- group: company
  title: ''
  type: Blog
  url: https://www.athenahealth.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.athenahealth.com/why-choose-us/cost-value
- group: operate
  title: ''
  type: StatusPage
  url: https://status.athenahealth.com/
- group: other
  title: ''
  type: X
  url: https://x.com/athenahealth
- group: other
  title: ''
  type: Marketplace
  url: https://www.athenahealth.com/solutions/marketplace-partners
- group: commercial
  title: ''
  type: Plans
  url: plans/athenahealth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/athenahealth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/athenahealth-finops.yml
created: '2026-06-13'
description: athenahealth is a cloud-based healthcare network offering REST APIs for electronic health records (EHR), practice management, patient portal, revenue cycle management, and care coordination across ambulatory and acute care settings. The platform provides over 800 API endpoints enabling developers to extend athenaOne and integrate clinical, financial, and operational workflows across a national network of 84,000+ care sites.
finops:
- name: Athenahealth Finops
  service_category: ''
  slug: athenahealth-finops
graphqls:
- description: athenahealth does not currently offer a public GraphQL API. The platform provides over 800 REST endpoints through its athenaOne proprietary API and FHIR R4 standards-based APIs. This conceptual GraphQ
  name: athenahealth GraphQL Schema
  slug: athenahealth-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/athenahealth.png
jsonld:
- class_count: 27
  name: Athenahealth Context
  property_count: 0
  slug: athenahealth-context
layout: provider
modified: '2026-06-13'
name: athenahealth
nav: Providers
network: true
overview: 'athenahealth publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, EHR, Electronic Health Records, Practice Management, and Revenue Cycle Management.


  The athenahealth catalog on APIs.io includes 1 JSON-LD context.


  athenahealth''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Athenahealth Plans Pricing
  plan_count: 3
  slug: athenahealth-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 0
  name: Athenahealth Rate Limits
  slug: athenahealth-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 5.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/athenahealth/refs/heads/main/screenshots/athenahealth-2026-06-20T172519.png
security:
- kind: domain-security
  name: Athenahealth Domain Security
  slug: athenahealth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: athenahealth
tags:
- Healthcare
- EHR
- Electronic Health Records
- Practice Management
- Revenue Cycle Management
- Patient Portal
- FHIR
- Care Coordination
- Interoperability
- HL7
website: https://www.athenahealth.com/
---
