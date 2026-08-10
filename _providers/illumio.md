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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Illumio Policy Compute Engine (PCE) REST API for managing Zero Trust Segmentation — workloads, labels, label groups, security policy, rulesets, IP lists, services, virtual services, enforcement bo
  name: Illumio Core PCE REST API
  slug: illumio-core-pce-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://illumio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.illumio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.illumio.com/core/
- group: docs
  title: ''
  type: APIReference
  url: https://product-docs-repo.illumio.com/Tech-Docs/Core/24.4/REST-APIs/out/en/index-en.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/illumio
- group: company
  title: ''
  type: Blog
  url: https://www.illumio.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.illumio.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.illumio.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/illumio-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.illumio.com/products/pricing
- group: start
  title: ''
  type: SignUp
  url: https://login.illum.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.illumio.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.illumio.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/illumio-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/illumio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/illumio-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/illumio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/illumio-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/illumio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/illumio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/illumio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/illumio-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/illumio-llms.txt
created: '2026-07-17'
description: Illumio is a Zero Trust Segmentation (microsegmentation) cybersecurity company whose platform stops the lateral spread of ransomware and breaches across data centers, cloud, and endpoints. Its Policy Compute Engine (PCE) exposes a REST API (base path /api/v2) for programmatically managing workloads, labels, security policy, rulesets, IP lists, virtual services, enforcement boundaries, and for querying traffic/flow (Illumination) data. Products include Illumio Core for host-based data center and cloud workload segmentation, Illumio CloudSecure for agentless public-cloud segmentation, and Illumio Endpoint. The API is authenticated with an organization-scoped API key (key ID + secret over HTTP Basic) and is accompanied by an official Python REST client, Terraform providers for Illumio Core and CloudSecure, and a certified Ansible collection.
image: https://www.illumio.com/hubfs/Illumio_Logo.svg
layout: provider
modified: '2026-07-19'
name: Illumio
nav: Providers
network: true
overview: 'Illumio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Zero Trust, and Microsegmentation.


  Illumio''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 67
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 34.5
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/illumio/refs/heads/main/screenshots/illumio-2026-07-25T222113.png
security:
- kind: authentication
  name: Illumio Authentication
  slug: illumio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Illumio Domain Security
  slug: illumio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Illumio Trust Center
  slug: illumio-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, FIPS 140
slug: illumio
tags:
- Company
- Security
- Cybersecurity
- Zero Trust
- Microsegmentation
- Cloud Security
- Networking
- Workload Protection
- Ransomware
- Endpoint Security
website: https://illumio.com
---
