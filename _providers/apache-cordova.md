---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Apache Cordova provides a JavaScript plugin API for accessing native device capabilities (camera, GPS, file system, contacts, etc.), a CLI for project management and multi-platform builds, a plugin de
  name: Apache Cordova
  slug: apache-cordova
artifact_total: 36
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/cordova/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/cordova/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-cordova-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-cordova-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://cordova.apache.org/
- group: company
  title: ''
  type: Blog
  url: https://cordova.apache.org/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cordova.apache.org/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://cordova.apache.org/docs/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://cordova.apache.org/docs/en/latest/guide/overview/
- group: operate
  title: ''
  type: Support
  url: https://cordova.apache.org/contact/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/cordova
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: CLI
  url: https://github.com/apache/cordova-cli
- group: build
  title: Plugman Plugin Manager
  type: Tools
  url: https://github.com/apache/cordova-plugman
- group: build
  title: Paramedic Test Runner
  type: Tools
  url: https://github.com/apache/cordova-paramedic
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-cordova/refs/heads/main/vocabulary/apache-cordova-vocabulary.yaml
created: '2026-03-16'
description: Apache Cordova is an open-source mobile development framework governed by the Apache Software Foundation that enables developers to build mobile applications using standard web technologies — HTML, CSS, and JavaScript. It bridges web code to native device capabilities through a plugin architecture, targeting iOS, Android, Electron, and Browser platforms from a single codebase.
examples:
- key_count: 11
  name: Apache Cordova Camera Options Example
  slug: apache-cordova-camera-options-example
- key_count: 12
  name: Apache Cordova Config Widget Example
  slug: apache-cordova-config-widget-example
- key_count: 2
  name: Apache Cordova Geolocation Position Example
  slug: apache-cordova-geolocation-position-example
features:
- description: Extensible plugin system that bridges JavaScript to native device APIs for camera, GPS, file system, contacts, battery, and more.
  name: Plugin Architecture
- description: Command-line interface for creating, building, testing, and deploying applications to multiple platforms from a single codebase.
  name: Cross-Platform CLI
- description: Access to native hardware capabilities including camera, geolocation, network information, vibration, media capture, and device info.
  name: Native Device Access
- description: Renders applications in a native WebView, enabling web technologies to run as native mobile apps on iOS, Android, and Electron.
  name: WebView-Based Runtime
- description: Full API for creating custom native plugins in Swift/Objective-C (iOS) and Java/Kotlin (Android) that expose device APIs to JavaScript.
  name: Plugin Development API
- description: Built-in allowlist mechanism for controlling which URLs and resources the application is permitted to access.
  name: Allowlist Security
finops:
- name: Apache Cordova Finops
  service_category: API
  slug: apache-cordova-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-cordova.png
integrations:
- description: Ionic uses Cordova (and Capacitor) as its native runtime, providing UI components on top of the Cordova platform.
  name: Ionic Framework
- description: PhoneGap was a commercial distribution of Apache Cordova, now retired, but helped establish the Cordova ecosystem.
  name: Adobe PhoneGap
- description: Cordova plugins and the CLI are published and distributed via npm, the Node.js package registry.
  name: npm Package Registry
- description: Android platform builds use Gradle for dependency management and compilation.
  name: Gradle (Android)
- description: iOS platform builds require Xcode for compilation, signing, and deployment.
  name: Xcode (iOS)
- description: Cordova-Electron platform target allows packaging Cordova apps as desktop Electron applications.
  name: Electron
json_schemas:
- name: CameraOptions
  property_count: 11
  slug: apache-cordova-camera-options
- name: Widget
  property_count: 12
  slug: apache-cordova-config-widget
- name: Position
  property_count: 2
  slug: apache-cordova-geolocation-position
json_structures:
- name: Apache Cordova Camera Options Structure
  property_count: 11
  slug: apache-cordova-camera-options-structure
- name: Apache Cordova Config Widget Structure
  property_count: 12
  slug: apache-cordova-config-widget-structure
- name: Apache Cordova Geolocation Position Structure
  property_count: 2
  slug: apache-cordova-geolocation-position-structure
jsonld:
- class_count: 1
  name: Apache Cordova Camera Context
  property_count: 11
  slug: apache-cordova-camera-context
- class_count: 5
  name: Apache Cordova Config Context
  property_count: 11
  slug: apache-cordova-config-context
- class_count: 1
  name: Apache Cordova Geolocation Context
  property_count: 9
  slug: apache-cordova-geolocation-context
layout: provider
modified: '2026-04-19'
name: Apache Cordova
nav: Providers
network: true
overview: 'Apache Cordova publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Cross-Platform, Hybrid Apps, JavaScript, and Mobile.


  The Apache Cordova catalog on APIs.io includes 3 JSON-LD contexts and 1 Spectral governance ruleset.


  Apache Cordova''s developer surface includes developer portal, engineering blog, release notes, documentation, getting-started guide, support, Stack Overflow tag, and 10 more developer resources.'
plans:
- name: Apache Cordova Plans Pricing
  plan_count: 3
  slug: apache-cordova-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Apache Cordova Rate Limits
  slug: apache-cordova-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Cordova API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-cordova-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 34.7
    developer_ergonomics: 69.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 36.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-cordova/refs/heads/main/screenshots/apache-cordova-2026-06-20T172048.png
security:
- kind: domain-security
  name: Apache Cordova Domain Security
  slug: apache-cordova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Cordova Vulnerability Disclosure
  slug: apache-cordova-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-cordova
tags:
- Apache
- Cross-Platform
- Hybrid Apps
- JavaScript
- Mobile
- Open-Source
- Plugins
use_cases:
- description: Build iOS and Android apps from a single HTML/CSS/JavaScript codebase, reducing development time and cost.
  name: Cross-Platform Mobile Apps
- description: Combine web application UIs with native device capabilities for apps that need both web flexibility and native hardware access.
  name: Hybrid App Development
- description: Rapidly prototype and deploy enterprise mobile applications leveraging existing web development skills.
  name: Enterprise Mobile Solutions
- description: Package web apps as Electron desktop applications using the same Cordova plugin model.
  name: Desktop Apps via Electron
- description: Interface with Bluetooth, sensors, and other hardware through community and custom Cordova plugins.
  name: IoT and Device Interfaces
website: https://cordova.apache.org/
---
