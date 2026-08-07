---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 78
  human_in_the_loop: 0
  name: Enveda Biosciences Agentic Access
  operation_count: 115
  slug: enveda-biosciences-agentic-access
  summary_line: 115 operations · 78 acting
api_count: 2
apis:
- description: The anonymously readable WordPress REST API that enveda.com serves at /wp-json/wp/v2 — news releases (the `news` custom post type, 34 published), In-Veda blog posts, marketing and clinical-trial recru
  name: Enveda Content API (WordPress REST wp/v2)
  slug: content
- description: A Model Context Protocol server endpoint advertised in the enveda.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The endpoint is live b
  name: Enveda MCP Server (WordPress MCP Adapter)
  slug: mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://enveda.com/
- group: company
  title: ''
  type: About
  url: https://enveda.com/purpose/
- group: company
  title: ''
  type: Blog
  url: https://enveda.com/in-veda/
- group: company
  title: ''
  type: BlogRSS
  url: https://enveda.com/feed/
- group: company
  title: ''
  type: News
  url: https://enveda.com/news/
- group: company
  title: ''
  type: Press
  url: https://enveda.com/press/
- group: operate
  title: ''
  type: Support
  url: https://enveda.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://enveda.com/careers/
- group: other
  title: ''
  type: Team
  url: https://enveda.com/people/
- group: other
  title: ''
  type: Technology
  url: https://enveda.com/platform/
- group: other
  title: ''
  type: Pipeline
  url: https://enveda.com/pipeline/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enveda.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enveda.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enveda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envedabio
- group: build
  title: ''
  type: Packages
  url: packages/enveda-biosciences-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enveda-biosciences-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enveda-biosciences-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enveda-biosciences-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enveda-biosciences-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enveda-biosciences-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enveda-biosciences-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enveda-biosciences-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/enveda-biosciences-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/enveda-biosciences_stock/
created: '2026-08-04'
description: Enveda (Enveda Biosciences) is a Boulder, Colorado based clinical-stage biotechnology company founded in 2019 that discovers medicines by decoding the chemistry of the natural world. It combines high-throughput mass spectrometry, metabolomics, robotics and machine learning — including PRISM, a foundation model trained on more than a billion small- molecule mass spectra — to build a searchable library of plant-derived molecules and translate them into drug candidates. Enveda has raised over $360M across Series B, C and D rounds from Premji Invest, Kinnevik, Lux Capital, Dimension and Sanofi, reached unicorn status in 2026, and runs FDA-cleared clinical programs including ENV-294 (atopic dermatitis and asthma), ENV-308 (obesity) and ENV-6946 (inflammatory bowel disease). Enveda publishes no product or developer API; the machine-readable surface on enveda.com is a published llms.txt plus the WordPress REST API (wp/v2) that serves the company newsroom, In-Veda blog, leadership profiles,
  clinical-trial site directory and media library as JSON, alongside a WordPress MCP Adapter endpoint that is present but authentication-gated. Its open science is published as research code and data in the github.com/enveda organization.
image: https://enveda.com/wp-content/uploads/2026/06/cropped-enveda-favicon.jpg
layout: provider
mcp_servers:
- description: ''
  name: enveda-biosciences-mcp.yml
  slug: enveda-biosciences-mcpyml
modified: '2026-08-04'
name: Enveda
nav: Providers
network: true
overview: 'Enveda publishes 1 API on the [APIs.io](https://apis.io/) network: Content API (WordPress REST wp/v2). Tagged areas include Company, Biotechnology, Drug Discovery, Life Sciences, and Artificial Intelligence.


  Enveda''s developer surface includes engineering blog, product news, support, authentication, and 22 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 15.1
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 23.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Enveda Biosciences Authentication
  slug: enveda-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Enveda Biosciences Domain Security
  slug: enveda-biosciences-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: enveda-biosciences
tags:
- Company
- Biotechnology
- Drug Discovery
- Life Sciences
- Artificial Intelligence
- Machine Learning
- Metabolomics
- Natural Products
- Pharmaceuticals
- Clinical Trials
- Research
- Content
website: https://enveda.com/
---
