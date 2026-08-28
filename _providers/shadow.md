---
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Shadow GPU is Shadow's sovereign GPU cloud, delivered as a curated OpenStack 2024.1 deployment rather than a bespoke REST API. Every programmatic action — launching NVIDIA RTX 2000 Ada or RTX A4500 GP
  name: Shadow GPU (OpenStack API)
  slug: shadow-gpu-openstack
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shadow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shadow.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://gpu-instances.shadow.tech/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://gpu-instances.shadow.tech/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://support.shadow.tech/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://shadow.tech/us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://gpu-instances.shadow.tech/en/#pricing
- group: start
  title: ''
  type: Login
  url: https://pc.shadow.tech/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shadow.tech/us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shadow.tech/us/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shadow.tech/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shadow-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shadow-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shadow-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shadow-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/shadow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shadow-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/shadow-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shadow-llms.txt
created: '2026-08-17'
description: 'Shadow is a French cloud computing company founded in 2015, launched commercially in 2016, and chaired by OVHcloud founder Octave Klaba. It streams complete high-end Windows desktops (Shadow PC, Shadow PC Pro), sells Nextcloud-based storage as Shadow Drive, and sells sovereign GPU compute as Shadow GPU — an OpenStack 2024.1 platform running across seven regions in France, Germany, the United States and Canada. Shadow GPU is programmable only through the standard OpenStack API: a Keystone v3.14 identity endpoint answers anonymously at https://auth.<region>.os.shadow.tech/v3, fronting Nova (compute), Neutron and Octavia (networking / load balancing), Designate (DNS), Cinder and Glance (storage and images), Placement, Barbican (secrets), CloudKitty (rating) and the Skyline / Horizon dashboards, driven with the upstream openstack CLI, Terraform, Ansible, Pulumi or Cluster API. Shadow publishes no OpenAPI, AsyncAPI, first-party SDK, MCP server or A2A agent card of its own.'
image: https://gpu-instances.shadow.tech/assets/images/vignette.png
layout: provider
modified: '2026-08-17'
name: Shadow
nav: Providers
network: true
overview: 'Shadow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Computing, GPU, Cloud Gaming, and Infrastructure.


  Shadow''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, authentication, and 13 more developer resources.'
plans:
- name: Shadow Plans Pricing
  plan_count: 3
  slug: shadow-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Shadow Rate Limits
  slug: shadow-rate-limits
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 34.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Shadow Authentication
  slug: shadow-authentication
  summary_line: keystone-password/keystone-application-credential · 2 schemes
- kind: domain-security
  name: Shadow Domain Security
  slug: shadow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shadow
tags:
- Company
- Cloud Computing
- GPU
- Cloud Gaming
- Infrastructure
- OpenStack
- AI Infrastructure
- Compute
- Storage
- Europe
website: https://shadow.tech/
---
