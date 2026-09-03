---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Xcel Energy Agentic Access
  operation_count: 57
  slug: xcel-energy-agentic-access
  summary_line: 57 operations · 8 acting
api_count: 29
apis:
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Third-party application registration metadata used by the Data Custodian.
  name: Xcel Energy ApplicationInformation API
  slug: xcel-energy-applicationinformation-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: OAuth 2.0 authorizations granted by retail customers to third-party applications.
  name: Xcel Energy Authorization API
  slug: xcel-energy-authorization-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Bulk Atom feeds aggregating multiple resources for a subscription.
  name: Xcel Energy Batch API
  slug: xcel-energy-batch-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Configuration resource for a device.
  name: Xcel Energy Configuration API
  slug: xcel-energy-configuration-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Demand Response programs and load control events.
  name: Xcel Energy DemandResponse API
  slug: xcel-energy-demandresponse-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Distributed Energy Resource programs, controls, and settings.
  name: Xcel Energy DER API
  slug: xcel-energy-der-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Root resource that lists the function sets supported by the meter.
  name: Xcel Energy DeviceCapability API
  slug: xcel-energy-devicecapability-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Manufacturer, hardware, and firmware metadata for a device.
  name: Xcel Energy DeviceInformation API
  slug: xcel-energy-deviceinformation-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Operational status, op-time, and event indicators for a device.
  name: Xcel Energy DeviceStatus API
  slug: xcel-energy-devicestatus-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Aggregate power-quality measurements for a UsagePoint.
  name: Xcel Energy ElectricPowerQualitySummary API
  slug: xcel-energy-electricpowerqualitysummary-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Billing-period aggregate summaries of electric power usage.
  name: Xcel Energy ElectricPowerUsageSummary API
  slug: xcel-energy-electricpowerusagesummary-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: End devices managed by the meter (the meter itself and any subordinate devices).
  name: Xcel Energy EndDevice API
  slug: xcel-energy-enddevice-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Groups of function sets assigned to an EndDevice by the server operator.
  name: Xcel Energy FunctionSetAssignments API
  slug: xcel-energy-functionsetassignments-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Time-series interval-level energy usage data captured at a meter.
  name: Xcel Energy IntervalBlock API
  slug: xcel-energy-intervalblock-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Time zone and daylight-savings-time parameters used to interpret interval timestamps.
  name: Xcel Energy LocalTimeParameters API
  slug: xcel-energy-localtimeparameters-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Log events emitted by the device.
  name: Xcel Energy Log API
  slug: xcel-energy-log-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Text and HTML messages targeted at end-users.
  name: Xcel Energy Messaging API
  slug: xcel-energy-messaging-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Container for measured IntervalBlocks captured at a UsagePoint.
  name: Xcel Energy MeterReading API
  slug: xcel-energy-meterreading-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Client-supplied mirror usage points used to publish readings to the server.
  name: Xcel Energy MirrorUsagePoint API
  slug: xcel-energy-mirrorusagepoint-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Real-time power flow and battery status for a device.
  name: Xcel Energy PowerStatus API
  slug: xcel-energy-powerstatus-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Metadata describing the units, multiplier, accumulation, and flow direction of meter readings.
  name: Xcel Energy ReadingType API
  slug: xcel-energy-readingtype-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: EndDevice registration and provisioning state.
  name: Xcel Energy Registration API
  slug: xcel-energy-registration-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Acknowledgement responses for received events.
  name: Xcel Energy Response API
  slug: xcel-energy-response-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Retail customer, account, agreement, service location, and meter information.
  name: Xcel Energy RetailCustomer API
  slug: xcel-energy-retailcustomer-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Convenience resource referring to the device that hosts the API.
  name: Xcel Energy SelfDevice API
  slug: xcel-energy-selfdevice-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Operational status of the Green Button Connect My Data service.
  name: Xcel Energy ServiceStatus API
  slug: xcel-energy-servicestatus-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Subscription/notification resources for resource-change events.
  name: Xcel Energy Subscription API
  slug: xcel-energy-subscription-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Current device time and time-zone configuration.
  name: Xcel Energy Time API
  slug: xcel-energy-time-api
- baseURL: https://api.xcelenergy.com
  baseurl_source: declared
  description: Logical metered points that produce energy usage data for a service.
  name: Xcel Energy UsagePoint API
  slug: xcel-energy-usagepoint-api
artifact_total: 95
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation API
  slug: open-xcel-energy-applicationinformation-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Authorization API
  slug: open-xcel-energy-authorization-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Batch API
  slug: open-xcel-energy-batch-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Configuration API
  slug: open-xcel-energy-configuration-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation DemandResponse API
  slug: open-xcel-energy-demandresponse-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation DER API
  slug: open-xcel-energy-der-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation DeviceCapability API
  slug: open-xcel-energy-devicecapability-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation DeviceInformation API
  slug: open-xcel-energy-deviceinformation-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation DeviceStatus API
  slug: open-xcel-energy-devicestatus-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation ElectricPowerQualitySummary API
  slug: open-xcel-energy-electricpowerqualitysummary-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation ElectricPowerUsageSummary API
  slug: open-xcel-energy-electricpowerusagesummary-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation EndDevice API
  slug: open-xcel-energy-enddevice-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation FunctionSetAssignments API
  slug: open-xcel-energy-functionsetassignments-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation IntervalBlock API
  slug: open-xcel-energy-intervalblock-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation LocalTimeParameters API
  slug: open-xcel-energy-localtimeparameters-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Log API
  slug: open-xcel-energy-log-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Messaging API
  slug: open-xcel-energy-messaging-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation MeterReading API
  slug: open-xcel-energy-meterreading-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation MirrorUsagePoint API
  slug: open-xcel-energy-mirrorusagepoint-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation PowerStatus API
  slug: open-xcel-energy-powerstatus-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation ReadingType API
  slug: open-xcel-energy-readingtype-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Registration API
  slug: open-xcel-energy-registration-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Response API
  slug: open-xcel-energy-response-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation RetailCustomer API
  slug: open-xcel-energy-retailcustomer-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation SelfDevice API
  slug: open-xcel-energy-selfdevice-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation ServiceStatus API
  slug: open-xcel-energy-servicestatus-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Subscription API
  slug: open-xcel-energy-subscription-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation Time API
  slug: open-xcel-energy-time-api
- collection_type: open
  name: Xcel Energy Green Button Connect My Data ApplicationInformation UsagePoint API
  slug: open-xcel-energy-usagepoint-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xcel-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xcel-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xcel-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xcel-energy-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Xcel-Energy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-apim.aws.xcelenergy.com/
- group: start
  title: ''
  type: Portal
  url: https://developer-apim.aws.xcelenergy.com/
- group: start
  title: ''
  type: Signup
  url: https://developer-apim.aws.xcelenergy.com/register
- group: start
  title: ''
  type: Login
  url: https://developer-apim.aws.xcelenergy.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer-apim.aws.xcelenergy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xcelenergy.com/privacy_policy
- group: operate
  title: ''
  type: Support
  url: https://www.xcelenergy.com/contact_us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xcel-energy
- group: other
  title: ''
  type: X
  url: https://twitter.com/xcelenergy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/XcelEnergyVideo
- group: agent
  title: ''
  type: LlmsText
  url: https://developer-apim.aws.xcelenergy.com/llms.txt
created: '2024-01-01'
description: 'Xcel Energy is a major U.S. electricity and natural gas utility holding company headquartered in Minneapolis, Minnesota, providing service to approximately 3.7 million electricity customers and 2.1 million natural gas customers across eight Midwestern and Western states: Colorado, Minnesota, Texas, New Mexico, North Dakota, South Dakota, Michigan, and Wisconsin. Xcel Energy operates a developer portal at developer-apim.aws.xcelenergy.com that organizes APIs across customer account management, billing, payments, product and service offerings, and request service. The company provides Green Button Connect My Data APIs based on the ESPI (Energy Services Provider Interface) standard developed by NAESB, enabling authorized third-party applications to access customer energy usage data via OAuth 2.0. Xcel Energy also supports IEEE 2030.5 protocol on newer Itron Gen 5 Riva smart meters for direct local-network access to real-time energy data including solar production. Beyond data
  APIs, Xcel Energy is a Fortune 500 company investing in clean energy, grid modernization, electric vehicle programs, demand response, and renewable energy interconnection.'
features:
- description: OAuth 2.0 authorized API access to customer electricity and natural gas usage data following the ESPI standard.
  name: Green Button Connect My Data
- description: Direct local-network access to real-time energy data including solar production from Itron Gen 5 Riva meters.
  name: IEEE 2030.5 Smart Meter API
- description: API category covering customer account profile, preferences, and service management.
  name: Customer Account Management
- description: API category for billing data, statements, and billing account operations.
  name: Billing & Billing Account Management
- description: API category for payment processing and payment service operations against customer accounts.
  name: Payments & Payment Services
- description: API category covering Xcel Energy product and service catalog and program enrollment.
  name: Product & Service Offerings
- description: API category for service requests, support workflows, and customer help operations.
  name: Request Service & Help
- description: Interval and billing-quality energy usage data captured from Xcel Energy smart meters across electricity and natural gas.
  name: Smart Meter Data
- description: Programs that allow utilities and third parties to coordinate load reduction events with smart meter and DER endpoints.
  name: Demand Response Integration
- description: Solar production data exposed through smart meter endpoints for customers with on-site photovoltaic systems.
  name: Solar Interconnection Data
finops:
- name: Xcel Energy Finops
  service_category: Regulated Utility / Energy Data
  slug: xcel-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xcel-energy.png
integrations:
- description: Certified Green Button Connect My Data implementation interoperable with the Green Button ecosystem.
  name: Green Button Alliance
- description: Implements the North American Energy Standards Board Energy Services Provider Interface standard for energy usage data.
  name: NAESB ESPI
- description: Smart Energy Profile 2.0 standard implemented on Itron Gen 5 Riva meters for local device APIs.
  name: IEEE 2030.5
- description: Smart meter deployments use Itron Gen 5 Riva devices that host the IEEE 2030.5 server.
  name: Itron
- description: Whole-building benchmarking workflows can consume Green Button data for commercial customers.
  name: ENERGY STAR Portfolio Manager
- description: Authorization framework used for customer-consented access to Green Button Connect My Data.
  name: OAuth 2.0
layout: provider
modified: '2026-05-19'
name: Xcel Energy
nav: Providers
network: true
overview: 'Xcel Energy publishes 29 APIs on the [APIs.io](https://apis.io/) network, including ApplicationInformation API, Authorization API, Batch API, and 26 more. Tagged areas include Electric Utility, Energy, Energy Data, Green Button, and Natural Gas.


  Xcel Energy''s developer surface includes authentication, developer portal, signup flow, support, YouTube channel, and 11 more developer resources.'
plans:
- name: Xcel Energy Plans Pricing
  plan_count: 1
  slug: xcel-energy-plans-pricing
press:
- date: '2026-05-25'
  title: Google Partners with Xcel Energy for Clean Energy Future
  url: https://www.linkedin.com/posts/brianakobor_this-new-model-can-accelerate-the-energy-activity-7432063857478762496-ToaW
- date: '2026-05-25'
  title: News Releases
  url: https://newsroom.xcelenergy.com/news
- date: '2026-05-25'
  title: Xcel Energy Using AI Technology to Detect Wildfires in ...
  url: https://corporate.my.xcelenergy.com/s/about/newsroom/press-release/xcel-energy-using-ai-technology-to-detect-wildfires-in-texas-panhandle-MCJQJAEYRTBZEFBBTON334QSURGQ
- date: '2026-05-25'
  title: Xcel Energy's Pano AI wildfire detection cameras provide ...
  url: https://www.facebook.com/news8000/posts/xcel-energys-pano-ai-wildfire-detection-cameras-provide-247-monitoring-in-areas-/1639533344677905/
- date: '2026-05-25'
  title: 'Xcel Energy: Brings AI-driven wildfire detection to Wisconsin'
  url: https://www.wispolitics.com/2026/xcel-energy-brings-ai-driven-wildfire-detection-to-wisconsin/
random_paper: 10
rate_limits:
- limit_count: 2
  name: Xcel Energy Rate Limits
  slug: xcel-energy-rate-limits
scopes:
- name: Xcel Energy Scopes
  scope_count: 2
  slug: xcel-energy-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 16.5
    developer_ergonomics: 0.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 18.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 96.8
      derived: 31
      marker_coverage: 100.0
      total: 31
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 39.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xcel-energy/refs/heads/main/screenshots/xcel-energy-2026-06-20T201656.png
security:
- kind: authentication
  name: Xcel Energy Authentication
  slug: xcel-energy-authentication
  summary_line: http/mutualTLS/oauth2 · 4 schemes
- kind: domain-security
  name: Xcel Energy Domain Security
  slug: xcel-energy-domain-security
  summary_line: TLSv1.2 · DMARC
slug: xcel-energy
solutions:
- description: Residential energy usage, billing, and program enrollment across electricity and natural gas service.
  name: Residential Customers
- description: Commercial and industrial customer programs, rates, and aggregated usage data.
  name: Business Customers
- description: Authorized energy management, demand response, and sustainability service providers consuming Green Button data.
  name: Third-Party Service Providers
- description: Contractors, installers, and program partners delivering energy efficiency and renewable installations.
  name: Trade Partners
- description: Anonymized and customer-authorized data access for academic and policy research.
  name: Researchers and Policy Analysts
tags:
- Electric Utility
- Energy
- Energy Data
- Green Button
- Natural Gas
- Smart Grid
- Smart Meter
- Utility
- ESPI
- IEEE 2030.5
- Fortune 500
use_cases:
- description: Third-party apps that help customers track and reduce electricity and natural gas usage.
  name: Energy Management Applications
- description: Applications that track on-site solar production and consumption from IEEE 2030.5 smart meters.
  name: Solar Monitoring
- description: Smart home and HVAC systems that automate energy use based on real-time meter data.
  name: Home Energy Automation
- description: Commercial customers reporting carbon and energy data for ESG and sustainability disclosures.
  name: Sustainability Reporting
- description: Whole-building energy benchmarking for ENERGY STAR Portfolio Manager and similar tools.
  name: Building Performance Benchmarking
- description: Aggregators and DER providers integrating with utility dispatch signals.
  name: Demand Response Programs
- description: EV charging applications that schedule charging based on time-of-use rates and grid conditions.
  name: Electric Vehicle Charging Optimization
- description: Academic and policy research on energy consumption patterns and decarbonization.
  name: Research and Policy Analysis
website: https://developer-apim.aws.xcelenergy.com/
---
