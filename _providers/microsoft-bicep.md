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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Microsoft Bicep Agentic Access
  operation_count: 23
  slug: microsoft-bicep-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 5
apis:
- description: Command-line interface for compiling and deploying Bicep files.
  name: Bicep CLI
  slug: bicep-cli
- description: Language server implementation for Bicep providing IntelliSense and validation.
  name: Bicep Language Server
  slug: bicep-language-server
- description: Create, validate, and manage ARM/Bicep template deployments
  name: Microsoft Bicep Deployments API
  slug: microsoft-bicep-deployments-api
- description: Manage versions of Template Spec resources
  name: Microsoft Bicep Template Spec Versions API
  slug: microsoft-bicep-template-spec-versions-api
- description: Manage Template Spec resources for reusable Bicep templates
  name: Microsoft Bicep Template Specs API
  slug: microsoft-bicep-template-specs-api
artifact_total: 19
collections:
- collection_type: open
  name: Microsoft Bicep Deployments API
  slug: open-microsoft-bicep-deployments
- collection_type: open
  name: Microsoft Bicep Template Specs API
  slug: open-microsoft-bicep-template-specs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bicep-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-bicep-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-bicep-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-bicep-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-bicep-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/azure-sdk/
- group: operate
  title: ''
  type: Support
  url: https://docs.microsoft.com/en-us/answers/topics/azure-bicep.html
- group: learn
  title: ''
  type: Learning Resources
  url: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/learn-bicep
- group: build
  title: ''
  type: Bicep Examples
  url: https://github.com/Azure/bicep/tree/main/docs/examples
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/Azure/bicep/releases
- group: docs
  title: ''
  type: Contributing Guide
  url: https://github.com/Azure/bicep/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/bicep/blob/main/LICENSE
- group: design
  title: ''
  type: JSONLD
  url: json-ld/microsoft-bicep-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-bicep-deployment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-bicep-template-spec-schema.json
created: '2024-01-15'
description: Microsoft Bicep is a domain-specific language (DSL) that uses declarative syntax to deploy Azure resources. It provides a transparent abstraction over ARM templates and offers a more concise syntax, improved type safety, and better support for modularity and code reuse.
finops:
- name: Microsoft Bicep Finops
  service_category: Developer Tools / Infrastructure as Code
  slug: microsoft-bicep-finops
image: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/media/bicep-logo.png
json_schemas:
- name: Microsoft Bicep Deployment
  property_count: 7
  slug: microsoft-bicep-deployment
- name: Microsoft Bicep Template Spec
  property_count: 7
  slug: microsoft-bicep-template-spec
jsonld:
- class_count: 0
  name: Microsoft Bicep Context
  property_count: 9
  slug: microsoft-bicep-context
layout: provider
modified: '2026-05-19'
name: Microsoft Bicep
nav: Providers
network: true
overview: 'Microsoft Bicep publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deployments API, Template Spec Versions API, and Template Specs API. Tagged areas include ARM Templates, Azure, Cloud, Deployment, and DevOps.


  The Microsoft Bicep catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Bicep''s developer surface includes authentication, engineering blog, support, release notes, and 12 more developer resources.'
plans:
- name: Microsoft Bicep Plans Pricing
  plan_count: 3
  slug: microsoft-bicep-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 6
  name: Microsoft Bicep Rate Limits
  slug: microsoft-bicep-rate-limits
rules:
- name: Microsoft Bicep API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-bicep-jsonschema-spectral-rules
scopes:
- name: Microsoft Bicep Scopes
  scope_count: 1
  slug: microsoft-bicep-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 48.3
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.7
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-bicep/refs/heads/main/screenshots/microsoft-bicep-2026-06-20T185444.png
security:
- kind: authentication
  name: Microsoft Bicep Authentication
  slug: microsoft-bicep-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Bicep Domain Security
  slug: microsoft-bicep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Bicep Vulnerability Disclosure
  slug: microsoft-bicep-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-bicep
tags:
- ARM Templates
- Azure
- Cloud
- Deployment
- DevOps
- Infrastructure as Code
---
