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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Qwilt Agentic Access
  operation_count: 22
  slug: qwilt-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 6
apis:
- description: Certificate templates for Qwilt-managed CSR workflows
  name: Qwilt Certificate Templates API
  slug: qwilt-certificate-templates-api
- description: TLS certificates
  name: Qwilt Certificates API
  slug: qwilt-certificates-api
- description: Qwilt CDN egress IP addresses for origin allow-listing
  name: Qwilt Origin Allow List API
  slug: qwilt-origin-allow-list-api
- description: Publish, un-publish, republish and cancel operations
  name: Qwilt Publishing Operations API
  slug: qwilt-publishing-operations-api
- description: Versioned site configuration revisions
  name: Qwilt Site Configurations API
  slug: qwilt-site-configurations-api
- description: CDN media-delivery site objects
  name: Qwilt Sites API
  slug: qwilt-sites-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qwilt CDN Certificate Manager Certificate Templates API
  slug: open-qwilt-certificate-templates-api
- collection_type: open
  name: Qwilt CDN Certificate Manager Certificate Templates Certificates API
  slug: open-qwilt-certificates-api
- collection_type: open
  name: Qwilt CDN Certificate Manager Certificate Templates Origin Allow List API
  slug: open-qwilt-origin-allow-list-api
- collection_type: open
  name: Qwilt CDN Certificate Manager Certificate Templates Publishing Operations API
  slug: open-qwilt-publishing-operations-api
- collection_type: open
  name: Qwilt CDN Certificate Manager Certificate Templates Site Configurations API
  slug: open-qwilt-site-configurations-api
- collection_type: open
  name: Qwilt CDN Certificate Manager Certificate Templates Sites API
  slug: open-qwilt-sites-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/qwilt-certificate-manager-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.qwilt.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qc-services.cqloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qwilt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.qwilt.cqloud.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qwilt.com/docs/quick-start-md
- group: start
  title: ''
  type: Login
  url: https://qc-services.cqloud.com/
- group: operate
  title: ''
  type: Support
  url: https://qwilt.com/support/
- group: company
  title: ''
  type: Blog
  url: https://qwilt.com/resources/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qwilt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qwilt.com/qwilt-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qwilt.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://qwilt.com/compliance/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qwilt-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qwilt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qwilt-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qwilt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qwilt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qwilt-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qwilt-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/qwilt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qwilt-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/qwilt-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qwilt-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qwilt-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qwilt-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qwilt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qwilt-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwilt-domain-security.yml
created: '2026-07-17'
description: Qwilt operates a global content delivery network built on the Open Edge Cloud — a true edge cloud with thousands of deeply embedded caching nodes inside service-provider networks — for OTT video streaming, low-latency live, gaming, and software delivery. Qwilt exposes programmatic control of its CDN through the Sites API (media-delivery site objects, versioned configurations, and publish/un-publish operations), the Certificate Manager API (TLS certificates and Qwilt-managed CSR workflows), the Origin Allow List API, plus Delivery Reports and Keys Manager APIs. Automation is available via the official Qwilt Terraform provider and the qctl command-line interface. Authentication uses QC Services API keys (Viewer/Editor) sent as an X-API-KEY Authorization header, or a username/password bearer token.
image: https://qwilt.com/wp-content/themes/qwilt/resources/img/favicons/favicon-196x196.png
layout: provider
mcp_servers:
- description: ''
  name: qwilt-mcp.yml
  slug: qwilt-mcpyml
modified: '2026-07-20'
name: Qwilt
nav: Providers
network: true
overview: 'Qwilt publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Certificate Templates API, Certificates API, Origin Allow List API, and 3 more. Tagged areas include Company, Media, CDN, Content Delivery Network, and Edge Computing.


  Qwilt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 23 more developer resources.'
random_paper: 114
score:
  band: developing
  composite: 41.4
  delta: 1.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 16.7
    contract_quality: 17.0
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Qwilt Authentication
  slug: qwilt-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Qwilt Domain Security
  slug: qwilt-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Qwilt Trust Center
  slug: qwilt-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: qwilt
tags:
- Company
- Media
- CDN
- Content Delivery Network
- Edge Computing
- Video Streaming
- Open Caching
- Media Delivery
- Certificates
- Infrastructure
website: https://www.qwilt.com
---
