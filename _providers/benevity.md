---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Benevity Agentic Access
  operation_count: 8
  slug: benevity-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: Create and manage locations (stores, franchises, offices) inside the Benevity ecosystem - address data, contact information, and tags - so multi-location organizations can attribute giving and volunte
  name: Benevity Location Services API
  slug: benevity-location-services-api
- description: The Authorization API from Benevity — 1 operation(s) for authorization.
  name: Benevity Authorization API
  slug: benevity-authorization-api
- description: The Causes API from Benevity — 1 operation(s) for causes.
  name: Benevity Causes API
  slug: benevity-causes-api
- description: The Giving API from Benevity — 2 operation(s) for giving.
  name: Benevity Giving API
  slug: benevity-giving-api
- description: The Receipts API from Benevity — 2 operation(s) for receipts.
  name: Benevity Receipts API
  slug: benevity-receipts-api
- description: The Spark API from Benevity — 2 operation(s) for spark.
  name: Benevity Spark API
  slug: benevity-spark-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Benevity Authorization API
  slug: open-benevity-authorization-api
- collection_type: open
  name: Benevity Authorization Causes API
  slug: open-benevity-causes-api
- collection_type: open
  name: Benevity Authorization Giving API
  slug: open-benevity-giving-api
- collection_type: open
  name: Benevity Authorization Receipts API
  slug: open-benevity-receipts-api
- collection_type: open
  name: Benevity Authorization Spark API
  slug: open-benevity-spark-api
- collection_type: open
  name: Benevity API
  slug: open-benevity
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/benevity-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/benevity-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/benevity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benevity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/benevity-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/benevity
- group: company
  title: ''
  type: Website
  url: https://benevity.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.benevity.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/benevity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/benevity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/benevity-finops.yml
created: '2026-07-03'
description: Benevity is a Calgary-based corporate purpose software platform for workplace giving, matching, grantmaking, and employee/customer volunteering. Its Giving API lets partners embed nonprofit-of-choice donations, optional matching, and charitable gift cards into e-commerce, banking, and rewards experiences; the Cause Search API exposes Benevity's vetted global nonprofit database; the Spark API lets existing Spark Employee Engagement clients surface giving and volunteering opportunities in other interfaces; and the Location Services API lets clients manage locations (stores, franchises, offices) inside the Benevity ecosystem. The API follows the RESTful/OpenAPI standard and is documented publicly at developer.benevity.org, but credentials are partner-gated - access requires requesting a demo/business relationship with Benevity rather than self-serve signup.
finops:
- name: Benevity Finops
  service_category: Corporate Social Responsibility / Workplace Giving Software
  slug: benevity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/benevity.png
layout: provider
modified: '2026-07-03'
name: Benevity
nav: Providers
network: true
overview: 'Benevity publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Causes API, Giving API, and 2 more. Tagged areas include Corporate Social Responsibility, Workplace Giving, Donations, Volunteering, and Non-Profit.


  Benevity''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Benevity Plans Pricing
  plan_count: 1
  slug: benevity-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Benevity Rate Limits
  slug: benevity-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 13.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/benevity/refs/heads/main/screenshots/benevity-2026-07-25T202731.png
security:
- kind: authentication
  name: Benevity Authentication
  slug: benevity-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Benevity Domain Security
  slug: benevity-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Benevity Vulnerability Disclosure
  slug: benevity-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Benevity Trust Center
  slug: benevity-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR, CSA STAR
slug: benevity
tags:
- Corporate Social Responsibility
- Workplace Giving
- Donations
- Volunteering
- Non-Profit
- Matching Gifts
- CSR
- ESG
website: https://benevity.com
---
