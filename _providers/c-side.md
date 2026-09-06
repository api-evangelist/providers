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
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: C Side Webhooks
  slug: c-side-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cside.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cside.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cside.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cside.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://cside.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://cside.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.cside.com/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cside.com/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://cside.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/client-side-dev
- group: agent
  title: ''
  type: MCPServer
  url: mcp/c-side-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/c-side-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/c-side-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/c-side-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/c-side-cli.yml
- group: design
  title: ''
  type: Components
  url: components/c-side-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/c-side-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/c-side-security.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/c-side-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/c-side-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/c-side-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cside.com
- group: design
  title: ''
  type: Conformance
  url: conformance/c-side-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cside.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/c-side-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/c-side-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cside.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/c-side-domain-security.yml
created: '2026-07-17'
description: c/side (cside) is a client-side security platform that detects script attacks, AI agents, account takeover, and fraud at the browser layer. It provides active runtime detection that watches what third-party scripts, users, and agents actually do as they execute in the live browser session, in real time, rather than relying on static scans or block-lists, and it automates PCI DSS 4.0.1 requirements 6.4.3 and 11.6.1 (validated by a VikingCloud QSA). cside deploys as a single JavaScript snippet with no proxy and no DNS changes, and was the first client-side security product with integrated AI analysis. The platform protects websites from malicious third-party scripts, e-skimming, Magecart, and supply chain attacks, and adds device fingerprinting (102+ signals), VPN/bot/AI-agent detection, chargeback evidence, and privacy monitoring for GDPR, CCPA, and HIPAA. Founded in 2024 and backed by Uncork Capital, cside integrates via a CLI, Next.js and Vite plugins, a manual script tag,
  and Salesforce Lightning, and sends security alerts through webhook, S3, and Jira/Linear notification endpoints. cside publishes an llms.txt, a public read-only MCP server, and a Trust Center covering SOC 2 Type II, PCI SAQ-D, and ISO 27001.
image: https://og.cside.com/?title=cside%2C%20Client-Side%20Security%20%26%20Browser%20Fraud%20Prevention
layout: provider
mcp_servers:
- description: cside operates a public, read-only remote MCP (Model Context Protocol) server at https://mcp.cside.com that exposes cside.com marketing-site and docs.cside.com documentation content (not the cside pro
  name: c/side MCP Server
  slug: cside-mcp-server
modified: '2026-07-18'
name: c/side
nav: Providers
network: true
overview: 'c/side is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Client-Side Security, Application Security, and Fraud Prevention.


  The c/side catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  c/side''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, CLI, changelog, and 21 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 44.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa-cpra
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/c-side/refs/heads/main/screenshots/c-side-2026-07-25T204147.png
security:
- kind: domain-security
  name: C Side Domain Security
  slug: c-side-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: C Side Vulnerability Disclosure
  slug: c-side-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: C Side Trust Center
  slug: c-side-trust-center
  summary_line: SOC 2 Type II, PCI DSS (SAQ-D AOC), ISO 27001 (in progress), GDPR
slug: c-side
tags:
- Company
- Security
- Client-Side Security
- Application Security
- Fraud Prevention
- PCI DSS Compliance
- Device Fingerprinting
- Bot Detection
- Web Security
- Script Monitoring
website: https://cside.com
---
