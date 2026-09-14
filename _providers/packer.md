---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.packer.io/'', ''status'': 308, ''note'': ''declared website redirects to https://developer.hashicorp.com/packer — a different registrable domain (packer.io -> hashicorp.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Packer Agentic Access
  operation_count: 24
  slug: packer-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 1
apis:
- description: Open-source tool for creating identical machine images for multiple platforms from a single source configuration.
  name: Packer
  slug: packer
- baseURL: https://api.cloud.hashicorp.com
  baseurl_source: declared
  description: The PackerService API from Packer — 13 operation(s) for packerservice.
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
random_paper: 0
rate_limits:
- limit_count: 5
  name: Packer Rate Limits
  slug: packer-rate-limits
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
