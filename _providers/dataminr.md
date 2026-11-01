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
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: OAuth2-secured REST API for consuming Dataminr real-time alerts and managing watchlists/lists. Token flow at /auth/2/token; alert polling at /api/3/alerts; account and list management at /account/2/*.
  name: Dataminr Pulse API
  slug: dataminr-pulse-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/dataminr/hosts/dataminr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataminr-hosts.yml
- group: build
  href: https://artifacts.apis.io/dataminr/integrations/dataminr-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dataminr-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dataminr/vendors/dataminr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataminr-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.dataminr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dataminr.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dataminr.com
- group: company
  title: ''
  type: Blog
  url: https://www.dataminr.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.dataminr.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dataminr
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataminr.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dataminr.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dataminr.com
- group: auth
  href: https://artifacts.apis.io/dataminr/security/dataminr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dataminr-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dataminr.com/v1/dataminr-trust-services/
- group: auth
  href: https://artifacts.apis.io/dataminr/authentication/dataminr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dataminr-authentication.yml
- group: design
  href: https://artifacts.apis.io/dataminr/conventions/dataminr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dataminr-conventions.yml
- group: design
  href: https://artifacts.apis.io/dataminr/lifecycle/dataminr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dataminr-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dataminr/conformance/dataminr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataminr-conformance.yml
- group: auth
  href: https://artifacts.apis.io/dataminr/security/dataminr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataminr-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: The Dataminr Developer Portal (a Salesforce Experience Cloud site at developer.dataminr.com) states all documentation requires an API-provisioned account and 302s every docs page such as /s/get-started to /s/login; no public OpenAPI, llms.txt, MCP server or SDK package was found.
  evidence:
  - status: 302
    url: https://developer.dataminr.com/s/get-started
  - status: 401
    url: https://developer.dataminr.com/llms.txt
  - status: 404
    url: https://gateway.dataminr.com/openapi.json
  - status: 200
    url: https://developer.dataminr.com/s/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Dataminr delivers AI-powered real-time event, threat and risk intelligence, detecting breaking events and emerging risks across more than one million public data sources using proprietary large language models and multi-modal fusion AI. Its product lines span corporate security, cyber defense, public sector (First Alert) and newsroom situational awareness, serving government agencies and a large share of the Fortune 50. The Dataminr Pulse API exposes real-time alert consumption plus watchlist and account management over an OAuth2-secured REST gateway (gateway.dataminr.com), enabling integrations with SIEM, SOAR and security operations tooling.
image: https://www.dataminr.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Dataminr
nav: Providers
network: true
overview: 'Dataminr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Threat Intelligence, Risk Management, and Real-Time.


  Dataminr''s developer surface includes documentation, engineering blog, support, authentication, and 15 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 28.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dataminr/dataminr-2026-07-25T211346.png
security:
- kind: authentication
  name: Dataminr Authentication
  slug: dataminr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Dataminr Domain Security
  slug: dataminr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dataminr Trust Center
  slug: dataminr-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: dataminr
tags:
- Company
- Analytics
- Threat Intelligence
- Risk Management
- Real-Time
- Security
- Artificial Intelligence
- Alerting
website: https://www.dataminr.com
---
