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
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fi-money-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fi.money
- group: company
  title: ''
  type: About
  url: https://fi.money/about
- group: company
  title: ''
  type: Careers
  url: https://fi.money/careers
- group: operate
  title: ''
  type: Contact
  url: https://fi.money/contact-us
- group: auth
  title: ''
  type: Security
  url: https://fi.money/Fi-Secure
- group: commercial
  title: ''
  type: Privacy
  url: https://fi.money/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fi.money/blog/tnc
- group: operate
  title: ''
  type: FAQ
  url: https://fi.money/FAQs
- group: company
  title: ''
  type: Blog
  url: https://fi.money/insights
- group: start
  title: ''
  type: MCPGettingStarted
  url: https://fi.money/features/getting-started-with-fi-mcp
- group: agent
  title: ''
  type: MCPUsage
  url: https://fi.money/features/using-fi-mcp-for-money-management
- group: agent
  title: ''
  type: MCPFAQ
  url: https://fi.money/FAQs/wealth-analyzer-(fi-mcp)
- group: other
  title: ''
  type: AIFeatures
  url: https://fi.money/features/ai-for-money-management
- group: build
  title: ''
  type: GitHub
  url: https://github.com/epiFi
- group: docs
  title: ''
  type: MCPDocs
  url: https://github.com/epiFi/mcp-docs
- group: agent
  title: ''
  type: MCPDevServer
  url: https://github.com/epiFi/fi-mcp-dev
- group: agent
  title: ''
  type: MCPEndpoint
  url: https://mcp.fi.money:8080/mcp/stream
- group: company
  title: ''
  type: PartnerBank
  url: https://www.federalbank.co.in
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/fi-money
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Bank_on_Fi
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/in/app/fi-money-savings-investments/id1503530120
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=in.fi.money
created: '2026-05-24'
description: Fi Money is a Bengaluru, India based money-management application and consumer fintech operated by Epifi Technologies, founded in 2019 by ex-Google Pay (Tez) executives Sujith Narayanan and Sumit Gwalani together with Neeraj Bhope and Prasanna Ranganathan. Fi is not a chartered bank; it delivers a millennial-focused mobile experience layered on top of partner RBI-licensed Federal Bank, providing zero-balance digital savings accounts, a Visa debit card, deposits, mutual funds, Indian and US stocks, EPF tracking, credit cards, personal loans, jump-style automated savings rules ("FIT Rules"), and an AI-powered money assistant. Fi has raised roughly US$169M across multiple rounds from investors including Sequoia Capital India (Peak XV), Ribbit Capital, Temasek, Alpha Wave, and B Capital, and serves Indian retail consumers via iOS and Android apps. There is no classic public REST developer API or partner banking-as-a-service surface; Fi's only developer-facing interface is the Fi
  MCP (Model Context Protocol) server — a JSON-RPC streaming endpoint at https://mcp.fi.money:8080/mcp/stream that lets users connect their own Fi account to LLM clients (Claude Desktop, Cursor, Windsurf, Gemini, ChatGPT) and call read-only tools such as fetch_net_worth, fetch_credit_report, fetch_epf_details, fetch_bank_transactions, fetch_mf_transactions, and fetch_stock_transactions to expose their net worth, holdings, EPF balance, credit report, and transactions to AI assistants. A hackathon-friendly mock server (epiFi/fi-mcp-dev, Go) and developer documentation (epiFi/mcp-docs) are published publicly on GitHub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fi-money.png
layout: provider
modified: '2026-05-24'
name: Fi Money
nav: Providers
network: true
overview: 'Fi Money is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Neobank, Consumer Banking, Personal Finance, and Money Management.


  Fi Money''s developer surface includes privacy policy, FAQ, engineering blog, GitHub presence, and 19 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fi-money/refs/heads/main/screenshots/fi-money-2026-06-20T181146.png
security:
- kind: domain-security
  name: Fi Money Domain Security
  slug: fi-money-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fi-money
tags:
- Fintech
- Neobank
- Consumer Banking
- Personal Finance
- Money Management
- Wealth Analyzer
- Mutual Funds
- Stocks
- EPF
- Credit Cards
- Personal Loans
- Savings
- UPI
- India
- Federal Bank
- MCP
- AI Assistant
- Mobile Banking
website: https://fi.money
---
