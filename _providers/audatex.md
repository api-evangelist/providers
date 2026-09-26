---
access_model:
  confidence: high
  label: Contact sales / partner approval
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://audaconnect.ax-aee.co.uk/AudaAPI.BMSAPI/home/register
  - https://audatex.co.uk/solutions/audaconnect/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-09-25'
api_count: 5
apis:
- baseURL: https://audaconnect.ax-aee.co.uk/AudaAPI.WebAPI
  baseurl_source: declared
  description: 'The AudaConnect WebAPI (Audatex UK) enables third-party software developers to access, query and update the Audatex platform: assessments (search, create shell, import/export AxFormat, PDF reports, ca'
  name: Audatex AudaConnect API
  slug: audatex-audaconnect-api
- baseURL: https://audaconnect.ax-aee.co.uk/AudaAPI.BMSAPI
  baseurl_source: declared
  description: 'Audatex services for Bodyshop Management Systems (BMS): lets a BMS get and update assessment-related data — resolve assessment IDs by originator and number, fetch and import assessment exports in AXFO'
  name: Audatex AudaConnect BMS API
  slug: audatex-audaconnect-bms-api
- baseURL: https://services-pat.auda-target.com/APIGateway
  baseurl_source: declared
  description: 'The Audatex.APIGateway exposes Solera''s guided image capture and intelligent vehicle inspection services: send image-capture requests by SMS, link or QR code, upload images, audio and video, run AI Tr'
  name: Audatex API Gateway (Intelligent Vehicle Inspection)
  slug: audatex-api-gateway
- baseURL: https://api-demo.audatex.com/TestGICapi
  baseurl_source: declared
  description: The Audatex EAPI GIC (Global Integration Component) Integration API is the North American claims-integration surface used to post GIC integration responses for a work assignment and to acknowledge M31
  name: Audatex GIC API
  slug: audatex-gic-api
- baseURL: https://api-demo.audatex.com/TestAssignmentapi
  baseurl_source: declared
  description: The Solera Dashboard Assignment API (Audatex North America) is the FNOL assignment integration surface behind the Solera claims dashboard. The publicly served OpenAPI 3.0.1 document describes only the
  name: Solera Dashboard Assignment API
  slug: audatex-dashboard-assignment-api
- description: 'The Solera Integrations Public API portal for North America lists the Audatex/Solera claims services available to integrators, including the ClaimImage document-return API, with Swagger documentation '
  name: Solera API Gateway (North America)
  slug: solera-api-gateway
artifact_total: 29
asyncapis:
- description: ''
  name: Audatex Webhooks
  slug: audatex-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://audatex.co.uk/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.solera.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/audatex-uk/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AudatexUK
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Audatexmarketing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://audaconnect.ax-aee.co.uk/AudaAPI.Portal/
- group: docs
  title: ''
  type: Documentation
  url: https://audaconnect.ax-aee.co.uk/AudaAPI.WebAPI/help
- group: docs
  title: ''
  type: APIReference
  url: https://audaconnect.ax-aee.co.uk/AudaAPI.WebAPI/help
- group: start
  title: ''
  type: GettingStarted
  url: https://audaconnect.ax-aee.co.uk/AudaAPI.BMSAPI/home/register
- group: start
  title: ''
  type: Login
  url: https://audaconnect.ax-aee.co.uk/AudaAPI.Portal/Account/Login
- group: operate
  title: ''
  type: Support
  url: https://audatex.co.uk/support/
- group: operate
  title: ''
  type: Contact
  url: https://audatex.co.uk/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://audatex.co.uk/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audatex.co.uk/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solera.com/us-canada-master-services-agreement/
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/sandbox/audatex-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/audatex-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/authentication/audatex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audatex-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/scopes/audatex-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/audatex-scopes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/well-known/audatex-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/audatex-openid-configuration.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/well-known/audatex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audatex-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/conformance/audatex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audatex-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/errors/audatex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audatex-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/lifecycle/audatex-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/audatex-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/conventions/audatex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/audatex-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/data-model/audatex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audatex-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/asyncapi/audatex-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/audatex-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/mcp/audatex-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audatex-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/llms/audatex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audatex-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/packages/audatex-packages.yml
  title: ''
  type: Packages
  url: packages/audatex-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/plans/audatex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/audatex-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/rate-limits/audatex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/audatex-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/security/audatex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audatex-domain-security.yml
created: '2025-01-01'
description: 'Audatex (a Solera company) provides automotive claims and repair solutions with data and technology services for the automotive insurance, collision repair, and fleet management industries. It publishes the AudaConnect API platform for third-party integration (Audatex UK: assessments, vehicle reference data, parts orders, images, total-loss quotes and notification subscriptions, plus a bodyshop-management BMS API), an Intelligent Vehicle Inspection API Gateway (image capture, AI triage, video assessment, webhooks), and North American GIC / Dashboard Assignment integration APIs. APIs are RESTful with JSON/XML support, secured with OAuth 2.0 (AudaConnect portal and an OpenID Connect identity server), and access is granted through the AudaConnect service desk rather than self-service sign-up.'
features:
- description: Search, create, download/upload (AxFormat), amend, complete and report on vehicle damage assessments via the AudaConnect WebAPI.
  name: Assessment Access
- description: Look up vehicle information by registration or VIN (VIN Plus), paint codes, and CAP valuations.
  name: Vehicle Lookup and Valuation
- description: Get supplier part prices, upload and update parts orders, and manage registered suppliers.
  name: Parts Pricing and Orders
- description: Send guided image-capture requests by SMS, link or QR code; upload images, audio and video; run AI Triage and VI damage calculations.
  name: Image, Audio and Video Capture
- description: Subscribe to hierarchical assessment topics (poll or push) on AudaConnect, and register webhooks for 14 image-capture and communication event types on the API Gateway.
  name: Notifications and Webhooks
- description: AudaConnect supports authorization-code, implicit and refresh-token flows with scoped access; NA services use an OpenID Connect identity server.
  name: OAuth 2.0 Security
finops:
- name: Audatex Finops
  service_category: API
  slug: audatex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/audatex.png
integrations:
- description: BMS API for automated assessment exchange, parts pricing, and parts-order workflows.
  name: Bodyshop Management Systems
- description: GIC and Dashboard Assignment APIs for insurer claims and FNOL assignment integration.
  name: Insurance Core Systems
- description: Supplier registration and parts-price lookups for repair estimates.
  name: Parts Suppliers
layout: provider
mcp_servers:
- description: ''
  name: Audatex MCP Server
  slug: audatex-mcp-server
modified: '2026-09-17'
name: Audatex
nav: Providers
network: true
overview: 'Audatex publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AudaConnect API, AudaConnect BMS API, API Gateway (Intelligent Vehicle Inspection), and 3 more. Tagged areas include Automotive, Claims Processing, Insurance, Repair Management, and Vehicle Data.


  The Audatex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Audatex''s developer surface includes YouTube channel, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 26 more developer resources.'
plans:
- name: Audatex Plans Pricing
  plan_count: 0
  slug: audatex-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Audatex Rate Limits
  slug: audatex-rate-limits
scopes:
- name: Audatex Scopes
  scope_count: 27
  slug: audatex-scopes
  summary_line: 27 scopes · implicit/password
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 47.0
    developer_ergonomics: 66.1
    discoverability: 78.6
    operational_transparency: 7.9
  previous_composite: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 40.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/screenshots/audatex-2026-06-20T172546.png
security:
- kind: authentication
  name: Audatex Authentication
  slug: audatex-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Audatex Domain Security
  slug: audatex-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: audatex
solutions:
- description: End-to-end automation of auto insurance claims from FNOL through repair authorization and settlement.
  name: Claims Process Automation
- description: Digital workflow management for collision repair shops integrating estimates, parts, labor, and customer communication.
  name: Repair Shop Workflow
tags:
- Automotive
- Claims Processing
- Insurance
- Repair Management
- Vehicle Data
- Collision Repair
- Vehicle Inspection
use_cases:
- description: Automate first notice of loss, damage assessment, and claims settlement workflows for auto insurers.
  name: Insurance Claims Automation
- description: Integrate bodyshop management systems with Audatex for assessment exchange, parts pricing, and parts orders.
  name: Bodyshop Management System Integration
- description: Request and manage Total Loss Avoidance quotes and vehicle valuations to inform total-loss decisions.
  name: Total Loss Determination
- description: Guide policyholders through mobile photo capture and feed images into AI triage and damage detection.
  name: Digital Claims Submission
website: https://audatex.co.uk/
---
