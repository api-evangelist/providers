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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Redox's modern FHIR API for exchanging clinical and administrative healthcare data across the Redox network using HL7 FHIR resources and notifications, authenticated with OAuth2.
  name: Redox FHIR API
  slug: redox-fhir-api
- description: Redox's legacy event-based Data Model API (Redox Messages) for exchanging structured healthcare data across the network via JSON message payloads.
  name: Redox Data Model API
  slug: redox-data-model-api
- description: The Redox Platform API for managing organizations, sources, destinations, and platform settings via user-level API keys.
  name: Redox Platform API
  slug: redox-platform-api
- description: The Redox FHIR R4 API exposes HL7 FHIR R4 resources for healthcare data exchange between connected systems, supporting FHIR notifications, queries, and writeback messages over an OAuth 2.0-secured bas
  name: Redox FHIR R4 API
  slug: redox-fhir-r4-api
- description: 'redox-hl7-v2 is Redox''s open-source JavaScript library for parsing and generating HL7 v2 messages, useful for teams integrating with legacy hospital interfaces or building tools that bridge HL7v2 and '
  name: Redox HL7 v2 Library
  slug: redox-hl7-v2-library
artifact_total: 57
asyncapis:
- description: ''
  name: Redox Webhooks
  slug: redox-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/redox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redox-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.redoxengine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redoxengine.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.redoxengine.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.redoxengine.com/basics/
- group: company
  title: ''
  type: Blog
  url: https://redoxengine.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RedoxEngine
- group: commercial
  title: ''
  type: Pricing
  url: https://redoxengine.com/forms/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.redoxengine.com/#/signup/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redoxengine.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://redoxengine.com/platform-security/
- group: auth
  title: ''
  type: Security
  url: https://docs.redoxengine.com/security/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://redoxengine.com/platform-security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/redox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/redox-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redox-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/redox-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/redox-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/redox-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/redox-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/redox-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redox-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/redox-mcp.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/redox-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/redox-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/redox-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/redox-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/redox-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/redox-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redoxengine.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redoxengine.com/legal/privacy-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redoxengine.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.redoxengine.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redoxengine.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.redoxengine.com/quickstart-for-redox/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.redoxengine.com/basics/what-is-redox/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.redoxengine.com/api-reference/redox-data-model-api/authenticate-an-oauth-api-key/
- group: start
  title: ''
  type: Console
  url: https://dashboard.redoxengine.com
- group: start
  title: ''
  type: Sandbox
  url: https://docs.redoxengine.com/quickstart-for-redox/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redoxengine.com/contact/
- group: start
  title: ''
  type: Signup
  url: https://www.redoxengine.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://docs.redoxengine.com/troubleshooting/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redoxengine.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://redoxengine.com/blog/category/changelog/
- group: auth
  title: ''
  type: Security
  url: https://docs.redoxengine.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.redoxengine.com/trust/
- group: company
  title: ''
  type: Blog
  url: https://www.redoxengine.com/blog/
- group: other
  title: ''
  type: Customers
  url: https://www.redoxengine.com/customers/
- group: company
  title: ''
  type: Partners
  url: https://www.redoxengine.com/partners/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redox-inc-
- group: other
  title: ''
  type: X
  url: https://x.com/RedoxEngine
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/RedoxEngine
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redox-domain-security.yml
created: '2026-07-17'
description: Redox is a healthcare data interoperability platform, founded in 2014 and headquartered in Madison, Wisconsin, that enables secure, real-time exchange of clinical and administrative data across the healthcare ecosystem. Through a single API and a network of 100+ EHR connections and 12,000+ connected healthcare organizations, Redox lets digital health vendors, providers, payers, EHRs, and life-sciences companies integrate once and reach the entire network. The platform offers a modern FHIR API, the legacy Redox Data Model (Redox Messages) event-based API, and a Platform API for managing organizations, sources, and destinations. Redox is HITRUST r2 and SOC 2 Type 2 certified and HIPAA, GDPR, and CCPA aligned, processing tens of billions of healthcare transactions annually.
features:
- description: Universal translation across HL7v2, CDA, X12, DICOM, and HL7 FHIR R4 so vendors write one integration and reach any connected EHR or network.
  name: Healthcare Data Normalization
- description: Pre-built connectivity to Epic, Oracle Health/Cerner, MEDITECH, Athenahealth, eClinicalWorks, NextGen, Allscripts/Veradigm, and dozens of other EHRs.
  name: 100+ EHR Connections
- description: Integrated access to Carequality, CommonWell, TEFCA, DirectTrust, and other clinical exchange networks through a single Redox connection.
  name: Clinical Network Onramps
- description: Redox EMPI powered by Verato links patient records across disparate sources to support longitudinal patient views and matching.
  name: Patient Identity (EMPI)
- description: Direct ingestion onramps into AWS, Microsoft Azure, Google Cloud, Databricks, and Snowflake for analytics, ML, and warehouse use cases.
  name: Cloud Connectivity
- description: Filters (allow/block rules), translation sets (value mappings), and config modifiers let teams customize processing logic without code deploys.
  name: Data Operations
- description: Event subscriptions and conditional routing govern how and when data moves across the connected ecosystem.
  name: Subscriptions and Orchestration
- description: Real-time message streaming plus bulk and batch delivery modes to fit both transactional and analytics workloads.
  name: Bulk and Real-Time Delivery
- description: Development, staging, and production environments with promotion workflows for safe configuration rollout.
  name: Environments and Promotions
- description: HITRUST r2 certified on AWS and GCP and SOC 2 Type 2 compliant security posture across the platform.
  name: HITRUST and SOC 2
image: https://redoxengine.com/wp-content/uploads/2023/01/redox-logo.png
integrations:
- description: Bi-directional connectivity to Epic EHR for clinical, ADT, scheduling, orders, and results workflows.
  name: Epic
- description: Connection to Oracle Health Millennium for FHIR, HL7v2, and Data Model traffic.
  name: Oracle Health (Cerner)
- description: Integration with MEDITECH Expanse and MAGIC for ambulatory and acute care data exchange.
  name: MEDITECH
- description: Connectivity to athenaOne for ambulatory and revenue-cycle workflows.
  name: Athenahealth
- description: Integration with eClinicalWorks ambulatory EHR.
  name: eClinicalWorks
- description: Connection to NextGen ambulatory EHR.
  name: NextGen Healthcare
- description: Integration with Veradigm/Allscripts ambulatory and acute EHRs.
  name: Allscripts (Veradigm)
- description: Onramp to the Carequality national interoperability framework for document and FHIR exchange.
  name: Carequality
- description: Onramp to the CommonWell network for cross-vendor patient record exchange.
  name: CommonWell Health Alliance
- description: Connectivity to the Trusted Exchange Framework and Common Agreement (TEFCA) network.
  name: TEFCA
- description: Secure Direct messaging through the DirectTrust network.
  name: DirectTrust
- description: Redox EMPI powered by Verato for enterprise master patient indexing and identity resolution.
  name: Verato EMPI
- description: IMO codeset normalization for diagnosis and procedure terminology.
  name: IMO
- description: Direct cloud connectivity into Amazon Web Services accounts and AWS Marketplace listing.
  name: AWS
- description: Cloud connectivity into Microsoft Azure and Azure Marketplace listing.
  name: Microsoft Azure
- description: Cloud connectivity into Google Cloud Platform and GCP Marketplace listing.
  name: Google Cloud
- description: Native onramp into Snowflake for clinical data warehousing.
  name: Snowflake
- description: Native onramp into Databricks for healthcare lakehouse and AI workloads.
  name: Databricks
layout: provider
mcp_servers:
- description: ''
  name: redox-mcp.yml
  slug: redox-mcpyml
modified: '2026-08-14'
name: Redox
nav: Providers
network: true
overview: 'Redox publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Interoperability, FHIR, and EHR.


  The Redox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Redox''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 48 more developer resources.'
plans:
- name: Redox Plans Pricing
  plan_count: 0
  slug: redox-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Redox Rate Limits
  slug: redox-rate-limits
scopes:
- name: Redox Scopes
  scope_count: 3
  slug: redox-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 62.7
  delta: 3.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 71.4
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 59.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redox/refs/heads/main/screenshots/redox-2026-06-20T192731.png
security:
- kind: authentication
  name: Redox Authentication
  slug: redox-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Redox Domain Security
  slug: redox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Redox Vulnerability Disclosure
  slug: redox-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Redox Trust Center
  slug: redox-trust-center
  summary_line: HITRUST r2, SOC 2 Type 2
slug: redox
solutions:
- description: Connect digital health products to providers and payers, integrate with EHR systems, and access clinical networks through a single API.
  name: Vendors
- description: Real-time data exchange for discharge coordination, infection risk detection, capacity management, registry submission, payer data exchange, lab order routing, and EHR migration.
  name: Providers
- description: HEDIS reporting, member data standardization, care gap identification, and prior authorization workflows powered by provider-sourced clinical data.
  name: Payers
- description: EHR vendors expose modern API surfaces to their ecosystems through Redox-mediated integration tooling.
  name: EHRs
- description: Real-world data acquisition, clinical trial recruitment, and post-market surveillance built on top of normalized healthcare data.
  name: Life Sciences
tags:
- Company
- Healthcare
- Interoperability
- FHIR
- EHR
- Health Data
- Integration
- HL7
- Digital Health
- Healthcare API
use_cases:
- description: Digital health startups embed Redox to reach hospital and clinic EHRs without building one-off interfaces per customer.
  name: Digital Health EHR Integration
- description: Patient-facing apps pull longitudinal records over FHIR and write encounter data back to provider EHRs.
  name: Patient Access and Engagement
- description: Providers exchange ADT, discharge, and referral messages with downstream partners in real time.
  name: Care Coordination and Discharge
- description: Aggregate clinical data across networks for registry submission, public health reporting, and population analytics.
  name: Population Health and Registries
- description: Payers run prior authorization, HEDIS reporting, member data standardization, and care-gap workflows on top of Redox-mediated provider data.
  name: Payer Data Exchange
- description: Labs and diagnostic vendors route orders and results bi-directionally across EHRs through standardized event types.
  name: Lab Order and Result Routing
- description: Device manufacturers stream telemetry and observations into EHR charts via the same integration surface.
  name: Medical Device Data Capture
- description: Health systems lift-and-shift between EHRs by replaying historical data through Redox during cutover.
  name: EHR Migration and Conversion
- description: Pharma and life sciences teams pull de-identified real-world data for clinical research and post-market surveillance.
  name: Life Sciences Real-World Data
- description: Hydrate Snowflake, Databricks, BigQuery, S3, and Azure data lakes with normalized clinical data for analytics and ML.
  name: Cloud Data Warehouse Hydration
website: https://www.redoxengine.com
---
