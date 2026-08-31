---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Vnc Agentic Access
  operation_count: 7
  slug: vnc-agentic-access
  summary_line: 7 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The VNC Connect API Access feature enables programmatic management of devices registered to a team account, supporting device inventory, renaming, deduplication, and integration with ITSM tools. Authe
  name: VNC Connect Management API
  slug: vnc-connect-api
- description: Cross-platform SDK for embedding VNC Viewer and Server functionality into applications. Available for C, Java, Python, .NET, and JavaScript. Supports direct TCP/UDP connections, VNC Cloud brokering, e
  name: VNC Developer SDK
  slug: vnc-sdk
- description: Manage cloud addresses for VNC Cloud connectivity brokering.
  name: VNC Cloud Addresses API
  slug: vnc-cloud-addresses-api
artifact_total: 24
collections:
- collection_type: postman
  name: VNC Cloud Cloud Addresses API
  slug: postman-vnc-cloud-addresses-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VNC Cloud Cloud Addresses API
  slug: open-vnc-cloud-addresses-api
- collection_type: open
  name: VNC Cloud API
  slug: open-vnc-cloud
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vnc/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vnc-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vnc-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vnc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vnc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vnc-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/realvnc
- group: company
  title: ''
  type: Website
  url: https://www.realvnc.com/en/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.realvnc.com/en/developer/docs/latest/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/vnc-cloud-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vnc-cloud-address-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/vnc-cloud-address-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vnc-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vnc-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/vnc-rules.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.realvnc.com/en/developer/docs/latest/overview.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/realvnc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/realvnc-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.realvnc.com/en/connect/pricing/
- group: operate
  title: ''
  type: Support
  url: https://help.realvnc.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realvnc.com/en/legal/
created: '2025'
description: RealVNC provides the VNC Connect remote desktop platform and VNC Developer SDK, enabling organizations to embed secure remote access into products and automate device management. The VNC Cloud REST API manages cloud address allocation and connectivity brokering, while the VNC Developer SDK (C, Java, Python, .NET, JavaScript) enables embedding Viewer and Server capabilities into applications.
examples:
- key_count: 2
  name: Vnc Createcloudaddress Example
  slug: vnc-createCloudAddress-example
- key_count: 2
  name: Vnc Deletecloudaddress Example
  slug: vnc-deleteCloudAddress-example
- key_count: 2
  name: Vnc Getcloudaddress Example
  slug: vnc-getCloudAddress-example
- key_count: 2
  name: Vnc Listcloudaddresses Example
  slug: vnc-listCloudAddresses-example
finops:
- name: Vnc Finops
  service_category: Remote Access / Remote Desktop
  slug: vnc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vnc.png
json_schemas:
- name: VNC Cloud Address
  property_count: 4
  slug: vnc-cloud-address
json_structures:
- name: Vnc Cloud Address Structure
  property_count: 0
  slug: vnc-cloud-address-structure
jsonld:
- class_count: 13
  name: Vnc Context
  property_count: 1
  slug: vnc-context
layout: provider
modified: '2026-05-19'
name: VNC
nav: Providers
network: true
overview: 'VNC publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud Addresses API. Tagged areas include Remote Desktop, Remote Access, VNC, Networking, and Screen Sharing.


  The VNC catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  VNC''s developer surface includes authentication, documentation, getting-started guide, pricing, support, and 16 more developer resources.'
plans:
- name: Vnc Plans Pricing
  plan_count: 4
  slug: vnc-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Vnc Rate Limits
  slug: vnc-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: VNC API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: vnc-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: VNC API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: vnc-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.8
    contract_quality: 72.1
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vnc/refs/heads/main/screenshots/vnc-2026-06-20T201123.png
security:
- kind: authentication
  name: Vnc Authentication
  slug: vnc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vnc Domain Security
  slug: vnc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vnc Vulnerability Disclosure
  slug: vnc-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Vnc Trust Center
  slug: vnc-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: vnc
tags:
- Remote Desktop
- Remote Access
- VNC
- Networking
- Screen Sharing
website: https://www.realvnc.com/en/developer/
---
