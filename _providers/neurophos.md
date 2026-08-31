---
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A live, unauthenticated Model Context Protocol endpoint served from the neurophos.com host and advertised in the company's own llms.txt. It is provided by the Wix site platform rather than authored by
  name: Neurophos Site MCP
  slug: neurophos-site-mcp
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.neurophos.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/neurophos-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurophos-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neurophos-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neurophos-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neurophos-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neurophos-conformance.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Neurophos
- group: company
  title: ''
  type: News
  url: https://www.neurophos.com/resources/news
- group: company
  title: ''
  type: Careers
  url: https://www.neurophos.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.neurophos.com/contact
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/neurophos_stock/
created: '2026-08-04'
description: 'Neurophos is an Austin, Texas semiconductor company, spun out of Duke University in 2020, building photonic AI inference silicon. Its Optical Processing Unit (OPU) integrates over a million micron-scale dynamic optical metasurface modulators — technology descended from metamaterials research — onto a single chip, performing the matrix multiplications behind AI inference in light rather than electrons. The company markets the T100 OPU as a drop-in data-center alternative to GPUs, publishing chip and server configurations rated at 235 TOPS/W with HBM-backed memory, and lists Triton and JAX as supported software frameworks. Neurophos raised a $110M Series A in January 2026 led by Gates Frontier with M12, Carbon Direct, Aramco Ventures and Bosch Ventures. It sells hardware, not software services: there is no developer program, no public API and no SDK. The only machine-readable surfaces at its domain are an llms.txt and the Wix-platform site MCP endpoint that llms.txt advertises.'
image: https://static.wixstatic.com/media/79aa3c_0cf41cb45de44d92ab97f571e6d733ff~mv2.jpg/v1/fill/w_1942,h_931,al_c/79aa3c_0cf41cb45de44d92ab97f571e6d733ff~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Neurophos MCP Server
  slug: neurophos-mcp-server
modified: '2026-08-04'
name: Neurophos
nav: Providers
network: true
overview: 'Neurophos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, photonics, Optical Computing, ai-inference, and ai-accelerators.


  Neurophos'' developer surface includes authentication, product news, and 10 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 10.8
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neurophos/refs/heads/main/screenshots/neurophos-2026-08-07T185039.png
security:
- kind: authentication
  name: Neurophos Authentication
  slug: neurophos-authentication
  summary_line: none/bearer-token · 2 schemes
- kind: domain-security
  name: Neurophos Domain Security
  slug: neurophos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: neurophos
tags:
- Company
- photonics
- Optical Computing
- ai-inference
- ai-accelerators
- semiconductors
- Metamaterials
- data-center
- deep-tech
- MCP
website: https://www.neurophos.com/
---
