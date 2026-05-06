---
aid: stifel-financial
name: Stifel Financial
description: Stifel Financial is a financial services holding company whose subsidiaries provide securities brokerage, investment banking, trading, investment advisory, and related financial services to individual investors, corporations, and government entities. Stifel bank accounts are accessible via open banking data aggregators including Plaid and Finicity (Mastercard) for third-party financial applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Finance
  - Wealth Management
  - Investment Banking
  - Open Banking
  - Financial Services
url: https://raw.githubusercontent.com/api-evangelist/stifel-financial/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stifel-financial:stifel-bank-finicity
    name: Stifel Bank Finicity Integration
    description: Stifel Bank account data accessible via Finicity (Mastercard) open banking aggregation API, enabling third-party applications to retrieve account balances, transaction history, and investment portfolio data.
    humanURL: https://fintable.io/coverage/banks/United%20States/4445_stifel
    tags:
      - Open Banking
      - Financial Data
      - Account Aggregation
      - Finicity
    properties:
      - type: Documentation
        url: https://developer.mastercard.com/open-banking-us/documentation/
  - aid: stifel-financial:stifel-bank-plaid
    name: Stifel Bank Plaid Integration
    description: Stifel Trust Company account data accessible via Plaid open banking aggregation API, enabling third-party applications to access financial account data through standardized connectivity.
    humanURL: https://fintable.io/coverage/banks/United%20States/31584_stifel-trust-company-client-point
    tags:
      - Open Banking
      - Financial Data
      - Account Aggregation
      - Plaid
    properties:
      - type: Documentation
        url: https://plaid.com/docs/
  - aid: stifel-financial:stifel-wealth-tracker
    name: Stifel Wealth Tracker
    description: Stifel Wealth Tracker is a client-facing portfolio management portal enabling investors to monitor account performance, holdings, and financial activity online.
    humanURL: https://www.stifel.com/Tracker/Support/Overview
    tags:
      - Wealth Management
      - Portfolio Management
      - Client Portal
    properties:
      - type: Documentation
        url: https://www.stifel.com/Tracker/Support/Overview
common:
  - type: Website
    url: https://www.stifel.com
  - type: Technology
    url: https://www.choosestifel.com/technology/
  - type: Open Banking Tracker
    url: https://www.openbankingtracker.com/provider/stifel-bank-personal/apis
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
