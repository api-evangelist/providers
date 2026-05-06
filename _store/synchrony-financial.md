---
aid: synchrony-financial
name: Synchrony Financial
description: Synchrony Financial is one of the nation's premier consumer financial services companies, providing a range of credit products through programs established with retailers, manufacturers, and merchants. Synchrony offers APIs enabling partners and retailers to integrate credit applications, authorizations, payments, loyalty, and account management into their digital commerce experiences.
url: https://raw.githubusercontent.com/api-evangelist/synchrony-financial/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
tags:
  - Financial Services
  - Credit
  - Payments
  - Consumer Finance
  - Retail Finance
apis:
  - aid: synchrony-financial:credit-authorization
    name: Synchrony Credit Authorization API
    description: The Synchrony Credit Authorization API allows merchants and retailers to perform credit card transactions including purchases, preauthorizations, completions, payments, refunds, and reversals. The API supports transactions via payment tokens or full account numbers across web, mobile, and point-of-sale channels.
    humanURL: https://developer.syf.com/our-products/credit-authorizations
    baseURL: https://api.syf.com
    tags:
      - Credit Authorization
      - Payments
      - Purchases
      - Refunds
      - Retail Finance
    properties:
      - type: Documentation
        url: https://developer.syf.com/our-products/credit-authorizations
      - type: OpenAPI
        url: openapi/synchrony-financial-credit-authorization-openapi.yml
  - aid: synchrony-financial:quickscreen-apply
    name: Synchrony Quickscreen Apply API
    description: Synchrony's Quickscreen API is a preapproval engine that allows merchants to offer instant credit decisions using only a customer's name and address. It runs a soft credit check and returns a real-time decision, enabling seamless credit offering within the shopping experience.
    humanURL: https://developer.syf.com/our-products/quickscreen-apply
    baseURL: https://api.syf.com
    tags:
      - Credit Application
      - Preapproval
      - Quickscreen
      - Consumer Finance
    properties:
      - type: Documentation
        url: https://developer.syf.com/our-products/quickscreen-apply
      - type: OpenAPI
        url: openapi/synchrony-financial-quickscreen-apply-openapi.yml
  - aid: synchrony-financial:account-management
    name: Synchrony Account Management API
    description: The Synchrony Account Management API provides access to cardholder account information, enabling partners to retrieve account details, balance information, transaction history, and manage account servicing operations on behalf of customers.
    humanURL: https://developer.syf.com/
    baseURL: https://api.syf.com
    tags:
      - Account Management
      - Consumer Finance
      - Credit Cards
    properties:
      - type: Documentation
        url: https://developer.syf.com/
common:
  - type: Website
    url: https://www.synchrony.com
  - type: DeveloperPortal
    url: https://developer.syf.com/
  - type: PortalProducts
    url: https://developer.syf.com/our-products
  - type: TermsOfService
    url: https://developer.syf.com/terms-of-use
  - type: Sandbox
    url: https://developer.syf.com/
  - type: JSONLDContext
    url: json-ld/synchrony-financial-context.jsonld
  - type: Vocabulary
    url: vocabulary/synchrony-financial-vocabulary.yml
features:
  - Credit Authorization
  - Preapproval Engine (Quickscreen)
  - Mobile Credit Application (mApply)
  - Account Servicing
  - Loyalty and Rewards Integration
  - Payment Tokens Support
  - Sandbox Environment
useCases:
  - Retail Credit Integration
  - E-Commerce Credit Offering
  - Mobile Point-of-Sale Financing
  - Credit Card Transaction Processing
  - Consumer Loyalty Programs
integrations:
  - type: AdobeCommerce
    url: https://commercemarketplace.adobe.com/synchrony-digital-buy-magento2-module.html
  - type: Plaid
    url: https://plaid.com/institutions/synchrony-bank/
solutions:
  - Buy Now Pay Later
  - Retail Financing
  - Consumer Credit Programs
  - Partner Credit Programs
---
