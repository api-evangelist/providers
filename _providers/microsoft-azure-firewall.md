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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Firewall Agentic Access
  operation_count: 7
  slug: microsoft-azure-firewall-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Firewalls operations
  name: Azure Firewall Firewalls API
  slug: microsoft-azure-firewall-firewalls-api
- description: Operations operations
  name: Azure Firewall Operations API
  slug: microsoft-azure-firewall-operations-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Firewall REST Firewalls API
  slug: open-microsoft-azure-firewall-firewalls-api
- collection_type: open
  name: Azure Firewall REST Firewalls Operations API
  slug: open-microsoft-azure-firewall-operations-api
- collection_type: open
  name: Azure Firewall REST API
  slug: open-microsoft-azure-firewall
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-firewall-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-firewall-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-firewall-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-firewall-scopes.yml
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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Firewall is a managed cloud-based network security service that protects your Azure Virtual Network resources. The REST API supports configuring network rules, application rules, NAT rules, and DNS proxy settings, with built-in high availability, unrestricted cloud scalability, and threat intelligence-based filtering.
finops:
- name: Microsoft Azure Firewall Finops
  service_category: API
  slug: microsoft-azure-firewall-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-firewall.png
layout: provider
modified: '2026-05-19'
name: Azure Firewall
nav: Providers
network: true
overview: 'Azure Firewall publishes 2 APIs on the [APIs.io](https://apis.io/) network: Firewalls API and Operations API. Tagged areas include Cloud Security, Firewall, Network Security, and Threat Protection.


  Azure Firewall''s developer surface includes authentication, developer portal, pricing, support, and 7 more developer resources.'
plans:
- name: Microsoft Azure Firewall Plans Pricing
  plan_count: 3
  slug: microsoft-azure-firewall-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Microsoft Azure Firewall Rate Limits
  slug: microsoft-azure-firewall-rate-limits
scopes:
- name: Microsoft Azure Firewall Scopes
  scope_count: 1
  slug: microsoft-azure-firewall-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-firewall/refs/heads/main/screenshots/microsoft-azure-firewall-2026-06-20T185416.png
security:
- kind: authentication
  name: Microsoft Azure Firewall Authentication
  slug: microsoft-azure-firewall-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Firewall Domain Security
  slug: microsoft-azure-firewall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-firewall
tags:
- Cloud Security
- Firewall
- Network Security
- Threat Protection
website: https://portal.azure.com/
---
