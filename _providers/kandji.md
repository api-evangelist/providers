---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 53
  human_in_the_loop: 10
  name: Kandji Agentic Access
  operation_count: 122
  slug: kandji-agentic-access
  summary_line: 122 operations · 53 acting · 10 human-in-the-loop
api_count: 2
apis:
- description: 'Hosted, tenant-scoped Model Context Protocol server that exposes the Iru Enterprise API surface as MCP tools for Claude Desktop, Cursor, OpenAI Codex and other MCP clients. Enabled per API token with '
  name: Iru MCP Server
  slug: iru-mcp-server
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Audit API from Iru — 1 operation(s) for audit.
  name: Iru Audit API
  slug: kandji-audit-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Behavioral Detections API from Iru — 1 operation(s) for behavioral detections.
  name: Iru Behavioral Detections API
  slug: kandji-behavioral-detections-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Blueprints API from Iru — 6 operation(s) for blueprints.
  name: Iru Blueprints API
  slug: kandji-blueprints-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Devices API from Iru — 34 operation(s) for devices.
  name: Iru Devices API
  slug: kandji-devices-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Integrations API from Iru — 8 operation(s) for integrations.
  name: Iru Integrations API
  slug: kandji-integrations-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Library API from Iru — 13 operation(s) for library.
  name: Iru Library API
  slug: kandji-library-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Prism API from Iru — 19 operation(s) for prism.
  name: Iru Prism API
  slug: kandji-prism-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Self Service API from Iru — 1 operation(s) for self service.
  name: Iru Self Service API
  slug: kandji-self-service-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Settings API from Iru — 1 operation(s) for settings.
  name: Iru Settings API
  slug: kandji-settings-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Tags API from Iru — 2 operation(s) for tags.
  name: Iru Tags API
  slug: kandji-tags-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Threat Details API from Iru — 1 operation(s) for threat details.
  name: Iru Threat Details API
  slug: kandji-threat-details-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Upload To S3 API from Iru — 1 operation(s) for upload to s3.
  name: Iru Upload To S3 API
  slug: kandji-upload-to-s3-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Users API from Iru — 2 operation(s) for users.
  name: Iru Users API
  slug: kandji-users-api
- baseURL: https://your-subdomain.api.kandji.io
  baseurl_source: declared
  description: The Vulnerability Management API from Iru — 5 operation(s) for vulnerability management.
  name: Iru Vulnerability Management API
  slug: kandji-vulnerability-management-api
- description: 'REST/JSON API for the Iru (formerly Kandji) endpoint management platform: read fleet data and run device actions, manage apps, Library items, Library uploads, Blueprints, tenant activity, and Automate'
  name: Iru Endpoint Management API
  slug: iru-endpoint-management-api
artifact_total: 35
collections:
- collection_type: open
  name: Iru Endpoint Management API
  slug: open-kandji-endpoint-management
- collection_type: open
  name: Upload to S3
  slug: open-kandji-upload-to-s3
common:
- group: commercial
  href: https://artifacts.apis.io/kandji/plans/kandji-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kandji-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.iru.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/kandji/capabilities/kandji-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kandji-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kandji/agentic-access/kandji-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kandji-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kandji/security/kandji-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kandji-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kandji/security/kandji-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kandji-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iru.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iru.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iru.com/en/endpoint/api/iru-api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.kandji.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iru.com/en/endpoint/getting-started/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.kandji.io/
- group: company
  title: ''
  type: Blog
  url: https://www.iru.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kandji-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iru.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.iru.com/request-demo
- group: start
  title: ''
  type: Login
  url: https://www.iru.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iru.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iru.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://api-docs.kandji.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kandji.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.iru.com/updates/
- group: operate
  title: ''
  type: ChangeLogRSS
  url: https://updates.iru.com/feed-en
- group: operate
  href: https://artifacts.apis.io/kandji/changelog/kandji-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kandji-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.iru.com/security/responsible-disclosure-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.iru.com/security
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/kandji_stock/
- group: docs
  href: https://artifacts.apis.io/kandji/openapi/_original/kandji-endpoint-management-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/kandji-endpoint-management-openapi.json
- group: agent
  href: https://artifacts.apis.io/kandji/mcp/kandji-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kandji-mcp.yml
- group: build
  href: https://artifacts.apis.io/kandji/mcp/kandji-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kandji-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/kandji/packages/kandji-packages.yml
  title: ''
  type: Packages
  url: packages/kandji-packages.yml
- group: build
  href: https://artifacts.apis.io/kandji/cli/kandji-cli.yml
  title: ''
  type: CLI
  url: cli/kandji-cli.yml
- group: agent
  href: https://artifacts.apis.io/kandji/llms/kandji-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kandji-llms.txt
- group: agent
  href: https://artifacts.apis.io/kandji/well-known/kandji-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kandji-well-known.yml
- group: auth
  href: https://artifacts.apis.io/kandji/authentication/kandji-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kandji-authentication.yml
- group: design
  href: https://artifacts.apis.io/kandji/conventions/kandji-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kandji-conventions.yml
- group: operate
  href: https://artifacts.apis.io/kandji/rate-limits/kandji-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kandji-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/kandji/errors/kandji-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kandji-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kandji/data-model/kandji-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kandji-data-model.yml
- group: design
  href: https://artifacts.apis.io/kandji/lifecycle/kandji-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kandji-lifecycle.yml
- group: operate
  title: ''
  type: ReleaseStages
  url: https://docs.iru.com/en/iru/platform-overview/iru-release-stages
- group: design
  href: https://artifacts.apis.io/kandji/conformance/kandji-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kandji-conformance.yml
- group: auth
  href: https://artifacts.apis.io/kandji/security/kandji-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kandji-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/kandji/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/kandji/overlays/kandji-endpoint-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kandji-endpoint-management-overlay.yaml
created: '2026-08-01'
description: Iru (formerly Kandji) is a San Francisco based endpoint management and security company whose AI-powered platform unifies workforce identity and access, cross-platform endpoint management for macOS, iOS, iPadOS, tvOS, visionOS, Windows and Android, endpoint detection and response, vulnerability management, compliance automation and a customer-facing trust center behind a single agent. The company rebranded from Kandji to Iru on 22 October 2025; the product surface, the developer documentation and the API hostnames still carry the kandji.io domain. The Iru Endpoint Management API is a tenant-scoped REST API published as OpenAPI 3.0.0 and as a public Postman collection, covering devices and device actions, Blueprints, Library Items, Prism inventory reporting, Automated Device Enrollment, tags, users, threats and vulnerabilities, and it also backs a hosted, tenant-scoped Model Context Protocol server for AI assistants.
finops:
- has_sources: true
  method: derived
  name: Kandji Finops
  primary_unit: ''
  service_category: ''
  slug: kandji-finops
  template: true
image: https://www.iru.com/hubfs/assets/favicons/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at YOUR_TENANT.connect.iru.com over HTTP.
  name: Iru MCP Server
  slug: iru
modified: '2026-10-06'
name: Iru
nav: Providers
network: true
overview: 'Iru publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, Behavioral Detections API, Blueprints API, and 13 more. Tagged areas include Company, Device Management, Mobile Device Management, apple-management, and Endpoint Security.


  Iru''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 38 more developer resources.'
plans:
- name: Kandji Plans Pricing
  plan_count: 1
  slug: kandji-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Iru Rate Limits
  slug: iru-rate-limits
- limit_count: 1
  name: Kandji Rate Limits
  slug: kandji-rate-limits
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.2
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 48.4
    developer_ergonomics: 70.8
    discoverability: 65.0
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 59.0
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 92.9
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kandji/kandji-2026-08-07T171059.png
security:
- kind: authentication
  name: Iru Authentication
  slug: iru-authentication
  summary_line: http · 1 scheme
- kind: authentication
  name: Kandji Authentication
  slug: kandji-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Kandji Domain Security
  slug: kandji-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kandji Vulnerability Disclosure
  slug: kandji-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Kandji Trust Center
  slug: kandji-trust-center
  summary_line: SOC 2 Type II, ISO 27001
skill_count: 6
skills:
- name: Export fleet inventory from Prism
  slug: kandji-export-fleet-inventory
- name: Find a device and read its posture
  slug: kandji-find-a-device
- name: Publish a Custom App and assign it to a Blueprint
  slug: kandji-publish-a-custom-app
- name: Renew an Automated Device Enrollment token before it expires
  slug: kandji-renew-ade-token
- name: Run a device action safely
  slug: kandji-run-a-device-action
- name: Triage a CVE across the fleet
  slug: kandji-triage-vulnerabilities
slug: kandji
tags:
- Company
- Device Management
- Mobile Device Management
- apple-management
- Endpoint Security
- Endpoint Detection and Response
- Vulnerability Management
- Compliance Automation
- Workforce Identity
- IT Operations
- MCP
- Agent-Native
website: https://www.iru.com/
---
