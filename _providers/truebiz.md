---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Web Presence Review endpoints allow you to provide information about a business for TrueBiz to review. We look at the content on the website, find social media profiles, review sites, and other broade
  name: TrueBiz Async Web Presence Review API
  slug: truebiz-async-web-presence-review-api
- description: The Fraud Searches API from TrueBiz — 2 operation(s) for fraud searches.
  name: TrueBiz Fraud Searches API
  slug: truebiz-fraud-searches-api
- description: The History API from TrueBiz — 1 operation(s) for history.
  name: TrueBiz History API
  slug: truebiz-history-api
- description: The Industry Discovery API from TrueBiz — 2 operation(s) for industry discovery.
  name: TrueBiz Industry Discovery API
  slug: truebiz-industry-discovery-api
- description: The Industry Discovery History API from TrueBiz — 2 operation(s) for industry discovery history.
  name: TrueBiz Industry Discovery History API
  slug: truebiz-industry-discovery-history-api
- description: Monitoring alerts endpoints allow you to see what alerts TrueBiz has found during monitoring.
  name: TrueBiz Monitoring Alerts API
  slug: truebiz-monitoring-alerts-api
- description: Monitored domain endpoints allow you to see what domains TrueBiz is currently monitoring.
  name: TrueBiz Monitoring Domains API
  slug: truebiz-monitoring-domains-api
- description: Web Presence Review endpoints allow you to provide information about a business for TrueBiz to review. We look at the content on the website, find social media profiles, review sites, and other broade
  name: TrueBiz Web Presence Review API
  slug: truebiz-web-presence-review-api
- description: Web Presence Review endpoints allow you to provide an input like a domain, url, or email associated with a website for TrueBiz to review. For business or compliance reasons, you may want to directly b
  name: TrueBiz Web Presence Review Blocklist API
  slug: truebiz-web-presence-review-blocklist-api
- description: Web Presence Review results are stored with TrueBiz until you request their deletion. These endpoints are designed to allow you to access these historical results.
  name: TrueBiz Web Presence Review History API
  slug: truebiz-web-presence-review-history-api
- description: Our website status endpoints help with checking to see if a provided URL is up and that it is not part of a website grouping that TrueBiz does not support.
  name: TrueBiz Website Status API
  slug: truebiz-website-status-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TrueBiz Web Presence Review Async Web Presence Review Fraud Searches API
  slug: open-truebiz-fraud-searches-api
- collection_type: open
  name: TrueBiz Web Presence Review Async Web Presence Review History API
  slug: open-truebiz-history-api
- collection_type: open
  name: TrueBiz Web Presence Review Async Web Presence Review Industry Discovery API
  slug: open-truebiz-industry-discovery-api
- collection_type: open
  name: TrueBiz Web Presence Review Async Web Presence Review Industry Discovery History API
  slug: open-truebiz-industry-discovery-history-api
- collection_type: open
  name: TrueBiz Web Presence Review Async Web Presence Review Monitoring Alerts API
  slug: open-truebiz-monitoring-alerts-api
- collection_type: open
  name: TrueBiz Web Presence Review Async Web Presence Review Monitoring Domains API
  slug: open-truebiz-monitoring-domains-api
- collection_type: open
  name: TrueBiz Web Presence Review Async Web Presence Review Website Status API
  slug: open-truebiz-website-status-api
common:
- group: start
  title: ''
  type: Portal
  url: https://ae.truebiz.io/api/v1/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truebiz.io
- group: docs
  title: ''
  type: APIReference
  url: https://ae.truebiz.io/api/v1/docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/truebiz-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truebiz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truebiz-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truebiz-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truebiz-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/truebiz-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truebiz-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/truebiz-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/truebiz-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truebiz-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://truebiz.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truebiz
- group: operate
  title: ''
  type: Support
  url: https://truebiz.io/contact-us
- group: start
  title: ''
  type: Login
  url: https://app.truebiz.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://truebiz.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://truebiz.io/privacy
- group: company
  title: ''
  type: Website
  url: https://truebiz.io
created: '2026-07-17'
description: TrueBiz automates merchant risk assessment by analyzing a business's internet footprint. Its Web Presence Review API scores a merchant's legitimacy and risk from a domain plus submitted business details, returning a rich Company profile with fraud-risk analysis, website content flags, customer reviews, connected people and entities, and domain/hosting intelligence. A Monitoring API watches domains continuously and raises alerts, and Blocklist, Industry Discovery, and Fraud Search endpoints round out the platform. Payments providers and financial institutions use TrueBiz to streamline underwriting and ongoing merchant due diligence. The REST API authenticates with an X-API-KEY header and is documented with an OpenAPI 3.0.2 specification.
image: https://truebiz.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: TrueBiz MCP Server
  slug: truebiz-mcp-server
modified: '2026-07-21'
name: TrueBiz
nav: Providers
network: true
overview: 'TrueBiz publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Async Web Presence Review API, Fraud Searches API, History API, and 8 more. Tagged areas include Company, Security, Fraud Prevention, Business Verification, and Merchant Risk.


  TrueBiz''s developer surface includes developer portal, documentation, API reference, authentication, engineering blog, support, and 15 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 53.2
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 35.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Truebiz Authentication
  slug: truebiz-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Truebiz Domain Security
  slug: truebiz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: truebiz
tags:
- Company
- Security
- Fraud Prevention
- Business Verification
- Merchant Risk
- KYB
- Underwriting
- Payments
- Monitoring
website: https://truebiz.io
---
