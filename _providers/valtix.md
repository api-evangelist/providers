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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Valtix Alerts Webhooks
  slug: valtix-alerts-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valtix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.valtix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.valtix.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.valtix.com/tutorials/overview
- group: operate
  title: ''
  type: Support
  url: https://docs.valtix.com/faq/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valtix-security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.valtix.com/releases/overview/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/valtix-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valtix-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/valtix-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valtix-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/valtix-alerts-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valtix-llms.txt
created: '2026-07-17'
description: Valtix is a multicloud network security platform delivering agentless, cloud-native firewalling — ingress WAF/IDS/IPS, egress TLS decryption and exfiltration prevention, and east-west inspection — across AWS, Azure, GCP, and OCI, driven by continuous cloud asset discovery and tag-based dynamic policy. Founded in 2018 and acquired by Cisco in 2023, the product is sold today as Cisco Multicloud Defense; the Valtix documentation site and the verified Terraform provider (valtix-security/valtix) remain live and actively maintained under the Valtix name, while the standalone website and commercial pages redirect to Cisco.
image: https://avatars.githubusercontent.com/valtix-security
layout: provider
modified: '2026-07-21'
name: Valtix
nav: Providers
network: true
overview: 'Valtix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, Network Security, and Multicloud.


  The Valtix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Valtix''s developer surface includes documentation, getting-started guide, support, changelog, authentication, and 8 more developer resources.'
random_paper: 94
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 30.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Valtix Authentication
  slug: valtix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Valtix Domain Security
  slug: valtix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: valtix
tags:
- Company
- Security
- Cloud Security
- Network Security
- Multicloud
- Firewall
- Terraform
website: https://www.valtix.com
---
