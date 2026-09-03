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
  - rate-limits
  - security
  trial: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://api.silentpush.com/api/v1/merge-api/
  baseurl_source: declared
  description: Unified REST gateway for Silent Push threat intelligence. Sections cover Enrich (single and bulk domain, IPv4 and IPv6 enrichment plus IP diversity), Export (CSV, JSON, TXT, RPZ, STIX), Feeds, Feed In
  name: Silent Push API
  slug: silent-push-api
- description: SaaS-hosted Model Context Protocol server announced in Release 6.0 (2026-06-12, beta). Exposes 33 read-only investigation tools across enrichment, PADNS, reputation, live scanning and SPQL fingerprint
  name: Silent Push MCP Server
  slug: silent-push-mcp-server
artifact_total: 10
collections:
- collection_type: postman
  name: Silent Push Web Scanner Quick Help Requests
  slug: postman-silent-push-web-scanner
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silent-push-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silentpush.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.silentpush.com/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.silentpush.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://help.silentpush.com/apidocs/perform-a-live-scan
- group: start
  title: ''
  type: GettingStarted
  url: https://help.silentpush.com/docs/get-started-with-api
- group: operate
  title: ''
  type: Support
  url: https://www.silentpush.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.silentpush.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Silent-Push
- group: start
  title: ''
  type: SignUp
  url: https://explore.silentpush.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.silentpush.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silentpush.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: postman/silent-push-web-scanner.postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silent-push-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/silent-push-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/silent-push-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/silent-push-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/silent-push-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/silent-push-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/silent-push-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/silent-push-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silent-push-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/silent-push-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/silent-push-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/silent-push-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/silent-push-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/silent-push-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/silent-push-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/silent-push-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/silent-push-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.silentpush.com/responsible-disclosure/
created: '2026-08-27'
description: Silent Push is a preemptive cyber defense company that maps adversary infrastructure before it is weaponized, using a continuously scanned view of the global DNS, web content, certificate and WHOIS landscape. Its platform turns that data into Indicators of Future Attack (IOFA), risk scores for domains and IP addresses, and threat intelligence feeds that security teams push into SIEM, SOAR and blocking infrastructure. The developer surface is a REST API gateway at api.silentpush.com covering enrichment, Passive Active DNS (PADNS), live web scanning and screenshots, SPQL search, feed and indicator CRUD, Threat Check, TLP reports and export in CSV, JSON, TXT, RPZ and STIX formats, authenticated with an x-api-key header. Silent Push also runs a hosted Model Context Protocol server that exposes 33 read-only investigation tools to MCP-compatible AI clients over OAuth 2.1.
image: https://www.silentpush.com/wp-content/uploads/Silent-Push-Logo-@2x.png
layout: provider
mcp_servers:
- description: ''
  name: Silent Push MCP Server
  slug: silent-push-mcp-server
modified: '2026-08-27'
name: Silent Push
nav: Providers
network: true
overview: 'Silent Push publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Threat Intelligence, Cybersecurity, and DNS.


  Silent Push''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 24 more developer resources.'
plans:
- name: Silent Push Plans Pricing
  plan_count: 2
  slug: silent-push-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Silent Push Rate Limits
  slug: silent-push-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 37.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silent-push/refs/heads/main/screenshots/silent-push-2026-09-02T155457.png
security:
- kind: authentication
  name: Silent Push Authentication
  slug: silent-push-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Silent Push Domain Security
  slug: silent-push-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Silent Push Vulnerability Disclosure
  slug: silent-push-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Silent Push Trust Center
  slug: silent-push-trust-center
  summary_line: trust center published
slug: silent-push
tags:
- Company
- Security
- Threat Intelligence
- Cybersecurity
- DNS
- Domain Intelligence
- Passive DNS
- Enrichment
- Threat Feeds
- WHOIS
- MCP
website: https://www.silentpush.com/
---
