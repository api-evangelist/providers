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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.7
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Public REST API for the Wordsmith legal AI platform. Lets developers ask questions of Wordsmith Assistants with optional file attachments, poll question status, list available assistants, generate pre
  name: Wordsmith Platform API
  slug: platform-api
- description: Model Context Protocol server that exposes Wordsmith Assistants, Playbooks, and Templates to MCP-aware clients (Claude, agent frameworks, IDEs) so legal context can be pulled into AI workflows without
  name: Wordsmith MCP Server
  slug: mcp-server
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wordsmith-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.wordsmith.ai/blog
- group: company
  title: ''
  type: Website
  url: https://www.wordsmith.ai
- group: other
  title: ''
  type: Application
  url: https://app.wordsmith.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://wordsmithai.mintlify.app/
- group: docs
  title: ''
  type: APIReference
  url: https://wordsmithai.mintlify.app/api-reference/user/get-me
- group: auth
  title: ''
  type: Authentication
  url: https://wordsmithai.mintlify.app/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://wordsmithai.mintlify.app/quickstart
- group: design
  title: ''
  type: Webhooks
  url: https://wordsmithai.mintlify.app/webhooks
- group: design
  title: ''
  type: ErrorCodes
  url: https://wordsmithai.mintlify.app/errors
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wordsmith.ai/pricing
- group: commercial
  title: ''
  type: PricingAU
  url: https://www.wordsmith.ai/au/pricing
- group: other
  title: ''
  type: ROI
  url: https://www.wordsmith.ai/roi
- group: other
  title: ''
  type: Customers
  url: https://www.wordsmith.ai/customers
- group: other
  title: ''
  type: Company
  url: https://www.wordsmith.ai/company
- group: company
  title: ''
  type: Careers
  url: https://www.wordsmith.ai/careers
- group: other
  title: ''
  type: Articles
  url: https://www.wordsmith.ai/articles
- group: other
  title: ''
  type: Comparisons
  url: https://www.wordsmith.ai/vs
- group: start
  title: ''
  type: BookDemo
  url: https://www.wordsmith.ai/book-demo
- group: learn
  title: ''
  type: Academy
  url: https://academy.wordsmith.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.wordsmith.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/wordsmith.ai/trust/ze3ctf4wjcl4713io5yps
- group: operate
  title: ''
  type: Status
  url: https://status.wordsmith.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wordsmith.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wordsmith.ai/terms-of-service
- group: operate
  title: ''
  type: ModernSlavery
  url: https://www.wordsmith.ai/modern-slavery
- group: other
  title: ''
  type: DiversityAndInclusion
  url: https://www.wordsmith.ai/diversity-and-inclusion
- group: build
  title: ''
  type: SlackIntegration
  url: https://www.wordsmith.ai/integrations/slack
- group: agent
  title: ''
  type: MCPIntegration
  url: https://www.wordsmith.ai/integrations/mcp
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wordsmith-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wordsmithai
created: '2026-05-24'
description: Wordsmith is an Edinburgh-based legal AI platform built for in-house legal teams, marketed as a Slack-native legal copilot that lets non-legal staff self-serve compliant answers, templates, and contract reviews directly in the tools they already use. The product line includes the Wordsmith Assistant (a chat surface that answers routine legal questions, summarises documents, and runs contract review against organisation-specific Playbooks), Templates (parameterised DOCX/Markdown document generation with placeholder fields and fallback clause logic), Playbooks (codified review rules used to flag non-standard terms in NDAs, MSAs, DPAs and similar agreements and to propose pre-approved compromise positions), and a growing set of channel integrations centred on Slack, Microsoft Teams, Gmail, Outlook, Microsoft Word, Google Docs/Drive, SharePoint, OneDrive, Notion, Confluence, Dropbox, Salesforce, HubSpot, Attio, Ironclad, Juro, Asana, Monday.com, Jira, Linear, Granola, Google Sheets,
  and Excel, plus programmatic reach via an MCP server, Zapier, and n8n. Wordsmith exposes a public REST API documented at wordsmithai.mintlify.app with Bearer-token authentication and resources for Assistants (ask a question with optional file attachments, poll question status, list assistants available to the account), Files (presigned upload URLs for documents), Playbooks (list accessible review playbooks), Templates (list accessible templates), User (get-me for the authenticated user and organisation), plus signed Webhooks for asynchronous notifications. The company was founded in October 2023 by Ross McNairn (CEO, formerly Head of Product at Skyscanner and CPTO at TravelPerk), Robbie Falkenthal (COO), and Volodymyr Giginyak (CTO), is headquartered in Edinburgh with offices in London and New York, raised a $25M Series A from Index Ventures in June 2025 at a reported $100M valuation, and counts Trustpilot, Skyscanner, AutoTrader, Deliveroo, BT, Trip.com, Coursera, Canva, The Financial
  Times, Remote.com, Multiverse, and Docplanner among its customers. Pricing is published as an Individual plan at $450 per user per month and a custom Enterprise plan, with a 30-minute book-a-demo flow as the primary onboarding path. WORDSMITH is a registered trade mark of Wordsmith Law LLP and is used under licence by Wordsmith AI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wordsmith.png
layout: provider
modified: '2026-05-24'
name: Wordsmith
nav: Providers
network: true
overview: 'Wordsmith publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Tech, Legal AI, In-House Legal, and General Counsel.


  Wordsmith''s developer surface includes engineering blog, documentation, API reference, authentication, getting-started guide, pricing, academy / training, and 24 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wordsmith/refs/heads/main/screenshots/wordsmith-2026-06-20T201549.png
security:
- kind: domain-security
  name: Wordsmith Domain Security
  slug: wordsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: wordsmith
tags:
- Legal
- Legal Tech
- Legal AI
- In-House Legal
- General Counsel
- Contract Review
- Contract Lifecycle Management
- Document Generation
- Playbooks
- Templates
- AI Assistants
- AI Agents
- Agentic AI
- Slack
- Microsoft Teams
- Compliance
- Governance
- Risk
- Legal Engineering
- MCP
website: https://www.wordsmith.ai
---
