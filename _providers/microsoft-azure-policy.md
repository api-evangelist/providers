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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Policy Agentic Access
  operation_count: 7
  slug: microsoft-azure-policy-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure Policy Operations API
  slug: microsoft-azure-policy-operations-api
- description: Policy Definitions operations
  name: Azure Policy Policy Definitions API
  slug: microsoft-azure-policy-policy-definitions-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Policy REST Operations API
  slug: open-microsoft-azure-policy-operations-api
- collection_type: open
  name: Azure Policy REST Operations Policy Definitions API
  slug: open-microsoft-azure-policy-policy-definitions-api
- collection_type: open
  name: Azure Policy REST API
  slug: open-microsoft-azure-policy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-policy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-policy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-policy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-policy-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/governance/policy/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/azure-policy
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Policy is a service that enables you to create, assign, and manage policies that enforce rules and effects over your Azure resources. It helps with compliance, governance, and consistency by evaluating resources against business standards and reporting on their state.
finops:
- name: Microsoft Azure Policy Finops
  service_category: API
  slug: microsoft-azure-policy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-policy.png
layout: provider
modified: '2026-05-19'
name: Azure Policy
nav: Providers
network: true
overview: 'Azure Policy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Policy Definitions API. Tagged areas include Compliance, Governance, Policy, and Resource Management.


  Azure Policy''s developer surface includes authentication, developer portal, pricing, documentation, signup flow, support, and 9 more developer resources.'
plans:
- name: Microsoft Azure Policy Plans Pricing
  plan_count: 3
  slug: microsoft-azure-policy-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Microsoft Azure Policy Rate Limits
  slug: microsoft-azure-policy-rate-limits
scopes:
- name: Microsoft Azure Policy Scopes
  scope_count: 1
  slug: microsoft-azure-policy-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 43.4
  delta: 0.6
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 56.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-policy/refs/heads/main/screenshots/microsoft-azure-policy-2026-06-20T185431.png
security:
- kind: authentication
  name: Microsoft Azure Policy Authentication
  slug: microsoft-azure-policy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Policy Domain Security
  slug: microsoft-azure-policy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-policy
tags:
- Compliance
- Governance
- Policy
- Resource Management
website: https://azure.microsoft.com/en-us/products/azure-policy
---
