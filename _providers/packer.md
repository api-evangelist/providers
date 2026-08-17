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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Packer Agentic Access
  operation_count: 24
  slug: packer-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 2
apis:
- description: Open-source tool for creating identical machine images for multiple platforms from a single source configuration.
  name: Packer
  slug: packer
- description: The PackerService API from Packer — 13 operation(s) for packerservice.
  name: Packer PackerService API
  slug: packer-packerservice-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Cloud Platform Packer Artifact Registry PackerService API
  slug: open-packer-packerservice-api
- collection_type: open
  name: HashiCorp Cloud Platform Packer Artifact Registry
  slug: open-packer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/packer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/packer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.packer.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/packer/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp/packer
- group: operate
  title: ''
  type: Community
  url: https://discuss.hashicorp.com/c/packer
created: '2026-03-16'
description: Packer is an open-source tool by HashiCorp for creating identical machine images for multiple platforms from a single source configuration. It automates the creation of pre-configured virtual machine and container images. HCP Packer adds a hosted artifact registry with a REST API for tracking image metadata, versions, channels, and security signals.
finops:
- name: Packer Finops
  service_category: API
  slug: packer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/packer.png
layout: provider
modified: '2026-05-19'
name: Packer
nav: Providers
network: true
overview: 'Packer publishes 1 API on the [APIs.io](https://apis.io/) network: PackerService API. Tagged areas include Automation, DevOps, HashiCorp, Image Building, and Infrastructure as Code.


  Packer''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Packer Plans Pricing
  plan_count: 3
  slug: packer-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Packer Rate Limits
  slug: packer-rate-limits
score:
  band: emerging
  composite: 27.2
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 46.3
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 27.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packer/refs/heads/main/screenshots/packer-2026-06-20T191313.png
security:
- kind: authentication
  name: Packer Authentication
  slug: packer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Packer Domain Security
  slug: packer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: packer
tags:
- Automation
- DevOps
- HashiCorp
- Image Building
- Infrastructure as Code
website: https://www.packer.io/
---
