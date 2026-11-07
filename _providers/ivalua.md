---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote Model Context Protocol endpoint on Ivalua's portal host, advertised by an OAuth 2.0 Protected Resource Metadata document; requires OAuth 2.0 authorization against portal.ivalua.com/oauth2 and r
  name: Ivalua MCP Server
  slug: ivalua-mcp-server
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/ivalua/json-ld/ivalua-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ivalua-context.jsonld
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ivalua.com/
- group: auth
  href: https://artifacts.apis.io/ivalua/security/ivalua-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ivalua-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ivalua/security/ivalua-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ivalua-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ivalua/authentication/ivalua-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ivalua-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ivalua/scopes/ivalua-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ivalua-scopes.yml
- group: agent
  href: https://artifacts.apis.io/ivalua/llms/ivalua-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ivalua-llms.txt
- group: auth
  href: https://artifacts.apis.io/ivalua/well-known/ivalua-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ivalua-security.txt
- group: auth
  href: https://artifacts.apis.io/ivalua/well-known/ivalua-it-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ivalua-it-security.txt
- group: auth
  href: https://artifacts.apis.io/ivalua/well-known/ivalua-fr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ivalua-fr-security.txt
- group: auth
  href: https://artifacts.apis.io/ivalua/well-known/ivalua-es-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ivalua-es-security.txt
- group: auth
  href: https://artifacts.apis.io/ivalua/well-known/ivalua-de-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ivalua-de-security.txt
- group: agent
  href: https://artifacts.apis.io/ivalua/well-known/ivalua-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ivalua-well-known.yml
- group: other
  href: https://artifacts.apis.io/ivalua/hosts/ivalua-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ivalua-hosts.yml
- group: build
  href: https://artifacts.apis.io/ivalua/integrations/ivalua-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/ivalua-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/ivalua/vendors/ivalua-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ivalua-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.ivalua.com/company/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.ivalua.com/company/leadership/
- group: auth
  href: https://artifacts.apis.io/ivalua/security/ivalua-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ivalua-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ivalua/security/ivalua-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ivalua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ivalua.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ivalua.com/technology/ivalua-open-ecosystem/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Ivalua
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ivalua
- group: company
  title: ''
  type: Blog
  url: https://www.ivalua.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.saasworthy.com/product/ivalua-procurement-solution/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/ivalua
- group: commercial
  href: https://artifacts.apis.io/ivalua/plans/ivalua-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ivalua-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.ivalua.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ivalua.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ivalua.com/legal/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ivalua.com/
- group: operate
  href: https://artifacts.apis.io/ivalua/rate-limits/ivalua-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ivalua-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ivalua/finops/ivalua-finops.yml
  title: ''
  type: FinOps
  url: finops/ivalua-finops.yml
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.ivalua.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-06-13'
description: Ivalua is an enterprise AI-powered procurement platform offering a unified source-to-pay solution that enables organizations to manage all categories of spend and suppliers. The platform exposes a REST API built on open standards, supporting JSON and XML data formats via secure web services, enabling programmatic integration for supplier onboarding, contract lifecycle management, sourcing events, purchase orders, invoice automation, and spend analytics. Ivalua's Enterprise Application Interface (EAI) module combines APIs, ETL, and query tools to orchestrate data transfer between Ivalua and external enterprise systems including SAP, Oracle, and Microsoft Dynamics. The Integration Hub supports 60+ ERP and enterprise system connectors, providing developer tooling to build and discover APIs without requiring middleware. Authentication leverages SAML-based SSO and two-factor authentication, with raw interface request/response logging available through the Integration Console for
  audit and debugging purposes.
finops:
- has_sources: false
  method: generated
  name: Ivalua Finops
  primary_unit: ''
  service_category: ''
  slug: ivalua-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ivalua.png
jsonld:
- class_count: 17
  name: Ivalua Context
  property_count: 5
  slug: ivalua-context
layout: provider
mcp_servers:
- description: Ivalua's portal host publishes an OAuth 2.0 Protected Resource Metadata document (RFC 9728) naming https://portal.ivalua.com/mcp as the protected resource, with https://portal.ivalua.com/oauth2 as its
  name: Ivalua MCP Server (portal.ivalua.com)
  slug: ivalua-mcp-server-portal-ivalua-com
modified: '2026-10-20'
name: Ivalua
nav: Providers
network: true
overview: 'Ivalua is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, Source-to-Pay, Supplier Management, Contract Management, and Sourcing.


  The Ivalua catalog on APIs.io includes 1 JSON-LD context.


  Ivalua''s developer surface includes authentication, documentation, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Ivalua Plans Pricing
  plan_count: 1
  slug: ivalua-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Ivalua Rate Limits
  slug: ivalua-rate-limits
scopes:
- name: Ivalua Scopes
  scope_count: 1
  slug: ivalua-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 28.6
    discoverability: 76.7
    operational_transparency: 23.7
  previous_composite: 35.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ivalua/ivalua-2026-06-20T183638.png
security:
- kind: authentication
  name: Ivalua Authentication
  slug: ivalua-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ivalua Domain Security
  slug: ivalua-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ivalua Vulnerability Disclosure
  slug: ivalua-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ivalua Trust Center
  slug: ivalua-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type II, SOC 1 Type II, HIPAA, CSA STAR, TISAX, SCF - EU GDPR, Ivalua ACSC IRAP ISM
slug: ivalua
tags:
- Procurement
- Source-to-Pay
- Supplier Management
- Contract Management
- Sourcing
- Purchase Orders
- Invoices
- Spend Analytics
- ERP Integration
- Enterprise
website: https://www.ivalua.com/
---
