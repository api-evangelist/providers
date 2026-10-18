---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Batch screening operations of the SanctionsKit API — list batches with progress, accept up to 100 inline requests or an authorized private upload, read batch and row outcomes, cancel pending rows, aut
  name: SanctionsKit Batches and files API
  slug: sanctionskit-batches-and-files-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Counterparty operations of the SanctionsKit API — list persistent customer and vendor records, read a counterparty with its linked screening, case and monitor history, and page through that history in
  name: SanctionsKit Counterparties API
  slug: sanctionskit-counterparties-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Ongoing monitoring operations of the SanctionsKit API — create, read, update and stop monitored subjects, read monitor health and estimated period capacity, pause, resume or change cadence, and read t
  name: SanctionsKit Monitoring API
  slug: sanctionskit-monitoring-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Reporting operations of the SanctionsKit API — backlog and period screening and reviewer activity, a bounded screening CSV, case audit packets in JSON or PDF, case archive export, and case retention g
  name: SanctionsKit Reports API
  slug: sanctionskit-reports-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Analyst review operations of the SanctionsKit API — list and open review cases on retained screenings, read cases with append-only decisions, read investigations with match decisions, notes and attach
  name: SanctionsKit Review evidence API
  slug: sanctionskit-review-evidence-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Screening operations of the SanctionsKit API — screen one subject against explicitly selected source coverage, list and retrieve retained results, and download retained JSON evidence. A potential matc
  name: SanctionsKit Screening and evidence API
  slug: sanctionskit-screening-and-evidence-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Screening policy operations of the SanctionsKit API — read current approved screening policy versions and the current version of one policy.
  name: SanctionsKit Screening policies API
  slug: sanctionskit-screening-policies-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Source discovery operation of the SanctionsKit API — discover source capabilities, qualification and availability before selecting screening coverage.
  name: SanctionsKit Source discovery API
  slug: sanctionskit-source-discovery-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Usage operation of the SanctionsKit API — read the period allowance, used subjects and pending reservations. Each completed subject consumes one allowance unit; failed rows and idempotent retries do n
  name: SanctionsKit Usage API
  slug: sanctionskit-usage-api
- baseURL: https://www.sanctionskit.com/api/v1
  baseurl_source: declared
  description: Webhook endpoint operations of the SanctionsKit API — read endpoints and recent delivery history, register a public HTTPS endpoint and receive its signing secret once, disable an endpoint, and retry a
  name: SanctionsKit Webhooks API
  slug: sanctionskit-webhooks-api
artifact_total: 16
asyncapis:
- description: ''
  name: Sanctionskit Webhooks
  slug: sanctionskit-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/rate-limits/sanctionskit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sanctionskit-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/plans/sanctionskit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sanctionskit-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/asyncapi/sanctionskit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sanctionskit-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/conventions/sanctionskit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sanctionskit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/conventions/sanctionskit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sanctionskit-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/authentication/sanctionskit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sanctionskit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/conformance/sanctionskit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sanctionskit-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/llms/sanctionskit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sanctionskit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/well-known/sanctionskit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sanctionskit-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/hosts/sanctionskit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sanctionskit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/vendors/sanctionskit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sanctionskit-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/packages/sanctionskit-packages.yml
  title: ''
  type: SDKs
  url: packages/sanctionskit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/packages/sanctionskit-packages.yml
  title: ''
  type: Packages
  url: packages/sanctionskit-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sanctionskit.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sanctionskit.com/product/for/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/security/sanctionskit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sanctionskit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sanctionskit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sanctionskit.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.sanctionskit.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sanctionskit.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.sanctionskit.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sanctionskit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.sanctionskit.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sanctionskit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sanctionskit.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sanctionskit.com/status
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/58547371-68c65997-3558-40b8-ad72-e2eb06706cb5?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D58547371-68c65997-3558-40b8-ad72-e2eb06706cb5%26entityType%3Dcollection
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SanctionsKit
- group: docs
  title: ''
  type: OpenAPI
  url: https://www.sanctionskit.com/openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/mcp/sanctionskit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sanctionskit-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://www.sanctionskit.com/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://www.sanctionskit.com/resources/mcp
- group: auth
  title: ''
  type: OAuthProtectedResource
  url: https://www.sanctionskit.com/.well-known/oauth-protected-resource/mcp
created: '2026-10-02'
description: SanctionsKit provides a comprehensive sanctions screening API and compliance dashboard that enables businesses to screen individuals and organizations against global restricted‑party lists, manage investigations, and maintain audit trails. The platform offers batch and real‑time screening, case management, and ongoing monitoring with a free sandbox key for developers to test integrations. It serves financial services, fintech, trade, logistics, and marketplace sectors, delivering detailed source evidence and customizable alerts.
image: https://www.sanctionskit.com/og/v1/home
layout: provider
mcp_servers:
- description: SanctionsKit operates one first-party remote developer MCP server at https://www.sanctionskit.com/mcp over Streamable HTTP. Anonymous initialize (serverInfo sanctionskit 1.0.0, protocol 2025-06-18, ca
  name: SanctionsKit MCP Server
  slug: sanctionskit
modified: '2026-10-05'
name: SanctionsKit
nav: Providers
network: true
overview: 'SanctionsKit publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batches and files API, Counterparties API, Monitoring API, and 7 more. Tagged areas include Company, Sanctions, Compliance, Screening, and Fintech.


  The SanctionsKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SanctionsKit''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Sanctionskit Plans Pricing
  plan_count: 3
  slug: sanctionskit-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Sanctionskit Rate Limits
  slug: sanctionskit-rate-limits
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.7
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 59.7
    developer_ergonomics: 66.7
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 55.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/screenshots/sanctionskit-2026-10-11T125521.png
security:
- kind: authentication
  name: Sanctionskit Authentication
  slug: sanctionskit-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sanctionskit Domain Security
  slug: sanctionskit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sanctionskit
tags:
- Company
- Sanctions
- Compliance
- Screening
- Fintech
website: https://www.sanctionskit.com/
---
