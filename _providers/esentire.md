---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: An authorization-gated Model Context Protocol server operated by eSentire on its own API host. Every path under https://api.esentire.com/mcp/ answers 401 UNAUTHORIZED with an RFC 9728 challenge (`WWW-
  name: eSentire MCP Server
  slug: esentire-mcp
artifact_total: 9
common:
- group: docs
  title: ''
  type: Documentation
  url: https://help.okta.com/
- group: auth
  href: https://artifacts.apis.io/esentire/security/esentire-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/esentire-trust-center.yml
- group: operate
  href: https://artifacts.apis.io/esentire/lifecycle/esentire-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/esentire-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/esentire/hosts/esentire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esentire-hosts.yml
- group: build
  href: https://artifacts.apis.io/esentire/integrations/esentire-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/esentire-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/esentire/vendors/esentire-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esentire-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.esentire.com/company/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.esentire.com/company/leadership
- group: auth
  href: https://artifacts.apis.io/esentire/security/esentire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esentire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.esentire.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/esentire-stock
- group: company
  title: ''
  type: Blog
  url: https://www.esentire.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eSentire
- group: start
  title: ''
  type: SignUp
  url: https://www.esentire.com/get-started
- group: start
  title: ''
  type: Login
  url: https://atlas.esentire.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.esentire.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esentire.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.esentire.com/
- group: auth
  href: https://artifacts.apis.io/esentire/security/esentire-trust-center.yml
  title: ''
  type: Compliance
  url: security/esentire-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/esentire/security/esentire-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/esentire-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/esentire/security/esentire-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/esentire-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/esentire/llms/esentire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/esentire-llms.txt
- group: agent
  href: https://artifacts.apis.io/esentire/well-known/esentire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/esentire-well-known.yml
- group: design
  href: https://artifacts.apis.io/esentire/conventions/esentire-conventions.yml
  title: ''
  type: Conventions
  url: conventions/esentire-conventions.yml
- group: design
  href: https://artifacts.apis.io/esentire/lifecycle/esentire-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/esentire-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/esentire/plans/esentire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/esentire-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/esentire/rate-limits/esentire-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/esentire-rate-limits.yml
coverage:
  checked: '2026-10-20'
  detail: api.esentire.com fronts an Okta-issued OAuth MCP server and API that answer 403/401 anonymously, with no public OpenAPI, developer portal or reference; only the OAuth metadata and the www.esentire.com llms.txt are readable.
  evidence:
  - status: 403
    url: https://api.esentire.com/mcp
  - status: 403
    url: https://api.esentire.com/openapi.json
  - status: 200
    url: https://api.esentire.com/.well-known/oauth-protected-resource
  reason: partner-login
  state: gated
created: '2026-08-12'
description: 'eSentire, Inc. is a Waterloo, Ontario-headquartered cybersecurity company and, in its own words, "the Authority in Managed Detection and Response (MDR)". Founded in 2001, it protects 2,000+ organizations across 80+ countries and 35 industries with 24/7/365 Managed Detection and Response, Digital Forensics and Incident Response (DFIR), and Continuous Threat Exposure Management (CTEM), delivered from its own Atlas Security Operations Platform and staffed Security Operations Centers. Its public machine-readable surface is narrow but real: an llms.txt at the marketing host, an OAuth 2.0 authorization-server and protected-resource metadata pair at api.esentire.com, and an authorization-gated MCP server behind that same host. There is no public OpenAPI, GraphQL schema, or developer portal — the API and the Atlas/Insight portal are reachable only by contracted customers and partners.'
image: https://storage.googleapis.com/vendor-risk-production-default-bucket/eSentire-Navy-1000x1000.png_b7cac947-6768-4bd5-9fa7-98997a9e13f7
layout: provider
mcp_servers:
- description: eSentire operates a Model Context Protocol server on its own API host. It was found by probe, not by documentation — eSentire publishes no developer portal and no page describing this server. The evid
  name: eSentire MCP Server
  slug: esentire-mcp-server
modified: '2026-08-12'
name: eSentire
nav: Providers
network: true
overview: 'eSentire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Managed Detection and Response, and Threat Intelligence.


  eSentire''s developer surface includes documentation, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Esentire Plans Pricing
  plan_count: 0
  slug: esentire-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Esentire Rate Limits
  slug: esentire-rate-limits
scopes:
- name: Esentire Scopes
  scope_count: 3
  slug: esentire-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 76.7
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 29.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/esentire/esentire-2026-09-02T145421.png
security:
- kind: authentication
  name: Esentire Authentication
  slug: esentire-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Esentire Domain Security
  slug: esentire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Esentire Vulnerability Disclosure
  slug: esentire-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Esentire Trust Center
  slug: esentire-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27001:2013, PCI DSS 4.0.1, HIPAA, GDPR, CCPA, PIPEDA, DORA (EU Digital Operational Resilience Act), CIS Controls v8.1, Shared Assessments SIG
slug: esentire
tags:
- Company
- Security
- Cybersecurity
- Managed Detection and Response
- Threat Intelligence
- Incident Response
- MCP
- Agents
- Authentication
- Software-as-a-Service
website: https://www.esentire.com/
---
