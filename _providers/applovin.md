---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Applovin Agentic Access
  operation_count: 30
  slug: applovin-agentic-access
  summary_line: 30 operations · 14 acting
api_count: 11
apis:
- description: Ad unit lifecycle and configuration
  name: AppLovin Ad Units API
  slug: applovin-ad-units-api
- description: Creative-level performance reporting
  name: AppLovin Asset Reporting API
  slug: applovin-asset-reporting-api
- description: Creative asset upload and listing
  name: AppLovin Assets API
  slug: applovin-assets-api
- description: Campaign create / update / list operations
  name: AppLovin Campaigns API
  slug: applovin-campaigns-api
- description: Server-to-server conversion event ingestion
  name: AppLovin Conversion Events API
  slug: applovin-conversion-events-api
- description: Creative set lifecycle operations
  name: AppLovin Creative Sets API
  slug: applovin-creative-sets-api
- description: Ad unit A/B experiment management
  name: AppLovin Experiments API
  slug: applovin-experiments-api
- description: Campaign performance reporting for advertisers and publishers
  name: AppLovin Growth Reporting API
  slug: applovin-growth-reporting-api
- description: Mediation revenue and user-level reporting
  name: AppLovin Revenue Reporting API
  slug: applovin-revenue-reporting-api
- description: Test device management
  name: AppLovin Test Devices API
  slug: applovin-test-devices-api
- description: Per-segment waterfall management
  name: AppLovin Waterfalls API
  slug: applovin-waterfalls-api
artifact_total: 46
collections:
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units API
  slug: postman-applovin-ad-units-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Asset Reporting API
  slug: postman-applovin-asset-reporting-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Assets API
  slug: postman-applovin-assets-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Campaigns API
  slug: postman-applovin-campaigns-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Conversion Events API
  slug: postman-applovin-conversion-events-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Creative Sets API
  slug: postman-applovin-creative-sets-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Experiments API
  slug: postman-applovin-experiments-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Growth Reporting API
  slug: postman-applovin-growth-reporting-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Revenue Reporting API
  slug: postman-applovin-revenue-reporting-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Test Devices API
  slug: postman-applovin-test-devices-api
- collection_type: postman
  name: AppLovin Axon Campaign Management Ad Units Waterfalls API
  slug: postman-applovin-waterfalls-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/applovin/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/applovin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/applovin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/applovin-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/applovin
- group: company
  title: ''
  type: Website
  url: https://www.applovin.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.axon.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.applovin.com
- group: operate
  title: ''
  type: Support
  url: https://support.axon.ai
- group: company
  title: ''
  type: Blog
  url: https://www.applovin.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.applovin.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.applovin.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AppLovin
- group: build
  title: MAX Android SDK
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-SDK-Android
- group: build
  title: MAX iOS SDK
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-SDK-iOS
- group: build
  title: MAX Swift Package
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Swift-Package
- group: build
  title: MAX Unity Plugin
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Unity-Plugin
- group: build
  title: MAX React Native Plugin
  type: SDKs
  url: https://www.npmjs.com/package/react-native-applovin-max
- group: build
  title: MAX Flutter Plugin
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Flutter
- group: build
  title: MAX Cordova Plugin
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Cordova
- group: build
  title: MAX Unreal Plugin
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Unreal
- group: build
  title: MAX Defold Plugin
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Defold
- group: build
  title: MAX Godot Plugin
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Godot
- group: build
  title: MAX Adobe AIR Plugin
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-AIR
- group: build
  title: MAX Ad Review Android SDK
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Ad-Review-SDK-Android
- group: build
  title: MAX Ad Review iOS SDK
  type: SDKs
  url: https://github.com/AppLovin/AppLovin-MAX-Ad-Review-SDK-iOS
- group: build
  title: MAX Unity Demo App
  type: CodeExamples
  url: https://github.com/AppLovin/AppLovin-MAX-Unity-Plugin
- group: build
  title: AppLovin CocoaPods Specs Repository
  type: Tools
  url: https://github.com/AppLovin/CocoaPods-Specs
- group: build
  title: Homebrew Mobile Tools Tap
  type: Tools
  url: https://github.com/AppLovin/homebrew-Mobile-Tools
- group: design
  title: AppLovin Spectral Ruleset
  type: SpectralRules
  url: rules/applovin-rules.yml
- group: design
  title: AppLovin JSON-LD Context
  type: JSONLD
  url: json-ld/applovin-context.jsonld
- group: design
  title: AppLovin Domain Vocabulary
  type: Vocabulary
  url: vocabulary/applovin-vocabulary.yml
- group: docs
  title: AppLovin Campaign Schema
  type: JSONSchema
  url: json-schema/applovin-campaign-schema.json
- group: docs
  title: AppLovin Creative Set Schema
  type: JSONSchema
  url: json-schema/applovin-creative-set-schema.json
- group: docs
  title: AppLovin Ad Unit Schema
  type: JSONSchema
  url: json-schema/applovin-ad-unit-schema.json
- group: docs
  title: AppLovin Conversion Event Schema
  type: JSONSchema
  url: json-schema/applovin-conversion-event-schema.json
created: '2026-05-04'
description: AppLovin is a marketing platform that helps businesses reach, monetize, and grow their global audiences through mobile advertising, mediation, and analytics. The company operates platforms including AppDiscovery (Axon) for performance-based user acquisition, MAX for in-app bidding mediation, Adjust for mobile measurement, and Wurl for connected TV. AppLovin provides SDKs and REST APIs that allow app developers and advertisers to integrate ad serving, monetization, campaign management, conversion tracking, and reporting capabilities into their applications.
examples:
- key_count: 3
  name: Applovin Axon Campaign Management Create Example
  slug: applovin-axon-campaign-management-create-example
- key_count: 3
  name: Applovin Axon Campaign Management List Example
  slug: applovin-axon-campaign-management-list-example
- key_count: 3
  name: Applovin Conversion Api Lead Gen Example
  slug: applovin-conversion-api-lead-gen-example
- key_count: 3
  name: Applovin Growth Asset Reporting Example
  slug: applovin-growth-asset-reporting-example
- key_count: 3
  name: Applovin Growth Reporting Example
  slug: applovin-growth-reporting-example
- key_count: 3
  name: Applovin Max Ad Unit Management Create Example
  slug: applovin-max-ad-unit-management-create-example
- key_count: 3
  name: Applovin Max Ad Unit Management List Example
  slug: applovin-max-ad-unit-management-list-example
- key_count: 3
  name: Applovin Max Revenue Reporting Example
  slug: applovin-max-revenue-reporting-example
finops:
- name: Applovin Finops
  service_category: API
  slug: applovin-finops
image: https://www.applovin.com/favicon.ico
json_schemas:
- name: AppLovin MAX Ad Unit
  property_count: 12
  slug: applovin-ad-unit
- name: AppLovin Axon Campaign
  property_count: 14
  slug: applovin-campaign
- name: AppLovin Conversion Event
  property_count: 6
  slug: applovin-conversion-event
- name: AppLovin Creative Set
  property_count: 9
  slug: applovin-creative-set
json_structures:
- name: Applovin Ad Unit Structure
  property_count: 0
  slug: applovin-ad-unit-structure
- name: Applovin Campaign Structure
  property_count: 0
  slug: applovin-campaign-structure
- name: Applovin Conversion Event Structure
  property_count: 0
  slug: applovin-conversion-event-structure
jsonld:
- class_count: 50
  name: Applovin Context
  property_count: 10
  slug: applovin-context
layout: provider
modified: '2026-05-19'
name: AppLovin
nav: Providers
network: true
overview: 'AppLovin publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Ad Units API, Asset Reporting API, Assets API, and 8 more. Tagged areas include Advertising, Mobile, AdTech, App Monetization, and Mediation.


  The AppLovin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AppLovin''s developer surface includes authentication, documentation, support, engineering blog, code examples, tooling, and 30 more developer resources.'
plans:
- name: Applovin Plans Pricing
  plan_count: 1
  slug: applovin-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 2
  name: Applovin Rate Limits
  slug: applovin-rate-limits
rules:
- name: AppLovin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: applovin-jsonschema-spectral-rules
- name: AppLovin API Rules
  rule_count: 28
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 15
  slug: applovin-rules
score:
  band: developing
  composite: 53.6
  delta: -6.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.0
    developer_ergonomics: 54.3
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/applovin/refs/heads/main/screenshots/applovin-2026-06-20T172326.png
security:
- kind: authentication
  name: Applovin Authentication
  slug: applovin-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Applovin Domain Security
  slug: applovin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: applovin
tags:
- Advertising
- Mobile
- AdTech
- App Monetization
- Mediation
- User Acquisition
- Marketing Technology
- Conversion Tracking
website: https://www.applovin.com
---
