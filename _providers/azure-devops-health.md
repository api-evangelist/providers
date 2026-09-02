---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Resource health helps you diagnose and get support when an Azure issue impacts your resources
  name: Azure DevOps Health
  slug: azure-devops-health
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-devops-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-devops-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.microsoft.com/en-us/rest/api/resourcehealth
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Resource health helps you diagnose and get support when an Azure issue impacts your resources
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-devops-health.png
layout: provider
modified: '2026-05-28'
name: Azure DevOps Health
nav: Providers
network: true
overview: Azure DevOps Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Continuous Integration and Public APIs.
random_paper: 17
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-devops-health/refs/heads/main/screenshots/azure-devops-health-2026-06-20T172851.png
security:
- kind: domain-security
  name: Azure Devops Health Domain Security
  slug: azure-devops-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Devops Health Vulnerability Disclosure
  slug: azure-devops-health-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-devops-health
tags:
- Continuous Integration
- Public APIs
website: https://docs.microsoft.com/en-us/rest/api/resourcehealth
---
