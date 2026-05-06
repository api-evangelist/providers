---
aid: bnp-paribas
name: BNP Paribas
description: BNP Paribas is a leading international banking group providing a wide range of financial services to individuals, businesses, and institutions worldwide. The company offers APIs through its CIB Developer Portal covering capital markets, payment services, securities services, and open banking integrations for corporate and institutional clients.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bnp-paribas/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Banking
  - Finance
  - Payments
  - Capital Markets
  - Open Banking
apis:
  - aid: bnp-paribas:bnp-paribas-cib-api
    name: BNP Paribas CIB API
    description: BNP Paribas Corporate and Institutional Banking (CIB) API platform provides programmatic access to capital markets, payment services, securities services, advisory, finance, and treasury solutions for corporate and institutional clients. APIs include payment initiation, fund availability checks, SEPA direct debit management, and open banking compliance services.
    humanURL: https://developers.cib.bnpparibas.com/api-catalog
    tags:
      - Banking
      - CIB
      - Capital Markets
      - Payments
      - Open Banking
    properties:
      - type: Portal
        url: https://developers.cib.bnpparibas.com/api-catalog
      - type: Documentation
        url: https://developers.cib.bnpparibas.com/api-catalog
      - type: GettingStarted
        url: https://developers.cib.bnpparibas.com/how-to
  - aid: bnp-paribas:bnp-paribas-open-banking-api
    name: BNP Paribas Open Banking API
    description: BNP Paribas Open Banking APIs provide PSD2-compliant payment services and account information access including check availability of funds for card-based payment instrument issuers, SEPA direct debit mandate management (EASYCOLLECT), and payment initiation services across European markets.
    humanURL: https://apistore.bnpparibas
    tags:
      - Open Banking
      - PSD2
      - Payments
      - SEPA
      - Banking
    properties:
      - type: Portal
        url: https://apistore.bnpparibas
      - type: Documentation
        url: https://apistore.bnpparibas
common:
  - type: Website
    url: https://www.bnpparibas.com
  - type: Portal
    url: https://developers.cib.bnpparibas.com/api-catalog
  - type: GettingStarted
    url: https://developers.cib.bnpparibas.com/how-to
  - type: OpenBankingPortal
    url: https://apistore.bnpparibas
  - type: FAQ
    url: https://developers.cib.bnpparibas.com/faq
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
