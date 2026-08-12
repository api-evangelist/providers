---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-11'
  detail: Darrow markets no API anywhere on darrow.ai — docs., developers. and api.darrow.ai do not resolve in DNS, the 248-URL sitemap contains no developer, docs or pricing page, the GitHub org holds two repos and neither is a client library, and the only HTTP API reachable on the public internet is the customer application's own backend at platform.darrow.ai/api/*, which answers 401 Unauthorized to anonymous callers.
  evidence:
  - status: 404
    url: https://www.darrow.ai/developers
  - status: 401
    url: https://platform.darrow.ai/api/openapi.json
  - status: 404
    url: https://www.darrow.ai/.well-known/agent-card.json
  - status: 200
    url: https://auth.darrow.ai/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: 'Darrow is an AI legal-intelligence company (founded 2020, offices in New York, Miami, Arizona and Tel Aviv) that scans public real-world signals — regulatory filings, court dockets, incident reports, corporate disclosures and web behavior — to detect legal violations at scale, size the affected class, predict outcomes and value the resulting cases. Its platform serves plaintiff law firms (case origination, predictive litigation analytics, portfolio management, PlaintiffLink intake), insurers (predictive underwriting) and corporate compliance teams (Privacy Radar, listed in the Microsoft Marketplace). Darrow publishes no public developer program: the product is delivered through an Auth0-protected customer portal at portal.darrow.ai, and the only machine-readable surface reachable without credentials is the OpenID Connect discovery document served by its identity tenant.'
image: https://cdn.prod.website-files.com/66c2f6a7d0f70f91592bbaa7/69d55692cb9358ee200d9517_home-OG.png
layout: provider
modified: '2026-08-11'
name: Darrow
nav: Providers
network: true
random_paper: 75
slug: darrow
tags:
- Company
- Legal
- Legal Intelligence
- Litigation
- Artificial Intelligence
- Compliance
- Risk Management
- Insurance
- Data Analytics
---
