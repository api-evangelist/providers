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
api_count: 1
apis:
- baseURL: https://api.opereit.com
  baseurl_source: declared
  description: The Contracts API from Opereit — 3 operation(s) for contracts.
  name: Opereit Contracts API
  slug: opereit-contracts-api
- baseURL: https://api.opereit.com
  baseurl_source: declared
  description: The Invoice Audits API from Opereit — 3 operation(s) for invoice audits.
  name: Opereit Invoice Audits API
  slug: opereit-invoice-audits-api
arazzos:
- description: Upload a contract, upload and audit an invoice against it, then read the findings.
  name: Opereit — audit a carrier invoice against a contract
  slug: opereit-audit-invoice
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Opereit Invoice Auditing Contracts API
  slug: open-opereit-contracts-api
- collection_type: open
  name: Opereit Invoice Auditing Contracts Invoice Audits API
  slug: open-opereit-invoice-audits-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/opereit-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/opereit-invoice-auditing-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.opereit.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.opereit.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.opereit.ai/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.opereit.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.opereit.ai/api-reference/introduction
- group: start
  title: ''
  type: Login
  url: https://dashboard.opereit.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opereit
- group: auth
  title: ''
  type: Authentication
  url: authentication/opereit-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opereit-domain-security.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/opereit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opereit-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Opereit is a Barcelona-based logistics technology company building AI agents that audit, claim, and recover logistics costs autonomously. Its agents detect carrier invoice discrepancies, identify lost and damaged shipments, and file carrier claims end to end with no human in the loop. The public Opereit Invoice Auditing API lets developers upload carrier contracts (rate cards and surcharges are extracted asynchronously), audit incoming carrier invoices against those contracts, and retrieve the resulting line items and discrepancy findings — building automated cost-recovery workflows without the dashboard. Opereit raised a ~$2.5M pre-seed round led by Seedcamp and Yellow in 2026.
image: https://www.opereit.ai/favicon.png
layout: provider
modified: '2026-07-20'
name: Opereit
nav: Providers
network: true
overview: 'Opereit publishes 2 APIs on the [APIs.io](https://apis.io/) network: Contracts API and Invoice Audits API. Tagged areas include Company, Logistics, Supply Chain, Shipping, and Invoice Auditing.


  Opereit''s developer surface includes documentation, API reference, getting-started guide, authentication, and 10 more developer resources.'
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/opereit/refs/heads/main/screenshots/opereit-2026-08-07T190714.png
security:
- kind: authentication
  name: Opereit Authentication
  slug: opereit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opereit Domain Security
  slug: opereit-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: opereit
tags:
- Company
- Logistics
- Supply Chain
- Shipping
- Invoice Auditing
- Cost Recovery
- Freight Audit
- Artificial Intelligence
- AI Agents
website: https://www.opereit.ai
---
