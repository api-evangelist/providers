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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: The modern Jamf Pro API, built on the OpenAPI 3.0 standard, for programmatically managing computers, mobile devices, policies, groups, inventory, and configuration on a Jamf Pro instance. Authenticate
  name: Jamf Pro API
  slug: jamf-pro-api
- description: The long-standing Classic API, the original resource for programmatically interacting with Jamf Pro, located at /JSSResource on each instance. Supports XML and JSON payloads and bearer-token authentic
  name: Jamf Pro Classic API
  slug: jamf-pro-classic-api
- description: A single, unified gateway to access any combination of Jamf APIs — Blueprints, Compliance Benchmarks, Device Management Actions, Declaration Reporting, Devices, and Device Groups — described as the lo
  name: Jamf Platform API Gateway
  slug: jamf-platform-api-gateway
artifact_total: 11
asyncapis:
- description: ''
  name: Jamf Webhooks
  slug: jamf-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/jamf/plans/jamf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jamf-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.jamf.com/blog/rss/
- group: auth
  href: https://artifacts.apis.io/jamf/security/jamf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jamf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jamf/security/jamf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jamf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jamf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.jamf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.jamf.com/jamf-pro/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.jamf.com/jamf-pro/reference/jamf-pro-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.jamf.com/developer-guide
- group: company
  title: ''
  type: Blog
  url: https://www.jamf.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jamf
- group: operate
  title: ''
  type: Support
  url: https://www.jamf.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jamf.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.jamf.com/request-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jamf.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jamf.com/trust-center/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jamf.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.jamf.com/jamf-pro/changelog
- group: agent
  href: https://artifacts.apis.io/jamf/llms/jamf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jamf-llms.txt
- group: agent
  href: https://artifacts.apis.io/jamf/well-known/jamf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jamf-well-known.yml
- group: other
  href: https://artifacts.apis.io/jamf/well-known/jamf-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/jamf-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/jamf/well-known/jamf-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jamf-security.txt
- group: agent
  href: https://artifacts.apis.io/jamf/mcp/jamf-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jamf-mcp.yml
- group: design
  href: https://artifacts.apis.io/jamf/asyncapi/jamf-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jamf-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/jamf/authentication/jamf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jamf-authentication.yml
- group: design
  href: https://artifacts.apis.io/jamf/conventions/jamf-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jamf-conventions.yml
- group: design
  href: https://artifacts.apis.io/jamf/lifecycle/jamf-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jamf-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/jamf/lifecycle/jamf-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/jamf-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jamf/conformance/jamf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jamf-conformance.yml
- group: auth
  href: https://artifacts.apis.io/jamf/security/jamf-trust-center.yml
  title: ''
  type: Compliance
  url: security/jamf-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/jamf/security/jamf-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jamf-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jamf.com/trust-center/vulnerability-disclosure/
created: '2026-07-17'
description: 'Jamf is the standard in managing and securing Apple devices at scale for business, education, and government. Its cloud platform pairs Apple device management (MDM), identity, and endpoint security with a broad developer surface: the modern Jamf Pro API (OpenAPI 3.0, bearer-token and OAuth client-credential API Roles & Clients), the long-standing Classic API (/JSSResource, XML/JSON), the new unified Platform API Gateway (Blueprints, Compliance Benchmarks, Device Management Actions), plus the Jamf School, Jamf Protect, and Jamf Security APIs. Jamf publishes an llms.txt developer index, a hosted MCP server for documentation and code generation, a webhooks event catalog, and a trust center enumerating SOC 2, ISO 27001/27701, PCI DSS, HIPAA, GDPR, and NIST 800-53 posture.'
finops:
- has_sources: true
  method: derived
  name: Jamf Finops
  primary_unit: macos device
  service_category: ''
  slug: jamf-finops
  template: false
image: https://www.jamf.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at developer.jamf.com over HTTP; 2 tools listed.
  name: JAMF MCP Server
  slug: jamf-developer
modified: '2026-10-06'
name: JAMF
nav: Providers
network: true
overview: 'JAMF is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Pro API, and 2 more. Tagged areas include Company, Apple Device Management, MDM, Endpoint Security, and Mobile Device Management.


  The JAMF catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  JAMF''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Jamf Plans Pricing
  plan_count: 3
  slug: jamf-plans-pricing
random_paper: 6
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 70.0
    operational_transparency: 63.2
  previous_composite: 53.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jamf/jamf-2026-07-25T223052.png
security:
- kind: authentication
  name: Jamf Authentication
  slug: jamf-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Jamf Domain Security
  slug: jamf-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jamf Vulnerability Disclosure
  slug: jamf-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jamf Trust Center
  slug: jamf-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27001 SoA, ISO/IEC 27701, PCI DSS, HIPAA, GDPR, CSA STAR, NIST 800-53 Rev. 5, Cyber Essentials, EU-US Data Privacy Framework, CCPA, CPRA
slug: jamf
tags:
- Company
- Apple Device Management
- MDM
- Endpoint Security
- Mobile Device Management
- IT Operations
- Identity
- Compliance
- Developer Tools
- Enterprise
website: https://www.jamf.com/
---
