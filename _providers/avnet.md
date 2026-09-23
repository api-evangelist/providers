---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-09-23'
api_count: 15
apis:
- description: 'Avnet''s distribution-business API programme, relaunched in June 2025 on a global Azure API Management portal: real-time price and availability (getPriceAndQty), inventory and product information for t'
  name: Avnet API Portal (Procurement APIs)
  slug: avnet-api-portal-procurement-apis
- baseURL: https://master.iotconnect.io
  baseurl_source: declared
  description: FAQs, country/state reference data and property types — the reference-data module behind the /IOTCONNECT console. Part of Avnet's /IOTCONNECT IoT platform REST API (27 operations, API version 2); ever
  name: Avnet /IOTCONNECT Master API
  slug: avnet-iotconnect-master-api
- baseURL: https://auth.iotconnect.io
  baseurl_source: declared
  description: 'Login with a solution-key header to obtain the JWT bearer token every other /IOTCONNECT module requires; refresh, verify and mobile-login methods. Part of Avnet''s /IOTCONNECT IoT platform REST API (5 '
  name: Avnet /IOTCONNECT Authenticate API
  slug: avnet-iotconnect-authenticate-api
- baseURL: https://user.iotconnect.io
  baseurl_source: declared
  description: 'Users, roles and the entity hierarchy that scopes devices and permissions inside an /IOTCONNECT tenant. Part of Avnet''s /IOTCONNECT IoT platform REST API (50 operations, API version 2); every request '
  name: Avnet /IOTCONNECT User API
  slug: avnet-iotconnect-user-api
- baseURL: https://device.iotconnect.io
  baseurl_source: declared
  description: Device templates, attributes, commands, certificates, groups, rules, settings, direct methods, telemetry export, Azure Device Update groups and deployments — the largest module (158 paths). Part of Av
  name: Avnet /IOTCONNECT Device API
  slug: avnet-iotconnect-device-api
- baseURL: https://firmware.iotconnect.io
  baseurl_source: declared
  description: Firmware packages, OTA upgrade scheduling and cancellation, module library and IoT Edge deployments. Part of Avnet's /IOTCONNECT IoT platform REST API (40 operations, API version 2); every request car
  name: Avnet /IOTCONNECT Firmware API
  slug: avnet-iotconnect-firmware-api
- baseURL: https://event.iotconnect.io
  baseurl_source: declared
  description: Event topics, subscriptions and delivery methods (including webhook URL + headers), event templates, user device registration and email send. Part of Avnet's /IOTCONNECT IoT platform REST API (23 oper
  name: Avnet /IOTCONNECT Event API
  slug: avnet-iotconnect-event-api
- baseURL: https://telemetry.iotconnect.io
  baseurl_source: declared
  description: Device sensor data, telemetry history, attribute history and MQTT/STOMP reader credentials over HTTP(S). Part of Avnet's /IOTCONNECT IoT platform REST API (15 operations, API version 2); every request
  name: Avnet /IOTCONNECT Telemetry API
  slug: avnet-iotconnect-telemetry-api
- baseURL: https://file.iotconnect.io
  baseurl_source: declared
  description: 'Upload, update, delete and bulk-upload files and resolve file URLs used by device telemetry. Part of Avnet''s /IOTCONNECT IoT platform REST API (6 operations, API version 1.1); every request carries a '
  name: Avnet /IOTCONNECT File API
  slug: avnet-iotconnect-file-api
artifact_total: 15
asyncapis:
- description: ''
  name: Avnet Iotconnect Webhooks
  slug: avnet-iotconnect-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/security/avnet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avnet.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avnet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avnet/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.avnet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iotconnect.io/iotconnect/rest-api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.iotconnect.io/iotconnect/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iotconnect.io/iotconnect/quick-start/
- group: operate
  title: ''
  type: FAQ
  url: https://apiportal.avnet.com/help/FAQ
- group: operate
  title: ''
  type: Support
  url: https://apiportal.avnet.com/help/Support
- group: start
  title: ''
  type: SignUp
  url: https://apiportal.avnet.com/signup
- group: start
  title: ''
  type: Login
  url: https://apiportal.avnet.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://my.avnet.com/emea/about-us/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://my.avnet.com/emea/about-us/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avnet-iotconnect
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.iotconnect.io/iotconnect/platform/health/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.iotconnect.io/iotconnect/platform/product-updates/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/authentication/avnet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avnet-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/conventions/avnet-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avnet-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/rate-limits/avnet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avnet-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/plans/avnet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avnet-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/lifecycle/avnet-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avnet-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/changelog/avnet-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avnet-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/conformance/avnet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avnet-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/errors/avnet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avnet-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/packages/avnet-packages.yml
  title: ''
  type: Packages
  url: packages/avnet-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/packages/avnet-packages.yml
  title: ''
  type: SDKs
  url: packages/avnet-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/cli/avnet-cli.yml
  title: ''
  type: CLI
  url: cli/avnet-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/mcp/avnet-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avnet-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/asyncapi/avnet-iotconnect-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/avnet-iotconnect-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/llms/avnet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avnet-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/data-model/avnet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avnet-data-model.yml
created: '2026-01-01'
description: 'Avnet is a global technology distributor and solutions provider that delivers electronic components, embedded solutions, and design and supply chain services to industrial and commercial customers. It publishes two API surfaces: the Avnet API Portal (apiportal.avnet.com, launched June 2025) for procurement data such as real-time price and availability across its Avnet, Abacus, Silica and EBV Elektronik trading companies, gated behind per-product subscription approval; and the /IOTCONNECT IoT platform (iotconnect.io), whose eight REST modules — master, authenticate, user, device, firmware, event, telemetry and file — serve live Swagger definitions and ship first-party device and REST SDKs on GitHub and PyPI.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avnet.png
layout: provider
mcp_servers:
- description: ''
  name: Avnet MCP Server
  slug: avnet-mcp-server
modified: '2026-09-18'
name: Avnet
nav: Providers
network: true
overview: 'Avnet publishes 8 APIs on the [APIs.io](https://apis.io/) network, including /IOTCONNECT Master API, /IOTCONNECT Authenticate API, /IOTCONNECT User API, and 5 more. Tagged areas include Fortune 500, Electronics, Components, Supply Chain, and IoT.


  The Avnet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Avnet''s developer surface includes documentation, API reference, getting-started guide, FAQ, support, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Avnet Plans Pricing
  plan_count: 0
  slug: avnet-plans-pricing
press:
- date: ''
  title: News & Press Releases | EBV Elektronik
  url: https://my.avnet.com/ebv/about-us/about-ebv-elektronik/newsroom/press-releases/
- date: ''
  title: EBV Elektronik augments its portfolio of Artificial ...
  url: https://my.avnet.com/wcm/connect/f8cde148-b6cc-465a-a5d1-83091ef9d0f6/EBV+Elektronik+augments+its+portfolio+of+Artificial+Intelligence+solutions+with+highly+innovative+technology+from+Hailo.pdf?MOD=AJPERES&ContentCache=NONE&CACHE=NONE&CVID=oMq7teE
- date: ''
  title: EMBRACING AI | Avnet Insight | Avnet APAC
  url: https://www.avnet.com/apac/resources/research/avnet-insight-2025-embracing-ai/press-release/
- date: ''
  title: 'Avnet Insights: Engineers Get Behind AI'
  url: https://news.avnet.com/press-releases/press-release-details/2025/Avnet-Insights-Engineers-Get-Behind-AI--2025-JtsDEnneAx/default.aspx
- date: ''
  title: Avnet's 5th Annual AI Adoption Research Series ...
  url: https://www.linkedin.com/posts/heather-vana-apr-93704a5_mediarelations-aiadoption-electroniccomponents-activity-7418000006252556288-yHY-
random_paper: 14
rate_limits:
- limit_count: 2
  name: Avnet Rate Limits
  slug: avnet-rate-limits
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 62.6
    developer_ergonomics: 70.8
    discoverability: 81.5
    operational_transparency: 63.2
  previous_composite: 55.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/avnet/refs/heads/main/screenshots/avnet-2026-07-25T202003.png
security:
- kind: authentication
  name: Avnet Authentication
  slug: avnet-authentication
  summary_line: apiKey/oauth2/http · 4 schemes
- kind: domain-security
  name: Avnet Domain Security
  slug: avnet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avnet
tags:
- Fortune 500
- Electronics
- Components
- Supply Chain
- IoT
- Manufacturing
- Distribution
- Procurement
- Device Management
- Firmware
website: https://www.avnet.com
---
