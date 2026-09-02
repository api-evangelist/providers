---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
  score: 18.0
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Orca Security's REST API provides programmatic access to the Orca Cloud Security Platform for querying cloud inventory and assets, managing alerts and risk findings, configuring integrations and autom
  name: Orca Security REST API
  slug: orca-security-rest-api
- description: SCIM 2.0 endpoint for provisioning and de-provisioning users and groups in Orca Security from identity providers such as Okta, Azure AD, and OneLogin.
  name: Orca Security SCIM 2.0 API
  slug: orca-security-scim-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orca-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orca-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orca.security/
- group: other
  title: ''
  type: Platform
  url: https://orca.security/platform/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orcasecurity.io/
- group: start
  title: ''
  type: Login
  url: https://app.orcasecurity.io/
- group: other
  title: ''
  type: RegionSelection
  url: https://region-selection.orcasecurity.io/
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/orcasecurity/orcasecurity/latest
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.orca.security/
- group: company
  title: ''
  type: Blog
  url: https://orca.security/resources/blog/
- group: other
  title: ''
  type: Resources
  url: https://orca.security/resources/
- group: other
  title: ''
  type: Customers
  url: https://orca.security/customers/
- group: company
  title: ''
  type: Partners
  url: https://orca.security/partners/
- group: company
  title: ''
  type: Careers
  url: https://orca.security/company/careers/
- group: company
  title: ''
  type: AboutUs
  url: https://orca.security/company/
- group: operate
  title: ''
  type: ContactSales
  url: https://orca.security/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orca-security/
created: '2026-05-23'
description: Orca Security is an agentless cloud security platform that uses its patented SideScanning technology to provide visibility into risks across AWS, Azure, Google Cloud, Oracle Cloud, Kubernetes, and serverless environments, covering CSPM, CWPP, CIEM, DSPM, vulnerability management, malware detection, API security, and AI security in a single platform. Orca exposes a region-aware REST API for assets, alerts, integrations, automations, and user management, plus SCIM 2.0 for identity provisioning and a Terraform provider for infrastructure-as-code workflows.
finops:
- name: Orca Security Finops
  service_category: API
  slug: orca-security-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Orca Security cloud security platform. Orca Security exposes a REST API for its Cloud Native Application Protection Platform (CNAPP), cove
  name: Orca Security GraphQL Schema
  slug: orca-security-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orca-security.png
layout: provider
modified: '2026-05-23'
name: Orca Security
nav: Providers
network: true
overview: 'Orca Security publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agentless, API Security, CIEM, Cloud Security, and CNAPP.


  Orca Security''s developer surface includes documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Orca Security Plans Pricing
  plan_count: 1
  slug: orca-security-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Orca Security Rate Limits
  slug: orca-security-rate-limits
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 2.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orca-security/refs/heads/main/screenshots/orca-security-2026-06-20T191207.png
security:
- kind: domain-security
  name: Orca Security Domain Security
  slug: orca-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orca Security Vulnerability Disclosure
  slug: orca-security-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: orca-security
tags:
- Agentless
- API Security
- CIEM
- Cloud Security
- CNAPP
- CSPM
- CWPP
- DSPM
- SideScanning
- Vulnerability Management
website: https://orca.security/
---
