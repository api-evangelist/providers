---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Rubrik Agentic Access
  operation_count: 4
  slug: rubrik-agentic-access
  summary_line: 4 operations · 4 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Rubrik Security Cloud (RSC) API is a single-endpoint GraphQL API at /api/graphql that exposes the full RSC platform, including SLA domain management and assignment, on-demand backups, recovery ope
  name: Rubrik Security Cloud API
  slug: rubrik-security-cloud-api
- description: REST API exposed by on-premises Rubrik clusters (CDM) with v1, v2, and internal endpoints for managing protected objects, SLA domains, backup jobs, recovery, cluster configuration, events, and reports
  name: Rubrik Cluster API
  slug: rubrik-cluster-api
- description: Fully-supported PowerShell module for automating Rubrik Security Cloud using cmdlets that wrap the underlying GraphQL API.
  name: Rubrik PowerShell Module
  slug: rubrik-powershell-sdk
- description: Terraform provider for managing Rubrik Security Cloud (Polaris) resources as infrastructure-as-code.
  name: Rubrik Polaris Terraform Provider
  slug: rubrik-terraform-provider
- description: The Client Token API from Rubrik — 1 operation(s) for client token.
  name: Rubrik Client Token API
  slug: rubrik-client-token-api
- description: The Graphql API from Rubrik — 1 operation(s) for graphql.
  name: Rubrik Graphql API
  slug: rubrik-graphql-api
- description: The Oauth API from Rubrik — 1 operation(s) for oauth.
  name: Rubrik Oauth API
  slug: rubrik-oauth-api
- description: The Session API from Rubrik — 1 operation(s) for session.
  name: Rubrik Session API
  slug: rubrik-session-api
artifact_total: 16
collections:
- collection_type: open
  name: Rubrik Security Cloud API
  slug: open-rubrik
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/rubrikinc/rubrik-powershell-sdk/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rubrik-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rubrik-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rubrik-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rubrik.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.rubrik.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rubrik.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rubrikinc
- group: other
  title: ''
  type: APIPlayground
  url: https://developer.rubrik.com/Rubrik-Security-Cloud-API/API-playground/
- group: build
  title: ''
  type: SDKs
  url: https://developer.rubrik.com/SDKs-and-Tools/
- group: operate
  title: ''
  type: Support
  url: https://support.rubrik.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rubrik.com/blog
- group: other
  title: ''
  type: Customers
  url: https://www.rubrik.com/customers
- group: company
  title: ''
  type: Partners
  url: https://www.rubrik.com/partners
- group: company
  title: ''
  type: AboutUs
  url: https://www.rubrik.com/company
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.rubrik.com/
- group: company
  title: ''
  type: Careers
  url: https://www.rubrik.com/company/careers
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.rubrik.com/company/trust
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rubrik-inc/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.rubrik.com/llms.txt
created: '2026-05-23'
description: Rubrik is a Zero Trust data security company that protects enterprise, cloud, and SaaS data with backup, recovery, threat analytics, data security posture management, and cyber recovery workflows through Rubrik Security Cloud (RSC) and on-premises Rubrik clusters. Rubrik publishes a comprehensive developer program including the Rubrik Security Cloud GraphQL API at /api/graphql, the legacy Rubrik Cluster REST API (v1, v2, and internal endpoints), an interactive API Playground, a PowerShell module, a Terraform provider, and Postman collections through the Rubrik Developer Center at developer.rubrik.com.
finops:
- name: Rubrik Finops
  service_category: API
  slug: rubrik-finops
graphqls:
- description: The Rubrik Security Cloud (RSC) API is a single-endpoint GraphQL API at /api/graphql that exposes the full RSC platform, including SLA domain management and assignment, on-demand backups, recovery ope
  name: Rubrik GraphQL API
  slug: rubrik-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rubrik.png
layout: provider
modified: '2026-05-23'
name: Rubrik
nav: Providers
network: true
overview: 'Rubrik publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Client Token API, Graphql API, Oauth API, and 1 more. Tagged areas include Backup, Cyber Recovery, Data Security, Data Security Posture Management, and GraphQL.


  Rubrik''s developer surface includes authentication, documentation, support, engineering blog, and 16 more developer resources.'
plans:
- name: Rubrik Plans Pricing
  plan_count: 1
  slug: rubrik-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 2
  name: Rubrik Rate Limits
  slug: rubrik-rate-limits
score:
  band: thin
  composite: 41.0
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 59.0
    developer_ergonomics: 41.3
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rubrik/refs/heads/main/screenshots/rubrik-2026-06-20T193244.png
security:
- kind: authentication
  name: Rubrik Authentication
  slug: rubrik-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rubrik Domain Security
  slug: rubrik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rubrik
tags:
- Backup
- Cyber Recovery
- Data Security
- Data Security Posture Management
- GraphQL
- Ransomware Recovery
- REST API
- SaaS Protection
- Threat Analytics
- Zero Trust
website: https://www.rubrik.com/
---
