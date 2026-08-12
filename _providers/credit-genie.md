---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-11'
  detail: Credit Genie ships only the consumer Cash Boost / Money Manager mobile app — there is no developer subdomain at all (api., developer. and docs.creditgenie.com return NXDOMAIN), the marketing host 404s /openapi.json, /swagger.json, /api-docs and /llms.txt, the first-party GitHub org github.com/CreditGenie holds zero public repositories, and the only machine-readable document the company serves anywhere is its RFC 9116 security.txt.
  evidence:
  - status: 0
    url: https://api.creditgenie.com/openapi.json
  - status: 404
    url: https://www.creditgenie.com/openapi.json
  - status: 404
    url: https://www.creditgenie.com/llms.txt
  - status: 404
    url: https://creditgenie.com/.well-known/api-catalog
  - status: 200
    url: https://creditgenie.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: 'Credit Genie is a consumer fintech operated by Creditly Corp. (Wilmington, Delaware, founded 2019) that runs a mobile-first money app for people living between paychecks. Its Cash Boost product advances $10-$150 with no interest and no hard credit check, funded against a linked bank account rather than a credit score, while Money Manager layers spending tracking, cash-flow prediction and subscription detection on top of that same bank connection. A Line of Credit product and AskGenie, an AI financial assistant, are in early access. Creditly Corp. is registered with the California DFPI under the CCFPL (registration 04-CCFPL-1956127-3514680) and has raised roughly $21M from Fortress Investment Group, Khosla Ventures, Sutter Hill Ventures, Tippet Venture Partners and Gabriel Investments. Credit Genie is a direct-to-consumer app company: it publishes no public API, developer portal, or machine-readable contract of any kind.'
image: https://creditgenie.com/images/app-logo.png
layout: provider
modified: '2026-08-11'
name: Credit Genie
nav: Providers
network: true
random_paper: 40
slug: credit-genie
tags:
- Company
- Financial Services
- Fintech
- Consumer Finance
- Lending
- Cash Advance
- Personal Finance
- Mobile Application
---
