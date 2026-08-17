---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.atombeamtech.com/
- group: company
  title: ''
  type: Blog
  url: https://www.atombeamtech.com/blog
- group: operate
  title: ''
  type: Support
  url: https://customersupport.atombeamtech.com/
- group: start
  title: ''
  type: Login
  url: https://acp.atombeamtech.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atombeamtech.com/utility/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atombeamtech.com/utility/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AtomBeam
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atombeam-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atombeam-domain-security.yml
- group: operate
  title: ''
  type: FAQ
  url: https://www.atombeamtech.com/faq
- group: start
  title: ''
  type: Demo
  url: https://www.atombeamtech.com/demo
- group: other
  title: ''
  type: Products
  url: https://www.atombeamtech.com/products/overview
- group: company
  title: ''
  type: Partners
  url: https://www.atombeamtech.com/partners/partners
- group: company
  title: ''
  type: Newsroom
  url: https://www.atombeamtech.com/about/newsroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.atombeamtech.com/investor-hub
- group: other
  title: ''
  type: Crowdfunding
  url: https://www.startengine.com/offering/atombeam
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/atombeam_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atombeam
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCVR_l_tlXbNgEsUwSlKSgRg
coverage:
  checked: '2026-08-06'
  detail: AtomBeam runs a real production API — acg-api.atombeamtech.com, the AWS API Gateway backend of its "Codebook Generator" customer portal, whose Angular bundle names the codebooks/, datasets/, companies/, simulation/, reports/, users/, categories/, notifications/ and tracking/ collections — but it answers 403 Forbidden on every path including /openapi.json, and the guides that would document it live inside a Jira Service Management portal that 302s to a login; the only public technical collateral is a set of Neurpac datasheet PDFs behind email-capture download forms.
  evidence:
  - status: 403
    url: https://acg-api.atombeamtech.com/openapi.json
  - status: 403
    url: https://acg-api.atombeamtech.com/
  - status: 302
    url: https://customersupport.atombeamtech.com/
  - status: 200
    url: https://www.atombeamtech.com/llms.txt
  - status: 404
    url: https://www.atombeamtech.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: 'AtomBeam Technologies is a Moraga, California software company founded in 2017 that sells "Compaction" — a machine-learning approach to shrinking machine-generated data that replaces recurring bit-level patterns with codewords drawn from a trained codebook, rather than compressing bytes. Its Neurpac product is an on-premises, protocol-agnostic bidirectional compaction tunnel that reduces IoT, telemetry and file payloads by roughly 75% while encrypting and obfuscating them in transit; Neurcom and PCM are earlier-stage research products. AtomBeam licenses the software to IoT device and gateway makers, satellite and LPWAN operators, telcos, and the US Department of Defense, and has raised capital through Regulation A and Regulation CF crowdfunding on StartEngine. There is no public developer API program: the customer-facing surface is the login-gated AtomBeam Customer Portal (codebook generation and simulation) plus a Jira Service Management support portal.'
image: https://cdn.prod.website-files.com/65ee960bca00890dd416e95c/65f8f36d0922a632a016240d_logo.png
layout: provider
modified: '2026-08-06'
name: AtomBeam
nav: Providers
network: true
overview: 'AtomBeam is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Compression, Internet of Things, Edge Computing, and Satellite Communications.


  AtomBeam''s developer surface includes engineering blog, support, FAQ, YouTube channel, and 15 more developer resources.'
random_paper: 93
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atombeam/refs/heads/main/screenshots/atombeam-2026-08-07T161858.png
security:
- kind: domain-security
  name: Atombeam Domain Security
  slug: atombeam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: atombeam
tags:
- Company
- Data Compression
- Internet of Things
- Edge Computing
- Satellite Communications
- Machine Learning
- Data Management
- Defense
- Telemetry
website: https://www.atombeamtech.com/
---
