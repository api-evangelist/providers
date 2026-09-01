---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 8.6
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.mana.bio/
- group: company
  title: ''
  type: Blog
  url: https://www.mana.bio/news
- group: other
  title: ''
  type: Publications
  url: https://www.mana.bio/publications
- group: company
  title: ''
  type: Jobs
  url: https://www.mana.bio/jobs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/manabio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/manabio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manabio-domain-security.yml
created: '2026-07-17'
description: Mana.bio is an AI-driven drug-delivery biotechnology company specializing in programmable lipid nanoparticles (LNPs) for nucleic-acid therapeutics and vaccines, including mRNA, DNA, and CRISPR-based gene therapy. The company runs a closed-loop design-build-test-learn platform that uses machine-learning models to design novel LNP candidates, synthesizes dozens of formulations weekly via high-throughput automation, screens them with comprehensive assays, and feeds results back to continuously improve its models — targeting precise, optimized extrahepatic delivery. Mana.bio also operates Mina (ChatLNP), an AI agent that helps scientists explore curated literature, predict LNP properties, and optimize formulations, plus an LNP patents / freedom-to-operate map. The company is backed by a16z. Mana.bio publishes no first-party developer or product API; its only public agent surface is a Wix Site MCP endpoint and an llms.txt on its site.
image: https://static.wixstatic.com/media/d7e63b_1d6eb702d51a4cdaad0396e94610de66~mv2.jpg/v1/fit/w_2500,h_1330,al_c/d7e63b_1d6eb702d51a4cdaad0396e94610de66~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Mana.bio Site MCP
  slug: manabio-site-mcp
modified: '2026-07-20'
name: Mana.bio
nav: Providers
network: true
overview: 'Mana.bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Drug Delivery, Lipid Nanoparticles, and Gene Therapy.


  Mana.bio''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manabio/refs/heads/main/screenshots/manabio-2026-07-25T230017.png
security:
- kind: domain-security
  name: Manabio Domain Security
  slug: manabio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: manabio
tags:
- Company
- Biotechnology
- Drug Delivery
- Lipid Nanoparticles
- Gene Therapy
- Artificial Intelligence
- Machine-Learning
- Genetic Medicine
- mRNA
website: https://www.mana.bio/
---
