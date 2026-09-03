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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft Edge Agentic Access
  operation_count: 12
  slug: microsoft-edge-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 8
apis:
- description: Build browser extensions for Microsoft Edge using the Chromium-based extensions platform. Supports the WebExtensions API standard for cross-browser compatibility.
  name: Microsoft Edge Extensions API
  slug: edge-extensions-api
- description: Modern web APIs and standards supported in Microsoft Edge, including Progressive Web App capabilities, Web Components, and emerging web platform features.
  name: Microsoft Edge Web Platform APIs
  slug: edge-web-platform-apis
- baseURL: https://api.addons.microsoftedge.microsoft.com
  baseurl_source: declared
  description: Browser-level information and management
  name: Microsoft Edge Browser API
  slug: microsoft-edge-browser-api
- baseURL: https://api.addons.microsoftedge.microsoft.com
  baseurl_source: declared
  description: Upload and manage extension packages
  name: Microsoft Edge Packages API
  slug: microsoft-edge-packages-api
- baseURL: https://api.addons.microsoftedge.microsoft.com
  baseurl_source: declared
  description: Page target management
  name: Microsoft Edge Pages API
  slug: microsoft-edge-pages-api
- baseURL: https://api.addons.microsoftedge.microsoft.com
  baseurl_source: declared
  description: Manage extension products in the Edge Add-ons store
  name: Microsoft Edge Products API
  slug: microsoft-edge-products-api
- baseURL: https://api.addons.microsoftedge.microsoft.com
  baseurl_source: declared
  description: Publish and unpublish extensions
  name: Microsoft Edge Publishing API
  slug: microsoft-edge-publishing-api
- baseURL: https://api.addons.microsoftedge.microsoft.com
  baseurl_source: declared
  description: Discover and manage debuggable browser targets
  name: Microsoft Edge Targets API
  slug: microsoft-edge-targets-api
arazzos:
- description: List debuggable targets, branch on whether any exist, and close the first target.
  name: Microsoft Edge Find And Close Target
  slug: microsoft-edge-find-and-close-target-workflow
- description: Read the browser version and then fetch the full DevTools Protocol schema.
  name: Microsoft Edge Inspect Browser Environment
  slug: microsoft-edge-inspect-browser-environment-workflow
- description: List the developer account's extensions and fetch full details for the first product.
  name: Microsoft Edge List And Inspect Product
  slug: microsoft-edge-list-and-inspect-product-workflow
- description: Confirm the DevTools endpoint, open a new tab at a URL, and bring it to the foreground.
  name: Microsoft Edge Open And Activate Target
  slug: microsoft-edge-open-and-activate-target-workflow
- description: Upload a new extension package, wait for validation, then create and track a store submission.
  name: Microsoft Edge Publish Extension Update
  slug: microsoft-edge-publish-extension-update-workflow
- description: Create a submission for an already-uploaded draft and poll it until Published or Failed.
  name: Microsoft Edge Submit Draft And Track
  slug: microsoft-edge-submit-draft-and-track-workflow
- description: Confirm a product exists, upload a draft package, and poll until the package is validated.
  name: Microsoft Edge Upload Package And Validate
  slug: microsoft-edge-upload-package-and-validate-workflow
artifact_total: 80
collections:
- collection_type: postman
  name: Microsoft Edge Add-ons API
  slug: postman-microsoft-edge-addons-api
- collection_type: postman
  name: Microsoft Edge DevTools Protocol HTTP API
  slug: postman-microsoft-edge-devtools-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Edge Add-ons Browser API
  slug: open-microsoft-edge-browser-api
- collection_type: open
  name: Microsoft Edge Add-ons Browser Packages API
  slug: open-microsoft-edge-packages-api
- collection_type: open
  name: Microsoft Edge Add-ons Browser Pages API
  slug: open-microsoft-edge-pages-api
- collection_type: open
  name: Microsoft Edge Add-ons Browser Products API
  slug: open-microsoft-edge-products-api
- collection_type: open
  name: Microsoft Edge Add-ons Browser Publishing API
  slug: open-microsoft-edge-publishing-api
- collection_type: open
  name: Microsoft Edge Add-ons Browser Targets API
  slug: open-microsoft-edge-targets-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-edge-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-edge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-edge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-edge-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-edge/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-edge-find-and-close-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-edge-inspect-browser-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-edge-list-and-inspect-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-edge-open-and-activate-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-edge-publish-extension-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-edge-submit-draft-and-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-edge-upload-package-and-validate-workflow.yml
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/microsoft-edge/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/microsoft-edge/
- group: company
  title: ''
  type: Blog
  url: https://blogs.windows.com/msedgedev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftEdge
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/MicrosoftEdge/WebView2Samples
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/nicedoc/nicedoc.io
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/microsoft-edge/web-platform/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.microsoft.com/en-us/microsoft-edge/status/
- group: other
  title: ''
  type: X
  url: https://twitter.com/MSEdgeDev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Microsoft.Web.WebView2
- group: start
  title: ''
  type: Signup
  url: https://partner.microsoft.com/dashboard/microsoftedge/
- group: start
  title: ''
  type: Login
  url: https://partner.microsoft.com/dashboard/
- group: other
  title: ''
  type: Marketplace
  url: https://microsoftedge.microsoft.com/addons/
- group: design
  title: DevTools API Context
  type: JSONLD
  url: json-ld/microsoft-edge-devtools-api-context.jsonld
- group: design
  title: Add-ons API Context
  type: JSONLD
  url: json-ld/microsoft-edge-addons-api-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-edge-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-edge-vocabulary.yaml
created: '2024-01-01'
description: APIs and resources for Microsoft Edge browser development and integration, including the Edge Add-ons API for extension management, DevTools Protocol for browser debugging and automation, Extensions API for building browser extensions, and Web Platform APIs for progressive web app development.
examples:
- key_count: 3
  name: Addons Api Package Upload Result Example
  slug: addons-api-package-upload-result-example
- key_count: 7
  name: Addons Api Product Example
  slug: addons-api-product-example
- key_count: 2
  name: Addons Api Product List Example
  slug: addons-api-product-list-example
- key_count: 5
  name: Addons Api Submission Example
  slug: addons-api-submission-example
- key_count: 6
  name: Devtools Api Browser Version Example
  slug: devtools-api-browser-version-example
- key_count: 2
  name: Devtools Api Protocol Schema Example
  slug: devtools-api-protocol-schema-example
- key_count: 8
  name: Devtools Api Target Example
  slug: devtools-api-target-example
features:
- description: Programmatically publish, update, and manage browser extensions in the Edge Add-ons store via REST API.
  name: Extension Publishing API
- description: Debug and inspect web pages, service workers, and extensions using the Chrome DevTools Protocol over WebSocket.
  name: Remote Debugging Protocol
- description: Embed Microsoft Edge rendering engine in native desktop applications using the WebView2 SDK.
  name: WebView2 Embedding
- description: Build installable PWAs with offline capability, push notifications, and system integration.
  name: Progressive Web App Support
- description: Build extensions using the Chromium WebExtensions API standard for cross-browser portability.
  name: Cross-Browser Extension Compatibility
- description: Automate browser tasks including page navigation, target management, and performance profiling.
  name: Browser Automation
- description: Load and test unpacked extensions locally during development without publishing to the store.
  name: Extension Sideloading
- description: Build extensions using the latest Manifest V3 specification with service workers and declarative APIs.
  name: Manifest V3 Support
finops:
- name: Microsoft Edge Finops
  service_category: Developer Tools
  slug: microsoft-edge-finops
image: https://www.microsoft.com/edge/favicon.ico
integrations:
- description: Authenticate to the Edge Add-ons API using Azure AD OAuth 2.0 client credentials flow.
  name: Azure Active Directory
- description: Manage extension listings, submissions, and analytics through the Partner Center dashboard.
  name: Microsoft Partner Center
- description: Debug Edge browser content directly from VS Code using the Edge DevTools extension.
  name: Visual Studio Code
- description: Automate Microsoft Edge browser for testing using Selenium with the Edge WebDriver.
  name: Selenium WebDriver
- description: Cross-browser automation framework with first-class support for Microsoft Edge testing.
  name: Playwright
- description: Control headless Microsoft Edge instances programmatically using the Puppeteer Node.js library.
  name: Puppeteer
- description: Automate extension publishing and browser testing in CI/CD workflows using GitHub Actions.
  name: GitHub Actions
- description: Integrate WebView2 into Windows desktop applications built with WinUI 3 and the Windows App SDK.
  name: Windows App SDK
json_schemas:
- name: PackageUploadResult
  property_count: 3
  slug: addons-api-package-upload-result
- name: ProductList
  property_count: 2
  slug: addons-api-product-list
- name: Product
  property_count: 7
  slug: addons-api-product
- name: Submission
  property_count: 5
  slug: addons-api-submission
- name: BrowserVersion
  property_count: 6
  slug: devtools-api-browser-version
- name: ProtocolSchema
  property_count: 2
  slug: devtools-api-protocol-schema
- name: Target
  property_count: 8
  slug: devtools-api-target
json_structures:
- name: Addons Api Package Upload Result Structure
  property_count: 3
  slug: addons-api-package-upload-result-structure
- name: Addons Api Product List Structure
  property_count: 2
  slug: addons-api-product-list-structure
- name: Addons Api Product Structure
  property_count: 7
  slug: addons-api-product-structure
- name: Addons Api Submission Structure
  property_count: 5
  slug: addons-api-submission-structure
- name: Devtools Api Browser Version Structure
  property_count: 6
  slug: devtools-api-browser-version-structure
- name: Devtools Api Protocol Schema Structure
  property_count: 2
  slug: devtools-api-protocol-schema-structure
- name: Devtools Api Target Structure
  property_count: 8
  slug: devtools-api-target-structure
jsonld:
- class_count: 3
  name: Microsoft Edge Addons Api Context
  property_count: 13
  slug: microsoft-edge-addons-api-context
- class_count: 3
  name: Microsoft Edge Devtools Api Context
  property_count: 16
  slug: microsoft-edge-devtools-api-context
layout: provider
modified: '2026-05-19'
name: Microsoft Edge
nav: Providers
network: true
overview: 'Microsoft Edge publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Browser API, Packages API, Pages API, and 3 more. Tagged areas include Browser, Chromium, Developer Tools, Edge, and Extensions.


  The Microsoft Edge catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Edge''s developer surface includes authentication, documentation, engineering blog, support, release notes, changelog, signup flow, and 26 more developer resources.'
plans:
- name: Microsoft Edge Plans Pricing
  plan_count: 2
  slug: microsoft-edge-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Microsoft Edge Rate Limits
  slug: microsoft-edge-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Edge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-edge-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Microsoft Edge API Rules
  rule_count: 32
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 16
  slug: microsoft-edge-spectral-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 39.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 28.8
    contract_quality: 28.3
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 50.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-edge/refs/heads/main/screenshots/microsoft-edge-2026-08-07T172849.png
security:
- kind: authentication
  name: Microsoft Edge Authentication
  slug: microsoft-edge-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Edge Domain Security
  slug: microsoft-edge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Edge Vulnerability Disclosure
  slug: microsoft-edge-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-edge
tags:
- Browser
- Chromium
- Developer Tools
- Edge
- Extensions
- Microsoft
- Progressive Web Apps
- Web Development
- Webview
use_cases:
- description: Use the Add-ons API to automate CI/CD pipelines for publishing and updating browser extensions.
  name: Automated Extension Deployment
- description: Leverage DevTools Protocol for automated browser testing, performance auditing, and regression detection.
  name: Browser Testing and QA
- description: Embed Edge rendering in desktop applications for custom browser experiences using WebView2.
  name: Custom Browser Controls
- description: Build enterprise extensions for content filtering, security policy enforcement, and compliance monitoring.
  name: Enterprise Content Filtering
- description: Use DevTools Protocol to programmatically navigate pages and extract structured data.
  name: Web Scraping and Data Extraction
- description: Automate accessibility audits using DevTools Protocol to inspect DOM, ARIA attributes, and contrast ratios.
  name: Accessibility Testing
- description: Collect real-time performance metrics, network traces, and JavaScript profiling data via DevTools Protocol.
  name: Performance Monitoring
- description: Build and distribute PWAs through the Microsoft Store with native-like installation and system integration.
  name: Progressive Web App Distribution
website: https://developer.microsoft.com/microsoft-edge/
---
