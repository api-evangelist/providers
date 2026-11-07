---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: The GraphQL backend behind the Lynx Fleet Dev Portal. Its /public/graphql endpoint answers anonymously and is the only way to reach Carrier's API contracts and integration guides in machine-readable f
  name: Carrier Lynx Dev Portal GraphQL
  slug: lynx-portal-graphql
- description: i-Vu is Carrier's web-based commercial building automation system for monitoring and controlling HVAC, lighting, and related building systems. It integrates with BACnet and other standard building pro
  name: Carrier i-Vu Building Automation
  slug: i-vu-building-automation
- description: Carrier Comfort Network (CCN) is Carrier's proprietary control and communication network for tying together chillers, air handlers, and related HVAC equipment, typically integrated into BMS/BAS deploy
  name: Carrier Comfort Network
  slug: carrier-comfort-network
- description: Abound is Carrier's cloud-based building intelligence platform that aggregates data from HVAC, IAQ sensors, and occupancy systems to provide indoor-environmental-quality analytics, energy insights, an
  name: Carrier Abound
  slug: abound-building-platform
- description: The Carrier SmartHome app lets homeowners remotely control Carrier connected smart thermostats and residential HVAC equipment. No public developer API is currently published; integration is via the co
  name: Carrier SmartHome App
  provenance: unpublished
  slug: carrier-smarthome
- baseURL: https://api.fleet.lynx.carrier.io
  baseurl_source: declared
  description: The core API from Carrier Global — 13 operation(s) for core.
  name: Carrier Global Core API
  slug: carrier-global-core-api
- baseURL: https://api.fleet.lynx.carrier.io
  baseurl_source: declared
  description: The Core2 API from Carrier Global — 3 operation(s) for core2.
  name: Carrier Global Core2 API
  slug: carrier-global-core2-api
artifact_total: 20
asyncapis:
- description: ''
  name: Carrier Global Lynx Webhooks
  slug: carrier-global-lynx-webhooks
common:
- group: other
  href: https://artifacts.apis.io/carrier-global/overlays/carrier-global-lynx-fleet-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/carrier-global-lynx-fleet-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/carrier-global/overlays/carrier-global-lynx-2way-command-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/carrier-global-lynx-2way-command-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/carrier-global/overlays/carrier-global-lynx-container-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/carrier-global-lynx-container-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.corporate.carrier.com
- group: other
  title: ''
  type: ConsumerSite
  url: https://www.carrier.com/us/en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carrier
- group: docs
  title: ''
  type: Documentation
  url: https://doc-api.fleet.lynx.carrier.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tta.lynxfleet.carrier.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.tta.lynxfleet.carrier.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://doc-api.fleet.lynx.carrier.io/api-documentation
- group: start
  title: ''
  type: SignUp
  url: https://api.tta.lynxfleet.carrier.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.corporate.carrier.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.corporate.carrier.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corporate.carrier.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corporate.carrier.com/legal/privacy-notice/
- group: auth
  title: ''
  type: Security
  url: https://www.carrier.com/us/en/product-security/report-an-issue.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.carrier.com/us/en/product-security.html
- group: auth
  href: https://artifacts.apis.io/carrier-global/authentication/carrier-global-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carrier-global-authentication.yml
- group: design
  href: https://artifacts.apis.io/carrier-global/conventions/carrier-global-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carrier-global-conventions.yml
- group: design
  href: https://artifacts.apis.io/carrier-global/errors/carrier-global-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carrier-global-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carrier-global/lifecycle/carrier-global-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/carrier-global-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/carrier-global/conformance/carrier-global-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carrier-global-conformance.yml
- group: design
  href: https://artifacts.apis.io/carrier-global/data-model/carrier-global-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carrier-global-data-model.yml
- group: operate
  href: https://artifacts.apis.io/carrier-global/rate-limits/carrier-global-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/carrier-global-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/carrier-global/plans/carrier-global-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carrier-global-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/carrier-global/finops/carrier-global-finops.yml
  title: ''
  type: FinOps
  url: finops/carrier-global-finops.yml
- group: design
  href: https://artifacts.apis.io/carrier-global/vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary.yml
- group: start
  href: https://artifacts.apis.io/carrier-global/sandbox/carrier-global-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/carrier-global-sandbox.yml
- group: design
  href: https://artifacts.apis.io/carrier-global/asyncapi/carrier-global-lynx-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/carrier-global-lynx-webhooks.yml
- group: build
  href: https://artifacts.apis.io/carrier-global/packages/carrier-global-packages.yml
  title: ''
  type: Packages
  url: packages/carrier-global-packages.yml
- group: agent
  href: https://artifacts.apis.io/carrier-global/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/carrier-global/mcp/carrier-global-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/carrier-global-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/carrier-global/mcp/carrier-global-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/carrier-global-mcp.yml
- group: agent
  href: https://artifacts.apis.io/carrier-global/well-known/carrier-global-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carrier-global-well-known.yml
- group: auth
  href: https://artifacts.apis.io/carrier-global/security/carrier-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carrier-global-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/carrier-global/security/carrier-global-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carrier-global-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/carrier-global/llms/carrier-global-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carrier-global-llms.txt
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.carrier.com
- group: company
  title: ''
  type: Careers
  url: https://www.corporate.carrier.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.corporate.carrier.com/contact-us/
created: '2026-03-21'
description: 'Carrier Global Corporation is a global provider of healthy, safe, sustainable, and intelligent building and cold-chain solutions, spanning HVAC, refrigeration, fire, security, and building automation technologies. Its digital ecosystem includes the Lynx Fleet telematics platform (Lynx APIs for transport refrigeration units and marine containers), the Abound building management platform, i-Vu and Carrier Comfort Network for commercial building automation, and the Carrier SmartHome app for residential smart thermostats. Lynx Fleet is the only Carrier product publishing machine-readable API contracts: three OpenAPI 3.0.0 documents covering 16 operations across truck/trailer telematics, two-way refrigeration control and container telemetry, served through the developer portal''s public GraphQL backend rather than as static files.'
finops:
- has_sources: true
  method: generated
  name: Carrier Global Finops
  primary_unit: ''
  service_category: HVAC / IoT Platform
  slug: carrier-global-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carrier-global.png
jsonld:
- class_count: 0
  name: Carrier Global Context
  property_count: 10
  slug: carrier-global-context
layout: provider
modified: '2026-09-05'
name: Carrier Global
nav: Providers
network: true
overview: 'Carrier Global publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Core API, Core2 API, and 1 more. Tagged areas include HVAC, Cold Chain, Telematics, Building Automation, and IoT.


  The Carrier Global catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Carrier Global''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 33 more developer resources.'
plans:
- name: Carrier Global Plans Pricing
  plan_count: 3
  slug: carrier-global-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Carrier Global Rate Limits
  slug: carrier-global-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Carrier Global API Rules
  rule_count: 61
  severity_counts:
    error: 55
    hint: 0
    info: 3
    warn: 3
  slug: carrier-global-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 63.0
    catalog_earned_first_party: 8.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 62.3
    developer_ergonomics: 54.2
    discoverability: 69.6
    operational_transparency: 39.5
  previous_composite: 54.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/carrier-global/carrier-global-2026-06-20T174016.png
security:
- kind: authentication
  name: Carrier Global Authentication
  slug: carrier-global-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Carrier Global Domain Security
  slug: carrier-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carrier Global Vulnerability Disclosure
  slug: carrier-global-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 4
skills:
- name: carrier-global-container-telemetry
  slug: carrier-global-container-telemetry
- name: carrier-global-monitor-cold-chain
  slug: carrier-global-monitor-cold-chain
- name: carrier-global-pull-asset-history
  slug: carrier-global-pull-asset-history
- name: carrier-global-send-refrigeration-command
  slug: carrier-global-send-refrigeration-command
slug: carrier-global
tags:
- HVAC
- Cold Chain
- Telematics
- Building Automation
- IoT
- Refrigeration
- Fortune 500
website: https://www.corporate.carrier.com
---
