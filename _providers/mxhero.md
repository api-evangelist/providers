---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: AI email knowledge-recovery service. Captured company email is optimized and stored in an isolated per-tenant vector database, then exposed to AI agents through an official MCP server (email_search to
  name: mxHERO Mail2Cloud Advanced (AI Email Knowledge)
  slug: mxhero-mail2cloud-advanced-ai-email-knowledge
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mxhero.com
- group: other
  title: ''
  type: Products
  url: https://www.mxhero.com/products
- group: docs
  title: ''
  type: Documentation
  url: https://mxhero.helpjuice.com/en_US/mxhero-ai
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.mxhero.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://web-new.mxhero.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www2.mxhero.com/products-pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mxhero.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mxhero.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mxaiorg
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mxhero-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/mxhero-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mxhero-authentication.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mxhero-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mxhero-domain-security.yml
created: '2026-07-17'
description: 'mxHERO Inc. is the pioneer of email-to-cloud content management, based in San Francisco and a long-time Box partner. Its Mail2Cloud platform is a bridge that intelligently captures email and attachments (in-flight or at-rest) over SMTP/S and IMAP/S and routes them, bi-directionally, into cloud content platforms such as Box, Egnyte, Microsoft OneDrive, Google Drive, and Dropbox — without retaining the content itself. Mail2Cloud Advanced adds an AI email-knowledge layer: captured email is deduplicated, metadata-preserved, and stored in an isolated per-tenant vector database that an official Model Context Protocol (MCP) server exposes to AI agents for secure email search and knowledge recovery, with a V3 REST API for dataset and S/MIME management.'
image: https://mxhero.com/wp-content/uploads/2021/03/mxhero-logo.png
layout: provider
mcp_servers:
- description: Official mxHERO Mail2Cloud Advanced MCP server. Provides AI agents with secure, multi-account email search and knowledge recovery over a company's captured email data, stored in an isolated per-tenant
  name: mxHero MCP Server
  slug: mxhero-mcp-server
modified: '2026-07-20'
name: mxHero
nav: Providers
network: true
overview: 'mxHero publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Cloud Storage, Content Management, and Email to Cloud.


  mxHero''s developer surface includes documentation, engineering blog, pricing, authentication, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.9
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mxhero/refs/heads/main/screenshots/mxhero-2026-08-07T184502.png
security:
- kind: authentication
  name: Mxhero Authentication
  slug: mxhero-authentication
  summary_line: token/apiKey · 2 schemes
- kind: domain-security
  name: Mxhero Domain Security
  slug: mxhero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mxhero
tags:
- Company
- Email
- Cloud Storage
- Content Management
- Email to Cloud
- Artificial Intelligence
- MCP
- Email Search
- Compliance
- Collaboration
website: https://mxhero.com
---
