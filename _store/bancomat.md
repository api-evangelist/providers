---
aid: bancomat
name: Bancomat
description: BANCOMAT S.p.A. is Italy's leading payment network operator managing the PagoBancomat debit card scheme, ATM network, and BANCOMAT Pay mobile payment service. Launched in 1983 for ATM withdrawals and expanded in 1986 with PagoBancomat for PIN-based POS payments, the network underpins Italian electronic payment infrastructure. BANCOMAT Pay, introduced in 2019, enables mobile e-commerce and P2P payments linked to bank accounts via phone number and IBAN.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ATM
  - Banking
  - Financial Services
  - Italy
  - Mobile Payments
  - Payments
  - Debit Cards
url: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: bancomat:bancomat-pay
    name: BANCOMAT Pay
    description: BANCOMAT Pay is a mobile payment service enabling Italian consumers to make e-commerce purchases and P2P transfers through a smartphone app linked to their bank account by phone number and IBAN. Merchant integration is typically handled through PSPs such as Nexi, Axerve, PPRO, and HiPay rather than a direct public API.
    humanURL: https://bancomat.it/en/bancomat-pay
    tags:
      - Mobile Payments
      - P2P
      - Payments
      - Italy
    properties:
      - type: Documentation
        url: https://bancomat.it/en/bancomat-pay
      - type: Documentation
        url: https://developer.nexigroup.com/xpayglobal/en-EU/docs/bancomat-pay/
        name: Nexi Integration Guide
common:
  - type: Website
    url: https://bancomat.it/en
    name: BANCOMAT S.p.A.
  - type: Website
    url: https://bancomat.it/en/the-company
    name: About BANCOMAT S.p.A.
  - type: SpectralRules
    url: rules/bancomat-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bancomat-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/bancomat-payment-capability.yaml
  - type: JSON-LD
    url: json-ld/bancomat-context.jsonld
  - name: Features
    type: Features
    data:
      - name: ATM Network
        description: Italy's largest ATM cash withdrawal network operational since 1983.
      - name: PagoBancomat Debit
        description: PIN-based POS debit card payments accepted at millions of Italian merchants.
      - name: BANCOMAT Pay Mobile
        description: Mobile app payment service for e-commerce and P2P transfers linked to bank accounts.
      - name: QR Code Payments
        description: QR code-based checkout integration for online and in-store merchants.
      - name: Bank Integration
        description: Deep integration with Italian banks enabling account-linked payment authorization.
      - name: P2P Transfers
        description: Person-to-person money transfers between Italian bank accounts via mobile app.
  - name: UseCases
    type: UseCases
    data:
      - name: ATM Cash Withdrawals
        description: Debit card ATM withdrawals across Italy's national banking network.
      - name: POS Debit Payments
        description: PIN-based debit card payments at retail point-of-sale terminals.
      - name: E-Commerce Payments
        description: Online checkout integration via BANCOMAT Pay mobile app.
      - name: P2P Money Transfer
        description: Person-to-person payments between bank accounts via mobile app.
      - name: Merchant Acceptance
        description: Enable BANCOMAT Pay as a local Italian payment method for online stores.
  - name: Integrations
    type: Integrations
    data:
      - name: Nexi
        description: Integration via Nexi XPay Global payment gateway for merchant acceptance.
      - name: Axerve (Fabrick)
        description: Integration via Axerve/Fabrick for Italian e-commerce BANCOMAT Pay acceptance.
      - name: PPRO
        description: Integration via PPRO for international PSP access to BANCOMAT Pay.
      - name: HiPay
        description: Integration via HiPay payment platform.
      - name: Viva.com
        description: Integration via Viva.com payment services.
      - name: PayPal Braintree
        description: Integration via PayPal Braintree payment gateway.
      - name: Nuvei
        description: Integration via Nuvei payment technology platform.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
