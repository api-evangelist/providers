---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: Avenue One ships AvenueOS only as a login-gated product to institutional clients and vetted partners — partners.avenueone.com 302s straight to an Auth0 universal login, and the AvenueOS backend at api.credit.avenueone.com answers every docs path (/docs, /redoc, /openapi.json, /api/openapi.json) identically to a control path, so no OpenAPI, SDK, webhook or developer portal exists to profile.
  evidence:
  - status: 404
    url: https://api.credit.avenueone.com/api/openapi.json
  - status: 404
    url: https://api.credit.avenueone.com/openapi.json
  - status: 302
    url: https://partners.avenueone.com/
  - status: 403
    url: https://avenueone.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Avenue One is a New York-based technology service platform and investment marketplace for institutional owners, buyers, sellers, lenders and borrowers of residential rental real estate. Founded in 2020, it connects institutional debt and equity capital to local operating partners and property owners across 21+ U.S. markets, combining proprietary property data, automated valuation, and a vetted partner network to find, finance, buy, renovate, lease, manage and sell single-family rental homes at scale. Its service lines span lending (bridge and SFR portfolio loans), strategy development, acquisitions, renovations, asset management, title and brokerage or dispositions. The company reports $2.2B+ of capital deployed. Its software runs as a private, login-gated product suite ("AvenueOS") for internal, builder, investor and partner users; no public developer program, API reference, or machine-readable contract is published.
image: https://avenueone.com/_assets/Avenue_One_Horizontal_Logo_Digital_FullColor_1-b0ddb1c50f.svg
layout: provider
modified: '2026-08-06'
name: Avenue One
nav: Providers
network: true
random_paper: 107
slug: avenue-one
tags:
- Company
- Real Estate
- Single-Family Rental
- PropTech
- Institutional Investing
- Lending
- Asset Management
- Property Data
- Marketplace
---
