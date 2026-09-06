---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: 3Shake Agentic Access
  operation_count: 15
  slug: 3shake-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 1
apis:
- baseURL: https://cdp-server.reckoner-api.com/api/external/v1
  baseurl_source: declared
  description: Public REST API for Reckoner, 3-shake's no-code ETL / data-integration SaaS. Fifteen operations across five tag groups let an external system run a workflow with parameter overrides, poll or cancel th
  name: Reckoner External API
  slug: reckoner-external-api
- description: 'Public API for Securify Scan, 3-shake''s automated vulnerability-diagnosis and ASM platform. A tenant creates a public API token in the console and calls the API to start a diagnosis, typically from a '
  name: Securify Scan Public API
  slug: securify-scan-public-api
artifact_total: 8
asyncapis:
- description: ''
  name: 3Shake Reckoner Webhooks
  slug: 3shake-reckoner-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/3shake-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://3-shake.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.reckoner-api.com/reckoner-external-api.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.reckoner-api.com/hc/ja
- group: docs
  title: ''
  type: APIReference
  url: https://developers.reckoner-api.com/reckoner-external-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.reckoner-api.com/hc/ja/articles/55143086798617
- group: operate
  title: ''
  type: Support
  url: https://reckoner.io/contact
- group: company
  title: ''
  type: Blog
  url: https://reckoner.io/rec_blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/3-shake
- group: commercial
  title: ''
  type: Pricing
  url: https://reckoner.io/price
- group: start
  title: ''
  type: SignUp
  url: https://reckoner.io/free-trial
- group: start
  title: ''
  type: Login
  url: https://cdp-console.reckoner-api.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reckoner.io/term
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3-shake.com/privacypolicy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://reckoner.io/news/feature-update/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/3shake-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://3-shake.com/isms/
- group: build
  title: ''
  type: Packages
  url: packages/3shake-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/3shake-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/3shake-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/3shake-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/3shake-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/3shake-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/3shake-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/3shake-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/3shake-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/3shake-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/3shake-reckoner-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3shake-securify-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3shake-sreake-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3shake-domain-security.yml
created: '2026-09-05'
description: 3-shake, Inc. (株式会社スリーシェイク) is a Tokyo-based cloud and reliability engineering company, founded in 2015, that operates four product lines. Sreake is its SRE / platform-engineering consulting and managed-operations practice for AWS, Google Cloud and Kubernetes. Reckoner is a no-code ETL and data-integration SaaS with 100+ SaaS, DWH and database connectors, a scheduling and workflow engine, and a public Reckoner External API (OpenAPI 3.0.3) for running workflows, reading job results, managing connections, projects and accounts from outside the console. Securify is a Japanese ASM and automated vulnerability-diagnosis platform covering web-application, SaaS, cloud-posture (CSPM), WordPress and SBOM scanning, with a public API for triggering diagnostics from a CI/CD pipeline and an API-diagnosis mode that scans a REST API from an uploaded OpenAPI definition. Relance is a freelance-engineer talent referral service. The company holds ISMS certification against ISO/IEC 27001:2013 and
  JIS Q 27001:2014 (registration IS 752246).
image: https://3-shake.com/wp-content/uploads/2020/01/20200124_OGP.jpg
layout: provider
modified: '2026-09-05'
name: 3-shake
nav: Providers
network: true
overview: '3-shake publishes 1 API on the [APIs.io](https://apis.io/) network: Reckoner External API. Tagged areas include Company, SRE, Data Integration, ETL, and iPaaS.


  The 3-shake catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  3-shake''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: 3Shake Plans Pricing
  plan_count: 4
  slug: 3shake-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: 3Shake Rate Limits
  slug: 3shake-rate-limits
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 63.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 3Shake Authentication
  slug: 3shake-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: 3Shake Domain Security
  slug: 3shake-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 3shake
tags:
- Company
- SRE
- Data Integration
- ETL
- iPaaS
- Workflow Automation
- Vulnerability Scanning
- Attack Surface Management
- Cloud Security
- DevSecOps
- SBOM
- Kubernetes
- Japan
website: https://3-shake.com/
---
