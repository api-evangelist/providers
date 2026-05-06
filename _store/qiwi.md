---
aid: qiwi
name: Qiwi
description: Qiwi provides payment reception, payouts, and banking platform APIs for processing wallet, card, mobile, and SBP transactions across Russia and CIS markets.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Payments
  - Wallet
  - Payouts
  - Fintech
  - Banking
url: https://raw.githubusercontent.com/api-evangelist/qiwi/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qiwi:qiwi-payment-protocol
    name: Qiwi Payment Protocol
    description: Protocol for accepting Qiwi payments from wallet, card, and account sources, including payment confirmation, status checks, and reconciliation.
    humanURL: https://developer.qiwi.com/ru/payments/
    tags:
      - Payments
      - Acceptance
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/payments/
  - aid: qiwi:qiwi-legal-entity-payouts
    name: Qiwi Legal Entity Payouts
    description: API for legal entities to issue payouts to wallets, cards, and bank accounts with batch and individual transfer support.
    humanURL: https://developer.qiwi.com/ru/payout/v2/
    tags:
      - Payouts
      - B2B
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/payout/v2/
  - aid: qiwi:qiwi-wallet-payouts
    name: Qiwi Wallet Payouts
    description: API for sending payouts directly to Qiwi wallets.
    humanURL: https://developer.qiwi.com/ru/topup-wallet/
    tags:
      - Payouts
      - Wallet
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/topup-wallet/
  - aid: qiwi:qiwi-card-wallet-sbp-payouts
    name: Qiwi Card Wallet SBP Payouts
    description: API for issuing payouts to bank cards, wallets, and SBP (Faster Payments System) recipients.
    humanURL: https://developer.qiwi.com/ru/topup-card/
    tags:
      - Payouts
      - Cards
      - SBP
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/topup-card/
  - aid: qiwi:qiwi-mobile-topups
    name: Qiwi Mobile Topups
    description: API for topping up mobile phone balances across telecom operators.
    humanURL: https://developer.qiwi.com/ru/topup-mobile/
    tags:
      - Payouts
      - Mobile
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/topup-mobile/
  - aid: qiwi:qiwi-baas
    name: Qiwi Banking Platform
    description: Banking-as-a-Service platform for issuing accounts, cards, and banking operations on top of Qiwi infrastructure.
    humanURL: https://developer.qiwi.com/baas/
    tags:
      - Banking
      - BaaS
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/baas/
  - aid: qiwi:qiwi-identification-service
    name: Qiwi Client Identification Service
    description: API for client identification and KYC verification workflows.
    humanURL: https://developer.qiwi.com/ru/identification-service/
    tags:
      - KYC
      - Identification
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/identification-service/
  - aid: qiwi:qiwi-terminal-map
    name: Qiwi Terminal Map
    description: API to retrieve Qiwi terminal locations and their service capabilities.
    humanURL: https://developer.qiwi.com/ru/qiwi-map/
    tags:
      - Terminals
      - Locations
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/qiwi-map/
  - aid: qiwi:qiwi-wallet-personal
    name: Qiwi Wallet Personal
    description: Personal Qiwi Wallet API for managing balance, transfers, payments, and transaction history for end users.
    humanURL: https://developer.qiwi.com/ru/qiwi-wallet-personal/
    tags:
      - Wallet
      - Personal
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/qiwi-wallet-personal/
  - aid: qiwi:qiwi-p2p-payments
    name: Qiwi P2P Payments
    description: Peer-to-peer payment API for accepting payments from individuals via payment forms and invoices.
    humanURL: https://developer.qiwi.com/ru/p2p-payments/
    tags:
      - Payments
      - P2P
    properties:
      - type: Documentation
        url: https://developer.qiwi.com/ru/p2p-payments/
common:
  - type: Portal
    url: https://developer.qiwi.com
  - type: GitHubOrganization
    url: https://github.com/QIWI-API
  - type: Website
    url: https://qiwi.com
  - type: Support
    url: https://qiwi.com/support
  - type: TermsOfService
    url: https://qiwi.com/legal
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
