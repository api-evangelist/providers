---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.4
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gigaio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gigaio.com/
- group: operate
  title: ''
  type: Support
  url: https://gigaio.com/support/
- group: start
  title: ''
  type: Login
  url: https://gigaio.com/sign-in-to-gigaio-support/
- group: company
  title: ''
  type: Blog
  url: https://gigaio.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gigaio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gigaio.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gigaio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gigaio-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gigaio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gigaio-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gigaio-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gigaio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gigaio-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gigaio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gigaio-rate-limits.yml
- group: build
  title: ''
  type: CLI
  url: cli/gigaio-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gigaio-llms.txt
created: '2026-08-21'
description: GigaIO is a Carlsbad, California hardware and software company building datacenter-class computing for the edge. Its current product line is Gryf, a carry-on suitcase-sized, ruggedized, field-serviceable AI supercomputer built from hot-swappable Accelerator, Compute, Network and Storage sleds, plus Manticore for larger deployments. The company was founded around FabreX, a PCIe/CXL-based composable memory fabric that disaggregates GPUs, FPGAs, NVMe and DRAM into dynamically composed clusters and is managed with DMTF Redfish RESTful APIs and a FabreX CLI that integrates with Ansible, Chef, Puppet, Slurm, OpenPBS, LSF and Kubernetes. In April 2026 GigaIO sold its datacenter technology and assets — including SuperNODE and FabreX — to d-Matrix, and refocused the company on edge AI inferencing. GigaIO publishes no public developer portal, API reference or machine-readable specification; the API documentation and knowledge base sit behind its Atlassian-hosted customer support portal.
  It does run a remote Model Context Protocol server on gigaio.com, protected by OAuth 2.0 with PKCE.
image: https://gigaio.com/wp-content/uploads/2020/09/logo.svg
layout: provider
mcp_servers:
- description: GigaIO runs a remote Model Context Protocol server on its own domain at https://gigaio.com/wp-json/mcp/mcp-oauth-server, advertised through an RFC 9728 protected-resource document and backed by an RFC
  name: GigaIO MCP Server
  slug: gigaio-mcp-server
modified: '2026-08-21'
name: GigaIO
nav: Providers
network: true
overview: 'GigaIO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Composable Infrastructure, Edge Computing, Artificial Intelligence, and High Performance Computing.


  GigaIO''s developer surface includes support, engineering blog, authentication, CLI, and 14 more developer resources.'
plans:
- name: Gigaio Plans Pricing
  plan_count: 0
  slug: gigaio-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Gigaio Rate Limits
  slug: gigaio-rate-limits
scopes:
- name: Gigaio Scopes
  scope_count: 0
  slug: gigaio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 61.1
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Gigaio Authentication
  slug: gigaio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gigaio Domain Security
  slug: gigaio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gigaio
tags:
- Company
- Composable Infrastructure
- Edge Computing
- Artificial Intelligence
- High Performance Computing
- Data Center
- Hardware
- GPU
- PCIe
- Infrastructure as Code
website: https://gigaio.com/
---
