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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Core JavaScript APIs for building Lightning Web Components including decorators, wire service, and component lifecycle methods.
  name: Lightning Web Components Runtime API
  slug: lightning-web-components
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://lwc.dev/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightning-web-components-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/component-library/overview/components
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.get_started_introduction
- group: build
  title: ''
  type: Examples
  url: https://github.com/trailheadapps/lwc-recipes
- group: build
  title: ''
  type: Packages
  url: packages/lightning-web-components-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightning-web-components-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightning-web-components-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightning-web-components-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/lightning-web-components-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightning-web-components-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightning-web-components-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/lightning-web-components-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lightning-web-components-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightning-web-components-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/lightning-web-components-cli.yml
- group: design
  title: ''
  type: Components
  url: components/lightning-web-components-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lightning-web-components-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lightning-web-components-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/lightning-web-components-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lightning-web-components-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/lightning-web-components-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lightning-web-components-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightning-web-components-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lwc.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://lwc.dev/guide/reference
- group: operate
  title: ''
  type: Support
  url: https://lwc.dev/community
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/salesforce/lwc
- group: commercial
  title: ''
  type: License
  url: https://github.com/salesforce/lwc/blob/master/LICENSE.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
created: '2024-01-15'
description: 'Lightning Web Components (LWC) is Salesforce''s MIT-licensed, open-source JavaScript UI framework, built directly on native web standards — custom elements, shadow DOM and ES modules — rather than on a proprietary component abstraction. It compiles components to native custom elements, renders in the browser and on the server, and is the component model for the Salesforce Platform as well as a standalone framework for any web app. LWC is distributed exclusively through npm: there is no hosted API, no API key, no pricing and no rate limit. Its contract surface is a JavaScript API — LightningElement, the @api, @track and @wire decorators, lifecycle hooks and wire adapters — accompanied by a published 109-code compiler diagnostic registry, a semver versioning and breaking-change policy, and a lightning-* base component library of 91 consumer-facing components.'
finops:
- name: Lightning Web Components Finops
  service_category: API
  slug: lightning-web-components-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightning-web-components.png
layout: provider
mcp_servers:
- description: ''
  name: Salesforce DX MCP Server — LWC toolsets
  slug: salesforce-dx-mcp-server-lwc-toolsets
modified: '2026-08-27'
name: Lightning Web Components
nav: Providers
network: true
overview: 'Lightning Web Components publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Frontend, JavaScript, Lightning Web Components, Salesforce, and Web Components.


  Lightning Web Components'' developer surface includes documentation, getting-started guide, code examples, changelog, CLI, sandbox, API reference, and 26 more developer resources.'
plans:
- name: Lightning Web Components Plans Pricing
  plan_count: 0
  slug: lightning-web-components-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Lightning Web Components Rate Limits
  slug: lightning-web-components-rate-limits
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 66.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 41.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightning-web-components/refs/heads/main/screenshots/lightning-web-components-2026-06-20T184521.png
security:
- kind: domain-security
  name: Lightning Web Components Domain Security
  slug: lightning-web-components-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lightning Web Components Vulnerability Disclosure
  slug: lightning-web-components-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lightning Web Components Trust Center
  slug: lightning-web-components-trust-center
  summary_line: PCI DSS, IRAP
slug: lightning-web-components
tags:
- Frontend
- JavaScript
- Lightning Web Components
- Salesforce
- Web Components
- Custom Elements
- Shadow DOM
- Open-Source
- UI Framework
- Component Library
website: https://lwc.dev/
---
