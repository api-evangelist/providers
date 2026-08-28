---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The public, anonymously-readable WordPress REST content API served by inflammatix.com. Alongside the standard WordPress collections (posts, pages, media, categories, tags, comments, search) it exposes
  name: Inflammatix Site Content API
  slug: site-content
- description: The public, anonymously-readable WordPress REST content API served by support.inflammatix.com, the Inflammatix customer support and TriVerity/Myrna operator-training portal. In addition to the standar
  name: Inflammatix Support and Training Content API
  slug: support-content
artifact_total: 7
collections:
- collection_type: open
  name: Inflammatix Site Content API (WordPress REST)
  slug: open-inflammatix-content
- collection_type: open
  name: Inflammatix Support & Training Content API (WordPress REST)
  slug: open-inflammatix-support-content
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inflammatix-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://inflammatix.com/
- group: operate
  title: ''
  type: Support
  url: https://support.inflammatix.com/
- group: start
  title: ''
  type: Login
  url: https://support.inflammatix.com/login/
- group: company
  title: ''
  type: Blog
  url: https://inflammatix.com/newsroom/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://inflammatix.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://inflammatix.com/newsroom/press-releases/
- group: operate
  title: ''
  type: Roadmap
  url: https://inflammatix.com/pipeline/
- group: auth
  title: ''
  type: Compliance
  url: https://inflammatix.com/about-us/
- group: other
  title: ''
  type: Patents
  url: https://inflammatix.com/patents/
- group: other
  title: ''
  type: Research
  url: https://inflammatix.com/evidence/
- group: company
  title: ''
  type: Careers
  url: https://inflammatix.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://inflammatix.com/contact-inflammatix/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inflammatix.com/privacy-and-cookies-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inflammatix.com/terms-and-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inflammatix/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/inflammatix_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/inflammatix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inflammatix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inflammatix-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inflammatix-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inflammatix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inflammatix-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inflammatix-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inflammatix-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Inflammatix is a molecular diagnostics company headquartered in Sunnyvale, California that reads the patient's own immune response to speed up decisions in emergency and critical care. Its FDA-cleared TriVerity Test System measures a 29-mRNA host-response panel from whole blood on the benchtop Myrna instrument using RT-LAMP, returning three machine-learning-derived scores — bacterial infection likelihood, viral infection likelihood, and risk of severe illness within seven days — in about 30 minutes, with under a minute of no-prep sample handling. The company was co-founded out of Stanford by Tim Sweeney and Purvesh Khatri, is backed by Khosla Ventures, Northpond Ventures, Think.Health Ventures, Iberis Capital, OSF HealthCare and Vesalius BioCapital plus federal funding from NIH, BARDA, DRIVe and DARPA, and holds ISO 13485:2016 certification and a State of California medical device manufacturing license. Inflammatix publishes no developer API for its clinical products; the Myrna
  instrument advertises "multiple LIS connectivity options" and remote notification, but no public interface specification. The machine-readable surfaces it does serve are the WordPress REST content APIs behind inflammatix.com and its customer support/training portal, which expose the company's peer-reviewed publication library and the TriVerity/Myrna course catalogue as JSON.
image: https://inflammatix.com/wp-content/uploads/2025/05/logo-revdark-850-1024x242.webp
layout: provider
mcp_servers:
- description: ''
  name: Inflammatix MCP Server
  slug: inflammatix-mcp-server
modified: '2026-08-01'
name: Inflammatix
nav: Providers
network: true
overview: 'Inflammatix publishes 2 APIs on the [APIs.io](https://apis.io/) network: Site Content API and Support and Training Content API. Tagged areas include Company, Health, Healthcare, Diagnostics, and Medical Devices.


  Inflammatix''s developer surface includes support, engineering blog, authentication, and 23 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 39.9
  delta: 0.9
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 58.5
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 30.3
    operational_transparency: 5.3
  previous_composite: 39.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inflammatix/refs/heads/main/screenshots/inflammatix-2026-08-07T170701.png
security:
- kind: authentication
  name: Inflammatix Authentication
  slug: inflammatix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inflammatix Domain Security
  slug: inflammatix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inflammatix
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Medical Devices
- In Vitro Diagnostics
- Molecular Diagnostics
- Sepsis
- Machine-Learning
- Life Sciences
- Point of Care
- Content
website: https://inflammatix.com/
---
