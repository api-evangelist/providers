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
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Microsoft Bicep Agentic Access
  operation_count: 23
  slug: microsoft-bicep-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 2
apis:
- description: Command-line interface for compiling and deploying Bicep files.
  name: Bicep CLI
  slug: bicep-cli
- description: Language server implementation for Bicep providing IntelliSense and validation.
  name: Bicep Language Server
  slug: bicep-language-server
- baseURL: https://github.com/Azure/bicep
  baseurl_source: declared
  description: Create, validate, and manage ARM/Bicep template deployments
  name: Microsoft Bicep Deployments API
  slug: microsoft-bicep-deployments-api
- baseURL: https://github.com/Azure/bicep
  baseurl_source: declared
  description: Manage versions of Template Spec resources
  name: Microsoft Bicep Template Spec Versions API
  slug: microsoft-bicep-template-spec-versions-api
- baseURL: https://github.com/Azure/bicep
  baseurl_source: declared
  description: Manage Template Spec resources for reusable Bicep templates
  name: Microsoft Bicep Template Specs API
  slug: microsoft-bicep-template-specs-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Bicep Deployments API
  slug: open-microsoft-bicep-deployments-api
- collection_type: open
  name: Microsoft Bicep Deployments API
  slug: open-microsoft-bicep-deployments
- collection_type: open
  name: Microsoft Bicep Deployments Template Spec Versions API
  slug: open-microsoft-bicep-template-spec-versions-api
- collection_type: open
  name: Microsoft Bicep Deployments Template Specs API
  slug: open-microsoft-bicep-template-specs-api
- collection_type: open
  name: Microsoft Bicep Template Specs API
  slug: open-microsoft-bicep-template-specs
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/bicep/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/bicep/blob/main/CODE_OF_CONDUCT.md
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
overview: 'Microsoft Bicep publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deployments API, Template Spec Versions API, and Template Specs API. Tagged areas include ArmTemplates, Azure, Cloud, Deployment, and DevOps.


  The Microsoft Bicep catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Bicep''s developer surface includes authentication, engineering blog, support, release notes, and 15 more developer resources.'
plans:
- name: Microsoft Bicep Plans Pricing
  plan_count: 3
  slug: microsoft-bicep-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Microsoft Bicep Rate Limits
  slug: microsoft-bicep-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Microsoft Bicep API Rules
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
- ArmTemplates
- Azure
- Cloud
- Deployment
- DevOps
- Infrastructure as Code
website: https://www.microsoft.com/
---
