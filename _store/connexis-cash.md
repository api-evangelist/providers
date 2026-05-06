---
aid: connexis-cash
name: Connexis Cash
description: Connexis Cash is BNP Paribas's corporate digital banking and cash management platform. It gives multinational corporates a unified online channel for payment initiation, real-time payment tracking, account reporting, reconciliation, and liquidity management across BNP Paribas's global network. Connexis Cash also exposes PSD2-compliant Open Banking APIs through the BNP Paribas CIB developer portal so that third-party providers (TPPs) can retrieve account information and initiate payments on behalf of Connexis Cash users, as well as a Strong Customer Authentication (SCA) flow.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/connexis-cash/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
tags:
  - Account Information
  - BNP Paribas
  - Cash Management
  - Corporate Banking
  - Digital Banking
  - Liquidity Management
  - Open Banking
  - Payments
  - PSD2
  - SCA
  - STET
apis:
  - aid: connexis-cash:psd2-account-information
    name: Connexis Cash PSD2 Account Information API (STET)
    description: A PSD2-compliant Account Information Service (AISP) API exposed by BNP Paribas Corporate and Institutional Banking. Third-party providers consume this REST/JSON API, which follows the STET PSD2 standard, to retrieve account information for Connexis Cash users. Production uses OAuth2 Authorization Code Grant with QWAC certificates; the sandbox uses Client Credentials. Onboarded TPPs must supply QWAC certificates, callback URLs, and EBA reference codes.
    humanURL: https://developers.cib.bnpparibas.com/index.php/api-docs/account-information-psd2-stet-mock
    baseURL: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - AISP
      - PSD2
      - REST
      - STET
    properties:
      - type: Documentation
        url: https://developers.cib.bnpparibas.com/index.php/api-docs/account-information-psd2-stet-mock
      - type: Developer Portal
        url: https://developers.cib.bnpparibas.com/
      - type: Production
        url: https://psd2.api.cib.bnpparibas.com/gb-account-information-psd2-stet
      - type: Fallback
        url: https://connexis.bnpparibas.com/
    contact:
      - FN: BNP Paribas PSD2 API Support
        email: dl.cib.api.psd2.support@bnpparibas.com
    x-features:
      - PSD2 STET Compliance
      - OAuth2 Authorization Code Grant (production)
      - Client Credentials (sandbox)
      - QWAC Certificate Authentication
      - Account Balances Retrieval
      - Transaction Listing
      - Full-AISP Consent Model
    x-use-cases:
      - Aggregate Connexis Cash balances into TPP dashboards
      - Build accounting tools that pull bank data automatically
      - Power treasury software with multi-bank account access
  - aid: connexis-cash:strong-authentication
    name: Connexis Cash Strong Customer Authentication (SCA)
    description: A documented Strong Customer Authentication flow that BNP Paribas provides for Connexis Cash to satisfy PSD2 SCA requirements. TPPs integrate the SCA flow into their PSD2 journeys so that Connexis Cash users authenticate with two factors before consenting to share account data or initiate payments.
    humanURL: https://developers.cib.bnpparibas.com/index.php/docs/sca
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - PSD2
      - SCA
      - Security
    properties:
      - type: Documentation
        url: https://developers.cib.bnpparibas.com/index.php/docs/sca
      - type: Developer Portal
        url: https://developers.cib.bnpparibas.com/
    x-features:
      - Two-Factor Authentication
      - PSD2 SCA Compliance
      - Redirect Authentication Flow
    x-use-cases:
      - Authenticate users for AISP/PISP consent
      - Satisfy PSD2 SCA in Open Banking integrations
  - aid: connexis-cash:digital-banking-platform
    name: Connexis Cash Digital Banking Platform
    description: The Connexis Cash digital banking application itself. While not a public REST API, it is the user-facing platform that powers payment initiation, real-time tracking, reconciliation, account reporting, and liquidity management for BNP Paribas corporate customers, with web and mobile apps and host-to-host connectivity options.
    humanURL: https://cashmanagement.bnpparibas.com/solutions/digital-channels
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Cash Management
      - Digital Channel
      - Mobile
    properties:
      - type: Documentation
        url: https://cashmanagement.bnpparibas.com/solutions/digital-channels
      - type: iOS App
        url: https://apps.apple.com/us/app/connexis-cash-mobile/id1053068521
    x-features:
      - Payment Initiation
      - Real-Time Tracking
      - Reconciliation
      - Liquidity Management
      - Mobile Companion App
      - Host-to-Host Connectivity
    x-use-cases:
      - Centralize global cash visibility for treasury teams
      - Initiate and authorize cross-border payments
      - Reconcile inflows and outflows across BNP Paribas accounts
common:
  - type: Website
    url: https://cashmanagement.bnpparibas.com/solutions/digital-channels
  - type: Developer Portal
    url: https://developers.cib.bnpparibas.com/
  - type: Open Banking Tracker
    url: https://www.openbankingtracker.com/provider/connexis-cash
  - type: BNP Paribas CIB
    url: https://cib.bnpparibas/
  - type: Mobile App
    url: https://apps.apple.com/us/app/connexis-cash-mobile/id1053068521
  - type: Support
    email: dl.cib.api.psd2.support@bnpparibas.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
