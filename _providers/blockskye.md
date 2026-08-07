---
api_count: 1
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: Blockskye runs a live production API at api.blockskye.com whose /health endpoint answers 200 anonymously, but the only Blockskye documentation that exists sits in a Freshworks-backed knowledge base where /support/solutions chains 302 to /support/home to /support/login and out to a blockskye.myfreshworks.com OAuth authorize URL, so the reference is reachable only by an existing customer tenant.
  evidence:
  - status: 302
    url: https://support.blockskye.com/support/solutions
  - status: 302
    url: https://support.blockskye.com/support/login
  - status: 200
    url: https://api.blockskye.com/health
  - status: 404
    url: https://api.blockskye.com/openapi.json
  - status: 404
    url: https://api.blockskye.com/documentation/json
  - status: 404
    url: https://www.blockskye.com/llms.txt
  - status: 404
    url: https://www.blockskye.com/.well-known/security.txt
  - status: 200
    url: https://horizon.blockskye.com/login
  reason: customer-only-docs
  state: gated
created: '2026-08-07'
description: 'Blockskye is an enterprise travel management and payments platform for large corporate travel programs, founded in 2017 and headquartered in New York. It combines a consumer-grade online booking tool sourced through direct supplier and NDC connectivity, BMAX direct settlement that wires a customer''s ERP straight to travel suppliers so booked travel bypasses corporate cards and expense reports, B360 for capturing personal co-brand card loyalty on business trips while holding policy compliance, and real-time reporting across every booking channel, with transactions recorded to a tamper-resistant distributed ledger. Blockskye delivers an end-to-end corporate travel solution in partnership with KAYAK for Business. The platform is sold and operated as an enterprise service: the booking, servicing and settlement application runs at horizon.blockskye.com behind a customer login and the knowledge base sits behind a Freshworks OAuth login. Blockskye operates a live production API host
  at api.blockskye.com but publishes no public developer portal, API reference, or machine-readable API contract.'
image: https://static1.squarespace.com/static/68efa9e7e26dde07bc4331ce/t/690a135f62cc1b156338a90e/1778097079157/SEOblockskye.jpg?format=1500w
layout: provider
modified: '2026-08-07'
name: Blockskye
nav: Providers
network: true
random_paper: 63
slug: blockskye
tags:
- Travel
- Corporate Travel
- Travel Management
- Payments
- Settlement
- Expense Management
- Booking
- Blockchain
- Distributed Ledger
- Enterprise
---
