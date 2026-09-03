---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Model Context Protocol server that Code Biotherapeutics' corporate website exposes at https://www.codebiotx.com/_api/mcp. It is the Wix platform site MCP server, served from the company's own host
  name: Code Bio Site MCP Server
  slug: code-bio-site-mcp-server
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/code-biotherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codebiotx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.codebiotx.com/overview
- group: company
  title: ''
  type: Blog
  url: https://www.codebiotx.com/latest-news
- group: operate
  title: ''
  type: Support
  url: https://www.codebiotx.com/general-inquiries
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.codebiotx.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.codebiotx.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/code-biotherapeutics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/code-biotherapeutics-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/code-biotherapeutics-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/code-biotherapeutics-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/code-biotherapeutics
- group: company
  title: ''
  type: Twitter
  url: https://x.com/codebiotx
created: '2026-08-09'
description: Code Biotherapeutics (Code Bio) is a privately held genetic medicine company headquartered in Hatfield, Pennsylvania, developing targeted non-viral gene therapies for serious and life-threatening genetic diseases. Its proprietary 3DNA multivalent synthetic DNA delivery platform is engineered to address the dose-related toxicity, off-target effects, immunogenicity, cargo-size limits, bioavailability, re-dosing and manufacturing complexity that constrain viral vectors. The company advances an internal pipeline led by Duchenne Muscular Dystrophy and Type 1 Diabetes programs, with additional targeting research in lung, pancreas and liver, alongside partnership programs including a collaboration with Takeda. Code Bio is not a software vendor and publishes no developer program or REST/GraphQL API; its only machine-readable agent surface is the Wix-platform Model Context Protocol server and llms.txt served from its own corporate website host.
image: https://static.wixstatic.com/media/9d709e_2d584e2635c94c1ca0de7d62d7cda343~mv2.jpg/v1/fill/w_960,h_504,al_c/9d709e_2d584e2635c94c1ca0de7d62d7cda343~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Code Bio Site MCP Server
  slug: code-bio-site-mcp-server
modified: '2026-08-09'
name: Code Biotherapeutics
nav: Providers
network: true
overview: 'Code Biotherapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Genetic Medicine, Gene Therapy, and Life Sciences.


  Code Biotherapeutics'' developer surface includes documentation, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/code-biotherapeutics/refs/heads/main/screenshots/code-biotherapeutics-2026-09-02T145118.png
security:
- kind: authentication
  name: Code Biotherapeutics Authentication
  slug: code-biotherapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Code Biotherapeutics Domain Security
  slug: code-biotherapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: code-biotherapeutics
tags:
- Company
- Biotechnology
- Genetic Medicine
- Gene Therapy
- Life Sciences
- Pharmaceuticals
- Rare Disease
- Drug Discovery
website: https://www.codebiotx.com/
---
