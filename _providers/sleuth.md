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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Sleuth Agentic Access
  operation_count: 4
  slug: sleuth-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: Sleuth's primary public API, built on GraphQL - the same API Sleuth uses internally - for managing projects, environments, deployments, and metrics, with an interactive GraphiQL explorer at the endpoi
  name: Sleuth GraphQL API
  slug: graphql
- description: Outbound webhook automation action that sends an HTTP POST with a JSON deployment payload to a URL of your choosing, signed with X-SLEUTH-TIMESTAMP and X-SLEUTH-SIGNATURE headers (Slack-style verifica
  name: Sleuth Webhook Actions
  slug: webhooks
- baseURL: https://app.sleuth.io/api/1
  baseurl_source: declared
  description: The Deployments API from Sleuth — 1 operation(s) for deployments.
  name: Sleuth Deployments API
  slug: sleuth-deployments-api
- baseURL: https://app.sleuth.io/api/1
  baseurl_source: declared
  description: The Impact API from Sleuth — 2 operation(s) for impact.
  name: Sleuth Impact API
  slug: sleuth-impact-api
- baseURL: https://app.sleuth.io/api/1
  baseurl_source: declared
  description: The Manual Changes API from Sleuth — 1 operation(s) for manual changes.
  name: Sleuth Manual Changes API
  slug: sleuth-manual-changes-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sleuth Deployment & Impact Registration Deployments API
  slug: open-sleuth-deployments-api
- collection_type: open
  name: Sleuth Deployment & Registration Deployments Impact API
  slug: open-sleuth-impact-api
- collection_type: open
  name: Sleuth Deployment & Impact Registration Deployments Manual Changes API
  slug: open-sleuth-manual-changes-api
- collection_type: open
  name: Sleuth Deployment & Impact Registration API
  slug: open-sleuth
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sleuth-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sleuth-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sleuth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sleuth-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sleuth-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sleuth-io
- group: company
  title: ''
  type: Website
  url: https://www.sleuth.io
- group: docs
  title: ''
  type: Documentation
  url: https://help.sleuth.io/sleuth-dora/sleuth-api
- group: commercial
  title: ''
  type: Plans
  url: plans/sleuth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sleuth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sleuth-finops.yml
created: '2026-06-21'
description: Sleuth is a deployment-based DORA metrics platform that tracks software delivery performance. Teams register deployments, manual changes, and custom impact values through Sleuth's REST registration API and GraphQL surface, then Sleuth computes the four DORA metrics (deploy frequency, lead time, change failure rate, and mean time to recovery) across projects and environments.
finops:
- name: Sleuth Finops
  service_category: Developer Tools and Observability
  slug: sleuth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sleuth.png
layout: provider
modified: '2026-06-21'
name: Sleuth
nav: Providers
network: true
overview: 'Sleuth publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deployments API, Impact API, and Manual Changes API. Tagged areas include DORA, DevOps, Deployment Tracking, Engineering Metrics, and Continuous Delivery.


  Sleuth''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Sleuth Plans Pricing
  plan_count: 3
  slug: sleuth-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Sleuth Rate Limits
  slug: sleuth-rate-limits
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 58.5
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sleuth/refs/heads/main/screenshots/sleuth-2026-09-02T155838.png
security:
- kind: authentication
  name: Sleuth Authentication
  slug: sleuth-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sleuth Domain Security
  slug: sleuth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sleuth Trust Center
  slug: sleuth-trust-center
  summary_line: SOC 2
slug: sleuth
tags:
- DORA
- DevOps
- Deployment Tracking
- Engineering Metrics
- Continuous Delivery
website: https://www.sleuth.io
---
