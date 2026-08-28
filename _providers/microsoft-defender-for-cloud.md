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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft Defender For Cloud Agentic Access
  operation_count: 15
  slug: microsoft-defender-for-cloud-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 5
apis:
- description: Azure Resource Manager REST API for managing Defender for Cloud assessments, alerts, recommendations, secure score, regulatory compliance, pricing/plans, security contacts, and connectors for multi-cl
  name: Microsoft Defender for Cloud REST API
  slug: rest-api
- description: Security alert operations
  name: Microsoft Defender for Cloud Alerts API
  slug: microsoft-defender-for-cloud-alerts-api
- description: Security assessment operations
  name: Microsoft Defender for Cloud Assessments API
  slug: microsoft-defender-for-cloud-assessments-api
- description: Defender plan/pricing operations
  name: Microsoft Defender for Cloud Pricings API
  slug: microsoft-defender-for-cloud-pricings-api
- description: Secure score operations
  name: Microsoft Defender for Cloud SecureScores API
  slug: microsoft-defender-for-cloud-securescores-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Defender for Cloud REST Alerts API
  slug: open-microsoft-defender-for-cloud-alerts-api
- collection_type: open
  name: Microsoft Defender for Cloud REST Alerts Assessments API
  slug: open-microsoft-defender-for-cloud-assessments-api
- collection_type: open
  name: Microsoft Defender for Cloud REST Alerts Pricings API
  slug: open-microsoft-defender-for-cloud-pricings-api
- collection_type: open
  name: Microsoft Defender for Cloud REST Alerts SecureScores API
  slug: open-microsoft-defender-for-cloud-securescores-api
- collection_type: open
  name: Microsoft Defender for Cloud REST API
  slug: open-microsoft-defender-for-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-defender-for-cloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-defender-for-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-defender-for-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-defender-for-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-defender-for-cloud-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/defender-for-cloud
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/defender-for-cloud/
- group: docs
  title: ''
  type: REST API Documentation
  url: https://learn.microsoft.com/en-us/rest/api/defenderforcloud/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: docs
  title: ''
  type: GitHub OpenAPI Specs
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/security
- group: agent
  title: ''
  type: LlmsText
  url: https://azure.microsoft.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/security/blog/product/microsoft-defender-for-cloud/feed/
created: '2026-05-11'
description: Microsoft Defender for Cloud is Microsoft's unified cloud-native application protection platform (CNAPP) that delivers cloud security posture management (CSPM) and cloud workload protection (CWPP) across Azure, AWS, GCP, and hybrid/on-premises workloads. It provides security recommendations, secure score, regulatory compliance assessments, vulnerability management, and advanced threat protection for servers, containers, databases, storage, and more. The Defender for Cloud REST APIs are part of the Azure Resource Manager surface and authenticate via Azure Active Directory OAuth 2.0 tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-defender-for-cloud.png
layout: provider
modified: '2026-05-11'
name: Microsoft Defender for Cloud
nav: Providers
network: true
overview: 'Microsoft Defender for Cloud publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Assessments API, Pricings API, and 1 more. Tagged areas include Cloud Security, CSPM, CWPP, CNAPP, and Threat Protection.


  Microsoft Defender for Cloud''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 15
scopes:
- name: Microsoft Defender For Cloud Scopes
  scope_count: 1
  slug: microsoft-defender-for-cloud-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-defender-for-cloud/refs/heads/main/screenshots/microsoft-defender-for-cloud-2026-06-20T185451.png
security:
- kind: authentication
  name: Microsoft Defender For Cloud Authentication
  slug: microsoft-defender-for-cloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Defender For Cloud Domain Security
  slug: microsoft-defender-for-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Defender For Cloud Vulnerability Disclosure
  slug: microsoft-defender-for-cloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-defender-for-cloud
tags:
- Cloud Security
- CSPM
- CWPP
- CNAPP
- Threat Protection
- Compliance
- Vulnerability Management
- Azure
website: https://azure.microsoft.com/en-us/products/defender-for-cloud
---
