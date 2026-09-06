---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: GraphQL API for the Brinqa Platform. Query assets, findings, hosts, tickets, and vulnerabilities using GraphQL and the Brinqa Query Language (BQL). Bearer-token authentication; the endpoint is per-ten
  name: Brinqa Platform API
  slug: brinqa-platform-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.brinqa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.brinqa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brinqa.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.brinqa.com/docs/brinqa-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brinqa.com/docs/category/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.brinqa.com/blog
- group: operate
  title: ''
  type: Support
  url: https://brinqa.atlassian.net/servicedesk/customer/portals
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brinqa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brinqa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brinqa.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/brinqa-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brinqa-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brinqa-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brinqa-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brinqa-llms.txt
created: '2026-07-17'
description: Brinqa is an AI-powered vulnerability and exposure management platform that unifies cyber risk data from across an enterprise's security tools into a single trusted data model. It ingests and correlates exposure findings from scanners and connectors, deduplicates them, and applies risk scoring, custom risk factors, and workflow automation to prioritize and drive remediation. The Brinqa Platform exposes a GraphQL API and the Brinqa Query Language (BQL) for traversing an entity-relationship graph of assets, findings, hosts, tickets, and vulnerabilities, plus reporting and dashboards on those datasets. This API Evangelist profile was seeded from an Insight Partners portfolio lead and enriched from Brinqa's public developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brinqa.png
layout: provider
modified: '2026-07-18'
name: Brinqa
nav: Providers
network: true
overview: 'Brinqa publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Vulnerability Management, Exposure Management, and Cyber Risk.


  Brinqa''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brinqa/refs/heads/main/screenshots/brinqa-2026-07-25T203912.png
security:
- kind: authentication
  name: Brinqa Authentication
  slug: brinqa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brinqa Domain Security
  slug: brinqa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: brinqa
tags:
- Company
- Cybersecurity
- Vulnerability Management
- Exposure Management
- Cyber Risk
- Risk Management
- Security
- GraphQL
website: https://www.brinqa.com/
---
