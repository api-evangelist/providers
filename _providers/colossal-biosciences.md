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
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Colossal Biosciences Agentic Access
  operation_count: 67
  slug: colossal-biosciences-agentic-access
  summary_line: 67 operations · 44 acting
api_count: 2
apis:
- description: The anonymously readable WordPress REST API that colossal.com serves at /wp-json/wp/v2 — newsroom posts, marketing pages, the media library, categories, tags, comments, users and a site-wide search en
  name: Colossal Biosciences Content API (WordPress REST wp/v2)
  slug: content
- description: A Model Context Protocol server endpoint advertised in the colossal.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The endpoint is live
  name: Colossal Biosciences MCP Server (WordPress MCP Adapter)
  slug: mcp
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/colossal-biosciences-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/colossal-biosciences-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/colossal-biosciences-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://colossal.com/
- group: company
  title: ''
  type: About
  url: https://colossal.com/company/
- group: company
  title: ''
  type: Blog
  url: https://colossal.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://colossal.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://colossal.com/newsletter/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://colossal.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://colossal.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://colossal.com/careers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/colossal-compsci
- group: other
  title: ''
  type: Technology
  url: https://colossal.com/technology/
- group: other
  title: ''
  type: Research
  url: https://colossal.com/labs/
- group: other
  title: ''
  type: Podcast
  url: https://colossal.com/podcast/
- group: other
  title: ''
  type: Foundation
  url: https://colossalfoundation.org/
- group: build
  title: ''
  type: Packages
  url: packages/colossal-biosciences-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/colossal-biosciences-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/colossal-biosciences-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/colossal-biosciences-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/colossal-biosciences-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Colossal Biosciences is a Dallas, Texas based de-extinction and species-preservation biotechnology company founded in 2021 by Ben Lamm and Harvard geneticist George Church. It applies ancient-DNA sequencing, comparative genomics, CRISPR multiplex genome editing, cloning and artificial-womb research to restoring extinct keystone species — the woolly mammoth, thylacine, dodo, moa, dire wolf and blue buck among them — and to conserving critically endangered living species. Colossal spun out the computational life-sciences platform Form Bio, runs the non-profit Colossal Foundation, and publishes its research code through the colossal-compsci GitHub organization. Colossal publishes no product or developer API; the machine-readable surface on colossal.com is the WordPress REST API (wp/v2) that serves the company newsroom, pages, media and site search as JSON, plus a WordPress MCP Adapter endpoint that is present but authentication-gated.
image: https://colossal.com/wp-content/uploads/Colossal_BrandingRegistered_Logo_Icon_RGB_Wht-1.png
layout: provider
mcp_servers:
- description: ''
  name: colossal-biosciences-mcp.yml
  slug: colossal-biosciences-mcpyml
modified: '2026-08-04'
name: Colossal Biosciences
nav: Providers
network: true
overview: 'Colossal Biosciences publishes 1 API on the [APIs.io](https://apis.io/) network: Content API (WordPress REST wp/v2). Tagged areas include Company, Biotechnology, Genomics, Life Sciences, and Conservation.


  Colossal Biosciences'' developer surface includes authentication, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 34
score:
  band: emerging
  composite: 25.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 15.1
    developer_ergonomics: 14.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 25.4
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
  name: Colossal Biosciences Authentication
  slug: colossal-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Colossal Biosciences Domain Security
  slug: colossal-biosciences-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: colossal-biosciences
tags:
- Company
- Biotechnology
- Genomics
- Life Sciences
- Conservation
- De-Extinction
- Synthetic Biology
- Research
- Content
website: https://colossal.com/
---
