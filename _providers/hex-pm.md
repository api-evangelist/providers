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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 3
  name: Hex Pm Agentic Access
  operation_count: 45
  slug: hex-pm-agentic-access
  summary_line: 45 operations · 23 acting · 3 human-in-the-loop
api_count: 12
apis:
- description: API key creation and management.
  name: Hex.pm API Keys API
  slug: hex-pm-api-keys-api
- description: Authentication verification.
  name: Hex.pm Authentication API
  slug: hex-pm-authentication-api
- description: HexDocs package documentation.
  name: Hex.pm Documentation API
  slug: hex-pm-documentation-api
- description: API index and discovery.
  name: Hex.pm Index API
  slug: hex-pm-index-api
- description: OAuth2 Device Authorization Grant flow.
  name: Hex.pm OAuth API
  slug: hex-pm-oauth-api
- description: Organization and member management.
  name: Hex.pm Organizations API
  slug: hex-pm-organizations-api
- description: Package ownership management.
  name: Hex.pm Package Owners API
  slug: hex-pm-package-owners-api
- description: Package search and metadata.
  name: Hex.pm Packages API
  slug: hex-pm-packages-api
- description: Package release publishing and management.
  name: Hex.pm Releases API
  slug: hex-pm-releases-api
- description: Hex repository management.
  name: Hex.pm Repositories API
  slug: hex-pm-repositories-api
- description: User account management.
  name: Hex.pm Users API
  slug: hex-pm-users-api
- description: Utility endpoints.
  name: Hex.pm Utilities API
  slug: hex-pm-utilities-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hex-pm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hex-pm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hex-pm-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hexpm
- group: commercial
  title: ''
  type: Pricing
  url: https://hex.pm/pricing
- group: operate
  title: ''
  type: Status
  url: https://status.hex.pm
- group: company
  title: ''
  type: Blog
  url: https://hex.pm/blog
- group: company
  title: ''
  type: About
  url: https://hex.pm/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hex.pm/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hex.pm/policies/privacy
- group: build
  title: ''
  type: CodeOfConduct
  url: https://hex.pm/policies/codeofconduct
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://osv.dev/list?ecosystem=Hex
- group: start
  title: ''
  type: Login
  url: https://hex.pm/login
- group: start
  title: ''
  type: Register
  url: https://hex.pm/signup
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/hexpm/hexpm
- group: operate
  title: ''
  type: Contact
  url: mailto:support@hex.pm
created: '2026-06-13'
description: Package registry for the Erlang and Elixir ecosystems with a REST API for searching packages, accessing metadata, managing releases, user authentication, and organization management. Supports public and private packages with HexDocs integration.
examples:
- key_count: 4
  name: Create Api Key
  slug: create-api-key
- key_count: 4
  name: Get Package
  slug: get-package
- key_count: 4
  name: Search Packages
  slug: search-packages
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hex-pm.png
json_schemas:
- name: Hex.pm API Key
  property_count: 7
  slug: api-key
- name: Hex.pm Package
  property_count: 10
  slug: package
- name: Hex.pm Release
  property_count: 13
  slug: release
layout: provider
modified: '2026-06-13'
name: Hex.pm
nav: Providers
network: true
overview: 'Hex.pm publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Authentication API, Documentation API, and 9 more. Tagged areas include Package Registry, Erlang, Elixir, Gleam, and BEAM.


  The Hex.pm catalog on APIs.io includes 1 Spectral governance ruleset.


  Hex.pm''s developer surface includes authentication, pricing, status page, engineering blog, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 38
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Hex.pm API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hex-pm-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.3
  delta: -4.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 59.0
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hex-pm/refs/heads/main/screenshots/hex-pm-2026-06-20T182659.png
security:
- kind: authentication
  name: Hex Pm Authentication
  slug: hex-pm-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Hex Pm Domain Security
  slug: hex-pm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hex-pm
tags:
- Package Registry
- Erlang
- Elixir
- Gleam
- BEAM
- Open Source
- Package Manager
---
