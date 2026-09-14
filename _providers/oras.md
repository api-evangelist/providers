---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 2
apis:
- description: Generic command-line registry client used to push and pull OCI artifacts to and from any OCI-compliant container registry.
  name: ORAS CLI
  slug: cli
- description: Client libraries for building custom OCI artifact tools and integrations on top of ORAS, available across multiple language ecosystems including Go, Rust, Python, JavaScript, .NET, and Java.
  name: ORAS Client Libraries
  slug: client-libraries
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oras-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oras.land/
- group: docs
  title: ''
  type: Documentation
  url: https://oras.land/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oras-project
- group: operate
  title: ''
  type: Community
  url: https://oras.land/community/
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/oras/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/oras-project/oras-mcp
- group: company
  title: ''
  type: Blog
  url: https://oras.land/blog/atom.xml
created: '2026-03-16'
description: ORAS (OCI Registry As Storage) is a CNCF project that provides a CLI and a set of client libraries for pushing and pulling arbitrary OCI artifacts to and from OCI-compliant registries, allowing container registries to be used as a generic artifact distribution mechanism.
finops:
- name: Oras Finops
  service_category: API
  slug: oras-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oras.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: ORAS
nav: Providers
network: true
overview: 'ORAS publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artifact Storage, Cloud-Native, Container Registry, and OCI.


  ORAS''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Oras Plans Pricing
  plan_count: 3
  slug: oras-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Oras Rate Limits
  slug: oras-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/oras/refs/heads/main/screenshots/oras-2026-06-20T191150.png
security:
- kind: domain-security
  name: Oras Domain Security
  slug: oras-domain-security
  summary_line: TLSv1.3 · HSTS
slug: oras
tags:
- Artifact Storage
- Cloud-Native
- Container Registry
- OCI
website: https://oras.land/
---
