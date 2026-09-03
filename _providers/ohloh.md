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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The REST API for Black Duck Open Hub (formerly Ohloh). Returns XML wrapped in a <response> root element that always carries a <status> (success/failed) and an <error> on failure. Requests append .xml '
  name: Open Hub API (Ohloh)
  slug: open-hub-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ohloh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openhub.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/blackducksoftware/ohloh_api
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/blackducksoftware/ohloh_api
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/blackducksoftware/ohloh_api/tree/master/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/blackducksoftware/ohloh_api/blob/master/README.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackducksoftware
- group: start
  title: ''
  type: SignUp
  url: https://www.openhub.net/accounts/me/api_keys/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.blackduck.com/s/article/Black-Duck-Open-Hub-API-Use-Agreement
- group: auth
  title: ''
  type: Authentication
  url: authentication/ohloh-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ohloh-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ohloh-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ohloh-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ohloh-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ohloh-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ohloh-llms.txt
created: '2026-07-17'
description: Ohloh is the open source directory and analytics service that was rebranded as Black Duck Open Hub (openhub.net) after Black Duck Software acquired it. It tracks hundreds of thousands of open source projects, their code, contributors, languages, licenses and activity, and exposes this data through a public REST API. The Open Hub / Ohloh API returns XML, authenticates with an api_key HTTP parameter (plus OAuth 2.0 for write access and private account data), is rate limited to 1,000 requests per key per day, and covers resources such as projects, accounts, organizations, analyses, languages, stacks, factoids and contributor facts. This profile was added to the API Evangelist network as a stub and enriched from the provider's public documentation.
image: https://avatars.githubusercontent.com/blackducksoftware
layout: provider
modified: '2026-07-20'
name: Ohloh
nav: Providers
network: true
overview: 'Ohloh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open-Source, Open Source Directory, Code Analytics, and Software Composition.


  Ohloh''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 11 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 1
  name: Ohloh Rate Limits
  slug: ohloh-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 26.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ohloh/refs/heads/main/screenshots/ohloh-2026-08-07T190035.png
security:
- kind: authentication
  name: Ohloh Authentication
  slug: ohloh-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ohloh Domain Security
  slug: ohloh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ohloh
tags:
- Company
- Open-Source
- Open Source Directory
- Code Analytics
- Software Composition
- Developer Data
- Project
- Contributors
- Black Duck
website: https://www.openhub.net
---
